is_rain=True
is_cold=True
if is_rain and is_cold:
    print("Bring umbrella and jacket")
elif is_rain and not(is_cold):
    print("Bring umbrella")
elif not(is_rain) and is_cold:
    print("Bring jacket")
else:
    print("don't take umbrella")