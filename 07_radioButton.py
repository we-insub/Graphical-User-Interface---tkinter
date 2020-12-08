from tkinter import *


root = Tk()
root.title("Mato GUI") # 제목설정
root.geometry('640x480')

# 4지선다 같은 느낌 = Radio Button
# 여러개 버튼 중에서 하나만 선택 가능 하다

Label(root, text="메뉴를 선택하세요").pack()

buger_var = IntVar() # 인트형으로 값을 저장 하게 된다.
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=buger_var)
btn_burger1.select() # 기본적으로 선택이 되어서 보여짐
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=buger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=buger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

# 라디오버튼 여러개 그룹핑
Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink1.pack()
btn_drink2.pack()


def btncmd():
   print(buger_var.get()) # 햄버거 중 선택된 라디오 항목의 값 (Valuie)을 출력 , 벨류값 짝짓기
   print(drink_var.get()) # 음료중 중 선택된 라디오 항목의 값 (Valuie)을 출력 , 벨류값 짝짓기



btn = Button(root, text="주문", command=btncmd)
btn.pack()


root.mainloop()
