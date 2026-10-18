<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Audit rack object names without relying on allocation suffixes

`create_upright` requests the same upright and base-plate name for each of a
rack's four corner locations. FreeCAD allocates distinct internal names when a
requested name already exists. Inspect the actual names rather than assuming a
suffix format or treating repeated source strings as one overwritten object.

The example groups objects by the three rack prefixes and reports their actual
names, labels, and types. Each group must contain four upright-prefixed objects,
four plate-prefixed objects, 15 level objects, and eight braces. The shared floor
reference belongs to no rack prefix.

| Group | Expected objects |
| --- | ---: |
| `Rack_01_` | 31 |
| `Rack_02_` | 31 |
| `Rack_03_` | 31 |
| `Floor_Aisle_Reference` | 1 |

Expected output includes three 31-object groups and 94 unique internal names.
The check uses actual `Name` values for lookup and does not assume labels are
unique. A name prefix is a useful local convention, not an explicit document
group, assembly relationship, or persistent external identifier. Renaming objects
can break downstream scripts even when the shape is unchanged; this diagnostic
does not rename or restructure the model.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/rack-object-identities.py')"
```

[Complete example](../examples/rack-object-identities.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_upright`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L82).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_rack`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L211).
- [`tests/validate_models.py`: `validate_warehouse_racks`](../../tests/validate_models.py#L51).
