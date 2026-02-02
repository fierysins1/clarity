# 💎 Clarity

> **CS2 External Assist** | RCS • NoFlash • NoSmoke

A lightweight, external memory manipulation tool written in Python using `pymem`. Designed for educational purposes to demonstrate game memory reading/writing and vector math operations.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

## ✨ Features(More features coming soon...)

* **RCS (Recoil Control System):** Standalone recoil compensation based on view angles.
* **NoFlash:** Instantly removes flashbang blindness.
* **NoSmoke:** Disables smoke grenade particle rendering.
* **Performance:** Optimized loop with minimal CPU usage.

## ⚠️ Important: Offsets

**Game updates will change memory addresses.** If the script stops working or crashes, you likely need to update the `OFFSETS` dictionary in the code.

👉 **Always check and get the latest offsets from:**
**[a2x/cs2-dumper](https://github.com/a2x/cs2-dumper)**

## 🚀 Installation & Usage

1.  **Install Python** (Ensure "Add to PATH" is checked).
2.  **Install dependencies:**
    ```bash
    pip install pymem
    ```
3.  **Start Counter-Strike 2.**
4.  **Run the script:**
    ```bash
    python cheat.py
    ```

## ⚖️ Disclaimer

**USE AT YOUR OWN RISK.**

This software is provided for **educational purposes only**. The author assumes no responsibility for any bans, account suspensions, or penalties resulting from the use of this tool.

* VAC (Valve Anti-Cheat) or other anti-cheat systems may detect this software.
* It is recommended to test on `-insecure` launch option or against bots.
