import sbb_4 
import unittest
  
class Sbb_test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sbb_4.deal_data(['Java', 'C','C', 'C'] ),{'C': 3, 'Java': 1})
        self.assertEqual(sbb_4.deal_data(['Java', 'C','C'] ),{'C': 2, 'Java': 1})
        self.assertEqual(sbb_4.deal_data(['Java', 'C'] ),{ 'Java': 1,'C': 1,})
        self.assertEqual(sbb_4.deal_data(['Java','Java', 'C','C', 'C'] ),{'C': 3, 'Java': 2})
        

if __name__ == '__main__':
    unittest.main()