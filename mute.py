import evdev
import subprocess
import time

while True:
    try:
        # ls /dev/input でevent番号要確認
        device = evdev.InputDevice('/dev/input/event18')
        print(device)
        device.grab() # get exclusive access

        for event in device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                if event.value == 1: # 0:KEYUP, 1:KEYDOWN
                    print(event.code)
                    if event.code == evdev.ecodes.KEY_VOLUMEUP:
                        subprocess.Popen(['amixer', 'set', 'Capture','cap'])
                    if event.code == evdev.ecodes.KEY_ENTER:
                        subprocess.Popen(['amixer', 'set', 'Capture','nocap'])

    except Exception as e:
        print(e)
        print('Retry...')
        time.sleep(1)
