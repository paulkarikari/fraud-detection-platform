# Diagram Index

This folder contains the template-aligned diagram set used by the reference architecture document.

## Canonical Diagram Set (Template Aligned)

| # | View | File | Purpose |
|---|---|---|---|
| 1 | Context | `01-system-context.png` | External actors, source systems, and trust boundary. |
| 2 | Logical | `02-logical-architecture.png` | Core components, responsibilities, and interactions. |
| 3 | Data Flow | `03-data-architecture.png` | Ingestion to serving path with control points. |
| 4 | Deployment | `06-deployment-architecture.png` | Environment isolation and cloud runtime placement. |

## Source and Rendered Assets

- Editable draw.io sources: `drawio/`
- Rendered PNG artifacts: `png/`
- Azure icons: `icons/`

To regenerate diagram renders:

```bash
bash scripts/render_drawio_diagrams.sh fraud-detection-platform
```
