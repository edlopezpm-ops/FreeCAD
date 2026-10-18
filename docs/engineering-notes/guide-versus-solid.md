<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Compare the sample guide model with the closed hull model

The two hull scripts answer different CAD questions. The sample exposes Draft
guide objects and bridge references; the full generator lofts closed profiles
and groups optional diagnostic geometry into compounds. A smaller tree does not
mean a simpler or less complete topological result.

| Property | Sample | Full |
| --- | --- | --- |
| Nominal length | 12000 mm | 12000 mm |
| Stations per hull | 15 | 19 |
| Section representation | open seven-point Draft curve | closed twelve-point profile |
| Document objects, defaults | 44 | 7 |
| Named hull solids | none | `Port_Hull`, `Starboard_Hull` |
| Bridge deck guides | three | none |

The example runs both models, reports their object counts and per-object solid
total, and requires zero solids in the sample and exactly two in the full model.
Expected output is `sample objects 44 solids 0` and `full objects 7 solids 2`.
It prints the separate document names so the active GUI tree cannot be mistaken
for the other execution's document.

The shared 12 m nominal length is not evidence of geometric equivalence. The
distribution functions, station profiles, raised sheer, and diagnostic grouping
differ. Do not use a sample-model screenshot or its passing validator as evidence
that the full loft is valid, or assume that full-model compounds preserve Draft
editing properties and individual station object identities.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/guide-versus-solid.py')"
```

[Complete example](../examples/guide-versus-solid.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD Hull/SampleCatHull.py`: `create_single_hull`](../../FreeCAD%20Hull/SampleCatHull.py#L72).
- [`FreeCAD Hull/FullCatamaranHull.py`: `station_profile_points`](../../FreeCAD%20Hull/FullCatamaranHull.py#L106).
- [`FreeCAD Hull/FullCatamaranHull.py`: `create_hull`](../../FreeCAD%20Hull/FullCatamaranHull.py#L130).
- [`tests/validate_models.py`: `validate_sample_catamaran`](../../tests/validate_models.py#L40).
