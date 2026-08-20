# Acta de Constitución del Proyecto Pipe

**Estado:** Aprobado  
**Fecha:** 2026-08-19  
**Sponsor:** Carlos Moreno  
**Product Owner:** Sr. Wolfan  
**Propósito:** Producto comercial para restaurantes de pollo frito  
**Nivel actual:** Caso de Estudio  
**Fase actual:** Descubrimiento

---

## 1. Contexto y objetivo

Pipe busca convertirse en un bot conversacional determinístico para WhatsApp, basado en reglas, opciones y flujos controlados. Estará dirigido a clientes que realizan pedidos en restaurantes de pollo frito.

El objetivo del proyecto es construir una solución comercial para restaurantes de pollo frito, tomando el bot de Frisby como referencia funcional. `DISCOVERY.md` extrae exhaustivamente los insumos secundarios y queda como antecedente documental. Sus escenarios orientan después los recorridos controlados en WhatsApp, cuyos resultados construyen directamente una línea base funcional autosuficiente para reconstruir la experiencia observable, resolver vacíos y proponer el alcance del MVP.

El caso de estudio conservará en un espejo interno los textos, marca, productos, precios, datos y comportamientos observados. Después, el MVP comercial adoptará identidad, contenido, datos y solución propios. Los documentos y recorridos del referente siguen siendo evidencia por validar, no una fuente absoluta de verdad sobre sus sistemas internos.

---

## 2. Alcance actual

El alcance vigente comprende la investigación controlada del referente, la construcción del espejo interno observable y la propuesta posterior del MVP de Pipe. Las inclusiones, exclusiones, controles, entregables y criterios de salida se definen únicamente en `docs/00-governance/SCOPE.md`.

---

## 3. Principios de trabajo

- Separar evidencia, inferencias, decisiones y pendientes.
- Usar datos reales durante la investigación y conservar la evidencia original sin enmascarar en almacenamiento privado no versionado.
- No sustituir con datos sintéticos la validación de los recorridos reales.
- Aplicar KISS, YAGNI y gobierno proporcional.
- Diseñar únicamente capacidades confirmadas o aprobadas.
- Mantener trazabilidad desde el flujo hasta la implementación y la prueba.

---

## 4. Gobierno y responsabilidades

| Rol | Responsabilidad | Autoridad |
|---|---|---|
| Sponsor — Carlos Moreno | Patrocinio y continuidad | Aprueba inversión, presupuesto de pruebas y cambios materiales de alcance |
| Product Owner — Sr. Wolfan | Visión, prioridad y valor | Aprueba escenarios, capacidades, flujos objetivo y MVP |
| PMO | Alcance, fases, roadmap, riesgos y seguimiento | Coordina y verifica las condiciones aprobadas; no autoriza inversión ni decide arquitectura |
| Analista Funcional | Investigación, evidencia y flujos | Propone el entendimiento funcional |
| Arquitecto de Soluciones | Coherencia end-to-end | Lidera la arquitectura de solución |
| Arquitecto de Integraciones | Meta y sistemas externos | Define contratos, webhooks y dependencias externas |
| Arquitecto de Software | Módulos, motor conversacional y repositorio | Define la estructura interna del software |
| Arquitecto de Datos | Información y persistencia | Define modelos, integridad e idempotencia |
| Backend Python | Implementación y pruebas | Decide detalles dentro de la arquitectura aprobada |
| Escritor Técnico | Consistencia y trazabilidad documental | Mantiene la documentación vigente |

El PMO supervisa proceso, compromisos y riesgos. El Arquitecto de Soluciones supervisa la coherencia técnica. El Sponsor y el Product Owner conservan la autoridad sobre inversión, alcance y valor.

---

## 5. Fases previstas

| Fase | Resultado | Lidera | Salida |
|---|---|---|---|
| 0. Inicio | Gobierno y alcance inicial | PMO y Sponsor | Acta aprobada |
| 1. Descubrimiento | Cierre de la extracción documental y construcción progresiva de la línea base mediante WhatsApp | Analista Funcional | Línea base funcional autosuficiente, caminos contrastados, vacíos y riesgos identificados, y alcance del MVP propuesto |
| 2. Definición de producto | Flujos objetivo y alcance del MVP | Product Owner y Analista | Story Map y alcance aprobados |
| 3. Arquitectura | Solución y diseño detallado suficientes | Arquitecto de Soluciones y equipo | Contratos y decisiones implementables |
| 4. MVP — condicionado | Flujo priorizado construido y probado | Equipo técnico | Criterios de aceptación superados |
| 5. Piloto y operación — condicionado | Servicio validado y soportable | Product Owner, pruebas y operación | Decisión de continuidad |

Las fases 3 a 5 se autorizan progresivamente. El PMO las coordina, pero no reemplaza la validación funcional ni técnica.

---

## 6. Decisiones y pendientes

### Decisiones

