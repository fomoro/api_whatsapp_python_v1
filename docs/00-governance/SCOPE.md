# Alcance de Descubrimiento de Pipe

**Estado:** Aprobado  
**Fecha:** 2026-08-19  
**Sponsor:** Carlos Moreno  
**Product Owner:** Sr. Wolfan  
**Fase:** Descubrimiento

---

## 1. Objetivo

Extraer exhaustivamente los insumos secundarios de Frisby en `DISCOVERY.md` y utilizar sus escenarios como hoja de ruta inicial para probar después el referente en WhatsApp. Los resultados observados construirán directamente una línea base funcional autosuficiente con las capacidades, contenido, datos, reglas y caminos del espejo interno. Esta línea base servirá para proponer los flujos propios de Pipe y el alcance de su MVP comercial.

El espejo conserva la experiencia observada como evidencia del caso de estudio. No demuestra cómo están construidos los sistemas internos de Frisby ni convierte automáticamente cada comportamiento en un requisito de Pipe.

---

## 2. Alcance incluido

- Analizar exhaustivamente `docs/01-discovery/inputs/frisby/FRISBY_1.MD` y `FRISBY_2.HTM` como insumos secundarios.
- Consolidar sus capacidades, escenarios, reglas, decisiones, datos, anomalías y vacíos en `DISCOVERY.md` sin presentarlos todavía como confirmados.
- Usar ChatGPT sobre una sesión autorizada de WhatsApp para recorrer de forma controlada todos los caminos conocidos o alcanzables del bot de Frisby.
- Registrar directamente en `docs/02-functional/FUNCTIONAL_BASELINE.md` los resultados obtenidos en WhatsApp, sin actualizar Discovery con evidencia primaria.
- Mantener la línea base funcional autosuficiente para que arquitectura, desarrollo y pruebas no dependan de `DISCOVERY.md` ni de los insumos secundarios para comprender el comportamiento observado.
- Registrar exactamente entradas, textos, marca, imágenes, productos, precios, respuestas, opciones, decisiones, validaciones, resultados y puntos de salida observados.
- Utilizar datos reales, sin sustituirlos por datos sintéticos.
- Ejecutar compras reales cuando el escenario, presupuesto, operador y punto de confirmación estén aprobados.
- Identificar caminos principales, alternos, errores, retornos, cancelaciones y comportamientos incompletos cuando sean observables.
- Clasificar dentro de la línea base cada hallazgo como **Confirmado**, **Parcial**, **Pendiente** o **Descartado**.
- Elaborar el mapa de capacidades de negocio y capacidades funcionales observadas.
- Documentar los flujos AS-IS y sus vacíos.
- Identificar dependencias externas y riesgos aparentes sin asumir su implementación interna.
- Proponer los flujos objetivo de Pipe y el alcance candidato del MVP.

“Todos los caminos” comprende los caminos conocidos o accesibles durante recorridos controlados. No incluye rutas ocultas, condiciones internas ni comportamientos que no puedan observarse o reproducirse; estos se registrarán como pendientes.

---

## 3. Fuera de alcance

- Publicar, distribuir u operar comercialmente el espejo antes de transformarlo en Pipe.
- Ejecutar pedidos, pagos, registros u otras acciones irreversibles sin las aprobaciones establecidas.
- Capturar credenciales, tokens, códigos de autenticación o datos completos del medio de pago.
- Realizar ingeniería inversa de código, infraestructura o sistemas internos del referente.
- Definir como ciertos contratos, algoritmos o integraciones no observables.
- Implementar Pipe o construir el MVP durante el Descubrimiento.
- Diseñar la arquitectura detallada, estimar fechas o comprometer costos antes de aprobar el MVP.

---

## 4. Método de investigación

1. Exprimir los insumos secundarios y registrar sus afirmaciones como pendientes.
2. Organizar capacidades, escenarios, reglas, datos, anomalías y vacíos en `DISCOVERY.md` y cerrar la extracción documental.
3. Tomar de Discovery el escenario inicial, las preguntas y los vacíos que orientarán la prueba, sin copiar sus afirmaciones como hechos.
4. Definir los datos reales requeridos, el presupuesto y el punto de confirmación del escenario.
5. Obtener las aprobaciones aplicables antes de controlar WhatsApp o ejecutar una acción irreversible.
6. Recorrer con ChatGPT una rama de WhatsApp a la vez y registrar la evidencia primaria.
7. Documentar directamente en `FUNCTIONAL_BASELINE.md` lo observado, resolver allí las reglas y vacíos aplicables, y agregar los nuevos caminos, errores o dudas que surjan.

