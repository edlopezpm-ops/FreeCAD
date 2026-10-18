<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Open committed reference models without overwriting them

The baseline validator checks source-generated geometry and independently opens
the two committed `.FCStd` references. Those are distinct evidence paths: a source
change can succeed while a stored reference fails to load, and a reference can
open even if the current generator has changed.

| Reference file | Readback checks in this recipe |
| --- | --- |
| `FreeCAD Hull/Catamaran_Hull_Only.FCStd` | open, recompute, inventory shaped objects, valid non-null shapes |
| `FreeCAD_WHRackDesign/FreeCAD_WHRackDesign_3_Racks_3_Levels.FCStd` | same checks |

The example opens each file in a fresh session, reports object counts and shape
counts, then closes only that opened document in `finally`. Expected output has
two `reference_valid True` rows and positive shaped-object counts. It never calls
`save` or `saveAs`, so the committed files are not regenerated or overwritten.

Do not assume the reference's internal document name from its filename; report
`document.Name` after opening. A recompute can modify the in-memory document even
when no bytes are saved. The current checks establish neither byte-for-byte nor
geometric equality with generated models. Such a comparison would need a separate
explicit tolerance and topology/placement comparison; this recipe does not invent
one. Reference readback is also not an approval of loads, flotation, or fabrication.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/committed-model-readback.py')"
```

[Complete example](../examples/committed-model-readback.py). The script is intended to be run as supplied.

## Source anchors

- [`tests/validate_models.py`: `validate_committed_models`](../../tests/validate_models.py#L62).
