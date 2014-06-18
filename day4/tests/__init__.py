from unittest import TestCase

class TestRecursion(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_reverse_a_list(self):
        from kata.katas import reverse_a_list

        self.assertEqual(reverse_a_list([1,2,3,4,5]), [5,4,3,2,1])
        self.assertEqual(reverse_a_list([[1,2],[3,4],[5,6]]), [[5,6],[3,4],[1,2]])

    def test_compress_a_sequence(self):
        from kata.katas import compress_a_sequence

        self.assertEqual(compress_a_sequence("Leeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerrrroyyyyyyyy"), "Leroy")
        self.assertEqual(compress_a_sequence([1,1,2,2,3,3,2,2,3]), [1,2,3,2,3])
        self.assertEqual(compress_a_sequence([[1,2],[1,2],[3,4],[1,2]]), [[1,2],[3,4],[1,2]])
