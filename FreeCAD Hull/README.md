# FreeCAD Catamaran Hull

Small hobby FreeCAD project for generating a simple catamaran hull-only model with Python.

The script creates two closed lofted hulls using FreeCAD's `Part` workbench APIs. It is meant to be copied into the FreeCAD Python console or executed with `FreeCADCmd` for quick geometry validation.

<!-- (kommiBo) The generator closes matching open documents before rebuilding. -->
## Before running

Use a fresh disposable FreeCAD session. `FullCatamaranHull.py` closes every open document whose
internal name starts with `Catamaran_Hull_Only` before rebuilding; the source contains no save step
for those documents. Save or export work you need to keep before running it, and do not
assume a matching suffix protects an earlier model.

Successful geometry checks do not establish buoyancy, vessel stability or safe fabrication. Review inputs and obtain any
required engineering assessment before real-world use. See the repository's
[use boundaries](../TERMS.md) and [data-handling guide](../docs/data-handling.md).

## File

- `FullCatamaranHull.py`: builds the catamaran hull model in millimeters.

## Notes

This is a visual/learning model, not a certified naval architecture design.
