username = "MiddleManagerChild"
password = "Sassyw0rd22"
locked = True
attempt = "SassyWordzz"

unlocked = locked == False
attempt_ok = attempt == password

if unlocked and attempt_ok:
    print("✅ Login allowed")
else:
    print("❌ Login blocked")