from tkinter import *
import subprocess
import time

def hide_icon():
    mac = 'defaults write com.apple.finder CreateDesktop false'
    subprocess.Popen(mac, shell=True)

    restart = 'killall Finder'
    subprocess.Popen(restart, shell=True)
    time.sleep(1)


def show_icon():
    mac = 'defaults write com.apple.finder CreateDesktop true'
    subprocess.Popen(mac, shell=True)

    restart = 'killall Finder'
    subprocess.Popen(restart, shell=True)
    time.sleep(1)

# 창 만들기
root = Tk()
root.title("Desktop Cleaner") # 창 이름 설정
root.geometry('200x70') # 창 크기 가로크기 x 세로크기 + x좌표 + y좌표

# 레이블, 텍스트창 만들기 (그냥 글자 또는 이미지 넣기)

frame = LabelFrame(root, text='switch')
frame.pack(padx=5, pady=5)

btn_on = Button(frame, text="show", width=7, command=show_icon)
btn_on.pack(side='left', padx=5)

btn_off = Button(frame, text="hide", width=7, command=hide_icon)
btn_off.pack(side='right', padx=5)

root.mainloop()
