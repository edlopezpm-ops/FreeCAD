<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Inspect a closed station profile before interpreting the loft

The full-hull generator interpolates twelve profile points into one closed
B-spline edge, wraps that edge in a `Part.Wire`, and rejects a wire that is not
closed. The profile includes a raised top return; it is not simply the sample
guide's open seven-point section with its endpoints joined.

| Midship port-profile input | Value |
| --- | --- |
| X plane | 6000 mm |
| Hull center Y | -2400 mm |
| Sheer endpoint Y | -2970 and -1830 mm |
| Keel coordinate | (6000, -2400, -1200) mm |
| Highest defining point | Z=85 mm |

The example loads the source, calls `station_profile_points` for t=0.5, prints
the twelve vectors, then passes them to the same closure helper used for the loft.
Expected output is `input_points 12`, `wire_edges 1`, `closed True`, and `valid True`.
It also prints the kernel bound, which need not equal the defining-point extents.

Closure describes topology, while validity describes the kernel's acceptance of
the current wire. Neither proves a fair surface, a successful solid loft, a physical
deck, or manufacturable shell thickness. When troubleshooting a loft, inspect
individual wires and their ordering before changing the loft's solid flag or
weakening the full model's solid assertions.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/closed-profile.py')"
```

[Complete example](../examples/closed-profile.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD Hull/FullCatamaranHull.py`: `station_profile_points`](../../FreeCAD%20Hull/FullCatamaranHull.py#L106).
- [`FreeCAD Hull/FullCatamaranHull.py`: `make_closed_profile`](../../FreeCAD%20Hull/FullCatamaranHull.py#L83).
- [`FreeCAD Hull/FullCatamaranHull.py`: `make_bspline_edge`](../../FreeCAD%20Hull/FullCatamaranHull.py#L73).
