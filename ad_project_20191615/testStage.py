import unittest

from stage import Stage

class TestStage(unittest.TestCase):

    def setUp(self):
        self.stageOne = Stage(1)
        self.stageTwo = Stage(2)
        self.stageThree = Stage(3)

    def tearDown(self):
        pass

    def testInit(self):
        # level
        self.assertEqual(self.stageOne.level, 1)
        self.assertEqual(self.stageTwo.level, 2)
        self.assertEqual(self.stageThree.level, 3)

        # stageList length
        self.assertEqual(len(self.stageOne.stageList), 3)
        self.assertEqual(len(self.stageTwo.stageList), 6)
        self.assertEqual(len(self.stageThree.stageList), 9)

        # indexList length
        self.assertEqual(len(self.stageOne.indexList), 4)
        self.assertEqual(len(self.stageTwo.indexList), 8)
        self.assertEqual(len(self.stageThree.indexList), 12)

        # indexList value
        for i,j in self.stageOne.indexList:
            self.assertLess(i, 3)
            self.assertLess(j, 3)
        for i,j in self.stageTwo.indexList:
            self.assertLess(i, 6)
            self.assertLess(j, 6)
        for i,j in self.stageThree.indexList:
            self.assertLess(i, 9)
            self.assertLess(j, 9)

    def testGetLevel(self):
        # get level
        self.assertEqual(self.stageOne.getLevel(), 1)
        self.assertEqual(self.stageTwo.getLevel(), 2)
        self.assertEqual(self.stageThree.getLevel(), 3)

    def testGetStrStage(self):
        # get string_stage
        self.assertEqual(self.stageOne.getStrStage(), "First")
        self.assertEqual(self.stageTwo.getStrStage(), "Second")
        self.assertEqual(self.stageThree.getStrStage(), "Third")

    def testLevelUp(self):
        # level Up
        self.assertEqual(self.stageOne.levelUp(), 2)
        self.assertEqual(self.stageTwo.levelUp(), 3)



if __name__ == '__main__':
    unittest.main()

