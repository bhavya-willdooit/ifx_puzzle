import unittest

def sort_brand_type(to_sort_arr):
    return sorted(to_sort_arr, key = lambda brand_type: (brand_type['brand'], brand_type['type']))

class TestSortBrandType(unittest.TestCase):

    def test_first(self):
        test_one = [{'brand':'xyz','type':3},
                    {'brand':'xyz','type':1},
                    {'brand':'abc','type':1},]
            
        sorted_test_one = [{'brand':'abc','type':1}, 
                           {'brand': 'xyz', 'type': 1}, 
                           {'brand': 'xyz', 'type': 3}]
                           
        self.assertEqual(sort_brand_type(test_one),sorted_test_one)
        
if __name__ == '__main__':
    unittest.main()