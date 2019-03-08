from inputs import devices, get_gamepad
import pprint
import pyautogui

AXIS_DEAD_ZONE = 2000
AXIS_MAX = 32768 - AXIS_DEAD_ZONE
AXIS_DPS = 50

current = 0
current_mode = None
move_mouse = False

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


def mouse_calculator(val):
    if val < AXIS_DEAD_ZONE:
        return 0

    sign = val/abs(val)
    val = val - sign * AXIS_DEAD_ZONE

    # give extra dead zone where the mouse moves really slowly
    if val < AXIS_DEAD_ZONE:
        return 1

    val = sign * AXIS_DPS * (val / AXIS_MAX)**2
    return int(val)


def mouse_handler(x, y):
    global move_mouse
    x = mouse_calculator(x)
    y = mouse_calculator(y)
    if abs(x) < 1 and abs(y) < 1:
        # print('('+str(x)+', '+str(y)+')')
        return
    pyautogui.move(x, y, 0.01)


def send_inputs():
    pyautogui.alert("Hello", "Test Alert")


def game_pad_tester():
    global move_mouse
    current_x = current_y = 0

    while True:
        try:
            events = get_gamepad()
            for event in events:
                assert isinstance(event.state, object)
                if event.code != "SYN_REPORT":
                    # print(event.ev_type, event.code, event.state)
                    state = int(event.state)
                    if event.code == "ABS_X":
                        if abs(state) > AXIS_DEAD_ZONE:
                            current_x = state
                            move_mouse = True
                        else:
                            print("x: "+str(state))
                    if event.code == "ABS_Y":
                        if abs(state) > AXIS_DEAD_ZONE:
                            current_y = -state
                            move_mouse = True
                        else:
                            print("y: "+str(state))

            if move_mouse:
                mouse_handler(current_x, current_y)
                current_y = current_x = 0
                move_mouse = False

        except Exception as e:
            pprint.pprint(str(e))
            break


# send_inputs()
game_pad_tester()


