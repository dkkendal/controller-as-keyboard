from inputs import devices, get_gamepad
import pprint
import json

for device in devices.gamepads:
    print(device)

current = 0
current_mode = None

try:
    config = json.load(open("user_settings.json", "r"))
    pprint.pprint(config)
    current_mode = config[current_mode]
except KeyError:
    config = json.load(open("defaults.json", "r"))
    print("Default")
    pprint.pprint(config)
    current_mode = config[str(current_mode)]


def gamepad_tester():
    while 1:
        try:
            events = get_gamepad()
            for event in events:
                assert isinstance(event.state, object)
                print(event.ev_type, event.code, event.state)
        except Exception as e:
            pprint.pprint(str(e))
            break


gamepad_tester()


