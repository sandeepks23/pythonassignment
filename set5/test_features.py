import unittest
import features

class TestFeatures(unittest.TestCase):

    def test_get_user(self):
        response=features.get_user(1)
        self.assertEqual(response,{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'})

    def test_get_detail(self):
        response=features.get_detail(1)
        self.assertEqual(response,"quia et suscipit\n"
                                  "suscipit recusandae consequuntur expedita et cum\n"
                                  "reprehenderit molestiae ut ut quas totam\n"
                                  "nostrum rerum est autem sunt rem eveniet architecto")

if __name__=='__main__':
    unittest.main()