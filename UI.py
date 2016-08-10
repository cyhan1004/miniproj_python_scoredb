from tkinter import *

class UI:
    def __init__(self, window):

        self.window = window

        #1번째 Frame : top_row
        self.top_row = Frame(self.window)
        self.top_row.grid(row=0,column=0,sticky=N)

        Label(self.top_row,text="이름: ").grid(row=0,column=0,sticky=W)
        self.name=Entry(self.top_row,width=20,bg="light green")
        self.name.grid(row=0,column=1,sticky=W)

        Label(self.top_row, text="번호: ").grid(row=4, column=0, sticky=W)
        Label(self.top_row, text="번호: ").grid(row=5, column=0, sticky=W)
        self.edit_nameidx=Entry(self.top_row, width=5, bg = "gray") #수정할 이름의 인덱스
        self.edit_nameidx.grid(row=4, column=1, sticky=W)
        self.edit_scoreidx = Entry(self.top_row, width=5, bg="gray")  # 수정할 점수의 인덱스
        self.edit_scoreidx.grid(row=5, column=1, sticky=W)

        r=0
        label_list = ["점수: ","번호: ","파일이름: ","파일이름: ","이름: ", "점수: "]
        for label in label_list:
            Label(self.top_row, text=label).grid(row=r, column=2,sticky=E)
            r += 1

        self.secframe_entlist = [] #0: 점수, 1: 번호, 2: 파일이름, 3: 파일이름
        width_list = [7,5,20,20]
        r=0
        for w in width_list:
            color = "light green"
            if w == 20:
                color = "light blue"
            self.secframe_entlist.append(Entry(self.top_row,width = w, bg=color))
            self.secframe_entlist[r].grid(row=r, column=3,sticky=W)
            r += 1

        self.edit_name=Entry(self.top_row, width=20,bg = "gray")
        self.edit_name.grid(row=4, column=3, sticky=W)

        self.edit_score=Entry(self.top_row, width=7,bg = "gray")
        self.edit_score.grid(row=5, column=3, sticky=W)


        #2번째 Frame: bottom_row
        self.bottom_row = Frame(self.window)
        self.bottom_row.grid(row=1,column=0,sticky=N)

        #bottom_row의 첫 번째 Frame : bottom_row_first
        self.bottom_row_first = Frame(self.bottom_row)
        self.bottom_row_first.grid(row=0,column=0,sticky=N)


        #bottom_row의 두 번째 Frame : bottom_row_second
        self.bottom_row_second = Frame(self.bottom_row)
        self.bottom_row_second.grid(row=1,column=0,sticky=N)
        self.data_output = Text(self.bottom_row_second,width=75,height=10,wrap=WORD,background="light yellow")
        self.data_output.grid(row=0,column=0,sticky=N)

        self.state_output = Text(self.bottom_row_second,width=75,height=1,bg="pink")
        self.state_output.grid(row=1,column=0,sticky=N)

    def get_dataModule(self,dataAdmin):
        self.data_admin = dataAdmin
        add_button = Button(self.top_row,text="추가",width=5,command=self.data_admin.add_click)
        add_button.grid(row=0,column=4,sticky=W)
        del_button = Button(self.top_row, text="삭제", width=5, command=self.data_admin.del_click)
        del_button.grid(row=1, column=4, sticky=W)

        editname_button = Button(self.top_row,text="수정",width=5, command=self.data_admin.change_name)
        editname_button.grid(row=4, column=4,sticky=W)
        editscore_button = Button(self.top_row,text="수정",width=5,command=self.data_admin.change_score)
        editscore_button.grid(row=5,column=4,sticky=W)

        numseq_button = Button(self.bottom_row_first, text="번호순", width=5, command=self.data_admin.sort_numseq)
        numseq_button.grid(row=0, column=0,sticky=N)
        nameseq_button = Button(self.bottom_row_first, text="이름순", width=5, command=self.data_admin.sort_nameseq)
        nameseq_button.grid(row=0, column=1,sticky=N)
        scoreseq1_button = Button(self.bottom_row_first, text="점수내림차순", width=15, command=self.data_admin.sort_scoreseqrev)
        scoreseq1_button.grid(row=0,column=2, sticky=N)
        scoreseq2_button = Button(self.bottom_row_first, text="점수오름차순", width=15, command=self.data_admin.sort_scoreseq)
        scoreseq2_button.grid(row=0,column=3,sticky=N)

    def get_fileModule(self, FileAdmin):
        self.file_admin = FileAdmin

        save_button = Button(self.top_row, text="저장", width=5, command=self.file_admin.save_file)
        save_button.grid(row=2, column=4, sticky=W)

        open_button = Button(self.top_row, text="열기", width=5, command=self.file_admin.open_file)
        open_button.grid(row=3, column=4, sticky=W)




    def state_clear(self):
        self.state_output.delete('1.0',END)

    def data_clear(self):
        self.data_output.delete('1.0',END)

