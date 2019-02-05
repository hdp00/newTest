#数学练习
#by hdp 2018.06.27
import random
import datetime
import os
import collections

def isLinux():
    return os.name == 'posix'

if not isLinux():   
    from windowsColorText import Color

class MathTest:
    '''乘除法计算练习'''
    _count = 4
    _max = 10
    _min = 1
    fileName = 'log.txt'
    _middle = _count / 2

    def run(self):
        index = 0
        wrongArray = [True] * self._count
        wrongCount = 0
        beginTime = datetime.datetime.now()

        while index < self._count:
            value1 = random.randint(self._min, self._max)
            value2 = random.randint(self._min, self._max)
            if value1 % 10 == 0 or value2 % 10 == 0:
                continue

            calcValue = 0
            operate = '*'
            # *
            if index < self._middle:
                calcValue = value1 * value2
            # /
            else:
                calcValue = value1
                value1 = value1 * value2
                operate = '/'

            result = False
            while not result:
                inputValue = input(f'({index + 1}) {value1}{operate}{value2}=')
                if inputValue.isdigit():
                    inputValue = int(inputValue)
                elif inputValue.upper() == 'LOG':
                    self.printLastLog()
                    continue
                else:
                    self.printRed('Wrong')
                    wrongArray[index] = False
                    continue

                if calcValue == inputValue:
                    self.printGreen('OK')
                    result = True
                else:
                    self.printRed('Wrong')
                    wrongArray[index] = False
            index = index + 1
        
        wrongCount =  collections.Counter(wrongArray)[False]
        endTime = datetime.datetime.now()
        interval = (endTime - beginTime).seconds
        score = int(100 / self._count * (self._count - wrongCount))
        self.printInfo(beginTime, interval, score)
        self.save(beginTime, interval, score)
        input()

    def printRed(self, text):
        if isLinux():
            print(f'\033[35m{text}\033[0m')
        else:
            c = Color()
            c.print_red_text(text)

    def printGreen(self, text):
        if isLinux():
            print(f'\033[32m {text}\033[0m')
        else:
            c = Color()
            c.print_green_text(text)

    def save(self, time, interval, score):
        datas = [str(time) + os.linesep, 
            str(interval) + os.linesep,
            str(score) + os.linesep,
            '--------------------------' + os.linesep]

        with open(self.fileName, 'a') as f:
            f.writelines(datas)

    def printInfo(self, time, interval, score):
        print(f'time:   {time}')
        print(f'spend:  {int(interval / 60)}:{interval % 60}')
        print(f'score:  {score}')

    def printLastLog(self):
        with open(self.fileName, 'r') as f:
            lines = f.readlines()
            if len(lines) < 4:
                return
            time = lines[-4].replace(os.linesep, '')
            interval = lines[-3].replace(os.linesep, '')
            score = lines[-2].replace(os.linesep, '')
            self.printInfo(time, interval, score)

    def operateDivValue(self, value1, value2):
        pass


MathTest().run()