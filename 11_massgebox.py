import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Mato GUI") # 제목설정
root.geometry('640x480')

# 메세지 박스, 에러가 떳을대 팝업박스 같은것
# 기차 예메 시스템이라고 가정하자

def info():
    msgbox.showinfo("알림","정상적으로 예매가 완료 되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당좌석은 이미 매진 되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생 되었습니다.")

def okcancle():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아 동반석입니다. 예매하시겠습니까?.")

def retrycancle():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류 입니다. 다시 시도 하시겠습니까??.")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향 입니다. 예매 하시겠습니까?.")

def yesnocancle():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장 되지 않았습니다.\n 저장후 프로그램을 종료 하시겠습니까?")
    # 네 : 저장후 종료
    # 아니오 : 저장하지 않고 종료
    # 취소ㅓ : 프로그램 종료 취소 ( 현재 화면에서 계속 작업)
    print("응답 :" , response) # Ture False None 1=예 2=아니오 그외
    if response == 1:
        print("예")
    elif response ==0:
        print("아니오")
    else:
        print("취소")
Button(root, command=info, text="알람").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancle, text="확인 캔슬").pack()
Button(root, command=retrycancle, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니요").pack()
Button(root, command=yesnocancle, text="예 아니요 취소").pack()



root.mainloop()
