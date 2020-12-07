from tkinter import *


root = Tk()
root.title("Mato GUI") # 제목설정
#root.geometry("640x480") # 가로 * 세로 레이블사이즈
root.geometry("640x480+100+300") # 가로 * 세로 레이블사이즈 에 x위치 y 좌표

root.resizable(False,False) # x,y 의 값 변경 불가 (창 크기 변경 불가)


root.mainloop()
