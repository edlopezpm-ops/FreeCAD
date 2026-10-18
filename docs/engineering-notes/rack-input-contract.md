<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Read the rack inputs and their actual construction dependencies

The warehouse generator exposes dimensions as module-level Python literals. The
standard-library example inventories those values without importing FreeCAD, then
checks the relationships needed by the current construction code.

| Input | Current value | Actual construction use |
| --- | --- | --- |
| `RACK_COUNT` | 3 | rack creation loop |
| `LEVEL_COUNT` | 3 | printed expected-count formula |
| `LEVEL_ELEVATIONS` | [900, 2300, 3700] mm | actual level creation loop |
| `RACK_WIDTH`, `RACK_DEPTH`, `RACK_HEIGHT` | 3600, 1100, 4200 mm | member geometry |
| `UPRIGHT_SIZE`, `BEAM_HEIGHT`, `DECK_THICKNESS` | 90, 140, 55 mm | section dimensions |

Expected output lists these dimensions and `level_count_matches True`. The source
iterates `LEVEL_ELEVATIONS`, not `range(LEVEL_COUNT)`. Changing only `LEVEL_COUNT`
changes the printed expectation without adding or removing modeled levels. The
example flags that mismatch rather than treating the printout as authoritative.

The diagnostic also checks positive dimensions, ordered levels, and that the top
deck stays below the upright's top. These are geometric preflight assumptions for
the current rectangular placeholders. They do not validate rack loading, material
grades, connectors, anchorage, code compliance, or safe storage clearances. No source
parameter or committed model is changed by this inventory.

## Run the complete example

Run from the repository root with Python 3; no FreeCAD runtime is loaded.

```shell
python docs/examples/rack-input-contract.py
```

[Complete example](../examples/rack-input-contract.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `LEVEL_COUNT`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L19).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `LEVEL_ELEVATIONS`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L32).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_rack`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L211).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `rebuild_document`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L248).
