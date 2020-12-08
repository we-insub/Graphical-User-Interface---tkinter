from tkinter import *

root = Tk()
root.title("Mato GUI") # 제목설정
root.geometry('640x480')

#btn1 = Button(root, text="버튼1")
#btn2 = Button(root, text="버튼2")
#btn1.pack()
#btn2.pack()
#btn1.pack(side="left")
#btn2.pack(side="right")

#그리드로 위치 잡기
#btn1.grid(row=0, column=0)
#btn2.grid(row=1, column=1)


# 맨 윗줄
btn_f16 = Button(root, text="F16", padx=20, pady=20)
btn_f17 = Button(root, text="F17", padx=20, pady=20)
btn_f18 = Button(root, text="F18", padx=20, pady=20)
btn_f19 = Button(root, text="F19", padx=20, pady=20)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=5, pady=5)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=5, pady=5)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=5, pady=5)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=5, pady=5)

# clear 줄
btn_clear = Button(root, text="clear", padx=20, pady=20)
btn_equal = Button(root, text="=", padx=20, pady=20)
btn_div = Button(root, text="/", padx=20, pady=20)
btn_mul = Button(root, text="*", padx=20, pady=20)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=5, pady=5)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=5, pady=5)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=5, pady=5)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=5, pady=5)

# 7 시작줄
btn_7 = Button(root, text="7", padx=20, pady=20)
btn_8 = Button(root, text="8", padx=20, pady=20)
btn_9 = Button(root, text="9", padx=20, pady=20)
btn_sub = Button(root, text="-", padx=20, pady=20)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=5, pady=5)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=5, pady=5)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=5, pady=5)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=5, pady=5)

# 4 시작줄
btn_4 = Button(root, text="4", padx=20, pady=20)
btn_5 = Button(root, text="5", padx=20, pady=20)
btn_6 = Button(root, text="6", padx=20, pady=20)
btn_add = Button(root, text="+", padx=20, pady=20)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=5, pady=5)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=5, pady=5)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=5, pady=5)
btn_add.grid(row=3, column=3, sticky=N+E+W+S, padx=5, pady=5)

# 1 시작줄
btn_1 = Button(root, text="1", padx=20, pady=20)
btn_2 = Button(root, text="2", padx=20, pady=20)
btn_3 = Button(root, text="3", padx=20, pady=20)
btn_enter = Button(root, text="enter", padx=20, pady=20) #세로로 합처저야 합니다.

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=5, pady=5)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=5, pady=5)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=5, pady=5)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=5, pady=5) #rowspan #두개를 합치겠다는 말

# 0 시작줄
btn_0 = Button(root, text="0", padx=20, pady=20)
btn_point = Button(root, text=".", padx=20, pady=20)
btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=5, pady=5) #
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=5, pady=5)

root.mainloop()
