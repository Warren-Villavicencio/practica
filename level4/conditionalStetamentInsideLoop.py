duration = 60
countdown = 30
for second in range(duration):
    if countdown == 0:
        status = "expired ❌"
    else:
        status = "active ✅"
    if countdown > 0 and countdown <= 10:
        status = "warning ⚠️"
    if status == "expired ❌":
        left = duration - second
        print("Code", status, "Request new code?", left)
    else:
        print("Code", status, countdown)
    if countdown > 0:
        countdown -= 1
print("Session expired")