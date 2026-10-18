<!-- (kommiBo) Source-reviewed engineering note; optional diagnostic. -->
# Report placeholder volumes with explicit component categories

Volume can catch a wrong dimension without pretending that the model is a
manufacturing bill of materials. This console example reports each rack component
category separately and excludes the floor reference from its component sum.

| Category | Expected object count | Representation |
| --- | ---: | --- |
| Uprights | 12 | 90 x 90 x 4200 boxes |
| Base plates | 12 | 220 x 220 x 18 boxes |
| Beams | 36 | four rectangular boxes per level |
| Decks | 9 | 3320 x 820 x 55 solid boxes |
| Braces | 24 | full cylinders of radius 22.5 |

Expected output contains these five counts, positive category volumes in mm^3,
and their conversion to m^3 by dividing by 1,000,000,000. The example requires one
valid solid for each counted component and fails on an unclassified rack object.
The floor is reported separately so its convenient reference geometry does not
silently become part of a material estimate.

Summing individual volumes double-counts overlapping joints; it is not the volume
of a fused rack. The so-called wire deck is a solid visual placeholder and therefore
particularly unsuitable for weight estimates. No density, mass, load rating,
procurement quantity, or structural claim follows from these sums. Changes to
component construction require reviewing both the classifier and the assumptions.

## Run the complete example

Use a fresh FreeCAD session. Run from the repository root; the example creates
or opens model objects as described above.

```shell
freecadcmd --safe-mode --console "import runpy; runpy.run_path('docs/examples/rack-volume-report.py')"
```

[Complete example](../examples/rack-volume-report.py). The script is intended to be run as supplied.

## Source anchors

- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `add_box`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L48).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `create_beam_level`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L107).
- [`FreeCAD_WHRackDesign/WarehouseRack3x3.py`: `add_cylinder_between_points`](../../FreeCAD_WHRackDesign/WarehouseRack3x3.py#L62).
