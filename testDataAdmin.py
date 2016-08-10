import unittest

class TestDataAdmin(unittest.TestCase):

    def add_click(self,dic,name,score):
        self.dic_name = name.strip()
        if self.dic_name == "":
            print("[추가 실패] 이름을 다시 입력해 주세요.")
            return False
        for key, value in dic.items():
            if self.dic_name == value[0]:
                print("[추가 실패] 동일한 이름이 존재합니다.")
                return False
        try:
            self.dic_score = eval(score)
        except:
            print("[추가 실패] 점수를 다시 입력하세요.")
            return False
        dic[len(dic)+1] = [self.dic_name, self.dic_score]
        print("성공적으로 추가하였습니다")
        return True

    def del_click(self,dic,index):
        try:
            self.del_index = eval(index)
            del dic[self.del_index]

        except:
            print("삭제에 실패했습니다.")
            return False

        print("성공적으로 삭제하였습니다")
        return True

    def sort_idx(self,dic):
        self.sorted_list = sorted(zip(dic.keys(), dic.values()))
        for i in range (len(dic)-1) :
            if self.sorted_list[i][0] > self.sorted_list[i+1][0]:
                return False
        print(self.sorted_list)
        return True

    def sort_name(self,dic):
        self.sorted_list = sorted(dic.items(), key=lambda x: x[1][0])
        for i in range(len(dic)-1):
            if self.sorted_list[i][1][0] > self.sorted_list[i+1][1][0]:
                return False
        print(self.sorted_list)
        return True

    def sort_scorerev(self,dic): #내림차순
        self.sorted_list = sorted(dic.items(), key=lambda x: x[1][1],reverse = True)
        for i in range(len(dic) - 1):
            if self.sorted_list[i][1][1] < self.sorted_list[i + 1][1][1]:
                return False
        print(self.sorted_list)
        return True

    def sort_score(self,dic): #오름차순
        self.sorted_list = sorted(dic.items(), key=lambda x: x[1][1])
        for i in range(len(dic) - 1):
            if self.sorted_list[i][1][1] > self.sorted_list[i + 1][1][1]:
                return False
        print(self.sorted_list)
        return True



    def testAddClick(self):
        self.assertTrue(self.add_click({1: ["Marge", 40], 2: ["Bart", 77], 3: ["Hommer", 25], 4: ["Lisa", 100]},"\tsimpson", "44"))
        self.assertTrue(self.add_click({1: ["Karl", 55], 2: ["Rick", 23], 3: ["Laury", 99]}, "Tom", "25"))
        self.assertFalse(self.add_click({1: ["Marge", 40], 2: ["Lisa", 40]}, " ", "34"))
        self.assertFalse(self.add_click({1: ["Karl", 55], 2: ["Rick", 23]}, "Amy", 'abc'))
        self.assertFalse(self.add_click({1: ["Karl", 55], 2: ["Amy", 23]}, "Karl", "89"))

    def testDelClick(self):
        self.assertTrue(self.del_click({1: ["Marge", 40], 2: ["Bart", 77], 3: ["Hommer", 25], 4: ["Lisa", 100]},"2"))
        self.assertFalse(self.del_click({1: ["Karl", 55], 2: ["Rick", 23], 3: ["Laury", 99]}, "5"))
        self.assertFalse(self.del_click({4:["chae",100], 2: ["yeon",44]},"a"))

    def testSortIdx(self):
        self.assertTrue(self.sort_idx({5: ["Marge", 40], 3 :  ["Bart", 77], 1: ["Hommer", 25], 2: ["Lisa", 100]}))

    def testSortName(self):
        self.assertTrue(self.sort_name({1: ["Marge", 40], 2: ["Bart", 77], 3: ["Hommer", 25], 4: ["Lisa", 100]}))

    def testSortScoreRev(self):
        self.assertTrue(self.sort_scorerev({1: ["Marge", 40], 2: ["Bart", 77], 3: ["Hommer", 25], 4: ["Lisa", 100]}))

    def testSortScore(self):
        self.assertTrue(self.sort_score({1: ["Marge", 40], 2: ["Bart", 77], 3: ["Hommer", 25], 4: ["Lisa", 100]}))


if __name__ == "__main__":
    unittest.main()