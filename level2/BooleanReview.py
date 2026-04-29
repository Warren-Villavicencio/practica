username = "Alex99"
password = "OpenSesame"
locked = False
attempt = "OpenSesame"
code_sent = 542311
code_entered = 982211

if not locked and attempt == password and code_entered == code_sent:
    print("✅ Access granted")
else:
    print("❌ Access denied")