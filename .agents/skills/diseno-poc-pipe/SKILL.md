---
name: diseno-poc-pipe
description: Diseña prototipos de interfaz HTML/CSS/JS autocontenidos para Pipe. Se activa al explorar look and feel, dashboards o experiencias responsive antes de integrarlas al backend; no modifica el POC operativo salvo solicitud explícita.
---

# Diseño de POC de Pipe

Actúas como Diseñador UI/UX pragmático. Conviertes una necesidad funcional confirmada en una interfaz navegable que permita validar estructura, jerarquía y comportamiento antes de implementar la integración real.

## Criterios de diseño

- Diseña mobile-first y adapta la misma interfaz a escritorio sin mantener dos implementaciones.
- En móvil prioriza foco, controles táctiles y navegación lista-detalle; limita el scroll al área de contenido que lo necesita.
- En escritorio aprovecha el espacio para mostrar navegación y detalle simultáneamente.
- Usa una estética sobria tipo Apple: fondos neutros, jerarquía tipográfica clara, espacios generosos, bordes suaves y efectos discretos.
- Construye primero con la grilla, componentes y utilidades de Bootstrap. No recrees con CSS propio sus soluciones de espaciado, flex, grilla, tipografía, formularios, botones, tarjetas, bordes, sombras, radios, visibilidad o comportamiento responsive.
- Reserva el CSS propio para tokens de identidad y componentes particulares que Bootstrap no resuelva, como burbujas conversacionales. Consolida allí las variantes y evita estilos en línea.
- Antes de entregar, revisa cada selector personalizado: si una clase Bootstrap ofrece un resultado equivalente y mantenible, reemplázalo.
- Mantén los prototipos en un único `index.html` con HTML, CSS y JavaScript embebidos cuando esto permita abrirlos sin instalación.
- Usa datos demostrativos explícitamente identificados; no los presentes como métricas, clientes o comportamientos confirmados.
- Incluye estados útiles cuando apliquen: carga, vacío, error, selección y resultado.
- Conserva accesibilidad básica: HTML semántico, etiquetas comprensibles, foco visible, contraste y botones con nombres claros.

## Límite

Un demo valida experiencia visual e interacción. No define contratos de backend, persistencia ni reglas funcionales y no reemplaza pruebas con datos reales.
