# Mechanical Integration Guidelines

## General Guidelines

### 1. Design Philosophy
- Design for manufacturability (DFM)
- Design for assembly (DFA)
- Design for serviceability
- Consider component accessibility
- Plan for future modifications
- Minimize custom parts where possible

### 2. Material Selection

#### Structural Materials
- **Aluminum 6061-T6**: General purpose, good machinability
- **Aluminum 7075-T6**: High strength applications
- **Steel**: High load, wear-resistant applications
- **Stainless Steel 304/316**: Corrosion-resistant applications

#### Plastic Materials
- **ABS**: General purpose, good impact resistance
- **PLA**: 3D printing, prototyping
- **PETG**: Better thermal resistance than PLA
- **Nylon (PA)**: High strength, wear resistance
- **Acrylic (PMMA)**: Transparent applications

### 3. Fastener Selection

#### Standard Metric Fasteners
| Application | Fastener Type | Size Range |
|-------------|---------------|------------|
| Light duty  | M2-M3         | < 5 kg     |
| Medium duty | M4-M6         | 5-50 kg    |
| Heavy duty  | M8-M12        | > 50 kg    |

#### Fastener Guidelines
- Use standard metric fasteners (M2, M3, M4, M6, M8, etc.)
- Prefer socket head cap screws for compact assemblies
- Use flat head screws for flush mounting
- Include washers for load distribution
- Specify lock nuts or threadlocker for vibration resistance
- Calculate proper torque values

### 4. Dimensioning and Tolerancing

#### General Tolerances
- **Standard machining**: ±0.1 mm for < 100mm, ±0.2 mm for > 100mm
- **3D printing**: ±0.2 mm minimum
- **Laser cutting**: ±0.1 mm
- **Water jet cutting**: ±0.25 mm

#### Hole Tolerances
| Type | Clearance | Application |
|------|-----------|-------------|
| Tight fit | +0.0/+0.1 mm | Press fits |
| Standard | +0.1/+0.3 mm | Fastener clearance |
| Loose | +0.3/+0.5 mm | Alignment pins |

#### Fastener Clearance Holes
- M2: 2.2 mm clearance, 3.8 mm counterbore
- M3: 3.2 mm clearance, 5.5 mm counterbore
- M4: 4.3 mm clearance, 7.0 mm counterbore
- M5: 5.3 mm clearance, 8.5 mm counterbore
- M6: 6.4 mm clearance, 10.0 mm counterbore
- M8: 8.4 mm clearance, 13.0 mm counterbore

### 5. Structural Design

#### Load Calculations
- Determine static and dynamic loads
- Apply appropriate safety factors (typically 2-4)
- Consider impact and shock loads
- Account for material fatigue

#### Safety Factors
| Application | Safety Factor |
|-------------|---------------|
| Static load, ductile material | 2-3 |
| Dynamic load, ductile material | 4-6 |
| Static load, brittle material | 5-7 |
| Unknown loads or critical | 8-10 |

### 6. Thermal Considerations

- Thermal expansion coefficients:
  - Aluminum: 23 × 10⁻⁶ /°C
  - Steel: 12 × 10⁻⁶ /°C
  - Plastic: 50-150 × 10⁻⁶ /°C
- Allow for thermal expansion in long components
- Consider heat dissipation for electronics
- Add ventilation where needed
- Use thermal interface materials appropriately

### 7. Assembly Considerations

#### Design for Assembly
- Minimize part count
- Use self-aligning features
- Reduce fastener variety
- Design for top-down assembly when possible
- Add alignment features (pins, keys, chamfers)
- Provide access for tools

#### Assembly Features
- Chamfers on holes: 0.5-1.0 mm at 45°
- Fillets on internal corners: 1-2 mm radius
- Alignment pins: H7/h6 tolerance fit
- Snap fits: proper draft angle and retention

### 8. Electronics Integration

