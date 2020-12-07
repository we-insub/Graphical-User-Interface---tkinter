from tkinter import *


root = Tk()
root.title("Mato GUI") # 제목설정

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="C:\\Users\\82104\\Desktop\\Graphical User Interface\\imiage.png") # 파일 정의하기
label2 = Label(root, image=photo) # 이미지 넣기
label2.pack()

#버튼을 눌렀을때 레이블 텍스트 값을 변경

def change():
    label1.config(text="또 만나요")

    global photo2 # 전역변수가 아니면 선언이 안되어서 전역변수를 글로벌로 선언해서 불러옴
    photo2 = PhotoImage(file="C:\\Users\\82104\\Desktop\\Graphical User Interface\\imiage2.png")
    label2.config(image=photo2)

btn1 = Button(root, text="클릭", command=change)
btn1.pack()



root.mainloop()
