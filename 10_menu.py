from tkinter import *

root = Tk()
root.title("Mato GUI") # 제목설정
root.geometry('640x480')

def create_new_file():
    print("새 파일을 만듭니다")

menu = Menu(root)

#File Menu
menu_file = Menu(menu,tearoff=0)
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New Windows")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save all", state="disable") # 비 활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File",menu=menu_file)

#Edit Menu (빈값)
menu.add_cascade(label="Edit")

#Languge 메뉴 추가 ( 라디오 버튼을 통해서 택 1)

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu_lang.add_radiobutton(label="C#")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)



root.config(menu=menu)
root.mainloop()
