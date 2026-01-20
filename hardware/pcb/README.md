# PCB Design

This directory contains all files related to the PCB (Printed Circuit Board) design for the project.

## Directory Structure

```
hardware/pcb/
├── schematic/       # Circuit schematic files
├── layout/          # PCB layout files
├── gerbers/         # Gerber files for manufacturing
├── bom/             # Bill of Materials
└── README.md        # This file
```

## Design Tools

Common PCB design tools that can be used:
- KiCad (Open Source)
- Altium Designer
- Eagle
- EasyEDA
- Fusion 360 Electronics

## Workflow

1. **Schematic Design**: Create the circuit schematic in the `schematic/` directory
2. **PCB Layout**: Design the PCB layout in the `layout/` directory
3. **Generate Gerbers**: Export Gerber files to the `gerbers/` directory for manufacturing
4. **Bill of Materials**: Maintain component list in the `bom/` directory

## Getting Started

1. Choose your PCB design software
2. Create a new project and save files in the appropriate directories
3. Follow the design guidelines in the docs folder
4. Keep the BOM updated as you add components

## Manufacturing

Once the design is complete:
1. Generate Gerber files (RS-274X format)
2. Include drill files
3. Prepare the BOM
4. Send to PCB manufacturer (e.g., JLCPCB, PCBWay, OSH Park)

## Notes

- Always include a ground plane
- Follow proper trace width for current requirements
- Consider signal integrity for high-speed signals
- Add test points for debugging
