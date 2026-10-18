<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Fingerprint source and inspect reference archives without opening CAD

An `.FCStd` file is a document archive. A standard-library preflight can fingerprint
it and check that `Document.xml` is present without loading FreeCAD or asserting
that its geometry is valid. This is useful when separating a missing/corrupt
artifact from a later CAD-kernel failure.

The example records SHA-256 and byte size for the three generators, the validator,
and both committed references. It then opens each reference as a ZIP archive,
tests entry CRCs, lists entry names, and requires `Document.xml`. It reports the
checkout HEAD where Git is available and explicitly labels geometry validation as
not run by this example.

| Check | Establishes | Does not establish |
| --- | --- | --- |
| SHA-256 | exact local bytes | equality with a different source-generated model |
| ZIP CRC test | archive entry integrity | CAD topology validity |
| `Document.xml` exists | expected document metadata entry | all objects recompute successfully |

Expected output is one JSON object with six file fingerprints and two archive
entry lists; archive CRC failures raise an assertion. No model is extracted,
rewritten, or saved. A source HEAD alone does not prove a clean worktree, and
matching archive names do not prove matching geometry. For a release note, pair
the manifest with the same-run worktree status, FreeCAD version, and complete
baseline validator output instead of presenting this preflight as a geometry pass.

## Run the complete example

Run from the repository root with Python 3; no FreeCAD runtime is loaded.

```shell
python docs/examples/reference-archive-manifest.py
```

[Complete example](../examples/reference-archive-manifest.py). The script is intended to be run as supplied.

## Source anchors

- [`tests/validate_models.py`: `validate_committed_models`](../../tests/validate_models.py#L62).
- [`tests/validate_models.py`: `main`](../../tests/validate_models.py#L76).
