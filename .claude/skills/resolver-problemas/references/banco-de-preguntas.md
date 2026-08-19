# Banco de preguntas por fase y tipo de problema

Preguntas de referencia para la Fase 2 (explorar) y la Fase 5 (causas). No son un formulario: elegir las 2-4 de mayor rendimiento para el turno, adaptar la redacción al registro del usuario y seguir los hilos que se abran.

## Por dimensión (Fase 2)

### Contexto
- ¿Quiénes están involucrados y qué rol tiene cada uno?
- ¿A quién le duele más este problema hoy: a vos, a un cliente, a tu equipo?
- ¿Dónde pasa exactamente? (sistema, lugar, relación, proceso)
- ¿Con qué frecuencia pasa? ¿Todos los días, a veces, una sola vez?

### Historia
- ¿Desde cuándo pasa esto?
- ¿Qué cambió justo antes de que empezara? (deploy, decisión, persona nueva, mudanza…)
- ¿Hubo alguna época en que esto funcionaba bien? ¿Qué era distinto entonces?
- ¿Cuándo NO pasa? ¿Hay excepciones?

### Impacto
- ¿Qué te está costando hoy, en concreto? (tiempo, plata, clientes, energía)
- Si no hacés nada y pasan tres meses, ¿qué pasa?
- Del 1 al 10, ¿qué tan urgente es esto contra todo lo demás que tenés?
- ¿Hay algo o alguien más afectado que todavía no mencionaste?

### Intentos previos
- ¿Qué probaste ya? ¿Qué pasó con cada intento?
- ¿Por qué creés que eso no funcionó?
- ¿Hay algo que descartaste sin probar? ¿Por qué?
- ¿Alguien más intentó resolver esto antes que vos?

### Restricciones
- ¿Para cuándo necesitás que esté resuelto?
- ¿Qué presupuesto/recursos hay? ¿Quién más puede ayudar?
- ¿Hay algo que NO estás dispuesto a hacer o cambiar?
- ¿Quién tiene que aprobar la solución, además de vos?

### Criterio de éxito
- Si mañana te levantás y el problema está resuelto, ¿qué es lo primero que notás distinto?
- ¿Cómo vas a medir que se resolvió? ¿Qué señal observable lo confirma?
- ¿Qué sería "suficientemente bueno", aunque no sea perfecto?

## Por tipo de problema

### Algo que falla (técnico / proceso roto)
- ¿Podés reproducirlo? ¿Qué pasos exactos lo disparan?
- ¿Qué dice el error, textualmente? / ¿Qué se ve cuando falla?
- ¿Falla siempre o a veces? ¿Hay patrón (hora, carga, usuario, dato)?
- ¿Qué versión/configuración/entorno? ¿Es igual en otro entorno?
- ¿Qué fue lo último que cambió antes de la primera falla?

### Una decisión a tomar
- ¿Cuáles son las opciones sobre la mesa hoy? ¿Descartaste alguna ya?
- ¿Qué es lo que más pesa en esta decisión: plata, tiempo, riesgo, lo que opinen otros?
- ¿Qué te frena de decidir ya? ¿Qué dato te falta?
- ¿Es reversible? Si elegís mal, ¿qué cuesta volver atrás?
- ¿Para cuándo tenés que decidir? ¿Qué pasa si no decidís?

### Una meta bloqueada
- ¿Qué querés lograr, en concreto? ¿Cómo se ve el resultado final?
- ¿Qué intentaste para avanzar y dónde te trabás exactamente?
- ¿Es que no sabés cómo seguir, o sabés cómo pero algo te lo impide?
- ¿Qué parte SÍ está avanzando o ya lograste?

### Conflicto con personas
- ¿Qué pasó, en hechos? (separar hechos de interpretaciones)
- ¿Cómo creés que la otra persona describe esta misma situación?
- ¿Qué necesitás vos de esa relación? ¿Qué creés que necesita el otro?
- ¿Ya hablaron del tema directamente? ¿Cómo salió?
- ¿Qué resultado sería aceptable para vos, aunque no sea el ideal?

### Malestar difuso ("algo no anda bien")
- Contame la última vez que sentiste eso fuerte. ¿Qué estaba pasando?
- Si tuvieras que apostar a una sola causa, ¿cuál sería?
- ¿En qué momentos NO lo sentís?
- ¿Es nuevo o viene de lejos? ¿Qué lo hizo más notorio ahora?

## Para excavar causas (Fase 5)

- ¿Y eso por qué pasa? (el porqué encadenado; validar cada eslabón con el usuario)
- Si arreglaras solo ese último eslabón, ¿el problema desaparece o vuelve por otro lado?
- ¿La causa está en las personas, el proceso, las herramientas, los insumos, el entorno o cómo se mide? (recorrer categorías Ishikawa cuando la cadena no es lineal)
- ¿Dónde/cuándo/a qué afecta — y dónde/cuándo/a qué NO? (Es / No-es)

## Cambios de ángulo ante respuestas vagas

| Si el usuario dice... | Probar con... |
|---|---|
| "No sé, siempre fue así" | "¿Cuál fue la última vez que lo notaste? Contame esa vez puntual." |
| "Todo anda mal" | "Si pudieras arreglar UNA sola cosa esta semana, ¿cuál elegirías?" |
| "Más o menos / a veces" | Cuantificar: "¿cuántas veces esta semana?" o AskUserQuestion con rangos |
| "Ya probé todo" | "Nombrame las últimas dos cosas que probaste y qué pasó con cada una." |
| Respuestas de una palabra | Cerrar la tanda, reformular lo que hay y confirmar; a veces la vaguedad es señal de que la pregunta no era la importante |
