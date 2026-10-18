<!-- (kommiBo) Operator-assisted engineering documentation; no certification claim. -->
# Engineering notes and console recipes

These recipes explain the current source, provide small reproducible examples, and
state what their results can establish. They are optional diagnostics under `docs/`;
the repository's generators, validator, workflows, and reference models are unchanged.

The documentation pattern is adapted from
[checktimecardandgivefeedback at 235a70f](https://github.com/edlopezpm-ops/checktimecardandgivefeedback/tree/235a70f1613f9a7c19515b3a579d7539dcff6b47):
record provenance, identify responsibility, keep examples concrete, and distinguish
observed evidence from assumptions. This is attribution of documentation patterns
only. No application, identity, timekeeping, or business facts are imported.

Recipes marked **Python** run without FreeCAD and report analytical or source
evidence. Recipes marked **FreeCAD** need the FreeCAD Python console/runtime; use
a fresh session and review the described document changes before running them.
For the full baseline, see the [existing validation guide](../validation-guide.md).
Successful syntax or analytical checks do not establish a geometry-runtime pass.

- [Read the rack inputs and their actual construction dependencies](rack-input-contract.md) — **Python**.
- [Reconcile rack members with the 94-object baseline](rack-parts-inventory.md) — **Python**.
- [Calculate deck elevations and nominal vertical gaps](rack-clearance-schedule.md) — **Python**.
- [Separate rack-center dimensions from component envelopes](rack-footprint.md) — **Python**.
- [Verify the direction and volume of a synthetic brace](brace-vector.md) — **FreeCAD**.
- [Audit rack object names without relying on allocation suffixes](rack-object-identities.md) — **FreeCAD**.
- [Report placeholder volumes with explicit component categories](rack-volume-report.md) — **FreeCAD**.
- [Execute the closed-hull distribution functions without a CAD kernel](hull-distributions.md) — **Python**.
- [Inspect a closed station profile before interpreting the loft](closed-profile.md) — **FreeCAD**.
- [Report closed hull topology and measured dimensions](loft-solid-report.md) — **FreeCAD**.
- [Check guide visibility options against the construction inventory](display-option-counts.md) — **FreeCAD**.
- [Compare the sample guide model with the closed hull model](guide-versus-solid.md) — **FreeCAD**.
- [Open committed reference models without overwriting them](committed-model-readback.md) — **FreeCAD**.
- [Export only the two hull solids to temporary BREP custody](hull-brep-roundtrip.md) — **FreeCAD**.
- [Demonstrate a document-property edit with restoration](rack-property-recompute.md) — **FreeCAD**.
- [Translate a copied hull without editing the source object](hull-placement-copy.md) — **FreeCAD**.
- [Fingerprint source and inspect reference archives without opening CAD](reference-archive-manifest.md) — **Python**.
