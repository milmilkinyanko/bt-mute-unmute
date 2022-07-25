import asyncio
import evdev
import subprocess
import time

async def readEvents(device):
    async for event in device.async_read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            if event.value == 1: # 0:KEYUP, 1:KEYDOWN
                print(event.code)
                if event.code == evdev.ecodes.KEY_VOLUMEUP:
                    # unmute
                    subprocess.Popen(['aplay', '/usr/share/sounds/sound-icons/hash'])
                    subprocess.Popen(['amixer', 'set', 'Capture','cap'])
                if event.code == evdev.ecodes.KEY_VOLUMEDOWN:
                    # mute
                    subprocess.Popen(['amixer', 'set', 'Capture','nocap'])
                    subprocess.Popen(['aplay', '/usr/share/sounds/sound-icons/capital'])

def main():
    try:
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        print(devices)
        for device in devices:
            if device.name.find("AB") != -1:
                print(device)
                device.grab() # get exclusive access
                asyncio.ensure_future(readEvents(device))

        loop = asyncio.get_event_loop()
        loop.run_forever()

    except Exception as e:
            print(e)
            print('Retry...')
            time.sleep(1)

if __name__ == "__main__":
    main()
