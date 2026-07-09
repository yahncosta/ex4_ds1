import json
import os
import sys

from unique_element import find_unique_element


def main():
    raw_input = sys.argv[1]
    values = json.loads(raw_input)
    result = find_unique_element(values)
    print(result)


if __name__ == "__main__":
    main()