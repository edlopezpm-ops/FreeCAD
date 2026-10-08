<!-- (kommiBo) Operator-assisted maintenance; source-reviewed documentation. -->
# FreeCAD model validation: validation and diagnosis

Run from the repository root:

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('tests/validate_models.py', run_name='__main__')"
```

Use FreeCAD 1.1.3 as pinned by [CI](../.github/workflows/validation.yml). The [validator](../tests/validate_models.py) executes three generators and independently opens both committed `.FCStd` references.

| Model | Assertions in the current validator |
| --- | --- |
| Full catamaran | Seven objects; named port/starboard hulls; one valid positive-volume solid per hull; approximately 12,000 mm length; opposite sides of the centerline. |
| Sample catamaran | 44 objects, a labeled centerline, and valid non-null shapes. |
| Warehouse racks | 94 objects, a floor/aisle reference, and valid non-null shapes. |
| Committed references | Each file opens, recomputes, contains shapes, and has no null or invalid checked shape. |

Object counts and dimensions describe the current checked source. If model parameters change intentionally, review which assertions must change and why. Do not relax validity or solid checks to conceal a geometry failure.

A failure loading a committed model is distinct from a generator failure. The validator checks both, but does not compare the generated model byte-for-byte or geometrically against the committed reference. Regenerating an `.FCStd` file solely because documentation changed is unnecessary.

For missing `FreeCAD`, use the FreeCAD command runtime rather than a plain Python interpreter. For Linux AppImage failures, inspect the download, verified digest, and extraction steps before interpreting the result as a geometry defect.

The checks do not certify storage capacity, structural loading, buoyancy, safety, or fabrication readiness. Review relevant GUI views separately when changing model construction.

See [change and recovery guidance](change-recovery.md) before merging a correction.
