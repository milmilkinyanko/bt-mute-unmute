import asyncio
import evdev
import subprocess
import time

async def helper(dev):
    async for event in dev.async_read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            if event.value == 1: # 0:KEYUP, 1:KEYDOWN
                print(event.code)
                if event.code == evdev.ecodes.KEY_VOLUMEUP:
                    subprocess.Popen(['amixer', 'set', 'Capture','cap'])
                if event.code == evdev.ecodes.KEY_ENTER:
                    subprocess.Popen(['amixer', 'set', 'Capture','nocap'])



def main():
    try:
        # ls /dev/input でevent番号要確認
        device = evdev.InputDevice('/dev/input/event7')
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
