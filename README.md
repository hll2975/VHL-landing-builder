# 🛠 Landing Builder (MVP)

Creador de páginas tipo landing totalmente personalizable con Flask.

🔧 En construcción. Este proyecto está pensado para escalar e incluir funcionalidades como:
- Editor visual (ej. GrapesJS) en futuras versiones
- Métricas personalizadas de visitas y formularios
- Soporte para plantillas seleccionables y renderizado único por usuario

🚀 Versión actual: MVP con render HTML personalizado desde plantillas Jinja2.

## 📦 Datos de ejemplo

El directorio `demo/` incluye un archivo `landing.json` que contiene una estructura representativa de una landing page.

Este archivo puede utilizarse para:
- Hacer pruebas locales de visualización (`/mi-landing-ejemplo`)
- Inspirar integración futura de importación/exportación de landings
- Compartir ejemplos preconfigurados

```json
{
  "slug": "mi-landing-ejemplo",
  "theme": "modern",
  "fields": {
    "title": "¡Bienvenido a mi proyecto!",
    "description": "Esta es una landing generada desde un archivo JSON."
  }
}
