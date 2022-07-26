import math

class ID3:
    def __init__(self,datas,questions):
        self.datas = datas
        self.datas_len = len(datas)
        self.questions = questions

        self.class_entropy = []
        self.end = True
        self.init_entropy = self.calc_init_entropy(datas, questions) #初期のエントロピーの計算

    def calc_init_entropy(self, m, n):

        yes_count = 0
        for data in self.datas:

            if data[-1] == "Yes":
                yes_count += 1

        no_count = len(self.datas) - yes_count
        m = yes_count
        n = no_count

        entropy = m/(m+n) * math.log((m+n)/m,2) + n/(m+n) * math.log((m+n)/n,2)

        return entropy

    #各エントロピーの計算
    def calc_each_entropy(self,idx):

        past_classlist = []
        entropy = 0
        count_list = []

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

                count_list.append([classname, yes_count, no_count])

                if yes_count == 0:
                    yes_count = 1e-10
                if no_count == 0:
                    no_count = 1e-10 #logがあるため，ゼロにならないようにする，yes_countも同様

                entropy += (- (yes_count/count)*math.log(yes_count/count, 2) - (no_count/count)*math.log(no_count/count, 2))*(count/self.datas_len)

            past_classlist.append(classname)

        return entropy, count_list

    #算出した各エントロピーから質問を決める
    def calc_entropy(self):

        each_entropy_list = []
        for idx,question in enumerate(questions):
            if questions[-1] != question:
                each_entropy, _= self.calc_each_entropy(idx)
                each_entropy_list.append(each_entropy)

        each_score = [self.init_entropy - each_entropy for each_entropy in each_entropy_list ]

        max_score = max(each_score)
        return questions[each_score.index(max_score)], max_score

    #決定木の終了判定
    def verify_completed(self,index):
        _,count_list = self.calc_each_entropy(index)

        zero_count = 0
        for counts in count_list:
            zero_count += counts.count(0)
            if counts.count(0):
                self.zero_ans = counts[0]
        if zero_count == len(count_list):
            return False
        else:
            return True

    def process(self):
        while self.end:
            max_score_question, max_score = self.calc_entropy()
            current_question_index = questions.index(max_score_question)
            self.end = self.verify_completed(current_question_index)
            print('質問:{},スコア:{}'.format(max_score_question, round(max_score,3)))

            if self.end:
                del self.questions[current_question_index]
                for idx, data in enumerate(self.datas):
                    for ans in data:
                        if ans == self.zero_ans:
                            del self.datas[idx]

                self.init_entropy = self.calc_init_entropy(self.datas, self.questions)
            else:
                print("END")

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
    id3.process()

