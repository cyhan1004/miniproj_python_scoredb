from UI import UI
import dataadmin
import fileadmin
from tkinter import *

def main():
    window = Tk()
    window.title("Score DataBase Management Program")

    #모듈 객체 생성
    ui = UI(window)
    data_admin = dataadmin.dataadmin(ui)
    file_admin = fileadmin.FileAdmin(ui, data_admin)

   #ui의 button초기화
    ui.get_dataModule(data_admin)
    ui.get_fileModule(file_admin)

    window.mainloop()

if __name__ == '__main__':
    main()