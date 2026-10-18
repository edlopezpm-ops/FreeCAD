<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Translate a copied hull without editing the source object

Shape geometry and document placement are separate pieces of a FreeCAD model.
This recipe creates a copy of the port hull's shape in a separate example
document, translates the copy by +15000 mm in X and +2500 mm in Z, then compares
bounds and volume with the original object.

| Quantity | Expected relationship |
| --- | --- |
| XMin and XMax | original + 15000 mm |
| ZMin and ZMax | original + 2500 mm |
| Y extent | unchanged |
| Volume | unchanged within numerical tolerance |
| Original hull placement | unchanged |

Expected output ends with `translated_copy True` and `original_unchanged True`.
The copied feature is a local shape snapshot; it is not a live `App::Link` or
assembly instance. Later rebuilding the source will not automatically update the
copy. The example adds only an in-memory document and does not save either model.

Bounding boxes report global axis-aligned extents after placement. A translation
test is deliberately simpler than a rotation, where X/Y/Z extents can change
even when volume stays constant. These checks explain coordinate handling and
cannot establish collision clearance, flotation, structural connections, or the
correctness of an external assembly coordinate system.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/hull-placement-copy.py')"
```

[Complete example](../examples/hull-placement-copy.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD Hull/FullCatamaranHull.py`: `add_shape`](../../FreeCAD%20Hull/FullCatamaranHull.py#L91).
- [`FreeCAD Hull/FullCatamaranHull.py`: `create_hull`](../../FreeCAD%20Hull/FullCatamaranHull.py#L130).
