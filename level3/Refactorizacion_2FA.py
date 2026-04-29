username = "MiddleManagerChild"
password = "Sassyw0rd22"
locked = False
attempt = "Sassyw0rd22"
code_sent = 214576
code_entered = 214576

unlocked = locked == False
attempt_ok = attempt == password
code_ok = code_sent == code_entered

login_success = unlocked and attempt_ok and code_ok

if login_success:
    print("✅ Login successful")
else:
    print("❌ Login failed")