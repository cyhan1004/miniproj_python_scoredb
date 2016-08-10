import unittest

class TestFileAdmin(unittest.TestCase):

    def save_file(self,dic,fn):
        if fn.strip() == "":
            print("파일 저장에 실패했습니다.")
            return False
        f = open("./" + fn.strip() + ".txt", 'w')
        for key, value in dic.items():
            f.write(str(key) + "\t" + dic[key][0] + "\t" + str(dic[key][1]) + '\n')
        f.close()
        print("파일 저장에 성공했습니다.")
        return True

    def open_file(self,fn):
        self.dic = {}
        if fn.strip() == "":
            print("파일 불러오기에 실패했습니다.")
            return False
        try:
            self.f = open("./" + fn.strip() + ".txt", 'r')
        except:
            print("파일 불러오기에 실패했습니다.")
            return False

        last_index = 0
        while True:
            line = self.f.readline().strip()
            if not line:
                break
            dic_list = line.split("\t")
            self.dic[eval(dic_list[0])] = [dic_list[1], eval(dic_list[2])]
            if last_index < eval(dic_list[0]):
                last_index = eval(dic_list[0])

        self.f.close()
        print ("성공적으로 파일을 읽었습니다. (파일 이름 : " + fn.strip() + ")")
        print(self.dic)
        return True


    def testSave(self):
        self.assertTrue(self.save_file({1: ["Marge", 40], 2: ["Bart", 77], 3: ["Hommer", 25], 4: ["Lisa", 100]}, "The Simpson"))
        self.assertTrue(self.save_file({1:["Karl",55], 2:["Rick", 23], 3:["Laury",99]},"\tWalking Dead\t"))
        self.assertFalse(self.save_file({1: ["Karl", 55], 2: ["Rick", 23], 3: ["Laury", 99]}, "\t"))

    def testOpen(self):
        self.assertTrue(self.open_file("\tThe Simpson\t"))
        self.assertFalse(self.open_file("Wow"))
        self.assertFalse(self.open_file("")) 

if __name__ == "__main__":
    unittest.main()