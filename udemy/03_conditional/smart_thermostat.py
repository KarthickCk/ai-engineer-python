device_status = "active"
temperature = 36

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal.")
else:
    print("The device is currently offline.")
    