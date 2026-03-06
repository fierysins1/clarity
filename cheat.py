import pymem
import pymem.process
import struct
import time

OFFSETS = {
    "dwLocalPlayerPawn": 0x2062850,
    "dwViewAngles": 0x2312BD8,
    "dwEntityList": 0x19BDD58,
    "m_flFlashDuration": 0x15F8,
    "m_iShotsFired": 0x270C,
    "m_aimPunchCache": 0x16F0,
    "m_iHealth": 0x334,
    "m_nSmokeEffectTickBegin": 0x1450,
    "m_bDidSmokeEffect": 0x1454
}

def main():
    try:
        pm = pymem.Pymem("cs2.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        print("cs2.exe process detected and cheat loaded")
    except Exception:
        print("start cs2.exe first")
        return

    old_punch_x = 0.0
    old_punch_y = 0.0
    loop_count = 0
    recoil_scale = 2.0
    smoke_check_interval = 10

    while True:
        try:
            local_player = pm.read_longlong(client + OFFSETS["dwLocalPlayerPawn"])
            if not local_player:
                time.sleep(0.002)
                continue

            if pm.read_int(local_player + OFFSETS["m_iHealth"]) <= 0:
                time.sleep(0.002)
                continue

            flash_addr = local_player + OFFSETS["m_flFlashDuration"]
            if pm.read_float(flash_addr) > 0.0:
                pm.write_float(flash_addr, 0.0)

            shots = pm.read_int(local_player + OFFSETS["m_iShotsFired"])
            if shots > 1:
                punch_x, punch_y = struct.unpack("ff", pm.read_bytes(local_player + OFFSETS["m_aimPunchCache"], 8))

                dx = (punch_x - old_punch_x) * recoil_scale
                dy = (punch_y - old_punch_y) * recoil_scale

                view_addr = client + OFFSETS["dwViewAngles"]
                curr_x, curr_y = struct.unpack("ff", pm.read_bytes(view_addr, 8))

                pm.write_bytes(view_addr, struct.pack("ff", curr_x - dx, curr_y - dy), 8)

                old_punch_x = punch_x
                old_punch_y = punch_y
            else:
                old_punch_x = 0.0
                old_punch_y = 0.0

            loop_count += 1
            if loop_count == smoke_check_interval:
                loop_count = 0
                ent_list = pm.read_longlong(client + OFFSETS["dwEntityList"])
                if ent_list:
                    entry = pm.read_longlong(ent_list + 16)
                    if entry:
                        for i in range(64, 512):
                            try:
                                ent = pm.read_longlong(entry + 120 * (i & 0x1FF))
                                if not ent: continue

                                tick_addr = ent + OFFSETS["m_nSmokeEffectTickBegin"]
                                if pm.read_int(tick_addr) > 0:
                                    state_addr = ent + OFFSETS["m_bDidSmokeEffect"]
                                    if pm.read_bool(state_addr):
                                        pm.write_bool(state_addr, False)
                                        pm.write_int(tick_addr, 0)
                            except Exception:
                                continue

            time.sleep(0.002)

        except KeyboardInterrupt:
            break
        except Exception:
            continue

if __name__ == "__main__":
    main()
