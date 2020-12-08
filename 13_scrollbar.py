from tkinter import *

root = Tk()
root.title("Mato GUI") # 제목설정
root.geometry('640x480')

# 스크롤바
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode = "extended", height=10, yscrollcommand = scrollbar.set)
for i in range(1,32): # 1~31 리스트정보
    listbox.insert(END,str(i) + "일") # 1 ~ 일
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)


root.mainloop()
