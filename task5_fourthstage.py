import unittest


class TestTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')


if __name__ == '__main__':
    unittest.main()
