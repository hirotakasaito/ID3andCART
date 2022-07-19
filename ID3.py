import math

class ID3:
    def __init__(self,datas,questions):
        self.datas = datas
        self.questions = questions

        yes_count = 0
        classnum = 2
        self.class_entropy = []

        for data in self.datas:

            if data[-1] == "Yes":
                yes_count += 1

        no_count = len(self.datas) - yes_count

        self.calc_init_entropy(yes_count, no_count, classnum)
        self.calc_entropy()

    def calc_init_entropy(self, m, n, classnum):

        entropy = m/(m+n) * math.log((m+n)/m,classnum) + n/(m+n) * math.log((m+n)/n,classnum)

        return entropy

    def calc_entropy(self):
        for idx,question in enumerate(self.questions.values()):
            yes_count = 0
            for data in self.datas:
                classname = data[idx]

                for i,data in enumerate(self.datas):
                    if classname == data[i]:
                        if data[]

            for i in range(question):
                entropy += m/(m+n) * math.log((m+nj



if __name__ == "__main__":

    datas = [
        ['晴れ','強い','高い','No'],
        ['曇り','弱い','高い','Yes'],
        ['曇り','強い','低い','No'],
        ['晴れ','弱い','高い','Yes'],
        ['雨','弱い','高い','No'],
    ]

    questions = {'天気': 3,'風速': 2,'湿度': 2,'花火': 2}

    id3 = ID3(datas,questions)




