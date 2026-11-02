# FreeCAD Warehouse Rack Design

Small hobby FreeCAD project for drawing a simple warehouse rack layout with Python.

The script creates three pallet racks with three storage levels each, including uprights, beams, base plates, decks, and side bracing. It is meant to be copied into the FreeCAD Python console or executed with `FreeCADCmd` for quick geometry validation.

<!-- (kommiBo) The generator closes matching open documents before rebuilding. -->
## Before running

Use a fresh disposable FreeCAD session. `WarehouseRack3x3.py` closes every open document whose
internal name starts with `FreeCAD_WHRackDesing_3_Racks_3_Levels` before rebuilding; the source contains no save step
for those documents. Save or export work you need to keep before running it, and do not
assume a matching suffix protects an earlier model.

Successful geometry checks do not establish rack load capacity, anchoring or safe installation. Review inputs and obtain any
required engineering assessment before real-world use. See the repository's
[use boundaries](../TERMS.md) and [data-handling guide](../docs/data-handling.md).

## File

- `WarehouseRack3x3.py`: builds the three-rack warehouse model in millimeters.

## Notes

This is a visual/learning model, not a certified structural engineering design.
