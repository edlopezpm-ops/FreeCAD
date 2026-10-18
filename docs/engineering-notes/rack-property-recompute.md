<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Demonstrate a document-property edit with restoration

The warehouse's box members are `Part::Box` objects with editable `Length`,
`Width`, and `Height` properties. That differs from a brace or full hull stored
as a computed `Part::Feature` shape. Changing a Python module constant is not
the same operation as editing an existing document object's property.

The example chooses the first rack's first visual deck, records its height and
volume, increases `Height` by 10 mm, recomputes, and compares the volume increase
with `Length * Width * 10`. It restores the original height in `finally` and
checks the original volume.

| Baseline deck quantity | Value |
| --- | ---: |
| Length | 3320 mm |
| Width | 820 mm |
| Height | 55 mm |
| Volume change for +10 mm height | 27,224,000 mm^3 |

Expected output includes this volume delta and `original_volume_restored True`.
The temporary edit does not move the next beam or change other decks: no formula
links those existing objects to this one's height. Recompute evaluates document
properties; it does not rerun `create_beam_level`. No file is saved, and restoration
of the geometric value does not promise a cleared document modified indicator.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/rack-property-recompute.py')"
```

[Complete example](../examples/rack-property-recompute.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `add_box`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L48).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_beam_level`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L107).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `rebuild_document`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L248).
