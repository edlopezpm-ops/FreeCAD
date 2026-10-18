<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Export only the two hull solids to temporary BREP custody

An interchange example should state exactly what it exports. This recipe selects
`Port_Hull` and `Starboard_Hull` from a newly generated full model, compounds their
shapes, writes one temporary BREP, reads it back, and verifies two valid solids
with a matching combined volume.

| Export boundary | Included? |
| --- | --- |
| Two lofted hull solids | yes |
| Station-frame compounds | no |
| Longitudinal-guide compounds | no |
| Shared centerline | no |
| Document presentation or procedural logic | not asserted |

Expected output is a positive file size, `restored_solids 2`, and
`hull_brep_roundtrip True`. The script uses `TemporaryDirectory`; its file is
removed after readback, and no committed `.FCStd` reference is touched. Relative
volume tolerance is 1e-9 for this same-runtime round-trip, not a design tolerance
for comparing different models.

The exported compound is a container for two separated solids, not a fused vessel,
an assembly with semantic links, or a structural manufacturing model. Successful
BREP readback does not establish STEP compatibility or preserve Draft parameters,
object names, view styles, or documentation. Retaining an export for review requires
an intentional destination and recorded source revision/runtime.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/hull-brep-roundtrip.py')"
```

[Complete example](../examples/hull-brep-roundtrip.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD Hull/FullCatamaranHull.py`: `create_hull`](../../FreeCAD%20Hull/FullCatamaranHull.py#L130).
- [`FreeCAD Hull/FullCatamaranHull.py`: `add_shape`](../../FreeCAD%20Hull/FullCatamaranHull.py#L91).
- [`tests/validate_models.py`: `validate_full_catamaran`](../../tests/validate_models.py#L21).
