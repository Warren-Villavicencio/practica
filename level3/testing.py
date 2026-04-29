username = "VeePeeWee"
password = "Go!ngUp65"
failed_logins = 2
locked = False

failed_logins += 1

if failed_logins >= 5:
    locked = True
    print("Cuenta bloqueada")
else:
    print("Intenta de nuevo")

print("Locked?", locked)