#### PCB Mounting
- Use standoffs with M2.5 or M3 screws
- Maintain minimum 3mm clearance beneath PCB
- Provide grounding connections if needed
- Route cables away from sensitive electronics
- Add strain relief for connectors

#### Cable Management
- Plan cable routing paths in early design
- Allow for cable bend radius (minimum 10× cable diameter)
- Use cable ties, clips, or channels
- Keep cables away from moving parts
- Provide service loops at connections

### 9. Motor and Actuator Integration

#### Motor Mounting
- Use proper coupling or transmission
- Align shaft within tolerance
- Provide overload protection
- Consider vibration isolation
- Allow for heat dissipation

#### Bearing Selection
- Calculate bearing loads (radial and axial)
- Consider bearing life (L10 rating)
- Proper bearing preload
- Seal selection for environment
- Lubrication requirements

### 10. Manufacturing Processes

#### CNC Machining
- Minimum feature size: 1 mm
- Minimum internal corner radius: 2 mm (tool radius)
- Standard hole sizes for cost efficiency
- Avoid deep pockets (depth < 3× width)

#### 3D Printing (FDM)
- Minimum wall thickness: 1.2-2.0 mm
- Overhang angle: < 45° without support
- Layer height: 0.1-0.3 mm
- Design for print orientation
- Add chamfers to first layer for adhesion

#### Sheet Metal
- Minimum bend radius: 1.5× material thickness
- Minimum flange width: 3× material thickness
- Standard material thicknesses: 1.0, 1.5, 2.0, 3.0 mm
- Add relief cuts at corners

#### Laser Cutting
- Minimum feature size: 0.5 mm
- Minimum hole diameter: equal to material thickness
- Kerf width: ~0.2-0.3 mm (account in tight fits)

### 11. Surface Finishes

| Process | Application | Roughness |
|---------|-------------|-----------|
| As-machined | General | Ra 3.2 μm |
| Fine machined | Smooth surfaces | Ra 1.6 μm |
| Ground | Bearing surfaces | Ra 0.8 μm |
| Polished | Optical/aesthetic | Ra 0.2 μm |

### 12. Documentation Requirements

For each mechanical component/assembly, provide:
- [ ] 3D CAD model (native + STEP format)
- [ ] Technical drawings with dimensions
- [ ] Bill of materials
- [ ] Assembly instructions
- [ ] Material specifications
- [ ] Manufacturing process specifications
- [ ] Quality control requirements
- [ ] Testing procedures

### 13. Integration Testing

#### Pre-Integration Checks
- Verify all dimensions against drawings
- Check material certifications
- Inspect surface finishes
- Verify part markings and revision

#### Assembly Testing
- Fit check all components
- Verify fastener torques
- Check alignment
- Test range of motion (if applicable)
- Verify clearances

#### System Testing
- Functional testing under rated loads
- Endurance testing (cycle counts)
- Environmental testing
- Safety testing
- Vibration and shock testing

### 14. Common Design Mistakes to Avoid

- Insufficient clearance for assembly tools
- No consideration for thermal expansion
- Inadequate fastener engagement (minimum 1.5× diameter)
- Sharp internal corners causing stress concentrations
- Over-constrained assemblies
- No provision for adjustment or alignment
- Inadequate access for maintenance
- Missing chamfers on insertion features
- Incorrect tolerance stack-up
- No consideration for manufacturing limitations

### 15. Quality Assurance

#### Inspection Points
- Incoming material inspection
- In-process dimensional checks
- Final assembly verification
- Functional testing
- Documentation review

#### Measurement Tools
- Calipers: ±0.02 mm accuracy
- Micrometers: ±0.001 mm accuracy
- CMM: ±0.001 mm accuracy
- Gauge pins for hole verification
- Thread gauges for threaded features

## References

- ISO 2768: General tolerances
- ISO 286: ISO system of limits and fits
- ISO 4762: Socket head cap screws
- ISO 7089: Washers
- DIN 934: Hexagon nuts
- ASME Y14.5: Dimensioning and tolerancing
