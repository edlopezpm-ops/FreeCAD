from __future__ import annotations

import runpy
from pathlib import Path

import FreeCAD as App


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run_generator(relative_path: str) -> dict[str, object]:
    return runpy.run_path(str(ROOT / relative_path), run_name="__aekr_validation__")


def validate_full_catamaran() -> None:
    namespace = run_generator("FreeCAD Hull/FullCatamaranHull.py")
    document = App.getDocument(str(namespace["DOC_NAME"]))
    require(len(document.Objects) == 7, "full catamaran must contain exactly seven objects")

    for name in ("Port_Hull", "Starboard_Hull"):
        hull = document.getObject(name)
        require(hull is not None, "%s is missing" % name)
        require(hull.Shape.isValid(), "%s is invalid" % name)
        require(len(hull.Shape.Solids) == 1, "%s must contain one solid" % name)
        require(hull.Shape.Volume > 0, "%s must have positive volume" % name)

    port = document.getObject("Port_Hull").Shape.BoundBox
    starboard = document.getObject("Starboard_Hull").Shape.BoundBox
    require(abs(port.XLength - 12000.0) < 1.0, "port hull length drifted")
    require(abs(starboard.XLength - 12000.0) < 1.0, "starboard hull length drifted")
    require(port.YMax < 0 and starboard.YMin > 0, "hulls must remain on opposite sides")


def validate_sample_catamaran() -> None:
    run_generator("FreeCAD Hull/SampleCatHull.py")
    document = App.getDocument("Draft_Catamaran_Hull_Lines")
    require(len(document.Objects) == 44, "sample catamaran object count drifted")
    require(document.getObjectsByLabel("Catamaran_Centerline_Reference"), "centerline is missing")
    require(
        all(not obj.Shape.isNull() and obj.Shape.isValid() for obj in document.Objects),
        "sample catamaran contains invalid geometry",
    )


def validate_warehouse_racks() -> None:
    namespace = run_generator("FreeCAD_WHRackDesign/WarehouseRack3x3.py")
    document = App.getDocument(str(namespace["DOC_NAME"]))
    require(len(document.Objects) == 94, "warehouse rack object count drifted")
    require(document.getObject("Floor_Aisle_Reference") is not None, "floor reference is missing")
    require(
        all(not obj.Shape.isNull() and obj.Shape.isValid() for obj in document.Objects),
        "warehouse rack contains invalid geometry",
    )


def validate_committed_models() -> None:
    model_paths = (
        ROOT / "FreeCAD Hull/Catamaran_Hull_Only.FCStd",
        ROOT / "FreeCAD_WHRackDesign/FreeCAD_WHRackDesign_3_Racks_3_Levels.FCStd",
    )
    for path in model_paths:
        document = App.openDocument(str(path))
        document.recompute()
        shapes = [obj.Shape for obj in document.Objects if hasattr(obj, "Shape")]
        require(shapes, "%s contains no shapes" % path.name)
        require(all(not shape.isNull() and shape.isValid() for shape in shapes), "%s is invalid" % path.name)
        App.closeDocument(document.Name)


def main() -> None:
    validate_full_catamaran()
    validate_sample_catamaran()
    validate_warehouse_racks()
    validate_committed_models()
    print("FreeCAD geometry validation: PASS")


if __name__ == "__main__":
    main()
