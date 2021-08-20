import unittest
import group04_ASP_project as prog

class TestMyProgram(unittest.TestCase):
    def test_total(self):
        num = prog.sorttop3
        result = prog.Calculate.sum(num)
        self.assertEqual(result, 55756301)
    def test_mean(self):
        num = prog.sorttop3
        result = round(prog.Calculate.mean(num), 2)
        self.assertEqual(result, 18585433.6)