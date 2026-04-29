username = "Micr0-Mngr"
face_id_ok = True
touch_id_ok = False
code_ok = False

second_step_ok = face_id_ok or touch_id_ok or code_ok

unlocked = True
attempt_ok = True

login_success = unlocked and attempt_ok and second_step_ok

if login_success:
    print("✅ Login successful")
else:
    print("❌ Login failed")