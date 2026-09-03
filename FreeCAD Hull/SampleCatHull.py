import FreeCAD as App
import Draft
import Part

try:
    import FreeCADGui as Gui
except Exception:
    Gui = None


doc = App.newDocument("Draft_Catamaran_Hull_Lines")


# Define las medidas base en milimetros.

L = 12000
# Usa 12 metros de largo total.

hull_beam = 1200
# Ajusta la manga de cada casco.

overall_beam = 6000
# Ajusta la manga total aproximada.

D = 1200
# Ajusta la profundidad de cada casco.

stations = 15
# Cambia la cantidad de secciones.

hull_spacing = overall_beam - hull_beam
# Calcula la separacion entre centros.

port_hull_y = -hull_spacing / 2
# Ubica el casco de babor.

starboard_hull_y = hull_spacing / 2
# Ubica el casco de estribor.


# Aplica color y grosor a cada curva.

def style(obj, color=(0.2, 0.45, 0.9), width=2):
    if Gui is not None and getattr(obj, "ViewObject", None) is not None:
        obj.ViewObject.LineColor = color
        obj.ViewObject.LineWidth = width
    return obj


# Calcula la forma del casco.

def beam_at(x):
    """Haz el casco mas ancho al centro."""
    t = x / L
    return hull_beam * (0.10 + 0.90 * (1 - (2*t - 1)**2))


def depth_at(x):
    """Haz el casco mas profundo al centro."""
    t = x / L
    return D * (0.40 + 0.60 * (1 - (2*t - 1)**2))


def z_keel(x):
    """Traza la quilla por debajo de la linea base."""
    t = x / L
    return -depth_at(x) * (0.70 + 0.30 * (1 - abs(2*t - 1)))


# Crea las curvas de un casco.

def create_single_hull(center_y, name_prefix):
    """Dibuja un casco y sus guias."""

    station_curves = []

    keel_pts = []
    port_sheer_pts = []
    starboard_sheer_pts = []
    port_chine_pts = []
    starboard_chine_pts = []

    for i in range(stations):
        x = L * i / (stations - 1)

        half_beam = beam_at(x) / 2
        depth = depth_at(x)
        keel_z = z_keel(x)

        # Dibuja una seccion transversal.

        pts = [
            App.Vector(x, center_y - half_beam, 0),
            App.Vector(x, center_y - half_beam * 0.80, -depth * 0.20),
            App.Vector(x, center_y - half_beam * 0.40, -depth * 0.70),
            App.Vector(x, center_y, keel_z),
            App.Vector(x, center_y + half_beam * 0.40, -depth * 0.70),
            App.Vector(x, center_y + half_beam * 0.80, -depth * 0.20),
            App.Vector(x, center_y + half_beam, 0),
        ]

        curve = Draft.make_bspline(pts, closed=False, face=False)
        curve.Label = "%s_Station_%02d" % (name_prefix, i)
        style(curve, (0.1, 0.4, 1.0), 2)
        station_curves.append(curve)

        # Guarda puntos para las guias largas.

        keel_pts.append(App.Vector(x, center_y, keel_z))

        port_sheer_pts.append(App.Vector(x, center_y - half_beam, 0))

        starboard_sheer_pts.append(App.Vector(x, center_y + half_beam, 0))

        port_chine_pts.append(App.Vector(x, center_y - half_beam * 0.50, -depth * 0.65))

        starboard_chine_pts.append(App.Vector(x, center_y + half_beam * 0.50, -depth * 0.65))

    # Dibuja las guias longitudinales.

    keel = Draft.make_bspline(keel_pts, closed=False, face=False)
    keel.Label = "%s_Keel_Line" % name_prefix
    style(keel, (1.0, 0.1, 0.1), 4)

    port_sheer = Draft.make_bspline(port_sheer_pts, closed=False, face=False)
    port_sheer.Label = "%s_Port_Sheer_Line" % name_prefix
    style(port_sheer, (0.0, 0.7, 0.2), 3)

    starboard_sheer = Draft.make_bspline(starboard_sheer_pts, closed=False, face=False)
    starboard_sheer.Label = "%s_Starboard_Sheer_Line" % name_prefix
    style(starboard_sheer, (0.0, 0.7, 0.2), 3)

    port_chine = Draft.make_bspline(port_chine_pts, closed=False, face=False)
    port_chine.Label = "%s_Port_Chine_Guide" % name_prefix
    style(port_chine, (0.9, 0.6, 0.0), 2)

    starboard_chine = Draft.make_bspline(starboard_chine_pts, closed=False, face=False)
    starboard_chine.Label = "%s_Starboard_Chine_Guide" % name_prefix
    style(starboard_chine, (0.9, 0.6, 0.0), 2)

    return station_curves


# Dibuja los dos cascos.

port_hull = create_single_hull(port_hull_y, "Port_Hull")

starboard_hull = create_single_hull(starboard_hull_y, "Starboard_Hull")


# Agrega guias visuales para la cubierta.

deck_z = 500
# Ajusta la altura de la cubierta.

bridge_station_indexes = [3, 7, 11]
# Elige donde van las lineas del puente.

for idx in bridge_station_indexes:
    x = L * idx / (stations - 1)

    bridge_pts = [
        App.Vector(x, port_hull_y, deck_z),
        App.Vector(x, starboard_hull_y, deck_z),
    ]

    bridge_line = Draft.make_bspline(bridge_pts, closed=False, face=False)
    bridge_line.Label = "Bridge_Deck_Guide_%02d" % idx
    style(bridge_line, (0.8, 0.2, 0.8), 2)


# Agrega la linea central.

centerline_pts = [
    App.Vector(0, 0, deck_z),
    App.Vector(L, 0, deck_z),
]

centerline = Draft.make_bspline(centerline_pts, closed=False, face=False)
centerline.Label = "Catamaran_Centerline_Reference"
style(centerline, (0.5, 0.5, 0.5), 1)


# Actualiza el modelo y centra la vista.

doc.recompute()

if Gui is not None and getattr(Gui, "ActiveDocument", None) is not None:
    Gui.ActiveDocument.ActiveView.viewAxometric()
    Gui.SendMsgToActiveView("ViewFit")


print("Draft catamaran hull lines created.")
print("Length:", L, "mm")
print("Single hull beam:", hull_beam, "mm")
print("Overall beam:", overall_beam, "mm")
print("Hull depth:", D, "mm")
print("Stations per hull:", stations)