- Carlos Moreno es el Sponsor y Sr. Wolfan es el Product Owner.
- Pipe será una solución comercial para restaurantes de pollo frito y comienza como Caso de Estudio en fase de Descubrimiento.
- Los usuarios principales son los clientes que realizan pedidos.
- Primero se extraerán exhaustivamente los insumos secundarios ubicados en `docs/01-discovery/inputs/frisby/` y se consolidarán como pendientes en `DISCOVERY.md`.
- Una vez cerrada la extracción documental, `DISCOVERY.md` se utilizará únicamente como hoja de ruta inicial y no se actualizará con los resultados de WhatsApp.
- Los caminos se investigarán mediante WhatsApp y con apoyo controlado de ChatGPT; sus resultados se registrarán directamente en `docs/02-functional/FUNCTIONAL_BASELINE.md`.
- La línea base funcional será autosuficiente: incluirá dentro de sí los comportamientos observados, capacidades, datos, reglas, escenarios, errores, nuevos caminos, pendientes y trazabilidad necesarios para comprender el referente.
- Para arquitectura, desarrollo y pruebas, `FUNCTIONAL_BASELINE.md` prevalecerá sobre `DISCOVERY.md`; solo los elementos confirmados o aprobados podrán tratarse como implementables.
- El espejo interno conservará exactamente el contenido y los datos observados; el MVP comercial tendrá identidad, contenido, datos y solución propios.
- La investigación utilizará datos reales y podrá incluir compras reales previamente aprobadas.
- La evidencia original permanecerá sin enmascarar en almacenamiento privado y fuera del control de versiones.
- El Descubrimiento termina con flujos validados, vacíos y riesgos identificados, y una propuesta de alcance para el MVP.
- No se requieren validadores adicionales del alcance.
- `poc/` conserva el POC operativo existente, separado del desarrollo futuro y sin refactorizar su código interno.
- La arquitectura de referencia solo se evaluará si el MVP o piloto demuestra patrones reutilizables.

### Pendientes

- Completar los caminos faltantes del referente.
- Seleccionar el flujo candidato para el MVP.
- Definir el presupuesto, los escenarios y el operador autorizado antes de ejecutar compras reales.
- Confirmar sistemas externos, datos y acceso de prueba a Meta.
- Estimar esfuerzo, costos y fechas después del descubrimiento.

---

## 7. Artefactos y ubicación prevista

| Artefacto | Ubicación | Contenido y responsabilidad exclusiva |
|---|---|---|
| Acta de Constitución | `docs/00-governance/PROJECT_CHARTER.md` | Objetivo, autoridad, fases y decisiones rectoras; no contiene el detalle operativo |
| Alcance | `docs/00-governance/SCOPE.md` | Inclusiones, exclusiones, restricciones, entregables y criterios de salida; no contiene cronograma ni escenarios individuales |
| Roadmap | `docs/00-governance/ROADMAP.md` | Resultados, secuencia, dependencias e hitos; no descompone tareas ni diseña la solución |
| Insumos secundarios de Frisby | `docs/01-discovery/inputs/frisby/` | Documentos previos que se explotan antes de WhatsApp; contienen datos reales, no se versionan y no confirman por sí solos el comportamiento actual |
| Evidencia privada original | `private-evidence/frisby/` | Chats, capturas, comprobantes y datos reales sin enmascarar; no se versiona ni se duplica en los documentos |
| Descubrimiento documental | `docs/01-discovery/DISCOVERY.md` | Extracción exhaustiva de los insumos secundarios, capacidades, datos, reglas candidatas, escenarios, diagramas, vacíos, anomalías y cobertura; queda cerrado como antecedente y hoja de ruta inicial para WhatsApp |
| Línea base funcional | `docs/02-functional/FUNCTIONAL_BASELINE.md` | Fuente funcional autosuficiente construida directamente mediante recorridos en WhatsApp; consolida validaciones, capacidades, datos, reglas confirmadas, escenarios, errores, nuevos caminos, pendientes y cobertura real |
| POC operativo existente | `poc/` | Implementación experimental funcional que debe preservarse; no define por sí sola la arquitectura futura de Pipe |

Cada información se mantiene en su artefacto responsable. Los diagramas documentales permanecen en `DISCOVERY.md`; los diagramas y recorridos observados se mantienen íntegramente en `FUNCTIONAL_BASELINE.md`, sin depender de Discovery para su comprensión. Los documentos de producto, arquitectura, entrega y operación se crearán únicamente cuando se autoricen esas fases y exista contenido real que documentar.

---

## 8. Validación y acción siguiente

**Aprobación del Sponsor:** Carlos Moreno — Aprobado el 2026-08-19  
**Aprobación del Product Owner:** Sr. Wolfan — Aprobado el 2026-08-19

1. Cerrar la extracción documental consolidada en `DISCOVERY.md`.
2. Crear la estructura autosuficiente de `FUNCTIONAL_BASELINE.md`.
3. Autorizar el recorrido SCN-001 en WhatsApp para iniciar su construcción con evidencia primaria.
