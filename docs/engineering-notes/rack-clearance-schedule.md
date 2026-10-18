<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Calculate deck elevations and nominal vertical gaps

`LEVEL_ELEVATIONS` locates the bottom of each horizontal beam. The deck starts at
the beam's top, so the top-of-deck elevation includes both beam height and deck
thickness. This distinction matters when reading a front elevation.

| Level | Beam bottom | Beam top | Deck top | Gap above deck |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 900 | 1040 | 1095 | 1205 to level-2 beam bottom |
| 2 | 2300 | 2440 | 2495 | 1205 to level-3 beam bottom |
| 3 | 3700 | 3840 | 3895 | 305 to upright top |

All values are millimeters. The example derives these values from the literal
parameters, prints a row per level, and asserts positive gaps. The top-level
comparison is to `RACK_HEIGHT`, which is an upright extent rather than a modeled
roof or overhead obstruction. Floor-to-first-beam space is a different measurement.

Expected output is the table's numerical schedule. It is an analytical reading of
the current rectangular geometry; it does not account for pallet height, load
deflection, equipment access, protective devices, or operational clearances. The
modeled deck is a solid visual box despite its `WireDeck_Visual` name. Do not use
these gaps to specify an installed rack without the appropriate engineered design
and site requirements.

## Run the complete example

Run from the repository root with Python 3; no FreeCAD runtime is loaded.

```shell
python docs/examples/rack-clearance-schedule.py
```

[Complete example](../examples/rack-clearance-schedule.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `LEVEL_ELEVATIONS`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L32).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_beam_level`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L107).
