duration = 30
elapsed = 0
status = "sent"
print("Code", status)
for second in range(duration):
    elapsed += 1
    status = "active"
    print("Code", status, "Elapsed:", elapsed)
status = "expired"
print("Code", status)