username = "EmilyVP"
password = "Safety1st!"
locked = False
attempt = "Safety1st!"
code_sent = 836027
code_entered = 836027

if locked == False and attempt == password and code_entered == code_sent:
    print("✅ Login successful")
else:
    print("❌ Login failed")