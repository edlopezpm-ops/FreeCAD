# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Execute the closed-hull distribution functions without a CAD kernel.

Uses standard-library Python; does not validate FreeCAD geometry.
See the paired engineering note for expected output and limitations.
"""

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def literals(relative_path):
    tree = ast.parse((ROOT / relative_path).read_text(encoding="utf-8"))
    values = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name):
                try:
                    values[target.id] = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    pass
    return values

import math

source = ROOT / "FreeCAD Hull/FullCatamaranHull.py"
tree = ast.parse(source.read_text(encoding="utf-8"))
names = {"clamp", "station_t", "longitudinal_fullness", "beam_at", "draft_at",
         "keel_z_at", "sheer_z_at", "x_at"}
nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
assert len(nodes) == len(names)
namespace = literals("FreeCAD Hull/FullCatamaranHull.py")
namespace["math"] = math
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source), "exec"), namespace)
for t in (0, .25, .5, .75, 1):
    row = [namespace[name](t) for name in ("x_at", "beam_at", "draft_at", "keel_z_at", "sheer_z_at")]
    print("t", t, "x_beam_draft_keel_sheer_mm", [round(value, 6) for value in row])
assert math.isclose(namespace["beam_at"](.5), 1200)
assert math.isclose(namespace["keel_z_at"](.5), -1200)
assert namespace["station_t"](9) == .5
