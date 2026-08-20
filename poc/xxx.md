# Acta de Constitución del Proyecto Pipe

**Estado:** Borrador inicial para validación  
**Fecha de creación:** 2026-08-19  
**Sponsor:** Carlos Morenos  
**Product Owner:** Sr. Wolfan  
**Madurez actual:** Caso de Estudio / Descubrimiento

---

## 1. Propósito

Pipe será un bot conversacional determinístico para WhatsApp, basado en reglas, opciones predefinidas y flujos controlados.

El proyecto busca entender, diseñar, construir y validar una experiencia conversacional inspirada en patrones observados en el bot de Frisby, sin copiar su marca, textos, catálogo, precios, datos ni activos.

Los documentos y recorridos de Frisby son fuentes de evidencia. No constituyen por sí mismos requisitos ni una fuente absoluta de verdad.

---

## 2. Objetivo inicial

Definir una versión funcionalmente validada de Pipe y construir un MVP del flujo priorizado, con arquitectura suficiente para evolucionar de forma controlada y operar sobre WhatsApp Cloud API.

---

## 3. Alcance inicial

### Incluye

- Investigación controlada de bots y documentos de referencia.
- Identificación de capacidades de negocio y funcionales.
- Documentación de flujos, reglas, alternativas, errores y vacíos.
- Definición de los flujos objetivo de Pipe.
- Story Mapping y selección del alcance del MVP.
- Arquitectura de solución y arquitectura detallada proporcional.
- Diseño de integraciones, software, datos y operación.
- Implementación, pruebas y validación controlada del MVP aprobado.

### No incluye por ahora

- Copia literal del bot, marca o catálogo de Frisby.
- Confirmación de compras, pagos o registros reales durante la investigación.
- Implementación de todos los caminos observados antes de priorizar el MVP.
- Fechas, costos o compromisos de producción sin estimación y aprobación.
- Arquitectura de referencia corporativa antes de validar patrones reutilizables.

---

## 4. Gobierno y responsabilidades

| Rol | Responsabilidad principal | Autoridad |
|---|---|---|
| Sponsor — Carlos Morenos | Patrocinar el proyecto y resolver decisiones de inversión o continuidad | Aprueba continuidad, presupuesto y cambios materiales de alcance |
| Product Owner — Sr. Wolfan | Definir visión, prioridades, reglas y valor esperado | Aprueba capacidades, flujos objetivo y alcance del MVP |
| PMO | Organizar alcance, fases, roadmap, EDT, dependencias, riesgos y seguimiento | Coordina el proceso; no aprueba decisiones técnicas |
| Analista Funcional | Investigar, levantar evidencia y construir la verdad funcional | Propone capacidades y flujos; no convierte inferencias en requisitos |
| Arquitecto de Soluciones | Mantener la coherencia end-to-end de la solución | Lidera la arquitectura de solución y coordina la arquitectura detallada |
| Arquitecto de Integraciones | Diseñar contratos con Meta y otros sistemas | Define APIs, webhooks, mensajes, errores y dependencias externas |
| Arquitecto de Software | Diseñar módulos, motor conversacional y estructura técnica | Define la organización interna del software y del repositorio |
| Arquitecto de Datos | Diseñar información, integridad y persistencia | Define modelos, relaciones, estados e idempotencia |
| Desarrollador Backend Python | Implementar y verificar la solución aprobada | Decide detalles de implementación dentro de la arquitectura acordada |
| Escritor Técnico | Mantener documentación verificable y trazable | Controla consistencia documental, no decisiones de negocio |

El PMO supervisa el cumplimiento del proceso, los compromisos y los riesgos. El Arquitecto de Soluciones supervisa la coherencia técnica. El Sponsor y el Product Owner conservan la autoridad sobre inversión, alcance y valor.

---

## 5. Fases previstas

| Fase | Resultado esperado | Lidera | Criterio de salida |
|---|---|---|---|
| 0. Inicio | Propósito, gobierno, alcance inicial y riesgos identificados | PMO y Sponsor | Acta validada y siguiente fase autorizada |
| 1. Descubrimiento | Capacidades y flujos del referente clasificados por evidencia | Analista Funcional | Caminos observados, vacíos y preguntas trazables |
| 2. Definición de producto | Comportamiento objetivo y MVP priorizado | Product Owner y Analista Funcional | Story Map, reglas y flujos objetivo aprobados |
| 3. Arquitectura de solución | Entendimiento end-to-end y decisiones principales | Arquitecto de Soluciones | Contexto, alcance técnico y atributos de calidad acordados |
| 4. Arquitectura detallada | Diseño implementable de componentes, integraciones y datos | Equipo de Arquitectura | Contratos, estados, secuencias, datos y decisiones suficientes |
| 5. Construcción del MVP | Flujo priorizado implementado y verificado | Backend Python | Criterios de aceptación y pruebas superados |
| 6. Validación y piloto | Operación comprobada en ambiente controlado | PMO y equipo | Riesgos operativos controlados y decisión de continuidad |
| 7. Operación | Servicio soportable y observable | Operaciones | Runbook, soporte, monitoreo y responsables definidos |

Las fases pueden solaparse de manera controlada, pero ninguna debe convertir pendientes funcionales en decisiones técnicas definitivas.

---

## 6. Fuentes y trazabilidad

La información del proyecto se organiza en cuatro niveles:

1. **Evidencia original:** conversaciones, capturas y documentos sin reinterpretar.
2. **Análisis AS-IS:** capacidades y flujos observados, diferenciando confirmado, inferido y pendiente.
3. **Diseño objetivo de Pipe:** decisiones aprobadas sobre qué adoptar, modificar o descartar.
4. **Contratos implementables:** estados, reglas, integraciones, datos y criterios de aceptación.

El documento funcional objetivo de Pipe será la fuente de verdad una vez validado por el Product Owner. Los documentos de Frisby permanecerán como evidencia de referencia.

---

## 7. Artefactos y ubicación prevista

| Artefacto | Ubicación | Momento |
|---|---|---|
| Acta de Constitución | `docs/00-governance/PROJECT_CHARTER.md` | Inicio |
| Alcance | `docs/00-governance/SCOPE.md` | Inicio y refinamiento continuo |
| Roadmap | `docs/00-governance/ROADMAP.md` | Preliminar al inicio; ajustado después de descubrimiento |
| EDT | `docs/00-governance/EDT.md` | Inicial a alto nivel; refinada después de arquitectura |
| Evidencia de Frisby | `docs/01-discovery/evidence/frisby/` | Descubrimiento |
| Registro de evidencia | `docs/01-discovery/EVIDENCE_REGISTER.md` | Descubrimiento |
| Flujos AS-IS | `docs/01-discovery/AS_IS_FLOWS.md` | Descubrimiento |
| Story Map | `docs/02-product/STORY_MAP.md` | Definición de producto |
| Especificación funcional de Pipe | `docs/02-product/PIPE_FUNCTIONAL_SPEC.md` | Definición de producto |
| Alcance del MVP | `docs/02-product/MVP_SCOPE.md` | Definición de producto |
| Entendimiento de solución | `docs/03-architecture/SOLUTION_OVERVIEW.md` | Arquitectura de solución |
| Arquitectura detallada | `docs/03-architecture/DETAILED_ARCHITECTURE.md` | Arquitectura detallada |
| Integraciones | `docs/03-architecture/INTEGRATIONS.md` | Arquitectura detallada |
| Arquitectura de datos | `docs/03-architecture/DATA_ARCHITECTURE.md` | Arquitectura detallada |
| Operación y soporte | `docs/05-operations/` | Antes del piloto |

La EDT organiza trabajo, no carpetas de código. La estructura técnica del repositorio será propuesta por el Arquitecto de Software cuando exista suficiente entendimiento funcional.

---

## 8. Decisiones iniciales

- Pipe comienza como Caso de Estudio / Descubrimiento.
- Carlos Morenos es el Sponsor del proyecto.
- Sr. Wolfan actúa inicialmente como Product Owner.
- Frisby se utiliza como referente funcional observable, no como especificación oficial.
- El PMO coordina gobierno y entrega; no reemplaza la autoridad funcional ni técnica.
- La arquitectura de referencia se evaluará después del MVP o piloto, si existen patrones reutilizables.
- La carpeta `new/` fue retirada después de trasladar los insumos de Frisby a `docs/01-discovery/inputs/frisby/`; `poc/` conserva el POC operativo existente.

---

## 9. Riesgos y pendientes iniciales

- Confirmar el objetivo comercial y los usuarios finales de Pipe.
- Definir cuál flujo aporta mayor valor para el primer MVP.
- Validar caminos incompletos del referente Frisby.
- Confirmar sistemas externos, datos disponibles y restricciones de integración.
- Confirmar acceso de prueba y configuración de WhatsApp Cloud API.
- Definir identidad, tono y políticas propias de Pipe.
- Estimar esfuerzo, costos y fechas después del descubrimiento y la arquitectura inicial.

---

## 10. Acción siguiente

1. Validar esta acta con el Sponsor y el Product Owner.
2. Elaborar el alcance inicial y el roadmap por resultados.
3. Inventariar la evidencia disponible sin alterar sus fuentes.
4. Preparar la matriz de escenarios para continuar el levantamiento funcional de Frisby.


api_whatsapp_python_v1/
├── .agents/
├── docs/
│   ├── 00-governance/
│   │   ├── PROJECT_CHARTER.md
│   │   ├── SCOPE.md
│   │   ├── ROADMAP.md
│   │   ├── EDT.md
│   │   └── RISKS_AND_DECISIONS.md
│   │
│   ├── 01-discovery/
│   │   ├── evidence/
│   │   │   └── frisby/
│   │   ├── EVIDENCE_REGISTER.md
│   │   ├── CAPABILITY_MAP.md
│   │   ├── AS_IS_FLOWS.md
│   │   └── GAPS_AND_QUESTIONS.md
│   │
│   ├── 02-product/
│   │   ├── PRODUCT_VISION.md
│   │   ├── STORY_MAP.md
│   │   ├── PIPE_FUNCTIONAL_SPEC.md
│   │   ├── BUSINESS_RULES.md
│   │   └── MVP_SCOPE.md
│   │
│   ├── 03-architecture/
│   │   ├── SOLUTION_OVERVIEW.md
│   │   ├── DETAILED_ARCHITECTURE.md
│   │   ├── INTEGRATIONS.md
│   │   ├── DATA_ARCHITECTURE.md
│   │   └── adr/
│   │
│   ├── 04-delivery/
│   │   ├── ACCEPTANCE_CRITERIA.md
│   │   └── TEST_STRATEGY.md
│   │
│   └── 05-operations/
│       ├── RUNBOOK.md
│       ├── SUPPORT_MODEL.md
│       └── SERVICE_CATALOG.md
│
├── src/
│   └── pipe/
├── tests/
├── scripts/
├── README.md
└── .env.example
