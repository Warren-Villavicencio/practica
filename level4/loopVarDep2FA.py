duration = 30
print("Code sent")
for second in range(duration):
    countdown = duration - second
    warning = countdown <= 10
    print("Countdown:", countdown, "Warning?", warning)
print("Code expired")