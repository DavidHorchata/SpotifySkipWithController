from inputs import get_gamepad
from skipSong import skipSong


while 1:
    events = get_gamepad()
    for event in events:
        if event.code == 'BTN_TR' and event.state == 1:
            skipSong()
