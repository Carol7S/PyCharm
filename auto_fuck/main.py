from pykeyboard import *
from pymouse import *
import time
import pyperclip

# lianHuaUrl = "https://zuanbot.com/api.php?level=min&lang=zh_cn"

# fileName = 'huoLi.txt'
# fileName = 'lianHua.txt'
fileName = 'fo.txt'

def readText(lines):
    try:
        with open(fileName, 'r') as f:
            for line in f:
                line = line.split('.', 1)
                # line = line[1].strip('\n')
                lines.append(line[1])
    except Exception:
        print('File Error')


def fuck():
    for i in range(10):
        try:
            # 输入文字
            pyperclip.copy(lines[i])
            # 以下语句模拟键盘点击ctrl+v
            k.press_key('command')
            k.tap_key('v')
            k.release_key('command')
            time.sleep(1)
            k.tap_key('return')
        except Exception:
            print('Error')

def fuck_all():
    for i in range(10):
        try:
            # 输入文字
            pyperclip.copy(lines[i])
            # 以下语句模拟键盘点击ctrl+v
            k.press_key('command')
            k.tap_key('v')
            k.release_key('command')
            time.sleep(1)
            k.tap_key('return')
        except Exception:
            print('Error')


if __name__ == '__main__':
    lines = []
    readText(lines)
    print(lines)


    m = PyMouse()  # 建立鼠标对象
    k = PyKeyboard()  # 建立键盘对象

    time.sleep(3)
    location1 = m.position()
    # 点击窗口
    m.click(location1[0], location1[1])

    fuck()
