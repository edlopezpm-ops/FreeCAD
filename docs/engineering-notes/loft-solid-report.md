<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Report closed hull topology and measured dimensions

The full generator calls `Part.makeLoft(station_wires, True, False, False, 5)`
and stores each result in a `Part::Feature`. The solid request is an input to the
kernel, so inspect the result instead of assuming the flag guarantees success.

| Object | Baseline expectation |
| --- | --- |
| `Port_Hull` | one valid, non-null, positive-volume solid |
| `Starboard_Hull` | one valid, non-null, positive-volume solid |
| Each hull's X extent | within 1 mm of 12000 mm |
| Lateral placement | port YMax < 0; starboard YMin > 0 |

The example reports solids, shells, faces, edges, volume in mm^3, and measured
bounds for both hulls. Expected output includes two valid single-solid rows; face
and edge counts are reported rather than frozen because they are diagnostic
topology details, not the existing validator's compatibility contract. It prints
the relative port/starboard volume difference without imposing a new tolerance.

Volume is enclosed by the generated solid and is not automatically displaced
water volume: no waterline is intersected, and no flotation condition is solved.
The model lacks engineered plating, laminate, internal structure, loading, and
stability analysis. Shape validity, a matching length, and opposite-side placement
are useful CAD invariants with a narrower meaning than naval suitability.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/loft-solid-report.py')"
```

[Complete example](../examples/loft-solid-report.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD Hull/FullCatamaranHull.py`: `create_hull`](../../FreeCAD%20Hull/FullCatamaranHull.py#L130).
- [`FreeCAD Hull/FullCatamaranHull.py`: `add_shape`](../../FreeCAD%20Hull/FullCatamaranHull.py#L91).
- [`tests/validate_models.py`: `validate_full_catamaran`](../../tests/validate_models.py#L21).
