# CAD Models

This directory contains 3D CAD model files for the mechanical components.

## File Organization

- Store native CAD files (e.g., .f3d, .sldprt, .ipt)
- Include STEP (.step, .stp) files for universal compatibility
- Organize by component or assembly

## Naming Convention

Use descriptive names:
- `component_name_vX.ext` (e.g., `chassis_base_v1.step`)
- `assembly_name_vX.ext` (e.g., `complete_assembly_v2.step`)

## File Types

### Native Files
- Fusion 360: .f3d, .f3z
- SolidWorks: .sldprt, .sldasm, .slddrw
- Inventor: .ipt, .iam, .idw
- FreeCAD: .FCStd

### Universal Formats
- STEP: .step, .stp (recommended for sharing)
- IGES: .iges, .igs
- STL: .stl (for 3D printing)
- OBJ: .obj (for visualization)

## Best Practices

1. Always export STEP files for cross-platform compatibility
2. Use parametric modeling when possible
3. Document design intent and parameters
4. Include assembly files showing part relationships
5. Add comments for complex features
6. Keep file size manageable (simplify unnecessary details)
7. Version control CAD files properly

## Notes

- Save project files regularly
- Export neutral formats after major changes
- Document material properties in CAD software
- Include coordinate system information
