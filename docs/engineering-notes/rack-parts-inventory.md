<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Reconcile rack members with the 94-object baseline

Count construction operations before changing the geometry validator's expected
total. One rack has four upright locations; each creates one upright and one base
plate. Each modeled level creates four beams and one visual deck. Two side planes,
two vertical brace bands, and two diagonals per band create eight braces.

| Category | Per rack | Three racks |
| --- | ---: | ---: |
| Uprights | 4 | 12 |
| Base plates | 4 | 12 |
| Beams | 4 x 3 = 12 | 36 |
| Visual decks | 3 | 9 |
| Side braces | 8 | 24 |
| Subtotal | 31 | 93 |
| Shared floor reference | - | 1 |

The analytical example reads actual level elevations and rack count, prints the
category counts, and requires 94 total objects. It separately compares that result
with the source's printed formula based on `LEVEL_COUNT`, so a metadata mismatch
cannot be mistaken for an extra component.

This is an object inventory for the present visual model, not a purchasing bill of
materials. The solid boxes omit holes, rolled profiles, fittings, and fasteners;
members can overlap at their joints. A matching count does not prove valid shapes,
correct dimensions, structural adequacy, or geometric identity with the committed
reference document. Run the baseline validator for those runtime invariants it
actually checks.

## Run the complete example

Run from the repository root with Python 3; no FreeCAD runtime is loaded.

```shell
python docs/examples/rack-parts-inventory.py
```

[Complete example](../examples/rack-parts-inventory.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_upright`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L82).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_beam_level`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L107).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_side_braces`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L177).
- [`tests/validate_models.py`: `validate_warehouse_racks`](../../tests/validate_models.py#L51).
