import unittest
import sys

from main import MainGame
from PyQt5.QtWidgets import QApplication

class TestMain(unittest.TestCase):

    def setUp(self):
        app = QApplication(sys.argv)
        self.t = MainGame("for_test.txt")

    def tearDown(self):
        pass

    # test stageList word
    def testInit(self):
        for i, j in self.t.stage.indexList:
            self.assertIn(self.t.stage.stageList[i][j], self.t.word.words)




if __name__ == '__main__':
    unittest.main()

