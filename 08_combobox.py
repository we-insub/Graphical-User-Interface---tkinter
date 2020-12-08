import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("Mato GUI") # 제목설정
root.geometry('640x480')

# 콤보박스
values = [str(i) + "일" for i in range(31)] # 1 ~ 31 숫자 반환
combobox = ttk.Combobox(root,height=5, values=values)
combobox.pack()
combobox.set(" 카드 결제일 " ) # 최초목록 제목 설정 버튼 클릭값 을 설정할수도 있다.

readonly_combobox = ttk.Combobox(root,height=10, values=values, state="readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 실행
readonly_combobox.pack()

def btncmd():
   print(combobox.get()) # 선택된 값을 출력한다 # 2일 출력
   print(readonly_combobox.get()) # 선택된 값을 출력한다 # 2일 출력


btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop()
