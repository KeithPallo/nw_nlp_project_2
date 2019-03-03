import unittest

from ingredient_parser.en import parse


class TestNewFeature(unittest.TestCase):
    def test_parse(self):
        parsed_query = parse("one kilogram red meat")
        print(parsed_query)
        self.assertEqual(parsed_query['measure'], "one kilogram")
        self.assertEqual(parsed_query['unit'], "kilogram")
        self.assertEqual(parsed_query['quantity'], "one")
        self.assertEqual(parsed_query['name'], "red meat")


if __name__ == '__main__':
    unittest.main()
