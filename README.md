# PAGINA-WEB

## Workflow de resolución de problemas (`resolver-problemas`)

Este repo incluye una *skill* de Claude Code en `.claude/skills/resolver-problemas/` que define un workflow conversacional para resolver problemas junto a Claude.

### Cómo se usa

Abrí una sesión de Claude Code en este repo y contale un problema con tus palabras — por ejemplo:

> "Tengo un problema: las ventas de la tienda vienen cayendo hace dos meses y no sé por qué."

No hace falta invocar nada: la skill se activa sola cuando contás un problema. A partir de ahí, Claude sigue estas fases:

1. **Escuchar y reformular** — te devuelve el problema con sus palabras para verificar que entendió.
2. **Explorar con preguntas** — tandas cortas (máx. 3-4) sobre contexto, historia, impacto, intentos previos, restricciones y criterio de éxito.
3. **Definir el problema** — escribe una definición estructurada (situación actual, deseada, brecha, impacto, restricciones, criterio de éxito).
4. **Confirmar el entendimiento** — checkpoint obligatorio: no propone nada hasta que valides la definición.
5. **Analizar causas** — 5 porqués / Ishikawa, cuando el problema es "algo que falla".
6. **Generar soluciones** — 2 a 4 opciones genuinamente distintas, con pros, contras, esfuerzo y riesgo.
7. **Evaluar y recomendar** — comparación contra tu criterio de éxito y una recomendación fundamentada.
8. **Plan de acción** — pasos concretos, primer paso para hoy, cómo medir el resultado y plan B.

Para problemas chicos existe una **vía exprés** (reformulación + 2-3 preguntas + solución) para no inflar el proceso.

### Estructura

```
.claude/skills/resolver-problemas/
├── SKILL.md                        # El workflow: fases, reglas y situaciones especiales
└── references/
    ├── metodologias.md             # Investigación: Polya, McKinsey, 5 porqués, Ishikawa,
    │                               # GROW, método socrático, doble diamante, IDEAL
    └── banco-de-preguntas.md       # Preguntas por fase y por tipo de problema
```

El workflow está fundamentado en metodologías probadas de resolución de problemas; `references/metodologias.md` documenta cada una, sus fuentes y qué fase del workflow la usa.

### Versión para cualquier chatbot

En `prompts/resolver-problemas-chatbot.md` hay una versión autocontenida del workflow como prompt: copialo y pegalo como primer mensaje en cualquier chatbot (Claude, ChatGPT, Gemini, etc.) y después contale tu problema.
