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
    OledData(image={0: OledReactionType.STATIC, 1: ["1.bmp"]}),
    toDisplay=OledDisplayMode.IMG,
    flip=True,
)
keyboard.extensions.append(oled_ext)

""" LED configuration """

rgb_matrix=Rgb_matrix_data(
    keys=[Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,
          Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,
          Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,
          Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE,Color.WHITE],
    underglow=[Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE]
)

rgb_ext = Rgb_matrix(split=True,ledDisplay=rgb_matrix, disable_auto_write=True)
keyboard.extensions.append(rgb_ext)

""" Keymap configuration """

keyboard.keymap = [
    [
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.ESC,
        KC.LSFT, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
        KC.LCTRL, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSFT,
        KC.RGUI, KC.TG(1), KC.RALT, KC.SPC, KC.BSPC, KC.TG(2) 
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
