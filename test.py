# Description: Test for line protocol parser
#
# This file implements some extremely basic tests for the line protocol parser
# in an intentionally clunky manner.
#
# Notes:
#
# (1) These tests should pass.
# (2) You should refactor the tests to make them more DRY.
# (3) You should add additional tests.
#
# You may use third-party libraries (e.g., pytest), but we do not require them.


import unittest

from interview import line_protocol_parser


TEST_FIELD_VALUE_FLOAT = (
    'weather,state=FL,region=south temperature="☀️",humidity=94.1 1556813463008000000'
)

TEST_FIELD_VALUE_STR = (
    'weather,state=FL,region=south temperature="☀️",humidity=94.1 1556813463008000000'
)

TEST_FIELD_VALUE_INT = (
    'weather,state=FL,region=south temperature="☀️",humidity=94i 1556813463008000000'
)


class TestLineProtocolParser(unittest.TestCase):
    def test_line_protocol_parser_1(self):
        out = line_protocol_parser(TEST_FIELD_VALUE_FLOAT)
        self.assertTrue(out[0] == "weather")
        self.assertTrue(isinstance(out[2].get("humidity"), float))

    def test_line_protocol_parser_2(self):
        out = line_protocol_parser(TEST_FIELD_VALUE_STR)
        self.assertTrue(out[0] == "weather")
        self.assertTrue(isinstance(out[2].get("temperature"), str))

    def test_line_protocol_parser_3(self):
        out = line_protocol_parser(TEST_FIELD_VALUE_INT)
        self.assertTrue(out[0] == "weather")
        self.assertTrue(isinstance(out[2].get("humidity"), int))


if __name__ == "__main__":
    unittest.main()
