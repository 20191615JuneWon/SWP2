import random

class Stage:

    def __init__(self, level = 1):
        self.level = level
        self.stageList = []
        self.indexList = []

        for i in range(3*self.level):
            self.stageList.append([])
            for j in range(3*self.level):
                self.stageList[i].append('') # len(the longest word) == 8

        while len(self.indexList) < self.level*2*2:
            idx = [random.randrange(3*self.level), random.randrange(3*self.level)]
            if(idx not in self.indexList):
                self.indexList.append(idx)

    def getLevel(self):
        return self.level

    def getStrStage(self):
        self.s = ["First", "Second", "Third", "Fourth", "Fifth"]
        return self.s[self.getLevel()-1]

    def levelUp(self):
        self.level +=1
        self.__init__(self.level)
        return self.level

    def remainTime(self):
        return 3*self.level*2

if __name__ == "__main__":
    a = Stage()
    print(a.stageList)
    print(a.indexList)
    a.levelUp()
    print(a.indexList)
