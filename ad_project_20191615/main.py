from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QLabel, QComboBox, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QVBoxLayout
from word import Word
from stage import Stage

import random
import sys

class MainGame(QWidget):
    def __init__(self, level = 1, parent = None):
        super().__init__(parent)
        self.word = Word('words.txt')
        self.stage = Stage(level)
        self.t = (15- self.stage.getLevel())

        # composing stage
        for i,j in self.stage.indexList:
            self.stage.stageList[i][j] = self.word.randWord()

        #UI
        self.initUI()

    def initUI(self):
        #timer
        self.timer = QTimer()

        # label
        self.changeStageLabel = QLabel("Change Stage: ")
        self.currentLavelLabel = QLabel("Current Level {}".format(self.stage.getLevel()))
        self.leftLifeLabel = QLabel("Left Word: {}".format(self.leftLife))
        self.stateLabel = QLabel("Hello User")
        self.timeLabel = QLabel("Left Time: {}".format(self.t))
        self.wallLabel = QLabel("_")

        #edit
        self.submitEdit = QLineEdit()

        # button
        self.submitButton = QPushButton("submit")
        self.changeButton = QPushButton("change")

        #connect
        self.submitButton.clicked.connect(self.submitButtonClicked)
        self.changeButton.clicked.connect(self.changeButtonClicked)

        # stage combobox
        self.stageCom = QComboBox()
        self.stageCom.addItem("1")
        self.stageCom.addItem("2")
        self.stageCom.addItem("3")

        #stageHBox
        stageHBox = QHBoxLayout()
        stageHBox.addStretch(1)
        stageHBox.addWidget(self.changeStageLabel)
        stageHBox.addWidget(self.stageCom)
        stageHBox.addWidget(self.changeButton)

        # vbox
        vBox = QVBoxLayout()

        # game list
        self.lstView = []
        for i in range((self.stage.getLevel()*3)**2):
            self.lstView.append(QLabel())

        # window size
        if(self.stage.getLevel() == 1):
            self.setGeometry(300, 300, 400, 300)
            self.wallLabel.setText("_"*50)
        elif(self.stage.getLevel() == 2):
            self.setGeometry(300, 300, 675, 350)
            self.wallLabel.setText("_" * 85)
        else:
            self.setGeometry(300, 300, 950, 400)
            self.wallLabel.setText("_" * 120)

        # label arrange
        self.arrangeList(vBox)
        self.lstWriter()

        #inform
        informBox = QHBoxLayout()
        informBox.addWidget(self.submitEdit)
        informBox.addWidget(self.submitButton)

        #second inform
        timeAndWordBox = QHBoxLayout()
        timeAndWordBox.addWidget(self.timeLabel)
        timeAndWordBox.addStretch(1)
        timeAndWordBox.addWidget(self.leftLifeLabel)

        #vBox
        vBox.addStretch(1)
        vBox.addWidget(self.wallLabel)
        vBox.addLayout(timeAndWordBox)
        vBox.addWidget(self.stateLabel)
        vBox.addLayout(stageHBox)
        vBox.addStretch(1)
        vBox.addLayout(informBox)

        #start time
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timePrinter)

        self.timer.start()

        self.setWindowTitle("{} Stage".format(self.stage.getStrStage()))
        self.setLayout(vBox)
        self.show()

    #timer
    def timePrinter(self):
        self.t -=1
        self.timeLabel.setText("Left Time: {}".format(self.t))
        if(self.t <=0):
            self.timeLabel.setText("Time Out!")
        if(self.t == -1):
            self.close()

    # set label
    def arrangeList(self, vBox):
        count = 0
        h = QHBoxLayout()
        for i in self.lstView:
            h.addWidget(i)
            count +=1
            if(count == 3*self.stage.getLevel()):
                count = 0
                vBox.addLayout(h)
                h = QHBoxLayout()
        return vBox

    # change stage
    def changeButtonClicked(self):
        self.close()
        return self.__init__(int(self.stageCom.currentText()))

    # edit writer
    def lstWriter(self):
        for i in self.lstView:
            i.clear()
        for i, j in self.stage.indexList:
            target = self.stage.stageList[i][j]
            self.lstView[random.randrange(len(self.lstView))].setText(target)
        if(not self.lstChecker()):
            return self.lstWriter()

    # blank checker
    def lstChecker(self):
        for i in self.lstView:
            if(i !=  '        '): # value exist
                return True
        else:
            if(self.leftLife != 0):
                self.stateLabel.setText("Left Word: {} but There is no Word!!".format(self.leftLife))
                self.lstWriter()
                return False
            else:
                return True

    # submit button clicked
    def submitButtonClicked(self):
        for i, j in self.stage.indexList:
            if(self.submitEdit.text().strip() == self.stage.stageList[i][j]):
                self.submitEdit.clear()
                self.stateLabel.setText("Good Job!")
                self.t = (16- self.stage.getLevel())
                self.leftLife -=1
                self.leftLifeLabel.setText("Left Word: {}".format(self.leftLife))
                self.timePrinter()
                self.stage.stageList[i][j] = '        '
                self.lstWriter()
                self.gameClear()
                break
        else:
            self.submitEdit.clear()
            self.stateLabel.setText("Try Again!")

    # enter key, escape key
    def keyPressEvent(self, e):
        if(e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter):
            return self.submitButtonClicked()
        elif(e.key() == Qt.Key_Escape):
            self.close()

    # timeout dialog
    def closeEvent(self, event):
        if(self.t <0):
            text = QMessageBox.question(self, 'Time Out!!', 'Wanna play again?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if text == QMessageBox.Yes:
                self.__init__()
            event.accept()

    # levelUp or quit
    def gameClear(self):
        if(not self.leftLife):
            if(self.stage.getLevel() <=2):
                self.close()
                self.__init__(self.stage.levelUp())
            else:
                self.stateLabel.setText("Congratulation!")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    game = MainGame()
    game.show()
    sys.exit(app.exec_())
