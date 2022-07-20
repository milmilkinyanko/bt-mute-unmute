import asyncio
import evdev
import subprocess
import time

async def helper(dev):
    async for event in dev.async_read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            if event.value == 1: # 0:KEYUP, 1:KEYDOWN
                print(event.code)
                # if event.code == evdev.ecodes.KEY_VOLUMEUP:
                if event.code == evdev.ecodes.BTN_LEFT:
                    # unmute
                    subprocess.Popen(['aplay', '/usr/share/sounds/sound-icons/hash'])
                    subprocess.Popen(['amixer', 'set', 'Capture','cap'])
                # if event.code == evdev.ecodes.KEY_ENTER:
                if event.code == evdev.ecodes.BTN_RIGHT:
                    # mute
                    subprocess.Popen(['amixer', 'set', 'Capture','nocap'])
                    subprocess.Popen(['aplay', '/usr/share/sounds/sound-icons/capital'])



def main():
    try:
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        device = next(i for i in devices if i.name.find("M57") != -1)
        print(device)
        device.grab() # get exclusive access
    
        loop = asyncio.get_event_loop()
        loop.run_until_complete(helper(device))
    
    except Exception as e:
            print(e)
            print('Retry...')
            time.sleep(1)

if __name__ == "__main__":
    main()
