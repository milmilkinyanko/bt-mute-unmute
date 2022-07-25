# Mute/Unmute Script with Bluetooth Button

## Features
- Amazonで買った[300円Bluetoothボタン](https://www.amazon.co.jp/gp/product/B00JX70WK4)を使ってマイクをミュート/アンミュートするスクリプト
- amixerを使ってマイクのインプットボリュームをいじることでどんなチャットツールであってもミュート/アンミュート可能

## Requirements
- python3.5+
- evdev (pip module)
- ALSA

## Usage
### 初回のみ
1. `# cp 99-ABShutter.rules /etc/udev/rules.d/`
1. `# udevadm trigger`
### 毎回
1. BluetoothボタンをPCに接続
1. `$ python3 mute.py`

## 参考
- https://monomonotech.jp/kurage/raspberrypi/daiso_btshutter.html
- https://flechasdesk.blogspot.com/2020/04/blog-post.html
    - マイクのインプットボリュームをいじるアイディアを参考にさせていただきました
- https://python-evdev.readthedocs.io/en/latest/tutorial.html#reading-events-using-asyncio
