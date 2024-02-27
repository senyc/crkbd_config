import supervisor
from storage import getmount
import board

from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_display import Oled, OledData, OledDisplayMode, OledReactionType
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color
from kmk.hid import HIDModes
from kmk.keys import KC
from kmk.modules.layers import Layers 
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()
layers_ext = Layers()
keyboard.modules.append(layers_ext)

keyboard.debug_enabled = False

""" Split configuration """

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

split = Split(use_pio=True)
keyboard.modules.append(split)

""" OLED configuration """

if side == SplitSide.LEFT:
    oled_ext = Oled(
        OledData(
            corner_one={0:OledReactionType.STATIC,1:["layer"]},
            corner_two={0:OledReactionType.LAYER,1:["1", "2", "3"]},
            corner_three={0:OledReactionType.STATIC,1:["Corne"]},
            corner_four={0:OledReactionType.LAYER,1:["qwerty", "nums", "func"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=False
    )
else:
    oled_ext = Oled(
        OledData(
            corner_one={0:OledReactionType.STATIC,1:["Corne"]},
            corner_two={0:OledReactionType.STATIC,1:["Corne"]},
            corner_three={0:OledReactionType.STATIC,1:["Corne"]},
            corner_four={0:OledReactionType.STATIC,1:["Corne"]},
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

keyboard.extensions.append(MediaKeys())

"""
GESC: Escape unless selected with super, then ` if shift then ~
BKDL: backspace unless selected with super, then del 
"""
keyboard.keymap = [
    [
        KC.GESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BKDL,
        KC.LSFT, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT,
        KC.LCTRL, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSFT,

        KC.LGUI, KC.TT(1), KC.SPC, KC.TAB, KC.TT(1), KC.LALT
    ],
    [
        KC.TRNS, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.ENT,
        KC.LSFT, KC.UNDERSCORE, KC.MINS, KC.EQL, KC.LPRN, KC.RPRN, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.LBRC, KC.RBRC,
        KC.TRNS, KC.PSCR, KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK, KC.TO(0), KC.TO(2), KC.BSLASH, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.TRNS, KC.TO(0), KC.TRNS, KC.TRNS, KC.TO(0), KC.TRNS
    ],
    [
        KC.TRNS, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.TRNS,
        KC.TRNS, KC.F11, KC.F12, KC.PGUP, KC.PGDN, KC.END, KC.SLCK, KC.NLCK, KC.CAPS, KC.NO, KC.NO, KC.TRNS,
        KC.LCTRL, KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        KC.TRNS, KC.TO(0), KC.TRNS, KC.TRNS, KC.TO(1),KC.TRNS
    ]
]


if __name__ == "__main__":
    keyboard.go(hid_type=HIDModes.USB)
