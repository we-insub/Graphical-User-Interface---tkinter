from tkinter import *


root = Tk()
root.title("Mato GUI") # 제목설정

btn1 = Button(root, text="버튼1") # 속성없이 텍스트만
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2") # 버튼내에서 공간을 좀더 차지해서 버튼 크기를 키워줄수 있다.
btn2.pack() #버튼 글자가 커지거나 많아지면 넓이가 넓어진다. 하지만  btn4는 글자가짤린다.

btn3 = Button(root, padx=10, pady=5, text="버튼3") # pad x,y 가로 세로 값을 설정할수 있다.
btn3.pack()


btn4 = Button(root, width=10, height=3, text="버튼4") # 버튼 크기를 선언해서 크기 만들기.
btn4.pack() # 위디스와 하이트는 글자와 상관없이 크기선언.

btn5 = Button(root, fg="red", bg="yellow", text="버튼6") # 생상 넣기
btn5.pack()

photo = PhotoImage(file="C:\\Users\\82104\\Desktop\\Graphical User Interface\\imiage.png") # 파일 정의하기
btn6 = Button(root, image=photo)
btn6.pack() # 버튼생성

def btncmd(): #함수선언
    print("버튼이 클릭 되었어요")
btn7 = Button(root, text="동작하는버튼", command=btncmd) # 커맨드 함수를 통해서 프린트문 출력
btn7.pack()

root.mainloop()
