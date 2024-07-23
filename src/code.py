import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros
from kmk.modules.macros import Delay, Press, Release, Tap

keyboard = KMKKeyboard()

layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12,
                     board.GP11, board.GP10, board.GP5, board.GP4,
                     board.GP3, board.GP2)
keyboard.row_pins = (board.GP9, board.GP8, board.GP7, board.GP6, board.GP27)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP17, board.GP16, None), # encoder #1 
    # reversed direction encoder with no button handling and divisor of 2
    (board.GP19, board.GP18, None), # encoder #2
    )

macros = Macros()
keyboard.modules.append(macros)

#Fast_left = KC.MACRO(Tap(KC.E), Tap(KC.E), Tap(KC.E),)
#Fast_right = KC.MACRO(Tap(KC.Q), Tap(KC.Q), Tap(KC.Q),)
Fast_left = KC.MACRO(Press(KC.E), Delay(200), Release(KC.E),)
Fast_right = KC.MACRO(Press(KC.Q), Delay(200), Release(KC.Q),)


# https://kmkfw.io/keycodes
# Baldur's Gate : https://www.reddit.com/r/BaldursGate3/comments/15o4fci/diagram_for_default_keyboard_controls/

keyboard.keymap = [[
    KC.ESCAPE, KC.F1,     KC.N,  KC.I,  KC.NO, KC.K,  KC.J,  KC.L,  KC.NO, KC.O,
    KC.TAB,    KC.F2,     KC.NO, KC.NO, KC.NO, KC.U,  KC.F,  KC.B,  KC.NO, KC.NO,
    KC.M,      KC.F3,     KC.NO, KC.C,  KC.NO, KC.X,  KC.V,  KC.Q,  KC.W,  KC.E,
    KC.SPACE,  KC.F4,     KC.NO, KC.Z,  KC.NO, KC.NO, KC.NO, KC.A,  KC.S,  KC.D,
    KC.O,      KC.O,      KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
]]
# missing key combo for "Help", "Speed", "Dip", "Disengage"

# https://www.reddit.com/r/olkb/comments/122s93j/how_to_configure_second_encoder_in_kmk/
# For the next layer open 2 parentheses again. After the open bracket there is one
#parentheses for the layer and another one for the encoder. 2 layers would look like this:
#
#encoder_handler.map = [ ((encoder 1 layer 1), (encoder 2 layer 2), ), 
#                        ((encoder 1 layer 2), (encoder 2 layer 2), ),
#                      ]

# Q = Camera Turn Left, E = Camera Turn Right
# PgUp = Camera Zoom in, PgDn = Camera Zoom Out
encoder_handler.map = [ ((Fast_left, Fast_right, ), (KC.PGUP, KC.PGDOWN, ),),
                        ]

if __name__ == '__main__':
    keyboard.go()
