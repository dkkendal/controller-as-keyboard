from inputs import devices, get_gamepad
import pprint
import pyautogui

for device in devices.gamepads:
    print(device)

current = 0
current_mode = None
axis_max = 32768
axis_deadzone = 2000

send_map = [
#     Browser/nav mode
    [
        [],  # no triggers
        [],  # LT only
        [],  # RT only
        []  # both triggers
    ],

#     Numbers/Math mode
    [
        [],  # no triggers
        [],  # LT only
        [],  # RT only
        []  # both triggers
    ],

#     Spelling mode
    [
        [],  # no triggers
        [],  # LT only
        [],  # RT only
        []  # both triggers
    ],

#     F keys mode
    [
        [],  # no triggers
        [],  # LT only
        [],  # RT only
        []  # both triggers
    ]
]


def univ_handler(event):
    print(event)


def send_inputs():
    pyautogui.alert("Hello", "Test Alert")


def gamepad_tester():
    max_y = 0
    max_x = 0
    min_y = 0
    min_x = 0

    while 1:
        try:
            events = get_gamepad()
            for event in events:
                assert isinstance(event.state, object)
                if event.code != "SYN_REPORT":
                    print(event.ev_type, event.code, event.state)
                    if event.code == "ABS_Y" and event.state > max_y:
                        max_y = event.state
                        print("max_y: " + str(max_y))
                    if event.code == "ABS_X" and event.state > max_x:
                        max_x = event.state
                        print("max_x: " + str(max_x))
                    if event.code == "ABS_Y" and event.state < min_y:
                        min_y = event.state
                        print("min_y: " + str(min_y))
                    if event.code == "ABS_X" and event.state < min_x:
                        min_x = event.state
                        print("min_x: " + str(min_x))
        except Exception as e:
            pprint.pprint(str(e))
            break

        # time.sleep(0.05)


# send_inputs()
gamepad_tester()


