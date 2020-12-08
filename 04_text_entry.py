from tkinter import *


root = Tk()
root.title("Mato GUI") # 제목설정
root.geometry('640x480')


txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요") # 글자입력창에 위에 텍스트 입력이 되어있음 기본갑 설정 수정가능

e = Entry(root, width=30) #한줄로 입력받을때, 엔트리 쓰면됨 로그인이나 패스워드같은거
e.pack()
e.insert(0, "한줄만 입력해요")

#버튼을 클릭했을때 이벤트 발생
def btncmd():
    #내용 출력
    print(txt.get("1.0",END)) # 1 : 첫 라인 0 : 0번째 컬럼 위치
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0,END)
btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()
