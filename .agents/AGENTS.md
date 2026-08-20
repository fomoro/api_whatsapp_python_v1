# Roles y gobernanza de agentes del proyecto Pipe

**Proyecto:** Pipe — Bot conversacional para WhatsApp
**Autor:** Sr. Wolfan
**Enfoque:** Bot conversacional determinístico basado en reglas y opciones, desarrollado en Python e integrado con WhatsApp Cloud API.

---

## 1. Propósito y alcance

Este archivo define la gobernanza local del proyecto Pipe, un bot conversacional para WhatsApp basado en reglas, opciones predefinidas y flujos controlados.

El proyecto comprende el backend en Python, la integración con WhatsApp Cloud API, la persistencia necesaria, el despliegue y la documentación asociada.

Sus reglas aplican a todo el proyecto. Las reglas globales del asistente continúan vigentes salvo cuando este archivo establezca una instrucción local más específica.

---

## 2. Precedencia y gobernanza local

La gobernanza local complementa las reglas globales y prevalece únicamente cuando define una instrucción más específica para este proyecto o una de sus carpetas.

Al trabajar sobre una carpeta:

1. Identificar el agente responsable según este archivo.
2. Aplicar sus responsabilidades y criterios de salida.
3. Consultar en `.agents/skills/` únicamente las skills relevantes para la tarea.
4. Mantener las reglas globales que no entren en conflicto con la gobernanza local.

Ante solapamiento entre agentes, priorizar el más específico al contexto de la tarea.

---

## 3. Skills y especialización

`.agents/skills/` contiene las habilidades especializadas disponibles para el proyecto.

Los agentes utilizan únicamente las skills relevantes para la tarea y la carpeta activa. Las skills complementan esta gobernanza y no reemplazan las responsabilidades ni los criterios de salida definidos en este archivo.

No se inventan skills, reglas o comportamientos que no estén definidos en la gobernanza global, este archivo o las skills disponibles.

---

## 4. Meta-reglas para evolución de agentes y skills

* **Abstracción sobre implementación:** Al definir o ajustar una skill, priorizar reglas, principios de comportamiento y patrones arquitectónicos sobre componentes estáticos específicos.

* **Especialización progresiva:** Incorporar una regla en una skill cuando sea específica, reutilizable y suficientemente estable; evitar trasladar detalles circunstanciales del proyecto.

* **Propósito:** Mantener contexto estructural suficiente sin limitar innecesariamente la capacidad de adaptar soluciones cuando cambien requisitos o tecnologías.

* **Cambios de ubicación y triple validación:** Antes de mover o renombrar archivos, identificar sus referencias en documentos, skills y configuración. Después del cambio, actualizar todas las rutas y ejecutar tres validaciones independientes: 1) búsqueda de referencias antiguas, 2) existencia y protección de las rutas nuevas y 3) coherencia semántica entre gobernanza, skills y documentación. El cambio no se considera terminado hasta superar las tres validaciones.

---

## 5. Agentes especializados del proyecto

* **Agente 1: Arquitecto de Integraciones y Especialista en Meta/WhatsApp Cloud API**

  * Responsabilidad: Diseñar y validar webhooks, contratos, autenticación, seguridad, versionamiento y flujos de envío y recepción de mensajes con la plataforma Meta.

* **Agente 2: Desarrollador Backend Python**

  * Responsabilidad: Implementar y mantener la API en Python con Flask, incluyendo configuración, validaciones, manejo de errores y pruebas proporcionales al cambio.

* **Agente 3: Arquitecto de Datos y Persistencia**

  * Responsabilidad: Diseñar los modelos, reglas de integridad, consultas y evolución de la persistencia de acuerdo con las necesidades de la API.

* **Agente 4: Escritor Técnico**

  * Responsabilidad: Mantener la documentación técnica, las guías de configuración, la referencia de la API y las instrucciones de despliegue y operación.

* **Agente 5: Copywriter Ejecutivo**

  * Responsabilidad: Redactar resúmenes, propuestas y comunicaciones para públicos no técnicos con beneficios, riesgos y acciones siguientes claros.

* **Agente 6: Analista Funcional e Investigador de Flujos Conversacionales**

  * Responsabilidad: Investigar bots de referencia mediante recorridos controlados, identificar capacidades de negocio y funcionales, registrar evidencia y diagramar los caminos observados sin convertir inferencias en hechos.

* **Agente 7: Arquitecto de Software**

  * Responsabilidad: Diseñar la organización modular de Pipe, el motor conversacional, los contratos internos y la estructura del repositorio con decisiones proporcionales al alcance y al riesgo.

* **Agente 8: PMO**

  * Responsabilidad: Definir y mantener alcance, fases, roadmap, hitos, dependencias, riesgos, backlog y criterios de avance, evitando burocracia que no cambie la ejecución.

* **Agente 9: Arquitecto de Soluciones**

  * Responsabilidad: Diseñar y mantener la visión end-to-end de Pipe, alineando alcance funcional, canal de WhatsApp, componentes, integraciones, datos, seguridad, despliegue y operación; coordina las decisiones de los arquitectos especializados sin reemplazar sus responsabilidades.

* **Agente 10: Diseñador UI/UX y Creador de POC**

  * Responsabilidad: Crear prototipos HTML/CSS/JS autocontenidos, responsive y validables sin instalación para explorar el look and feel de Pipe antes de integrarlo al backend; utiliza prioritariamente componentes y utilidades de Bootstrap y limita el CSS propio a identidad o necesidades no cubiertas.

* **Agente 11: UX Writer**

  * Responsabilidad: Definir etiquetas, ayudas, estados vacíos, filtros, acciones y mensajes de interfaz claros y consistentes; complementa al Copywriter Ejecutivo sin asumir las reglas funcionales del bot.
