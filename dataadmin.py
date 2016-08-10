from tkinter import *

class dataadmin:

    def __init__(self,UI):
        self.dic = {}
        self.index = 1
        self.ui = UI

    #출력함수
    def show_info(self):
        self.ui.data_clear()
        for key,value in self.dic.items():
            self.ui.data_output.insert(END, key)
            self.ui.data_output.insert(END, "\t" + self.dic[key][0] + "\t")
            self.ui.data_output.insert(END, self.dic[key][1])
            self.ui.data_output.insert(END, '\n')

    #추가함수
    def add_click(self):
        self.ui.state_clear()
        self.dic_value1 = self.ui.name.get().strip()

        if self.dic_value1 == "":
            self.ui.state_output.insert(END, "[추가 실패] 이름을 다시 입력해 주세요.")
            return
        for key,value in self.dic.items() :
             if self.dic_value1 == value[0]:
                self.ui.state_output.insert(END, "[추가 실패] 동일한 이름이 존재합니다.")
                return

        try:
            self.dic_value2 = eval(self.ui.secframe_entlist[0].get())
        except:
            self.ui.state_output.insert(END, "[추가 실패] 점수를 다시 입력하세요.")
            return

        self.dic[self.index] = [self.dic_value1, self.dic_value2]
        self.show_info()
        self.ui.state_output.insert(END,"성공적으로 추가하였습니다")
        self.index += 1
        self.ui.name.delete(0,END)
        self.ui.secframe_entlist[0].delete(0, END)


    #삭제함수
    def del_click(self):
        self.ui.state_clear()
        try:
            self.del_num  = eval(self.ui.secframe_entlist[1].get())
            del self.dic[self.del_num]
            self.show_info()
        except:
            self.ui.state_output.insert(END,"삭제에 실패했습니다.")
            return

        self.ui.state_output.insert(END, "성공적으로 삭제하였습니다")
        self.ui.secframe_entlist[1].delete(0,END)


    #이름 수정함수
    def change_name(self):
        self.ui.state_clear()
        index = self.ui.edit_nameidx.get().strip()
        self.editname = self.ui.edit_name.get().strip()
        if index == "" or self.editname == "":
            self.ui.state_output.insert(END, "수정에 실패했습니다.")
            return
        for key, value in self.dic.items():
            if self.editname == value[0]:
                self.ui.state_output.insert(END, "[수정 실패] 동일한 이름이 존재합니다.")
                return
        try:
            self.dic[eval(index)][0] = self.editname
        except:
            self.ui.state_output.insert(END, "수정에 실패했습니다.")
            return
        self.ui.data_clear()
        self.show_info()
        self.ui.edit_nameidx.delete(0, END)
        self.ui.edit_name.delete(0, END)

    #점수 수정함수
    def change_score(self):
        self.ui.state_clear()
        index = self.ui.edit_scoreidx.get().strip()
        self.editscore = self.ui.edit_score.get().strip()
        if index == "" or self.editscore == "":
            self.ui.state_output.insert(END, "수정에 실패했습니다.")
            return
        try:
            self.dic[eval(index)][1] = eval(self.editscore)
        except:
            self.ui.state_output.insert(END, "수정에 실패했습니다.")
            return
        self.ui.data_clear()
        self.show_info()
        self.ui.edit_scoreidx.delete(0, END)
        self.ui.edit_score.delete(0, END)


    #sorting
    def sort_numseq(self):
        self.ui.state_clear()
        self.sorted_list = sorted(zip(self.dic.keys(),self.dic.values()))
        self.dic.clear()
        self.dic = dict(self.sorted_list)
        self.show_info()


    def sort_nameseq(self):
        self.ui.state_clear()
        self.ui.data_clear()
        self.sorted_list = sorted(self.dic.items(),key=lambda x:x[1][0])
        for i in range (len(self.sorted_list)):
            self.ui.data_output.insert(END,self.sorted_list[i][0])
            self.ui.data_output.insert(END, "\t" + self.sorted_list[i][1][0] + "\t")
            self.ui.data_output.insert(END, self.sorted_list[i][1][1])
            self.ui.data_output.insert(END, '\n')


    def sort_scoreseqrev(self): #내림차순
        self.ui.state_clear()
        self.ui.data_clear()
        self.sorted_list = sorted(self.dic.items(), key=lambda x: x[1][1],reverse = True)
        for i in range(len(self.sorted_list)):
            self.ui.data_output.insert(END, self.sorted_list[i][0])
            self.ui.data_output.insert(END, "\t" + self.sorted_list[i][1][0] + "\t")
            self.ui.data_output.insert(END, self.sorted_list[i][1][1])
            self.ui.data_output.insert(END, '\n')


    def sort_scoreseq(self): #오름차순
        self.ui.state_clear()
        self.ui.data_clear()
        self.sorted_list = sorted(self.dic.items(), key=lambda x: x[1][1])
        for i in range(len(self.sorted_list)):
            self.ui.data_output.insert(END, self.sorted_list[i][0])
            self.ui.data_output.insert(END, "\t" + self.sorted_list[i][1][0] + "\t")
            self.ui.data_output.insert(END, self.sorted_list[i][1][1])
            self.ui.data_output.insert(END, '\n')

