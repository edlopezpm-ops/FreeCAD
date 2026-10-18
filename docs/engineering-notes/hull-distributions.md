<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Execute the closed-hull distribution functions without a CAD kernel

The full hull uses sine-based fullness functions, unlike the sample's parabolic
guide model. This example extracts the actual numeric distribution functions from
the local AST and executes only those functions with their literal constants and
Python's `math` module. It never runs the module's top-level rebuild.

| Normalized t | X | Beam | Draft | Keel Z | Sheer Z |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | 120 | 192 | -192 | 70 |
| 0.5 | 6000 | 1200 | 1200 | -1200 | 0 |
| 1 | 12000 | about 120 | about 192 | about -192 | 70 |

Expected output includes these rows and quarter-length samples, with floating-point
tolerance at t=1. The current 19 stations produce `t=index/18`, so index 9 is the
exact midpoint. `beam_at`, `draft_at`, and `keel_z_at` consume normalized t, not X
in millimeters; passing X=6000 is a coordinate-domain error.

The sine input is clamped to [0,1] for fullness and draft, but `x_at` and
`sheer_z_at` are not clamped. Stay within the intended domain instead of assuming
all functions enforce it. The extracted functions establish scalar calculations,
not profile validity, loft continuity, solid volume, buoyancy, or measured bounds.

## Run the complete example

Run from the repository root with Python 3; no FreeCAD runtime is loaded.

```shell
python docs/examples/hull-distributions.py
```

[Complete example](../examples/hull-distributions.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD Hull/FullCatamaranHull.py`: `longitudinal_fullness`](../../FreeCAD%20Hull/FullCatamaranHull.py#L43).
- [`FreeCAD Hull/FullCatamaranHull.py`: `draft_at`](../../FreeCAD%20Hull/FullCatamaranHull.py#L53).
- [`FreeCAD Hull/FullCatamaranHull.py`: `station_t`](../../FreeCAD%20Hull/FullCatamaranHull.py#L39).
- [`FreeCAD Hull/FullCatamaranHull.py`: `sheer_z_at`](../../FreeCAD%20Hull/FullCatamaranHull.py#L63).
