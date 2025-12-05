import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB

# --- 1. Nastavení Hardware ---
keyboard = KMKKeyboard()

# Přidáme podporu pro mediální klávesy (Hlasitost) a Vrstvy
keyboard.extensions.append(MediaKeys())
layers = Layers()
keyboard.modules.append(layers)

# --- 2. Definice PINŮ (Podle tvého KiCad schématu) ---
# Pozor: CircuitPython používá značení D0-D10 nebo A0-A3.
# Zde je převod tvých fyzických pinů (červená čísla) na CircuitPython:

PIN_ENC_A = board.A0    # Pin 1
PIN_ENC_B = board.A1    # Pin 2
PIN_SW1   = board.D10   # Pin 11 (MOSI)
PIN_SW2   = board.A3    # Pin 4
PIN_SW3   = board.D5    # Pin 6 (SCL)
PIN_SW4   = board.A2    # Pin 3
PIN_SW5   = board.D6    # Pin 7 (TX)
PIN_SW6   = board.D8    # Pin 9 (SCK) - Pozor, někdy to bývá D9, zkusíme D8
PIN_KNOB  = board.D7    # Pin 8 (RX) - Tlačítko v kolečku
PIN_LED   = board.D4    # Pin 5 (SDA) - Data pro LED

# Definice tlačítek pro KeysScanner (pořadí SW1 až SW6 + KnobButton)
PINS = [
    PIN_SW1, PIN_SW2, PIN_SW3, 
    PIN_SW4, PIN_SW5, PIN_SW6, 
    PIN_KNOB
]

# --- 3. Nastavení Matice (Tlačítka) ---
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False, # Tlačítka spínají na GND (False)
)

# --- 4. Nastavení Kolečaka (Encoder) ---
encoder_handler = EncoderHandler()
encoder_handler.pins = ((PIN_ENC_A, PIN_ENC_B, None, False),)
keyboard.modules.append(encoder_handler)

# --- 5. Nastavení LED (Fanta Orange) ---
rgb = RGB(
    pixel_pin=PIN_LED,
    num_pixels=2,
    val_limit=100,
    hue_default=20,  # 20 je cca oranžová/žlutá
    sat_default=255,
    val_default=100,
)
keyboard.extensions.append(rgb)

# --- 6. KLÁVESOVÁ MAPA (To hlavní!) ---

# Definujeme přepínače vrstev (Když zmáčkneš kolečko)
TO_LAYER0 = KC.TO(0)
TO_LAYER1 = KC.TO(1)
TO_LAYER2 = KC.TO(2)

# MAPA TLAČÍTEK
# Pořadí v poli odpovídá pořadí v PINS: [SW1, SW2, SW3, SW4, SW5, SW6, KNOB_BTN]
keyboard.keymap = [
    # LAYER 0: VOLUME MODE (Oranžová)
    # Kolečko ovládá hlasitost
    [
        KC.LCTRL(KC.C),  KC.LCTRL(KC.V),  KC.LCTRL(KC.Z),  # SW1, SW2, SW3 (Copy, Paste, Undo)
        KC.LCTRL(KC.X),  KC.DELETE,       KC.ENTER,        # SW4, SW5, SW6 (Cut, Del, Enter)
        TO_LAYER1,                                         # KNOB CLICK -> Jdi na Layer 1
    ],
    
    # LAYER 1: ZOOM MODE
    # Kolečko ovládá Zoom (Ctrl + / Ctrl -)
    [
        KC.TRNS, KC.TRNS, KC.TRNS, # KC.TRNS znamená "dělej to samé co ve vrstvě 0"
        KC.TRNS, KC.TRNS, KC.TRNS,
        TO_LAYER2,                 # KNOB CLICK -> Jdi na Layer 2
    ],

    # LAYER 2: TIMELINE SCRUB MODE
    # Kolečko ovládá šipky (Doleva / Doprava)
    [
        KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS,
        TO_LAYER0,                 # KNOB CLICK -> Zpět na Layer 0
    ],
]

# MAPA KOLEČKA (Co dělá točení v každé vrstvě)
encoder_handler.map = [
    # Layer 0: Volume Up / Down
    ((KC.VOLU, KC.VOLD),), 
    
    # Layer 1: Zoom In (Ctrl+) / Zoom Out (Ctrl-)
    ((KC.LCTRL(KC.PLUS), KC.LCTRL(KC.MINUS)),),
    
    # Layer 2: Šipka Vpravo / Šipka Vlevo (Posun ve videu)
    ((KC.RIGHT, KC.LEFT),),
]

if __name__ == '__main__':
    keyboard.go()
