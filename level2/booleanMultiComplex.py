username = "BossIAm"
device = "Android_2273468"
trusted_device = "iPhone_1934392"

device_ok = device == trusted_device
code_ok = True
face_id_ok = False
touch_id_ok = False

second_step_ok = code_ok or touch_id_ok or face_id_ok
locked = False
attempt_ok = True

if not locked and attempt_ok and not device_ok and second_step_ok:
    print("Trust this device?")