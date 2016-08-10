from tkinter import *

class FileAdmin:
    def __init__(self,UI,DataAdmin):
        self.data_admin = DataAdmin
        self.ui = UI

    def save_file(self):
        self.ui.state_clear()
        if self.ui.secframe_entlist[2].get().strip() == "":
            self.ui.state_output.insert(END, "파일 저장에 실패했습니다.")
            return
        self.f = open("./"+self.ui.secframe_entlist[2].get().strip()+".txt",'w')
        for key,value in self.data_admin.dic.items():
            self.f.write(str(key) + "\t" + self.data_admin.dic[key][0]
                         + "\t" + str(self.data_admin.dic[key][1]) + '\n')
        self.f.close()
        self.ui.state_output.insert(END, "성공적으로 저장하였습니다. (파일 이름 : " +self.ui.secframe_entlist[2].get().strip() + ")")
        self.ui.secframe_entlist[2].delete(0, END)


    def open_file(self):
        self.ui.state_clear()
        self.ui.data_clear()
        self.data_admin.dic.clear()
        if self.ui.secframe_entlist[3].get().strip() == "":
            self.ui.state_output.insert(END, "파일 불러오기에 실패했습니다.")
            return
        try:
            self.f = open("./"+ self.ui.secframe_entlist[3].get().strip() + ".txt",'r')
        except:
            self.ui.state_output.insert(END, "파일 불러오기에 실패했습니다.")
            return

        last_index = 0
        while True:
            line = self.f.readline().strip()
            if not line:
                break
            dic_list = line.split("\t")
            self.data_admin.dic[eval(dic_list[0])] = [dic_list[1],eval(dic_list[2])]
            if last_index < eval(dic_list[0]):
                last_index = eval(dic_list[0])

        self.data_admin.index = last_index + 1
        self.f.close()
        self.data_admin.show_info()
        self.ui.state_output.insert(END, "성공적으로 파일을 읽었습니다. (파일 이름 : " + self.ui.secframe_entlist[3].get().strip() + ")")
        self.ui.secframe_entlist[3].delete(0, END)