import tkinter.ttk as ttk
from tkinter import *
import time


root = Tk()
root.title("Mato GUI") # 제목설정
root.geometry('640x480')

# 프로그래스 바 , 진행 상태 표시

# #progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # 결정되지않고 언제 끝날지 모름 ㅋ
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 순차적으로 오름
# progressbar.start(10)  # 10ms 마다 움직임
# progressbar.pack()
#
# def btncmd():
#     progressbar.stop() # 작동 중지
#
# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var = DoubleVar() # 퍼센테이즈 소수점으로올라갈수 있어서 실수로 사용하기 위해서
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var)
progressbar2.pack()

def btncmd2():
    for i in range(1,101): # 0 ~ 100 까지
        time.sleep(0.01) # 0.01 초 대기

        p_var.set(i) # 프로그래스의 값을 설정
        progressbar2.update() # ui 업데이트를 하기 위해서 (시각적으로 보이게 하기위해서)
        print(p_var.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()
