<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Separate rack-center dimensions from component envelopes

The rack origins are spaced by `RACK_WIDTH + RACK_GAP`, giving X=0, 4300, and
8600 mm. Uprights and base plates are centered on the corner coordinates, so their
outside faces extend beyond the nominal rack width and depth.

| Measurement | Current analytical value |
| --- | ---: |
| First-left to last-right upright centers | 12200 mm |
| Base-plate envelope, X | -110 to 12310 mm |
| Base-plate envelope, Y | -110 to 1210 mm |
| Floor reference, X | -600 to 12800 mm |
| Floor reference, Y | -600 to 1700 mm |
| Gap between adjacent base-plate edges | 480 mm |

Expected output prints these extents and verifies that the base plates fit inside
the floor reference with 490 mm margins on each side. The nominal `RACK_GAP` is
700 mm between adjacent end upright centers; it is not 700 mm of empty space
between the plates. Upright-face clearance alone would be 610 mm.

The source embeds a 600 mm floor margin inside `create_floor_reference`; the
example names that local design assumption explicitly rather than presenting it
as a configurable global. This analysis covers axis-aligned box components. It
does not measure every brace's cylinder envelope, certify an aisle width, establish
vehicle access, or describe safe warehouse operation.

## Run the complete example

Run from the repository root with Python 3; no FreeCAD runtime is loaded.

```shell
python docs/examples/rack-footprint.py
```

[Complete example](../examples/rack-footprint.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_upright`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L82).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_floor_reference`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L230).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `rebuild_document`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L248).
