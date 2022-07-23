
class CART:

    def __init__(self,datas,questions):
            self.datas = datas
            self.datas_len = len(datas)
            self.questions = questions

            self.class_gini = []
            self.end = True
            self.init_gini = self.calc_init_gini(datas, questions)

    def calc_init_gini(self, m, n):

        yes_count = 0
        for data in self.datas:

            if data[-1] == "Yes":
                yes_count += 1

        no_count = len(self.datas) - yes_count
        m = yes_count
        n = no_count

        gini = 1 - ((m/(n+m))**2 + ((n/(n+m))**2))

        return gini

    def calc_each_gini(self,idx):

        past_classlist = []
        gini = 0
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
                    no_count = 1e-10

                gini += (1 - ((yes_count/count)**2 + (no_count/count)**2))*(count/self.datas_len)

            past_classlist.append(classname)

        return gini, count_list

    def calc_gini(self):

        each_gini_list = []
        for idx,question in enumerate(questions):
            if questions[-1] != question:
                each_gini, _= self.calc_each_gini(idx)
                each_gini_list.append(each_gini)

        each_score = [self.init_gini - each_gini for each_gini in each_gini_list ]

        max_score = max(each_score)
        return questions[each_score.index(max_score)], max_score

    def verify_completed(self,index):
        _,count_list = self.calc_each_gini(index)

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
            max_score_question, max_score = self.calc_gini()
            current_question_index = questions.index(max_score_question)
            self.end = self.verify_completed(current_question_index)
            print('質問:{},スコア:{}'.format(max_score_question, round(max_score,3)))

            if self.end:
                del self.questions[current_question_index]
                for idx, data in enumerate(self.datas):
                    for ans in data:
                        if ans == self.zero_ans:
                            del self.datas[idx]

                self.init_gini = self.calc_init_gini(self.datas, self.questions)
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

    cart = CART(datas,questions)
    cart.process()

