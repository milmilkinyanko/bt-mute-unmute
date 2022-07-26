import asyncio
import evdev
import subprocess
import time

def custom_exception_handler(loop, context):
    # first, handle with default handler
    loop.default_exception_handler(context)

    exception = context.get('exception')
    print(exception)
    loop.stop()

async def readEvents(device):
    async for event in device.async_read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            if event.value == 1: # 0:KEYUP, 1:KEYDOWN
                print(event.code)
                if event.code == evdev.ecodes.KEY_VOLUMEUP:
                    # unmute
                    subprocess.Popen(['aplay', '/usr/share/sounds/sound-icons/hash'])
                    subprocess.Popen(['pactl', 'set-sink-mute', '@DEFAULT_SINK@', 'false'])
                if event.code == evdev.ecodes.KEY_VOLUMEDOWN:
                    # mute
                    subprocess.Popen(['pactl', 'set-sink-mute', '@DEFAULT_SINK@', 'true'])
                    subprocess.Popen(['aplay', '/usr/share/sounds/sound-icons/capital'])

def loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.set_exception_handler(custom_exception_handler)

    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    print(devices)

    if len(devices) == 0:
        raise Exception("device num is 0")

    for device in devices:
        if device.name.find("AB") != -1:
            print(device)
            device.grab() # get exclusive access
            asyncio.ensure_future(readEvents(device), loop=loop)

    loop.run_forever()

def main():
    while True:
        try:
            loop()
        except Exception as e:
            print(e)
            print('Retry...')
            time.sleep(1)

if __name__ == "__main__":
    main()
