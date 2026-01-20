# Gerber Files Directory

Place your Gerber manufacturing files here.

## Required Files for Manufacturing

### Standard Gerber Files (RS-274X format)
- Top Copper Layer (*.GTL)
- Bottom Copper Layer (*.GBL)
- Top Solder Mask (*.GTS)
- Bottom Solder Mask (*.GBS)
- Top Silkscreen (*.GTO)
- Bottom Silkscreen (*.GBO)
- Board Outline (*.GKO or *.GM1)

### Drill Files
- Drill file (*.DRL or *.TXT)
- Drill map (optional, for reference)

### Additional Files
- Pick and place file (*.CSV) - for assembly
- Bill of Materials (*.CSV or *.XLS)
- Assembly drawing (*.PDF)
- Fabrication notes (*.PDF or *.TXT)

## Generating Gerbers

### KiCad
1. Open your PCB file
2. Go to File → Plot
3. Select Gerber format
4. Check required layers
5. Generate drill files separately
6. Zip all files together

### Eagle
1. Open your board file
2. Run CAM Processor
3. Use CAM job file or configure manually
4. Generate Gerber and drill files
5. Zip all files together

## Verification
Always verify your Gerber files with a viewer before sending to manufacturer:
- Gerbv (Linux/Mac/Windows)
- ViewMate (Windows)
- Online Gerber viewers

## Manufacturing Notes
- Most manufacturers accept ZIP files containing all Gerbers
- Specify PCB specifications: thickness, copper weight, color
- Include any special requirements in a README
