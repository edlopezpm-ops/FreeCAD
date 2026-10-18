<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Verify the direction and volume of a synthetic brace

The brace helper starts with a cylinder along local +Z, computes `end - start`,
and rotates that Z axis onto the direction vector. A radius is supplied explicitly;
the rack calls it with `SIDE_BRACE_SIZE / 2`, so the current 45 mm parameter acts
as a cylinder diameter rather than a square brace section.

| Synthetic brace input | Value |
| --- | --- |
| Start | (0, 0, 200) mm |
| End | (0, 1100, 2100) mm |
| Radius | 22.5 mm |
| Axis length | sqrt(1100^2 + 1900^2), about 2195.45 mm |
| Center of mass | (0, 550, 1150) mm |

The example first loads the source, then creates one helper-generated brace in a
separate example document. It checks center of mass, cylinder volume, and that
coincident endpoints raise the helper's explicit `RuntimeError` before an object
is added. Expected output ends with `brace_geometry True` and
`zero_length_rejected True`.

The calculated volume is the ideal full cylinder's volume. This representation
does not describe a manufactured brace profile, fasteners, holes, welded joints,
or a force-resisting connection. It exercises the source's vector and placement
logic without changing the warehouse generator or saving any document.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/brace-vector.py')"
```

[Complete example](../examples/brace-vector.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `add_cylinder_between_points`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L62).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_side_braces`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L177).
