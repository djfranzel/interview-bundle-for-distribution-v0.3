import datetime
import sys
from typing import Any

"""
In this exercise, you will be implementing a parser for (a simplified version)
of the line protocol format.

See:

https://docs.influxdata.com/influxdb/v2.6/reference/syntax/line-protocol/

// Syntax
<measurement>[,<tag_key>=<tag_value>[,<tag_key>=<tag_value>]] <field_key>=<field_value>[,<field_key>=<field_value>] [<timestamp>]

// Example
myMeasurement,tag1=value1,tag2=value2 fieldKey="fieldValue" 1556813561098000000

Additional simplifying assumptions you *may* make:

- Whitespace is not allowed in tag keys or values,
- Whitespace is not allowed in field keys or values.

Your base tasks (not in order):

- Consult the line protocol documentation to understand the format,
- Implement the line_protocol_parser function below,
- Ensure that the tests pass: `python test.py`

Bonus tasks:

- Refactor the testing code to make it more DRY.
- Add additional test cases.

Guidelines:

- You do not *need* to use any third-party libraries,
- You are permitted to use third-party libraries but you must implement the parser yourself :)
- You are allowed to use any specific Python version you like,
- You *can* consult external sources and tools (e.g., StackOverflow, Search Engines, AutoPilot, ChatGPT)
"""


def line_protocol_parser(
    line: str,
) -> tuple([str, dict[str, str], dict[str, Any], datetime.datetime]):
    
    line = line.split()
    measurement = line[0].split(",")[0]
    tagSet = line[0][len(measurement)+1:len(line[0])]
    fieldSet = line[1]
    timeStamp = line[2]

    tagSetParsed = extractKeyValuePairs(tagSet)
    fieldSetParsed = extractKeyValuePairs(fieldSet)
    
    return tuple([measurement, tagSetParsed, fieldSetParsed, timeStamp])

def extractKeyValuePairs(stringSet: str) -> dict[str, str]:

    keyValuePairs = {}
    keyValueList = stringSet.split(",")

    for subString in keyValueList:
        temp = subString.split("=")

        key = temp[0]
        value = temp[1]

        if isInt(value):
            value = parseInt(value)
        elif isFloat(value):
            value = parseFloat(value)

        keyValuePairs[key] = value

    return keyValuePairs

def isInt(value: str) -> bool:
    try:
        value = parseInt(value)
        int(value)
        return True
    except ValueError:
        return False
    
def isFloat(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def parseInt(value: str) -> int:

    if value[len(value) - 1 == "i"]:
        value = value[0:value.index("i")]

    return int(value)

def parseFloat(value: str) -> float:
    return float(value)


def main() -> int:
    for line in sys.stdin:
        parsed = line_protocol_parser(line)
        print(parsed)
    return


if __name__ == "__main__":
    sys.exit(main())
