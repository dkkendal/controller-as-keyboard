from inputs import devices, get_gamepad

for device in devices.gamepads:
    print(device)

while 1:
    events = get_gamepad()
    for event in events:
        assert isinstance(event.state, object)
        print(event.ev_type, event.code, event.state)
