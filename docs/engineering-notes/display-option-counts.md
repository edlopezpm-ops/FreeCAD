<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Check guide visibility options against the construction inventory

`SHOW_STATION_FRAMES` and `SHOW_LONGITUDINAL_GUIDES` control whether auxiliary
objects are created. They do not merely hide already-existing objects. Each hull
always contributes one solid, optionally one compound of station frames and one
compound of longitudinal guides; one shared centerline is always created.

| Frames | Guides | Document objects |
| --- | --- | ---: |
| false | false | 3 |
| true | false | 5 |
| false | true | 5 |
| true | true | 7 |

The example exercises all four combinations in the actual function-global
namespace, rebuilds each model, and verifies both named hull solids remain present.
It restores the original flags in `finally` and rebuilds the default model.
Expected output is the four counts in this table and `default_restored True`.

Run in a fresh session: `rebuild_document` closes every open document whose name
starts with `DOC_NAME`, including a previously edited model. The returned `runpy`
dictionary is not used as a live parameter sheet; Python functions keep their own
global namespace. This diagnostic uses `rebuild.__globals__` deliberately.
The existing baseline validator expects seven objects with the committed defaults;
changing the defaults requires a coordinated review, not simply accepting a new count.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/display-option-counts.py')"
```

[Complete example](../examples/display-option-counts.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD Hull/FullCatamaranHull.py`: `SHOW_STATION_FRAMES`](../../FreeCAD%20Hull/FullCatamaranHull.py#L25).
- [`FreeCAD Hull/FullCatamaranHull.py`: `SHOW_LONGITUDINAL_GUIDES`](../../FreeCAD%20Hull/FullCatamaranHull.py#L26).
- [`FreeCAD Hull/FullCatamaranHull.py`: `create_hull`](../../FreeCAD%20Hull/FullCatamaranHull.py#L130).
- [`FreeCAD Hull/FullCatamaranHull.py`: `rebuild_document`](../../FreeCAD%20Hull/FullCatamaranHull.py#L195).
