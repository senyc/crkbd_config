import supervisor
import board

from kmk.extensions.media_keys import MediaKeys
from kb import KMKKeyboard

from kmk.extensions.peg_oled_display import Oled, OledData, OledDisplayMode, OledReactionType
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color
from kmk.hid import HIDModes
from kmk.keys import KC, make_key
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()
modtap = ModTap()
layers_ext = Layers()
keyboard.modules.append(layers_ext)
keyboard.modules.append(modtap)

keyboard.debug_enabled = True

""" Split configuration """

split = Split(use_pio=True)
keyboard.modules.append(split)

""" OLED configuration """

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1", "2", "3"]},
        corner_three={0:OledReactionType.STATIC,1:["Corne"]},
        corner_four={0:OledReactionType.LAYER,1:["qwerty", "nums", "func"]}
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

""" Media keys configuration """
keyboard.extensions.append(MediaKeys())

""" Keymap configuration """

"""
GESC: Escape unless selected with shift or super, then `
BKDL: backspace unless selected with super, then del 
"""
keyboard.keymap = [
    [
        KC.GESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BKDL,
        KC.LSFT, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
        KC.LCTRL, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSFT,

        KC.LGUI, KC.TT(1), KC.TAB, KC.LALT, KC.SPC, KC.TT(1)
    ],
    [
        KC.TRNS, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.ENT,
        KC.LSFT, KC.UNDERSCORE, KC.MINS, KC.EQL, KC.LPRN, KC.RPRN, KC.HT(KC.LEFT, KC.MEDIA_PREV_TRACK), KC.HT(KC.DOWN, KC.AUDIO_VOL_DOWN), KC.HT(KC.UP, KC.AUDIO_VOL_UP), KC.HT(KC.RIGHT, KC.MEDIA_NEXT_TRACK), KC.HT(KC.LBRC, KC.MEDIA_PLAY_PAUSE), KC.HT(KC.RBRC, KC.PSCR),
        KC.TRNS, KC.NO, KC.NO, KC.NO, KC.NO, KC.TO(2), KC.NO, KC.BSLASH, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.TRNS, KC.TO(0), KC.TRNS, KC.TRNS, KC.TRNS, KC.TO(0)
    ],
    [
        KC.TRNS, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.TRNS,
        KC.TRNS, KC.F11, KC.F12, KC.PGUP, KC.PGDN, KC.END, KC.SLCK, KC.NLCK, KC.CAPS, KC.NO, KC.NO, KC.TRNS,
        KC.LCTRL, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.TRNS, KC.TO(0), KC.TRNS, KC.TRNS, KC.TRNS, KC.TO(1)
    ]
]


if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