El Sponsor aprueba el presupuesto; el Product Owner aprueba el escenario; el PMO verifica las condiciones y registra el resultado. El operador autorizado confirma la compra o acción irreversible en el momento de ejecutarla.

---

## 5. Entregables

- Inventario de evidencia disponible.
- Matriz de escenarios y recorridos.
- Mapa de capacidades de negocio y funcionales.
- Espejo interno del contenido y comportamiento observable.
- Flujos AS-IS con decisiones y estados esenciales.
- Registro priorizado de vacíos, pendientes y riesgos.
- Propuesta de flujos objetivo de Pipe.
- Propuesta de alcance del MVP.

La extracción de los insumos secundarios se consolida exclusivamente en `docs/01-discovery/DISCOVERY.md`. Los resultados de WhatsApp, el espejo observable y sus pendientes se consolidan exclusivamente en `docs/02-functional/FUNCTIONAL_BASELINE.md`, que no depende de Discovery para su comprensión.

---

## 6. Manejo de datos y evidencia

- La investigación utiliza datos reales; no emplea datos sintéticos para sustituir la validación del recorrido.
- Los insumos secundarios sin enmascarar se conservan en `docs/01-discovery/inputs/frisby/` y permanecen fuera del control de versiones.
- La evidencia original se conserva sin enmascarar en `private-evidence/frisby/`.
- La evidencia privada permanece fuera del control de versiones y con acceso limitado al equipo autorizado.
- Los documentos versionados referencian la evidencia por identificador y no duplican su contenido sensible.
- Credenciales, tokens, códigos de autenticación y datos completos del medio de pago no se capturan ni se consideran evidencia funcional.
- Cada evidencia registra procedencia y fecha porque productos, precios y comportamientos pueden cambiar.

---

## 7. Gobierno aplicable

Las autoridades y responsabilidades se mantienen únicamente en `docs/00-governance/PROJECT_CHARTER.md`. Este documento define cómo se aplican al alcance de investigación y no replica la tabla de gobierno.

---

## 8. Criterios de salida

El Descubrimiento se considerará terminado cuando:

- Los caminos conocidos o alcanzables estén registrados como confirmados, parciales, pendientes o descartados.
- Los flujos observados tengan evidencia y procedencia identificables.
- El contenido y los datos observados estén reflejados en la línea base funcional autosuficiente.
- Las reglas candidatas utilizadas para orientar las pruebas hayan sido confirmadas, ajustadas o descartadas; ninguna se trate como implementable mientras permanezca pendiente.
- Los escenarios autorizados de compra real tengan resultado y evidencia registrados.
- Los vacíos funcionales y de información estén registrados y priorizados.
- Los riesgos principales estén identificados.
- Exista una propuesta de flujos objetivo para Pipe.
- Exista una propuesta de alcance para el MVP.

Los pendientes que dependan de rutas no accesibles o información interna no impedirán cerrar la fase si están identificados junto con su impacto.

---

## 9. Restricciones y riesgos iniciales

- El comportamiento del referente puede cambiar durante la investigación.
- Algunas rutas pueden depender de ubicación, horario, catálogo, historial u otras condiciones no disponibles.
- La evidencia existente puede estar incompleta o desactualizada.
- Los dos insumos secundarios se superponen y no constituyen validaciones independientes entre sí.
- El acceso a WhatsApp y las condiciones de prueba deben confirmarse antes de iniciar recorridos.
- Las compras reales generan costos y efectos operativos que requieren presupuesto y confirmación previa.
- La evidencia sin enmascarar exige almacenamiento privado y control de acceso.

---

## 10. Aprobación y acción siguiente

**Aprobación del Sponsor:** Carlos Moreno — Aprobado el 2026-08-19  
**Aprobación del Product Owner:** Sr. Wolfan — Aprobado el 2026-08-19

La secuencia posterior se mantiene exclusivamente en `docs/00-governance/ROADMAP.md`.
