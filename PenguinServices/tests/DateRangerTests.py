from DateRanger import DateRangeGenerator
import unittest

class TestDateRanger(unittest.TestCase):
    def setUp(self):
        self.forward = [str(date) for date in DateRangeGenerator(15, 1, 2022, count = 78)]
        self.backwards = [str(date) for date in DateRangeGenerator(15, 1, 2022, count = 78, forward = False)]
        
    def test_count(self):
        self.assertEqual(len(self.forward), 78, "Length should be 78")

    def test_forward(self):
        self.assertEqual(self.forward[-1], "02-04-2022", "Date should be 02-04-2022")

    def test_backwards(self):
        self.assertEqual(self.backwards[-1], "30-10-2021", "Date should be 30-10-2021")
        
if __name__ == "__main__":
    forward = DateRangeGenerator(15, 1, 2022, count=78)
    backwards = DateRangeGenerator(15, 1, 2022, count=78, forward = False)

    for day in forward:
        print(day, end=", ")

    print()

    for day in backwards:
        print(day, end=", ")
