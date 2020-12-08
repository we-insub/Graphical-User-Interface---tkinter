from tkinter import *


root = Tk()
root.title("Mato GUI") # 제목설정
root.geometry('640x480')

listbox = Listbox(root, selectmode = "extended", height=0) # 복수 단수 선택가능
#listbox = Listbox(root, selectmode = "single", height=0) # 단수만 선택가능 # 높이 3이라하면 3개만 보여줌
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"포도")
listbox.insert(END,"수박")
listbox.pack()

#버튼을 클릭했을때 이벤트 발생
def btncmd():
   #listbox.delete(END) # 맨 뒤 항목을 삭제
   #listbox.delete(0) # 맨 앞 항목을 삭제

   # 갯수 확인
   #print("리스트에는 ", listbox.size()," 개가 있습니다")

   # 항목확인 # 시작 인덱스 끝 인덱스를 부여하면된다.
   #print("1 ~ 3 번째 항목 직기 ! :", listbox.get(0,2))

   # 선택된 항목 확인
   print("선택된 항목은 : ",listbox.curselection()) # 문자열이 아닌 인덱스 값으로 값이 출력 됨


btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()
