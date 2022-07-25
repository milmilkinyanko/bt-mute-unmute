# Mute/Unmute Script with Bluetooth Button

## Features
- Amazonで買った[300円Bluetoothボタン](https://www.amazon.co.jp/gp/product/B00JX70WK4)を使ってマイクをミュート/アンミュートするスクリプト
- amixerを使ってマイクのインプットボリュームをいじることでどんなチャットツールであってもミュート/アンミュート可能

## Requirements
- python3.5+
- evdev (pip module)
- ALSA

## Usage
1. `$ls /dev/input > pre`
1. BluetoothでボタンをPCに接続
1. `$ls /dev/input > post`
1. `$diff pre post`
    - このときのevent番号を記録
    - 以下では、event17とevent18であったとする
1. `#chmod 666 /dev/input/event17`
1. `#chmod 666 /dev/input/event18`
1. `$python3 mute.py`

## 参考
- https://monomonotech.jp/kurage/raspberrypi/daiso_btshutter.html
- https://flechasdesk.blogspot.com/2020/04/blog-post.html
    - マイクのインプットボリュームをいじるアイディアを参考にさせていただきました
- https://python-evdev.readthedocs.io/en/latest/tutorial.html#reading-events-using-asyncio
