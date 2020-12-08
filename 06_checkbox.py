from tkinter import *


root = Tk()
root.title("Mato GUI") # 제목설정
root.geometry('640x480')

#check box 팝업이뜨면 1주일동안 보지않기 이런것.
chkvar = IntVar() # 체크바에 인트형 값으로 저장을 한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar) # variable변수값이 저장됨
#chkbox.select() # 기본 자동설정
#chkbox.deselect() # 기본 자동해제
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기",variable=chkvar2)
chkbox2.pack()

def btncmd():
   print(chkvar.get()) # 0일때는 체크해제 1일때 체그값 F/T  값
   print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()
