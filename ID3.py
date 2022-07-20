import math

class ID3:
    def __init__(self,datas,questions):
        self.datas = datas
        self.datas_len = len(datas)
        self.questions = questions

        yes_count = 0
        classnum = 2
        self.class_entropy = []

        for data in self.datas:

            if data[-1] == "Yes":
                yes_count += 1

        no_count = len(self.datas) - yes_count

        self.init_entropy = self.calc_init_entropy(yes_count, no_count, classnum)
        self.calc_entropy()

    def calc_init_entropy(self, m, n, classnum):

        entropy = m/(m+n) * math.log((m+n)/m,classnum) + n/(m+n) * math.log((m+n)/n,classnum)

        return entropy

    def calc_each_entropy(self,idx):

        past_classlist = []
        entropy = 0
        for data in self.datas:
            classname = data[idx]
            yes_count = 0
            no_count = 0
            count = 0

            if classname not in past_classlist and classname != "Yes" and classname != "No":
                for data in self.datas:
                    if classname == data[idx]:
                        count += 1
                        if data[-1] == "Yes":
                            yes_count += 1
                        else:
                            no_count += 1
                if yes_count == 0:
                    yes_count = 1e-10
                if no_count == 0:
                    no_count = 1e-10

                entropy += (- (yes_count/count)*math.log(yes_count/count, 2) - (no_count/count)*math.log(no_count/count, 2))*(count/self.datas_len)

            past_classlist.append(classname)

        return entropy

    def calc_entropy(self):

        each_entropy_list = []
        for idx,question in enumerate(questions):
            if question != "花火":
                each_entropy = self.calc_each_entropy(idx)
                each_entropy_list.append(each_entropy)

        each_score = [self.init_entropy - each_entropy for each_entropy in each_entropy_list ]

        max_score = max(each_score)
        print(questions[each_score.index(max_score)])


if __name__ == "__main__":

    datas = [
        ['晴れ','強い','高い','No'],
        ['曇り','弱い','高い','Yes'],
        ['曇り','強い','低い','No'],
        ['晴れ','弱い','高い','Yes'],
        ['雨','弱い','高い','No'],
    ]

    questions = ['天気', '風速', '湿度', '花火']

    id3 = ID3(datas,questions)

