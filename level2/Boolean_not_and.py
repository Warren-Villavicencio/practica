username = "Sr_JuniorAnalyst"
password = "HelloH@ck3rs!"
locked = False
attempt = "HelloH@ck3rs!"

attempt_ok = attempt == password
code_sent = 881640
code_entered = 881640

code_ok = code_entered == code_sent

login_success = (not locked) and attempt_ok and code_ok

if not login_success:
    print("❌ Login failed")
else:
    print("✅ Login successful")

if (not locked) and (not attempt_ok):
    print("Account unlocked, but password wrong")

if (not locked) and attempt_ok and (not code_ok):
    print("Account unlocked, correct password, wrong 2FA code")           