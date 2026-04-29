username = "BossIAm"
device = "iPhone_1934392"
trusted_device = "iPhone_1934392"

device_ok = device == trusted_device
code_ok = False
face_id_ok = False
touch_id_ok = False

second_step_ok = code_ok or touch_id_ok or face_id_ok

if second_step_ok:
    print("Second step passed")
else:
    print("Second step failed")