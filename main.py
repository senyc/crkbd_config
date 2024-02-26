import supervisor
import board

from kb import KMKKeyboard

from kmk.extensions.peg_oled_display import Oled, OledData, OledDisplayMode, OledReactionType
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color
from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)

keyboard.debug_enabled = False

""" Split configuration """

split = Split(use_pio=True)
keyboard.modules.append(split)

""" OLED configuration """

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2"]},
        corner_three={0:OledReactionType.STATIC,1:["Corne"]},
        corner_four={0:OledReactionType.LAYER,1:["qwerty","nums"]}
    ),
    toDisplay=OledDisplayMode.TXT,flip=False
)

keyboard.extensions.append(oled_ext)

""" LED configuration """

rgb_matrix=Rgb_matrix_data(
    keys=[Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,
          Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,
          Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,
          Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE,Color.BLUE],
    underglow=[Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE, Color.BLUE]
)

rgb_ext = Rgb_matrix(split=True,ledDisplay=rgb_matrix, disable_auto_write=True)
keyboard.extensions.append(rgb_ext)

""" Keymap configuration """

keyboard.keymap = [
    [
        KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.ENT,
        KC.LSFT, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
        KC.LCTRL, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSFT,

        KC.RGUI, KC.LT(1, KC.TG(1)), KC.TAB, KC.ALT, KC.SPC, KC.BSPC
    ],
    [
        KC.TRNS, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.TRNS,
        KC.LSFT, KC.GRV, KC.MINS, KC.EQL, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TRNS,
        KC.TRNS, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.PLUS, KC.NO, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS
    ]
]

if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
