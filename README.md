# 🍊 FantaPad

> **A refreshing macro pad for video editing, designed around the Fanta aesthetics.**

  

## 📖 Story

My surname is **Fanta**. Naturally, I've always had an affinity for the iconic orange soda. When I decided to build a custom macro pad to speed up my video editing workflow, I knew exactly what the theme had to be.

**The FantaPad** combines functionality with personal branding. It features a custom-designed PCB, mechanical switches, and a "Fanta Orange" 3D-printed enclosure.

## ✨ Features

  * **6 Mechanical Keys:** Mapped to essential shortcuts (Cut, Paste, Delete, Undo).
  * **Modal Rotary Encoder:** The knob isn't just for volume. Clicking it cycles through 3 different layers:
    1.  🔊 **Volume Mode**
    2.  🔍 **Zoom Mode** (Timeline Zoom)
    3.  🎞️ **Scrub Mode** (Frame-by-frame navigation)
  * **RGB Underglow:** Powered by SK6812MINI LEDs, glowing in signature Orange.
  * **Custom PCB:** Designed in KiCad specifically for the Seeed XIAO RP2040.
  * **KMK Firmware:** easy-to-configure Python-based firmware.

## 🛠️ Hardware & BOM

| Component | Quantity | Description |
| :--- | :---: | :--- |
| **Microcontroller** | 1 | Seeed Studio XIAO RP2040 |
| **Switches** | 6 | Cherry MX Style Mechanical Switches |
| **Encoder** | 1 | EC11 Rotary Encoder (with Push Button) |
| **LEDs** | 2 | SK6812MINI (NeoPixel compatible) |
| **Keycaps** | 6 | Transparent / White for RGB diffusion |
| **Case** | 1 | 3D Printed (Orange PLA/PETG) |

## 🔌 Pinout & Wiring

The project is built around the XIAO RP2040 with a direct-pin connection (no matrix) for simplicity and speed.

| Component | XIAO Pin (Physical) | CircuitPython Pin |
| :--- | :--- | :--- |
| **Encoder A** | Pin 1 | `board.A0` |
| **Encoder B** | Pin 2 | `board.A1` |
| **Encoder Switch** | Pin 8 | `board.D7` |
| **LED Data** | Pin 5 | `board.D4` |
| **Switch 1** | Pin 11 | `board.D10` |
| **Switch 2** | Pin 4 | `board.A3` |
| **Switch 3** | Pin 6 | `board.D5` |
| **Switch 4** | Pin 3 | `board.A2` |
| **Switch 5** | Pin 7 | `board.D6` |
| **Switch 6** | Pin 9 | `board.D8` |

## 🖥️ PCB Design

The PCB was designed in **KiCad**. It features a compact layout with 3D-printable mounting holes.

*(Replace this text with a screenshot of your PCB from KiCad 3D Viewer)*
`![PCB 3D Render](./images/pcb_render.png)`

## 🚀 Firmware Setup

This board runs on **CircuitPython** with **KMK Firmware**.

1.  **Install CircuitPython:** Hold the `BOOT` button on the XIAO RP2040, plug it into your PC, and copy the `.uf2` file to the `RPI-RP2` drive.
2.  **Install KMK:** Download the [KMK Firmware](https://github.com/KMKfw/kmk_firmware) and copy the `kmk` folder to the `lib` folder on your `CIRCUITPY` drive.
3.  **Upload Code:** Copy the provided `code.py` to the root of the `CIRCUITPY` drive.

## 🎮 Controls (Default Keymap)

| Layer | Knob Rotate | Knob Click | Keys (SW1-SW6) |
| :--- | :--- | :--- | :--- |
| **0. Volume** | Vol Up / Down | Switch to Zoom | Copy, Paste, Undo, Cut, Del, Enter |
| **1. Zoom** | Ctrl + / Ctrl - | Switch to Scrub | *Pass-through* |
| **2. Scrub** | Left / Right | Switch to Volume | *Pass-through* |

## 📂 Enclosure

The case is designed in **Tinkercad** to resemble the aesthetics of a soda crate/bottle.

*(Replace this text with a screenshot of your Tinkercad model)*
`![Case Design](./images/case_design.png)`

## 📜 License

This project is open-source hardware.
Designed by **Tomas Fanta** for Hack Club Blueprint.
