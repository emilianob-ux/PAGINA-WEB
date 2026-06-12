#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inspeccionar_yaypricing.py  (PASO 1 - SOLO LECTURA)

Objetivo: descubrir COMO guarda este WordPress/WooCommerce las "Tablas" de
YayPricing y donde esta la asignacion SKU -> Tabla, para poder construir
despues el UPDATE correcto.

NO modifica absolutamente nada. Solo hace SELECTs e imprime un reporte.

USO:
    1) Instala el conector si no lo tenes:   pip install pymysql
    2) Configura las credenciales por variables de entorno (NO se hardcodean
       en el archivo por seguridad). Ejemplo:

           export DB_HOST=167.250.5.80    # dentro del server usar 127.0.0.1
           export DB_PORT=3306
           export DB_USER=tu_usuario
           export DB_PASSWORD='tu_clave'
           export DB_NAME=tu_base
           export DB_PREFIX=wp_

       (o cargalas desde tu .env como ya hace test_db.py)
    3) Ejecuta:   python3 inspeccionar_yaypricing.py > reporte_yaypricing.txt
    4) Pasame el archivo reporte_yaypricing.txt (podes borrar/censurar lo que
       te parezca sensible; lo unico que necesito es la ESTRUCTURA).
"""

import os
import sys
import json

# ----------------------------------------------------------------------------
# CONFIG - se lee desde variables de entorno (no guardar secretos en el repo)
# ----------------------------------------------------------------------------
CONFIG = {
    "host": os.environ.get("DB_HOST", "127.0.0.1"),
    "port": int(os.environ.get("DB_PORT", "3306")),
    "user": os.environ.get("DB_USER", ""),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", ""),
    "prefix": os.environ.get("DB_PREFIX", "wp_"),
}
if not (CONFIG["user"] and CONFIG["database"]):
    sys.exit("Falta configuracion. Defini DB_USER, DB_PASSWORD, DB_NAME "
             "(y DB_HOST si no es 127.0.0.1) como variables de entorno.")
# ----------------------------------------------------------------------------

try:
    import pymysql
except ImportError:
    sys.exit("Falta el conector. Ejecuta:  pip install pymysql")


def main():
    p = CONFIG["prefix"]
    conn = pymysql.connect(
        host=CONFIG["host"], port=CONFIG["port"],
        user=CONFIG["user"], password=CONFIG["password"],
        database=CONFIG["database"], charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    print("=" * 70)
    print("CONEXION OK a", CONFIG["database"], "@", CONFIG["host"])
    print("=" * 70)

    with conn.cursor() as cur:

        # 1) Tablas relacionadas con yay / pricing -----------------------------
        print("\n### 1) TABLAS que contienen 'yay' o 'pricing' ###")
        cur.execute("""
            SELECT table_name, table_rows
            FROM information_schema.tables
            WHERE table_schema = %s
              AND (table_name LIKE '%%yay%%' OR table_name LIKE '%%pricing%%'
                   OR table_name LIKE '%%discount%%')
            ORDER BY table_name
        """, (CONFIG["database"],))
        yay_tables = cur.fetchall()
        if yay_tables:
            for t in yay_tables:
                print(f"   - {t['table_name']}  (~{t['table_rows']} filas)")
        else:
            print("   (ninguna tabla propia; probablemente usa wp_options)")

        # 2) Opciones en wp_options relacionadas -------------------------------
        print("\n### 2) wp_options con 'yay' / 'pricing' / 'discount' ###")
        cur.execute(f"""
            SELECT option_id, option_name, LENGTH(option_value) AS largo, autoload
            FROM {p}options
            WHERE option_name LIKE '%%yay%%'
               OR option_name LIKE '%%pricing%%'
               OR option_name LIKE '%%discount%%'
            ORDER BY largo DESC
        """)
        opts = cur.fetchall()
        for o in opts:
            print(f"   - {o['option_name']}  (largo={o['largo']}, autoload={o['autoload']})")

        # 2b) Volcar una muestra del contenido de las opciones mas grandes -----
        print("\n### 2b) MUESTRA del contenido de las opciones (primeros 1500 chars) ###")
        for o in opts[:6]:
            cur.execute(f"SELECT option_value FROM {p}options WHERE option_id=%s",
                        (o["option_id"],))
            val = cur.fetchone()["option_value"] or ""
            print(f"\n--- {o['option_name']} ---")
            print(val[:1500])
            if len(val) > 1500:
                print(f"... [+{len(val)-1500} chars mas]")

        # 3) Si hay tablas propias, mostrar su estructura + muestra ------------
        for t in yay_tables:
            tn = t["table_name"]
            print(f"\n### 3) ESTRUCTURA de {tn} ###")
            cur.execute(f"DESCRIBE `{tn}`")
            for col in cur.fetchall():
                print(f"   {col['Field']:30} {col['Type']}")
            print(f"\n   --- MUESTRA (hasta 5 filas) de {tn} ---")
            cur.execute(f"SELECT * FROM `{tn}` LIMIT 5")
            for row in cur.fetchall():
                print("   ", json.dumps(row, default=str, ensure_ascii=False)[:1200])

        # 4) Como se guarda el SKU (referencia para cruzar con el CSV) --------
        print("\n### 4) Verificacion de SKUs (wp_postmeta _sku) ###")
        cur.execute(f"""
            SELECT pm.post_id, pm.meta_value AS sku, p.post_type, p.post_status
            FROM {p}postmeta pm
            JOIN {p}posts p ON p.ID = pm.post_id
            WHERE pm.meta_key = '_sku'
              AND pm.meta_value IN ('3099','ADP-110','ADP111','CDPF-1.2NF','F20-10A')
            LIMIT 10
        """)
        rows = cur.fetchall()
        if rows:
            for r in rows:
                print(f"   SKU {r['sku']:15} -> post_id {r['post_id']} "
                      f"({r['post_type']}/{r['post_status']})")
        else:
            print("   No se encontraron esos SKUs de ejemplo en _sku (revisar meta_key).")

        # 5) Conteo total de productos con SKU --------------------------------
        cur.execute(f"""
            SELECT COUNT(*) AS n FROM {p}postmeta
            WHERE meta_key='_sku' AND meta_value <> ''
        """)
        print(f"\n### 5) Total de productos con _sku: {cur.fetchone()['n']}")

        # 6) Meta keys candidatos a guardar la 'Tabla' por producto -----------
        print("\n### 6) meta_keys que podrian guardar la 'Tabla' por producto ###")
        cur.execute(f"""
            SELECT DISTINCT meta_key FROM {p}postmeta
            WHERE meta_key LIKE '%%yay%%' OR meta_key LIKE '%%pricing%%'
               OR meta_key LIKE '%%tabla%%' OR meta_key LIKE '%%table%%'
               OR meta_key LIKE '%%discount%%'
            LIMIT 50
        """)
        mks = cur.fetchall()
        if mks:
            for m in mks:
                print("   -", m["meta_key"])
        else:
            print("   (ninguno; la asignacion NO esta en postmeta -> es por reglas)")

    conn.close()
    print("\n" + "=" * 70)
    print("FIN. Pasame este reporte para armar el UPDATE exacto.")
    print("=" * 70)


if __name__ == "__main__":
    main()
