# Unused import
# Long line
# Tabs
# Unused variable
# Trailing white spaces
# Unnecessary white spaces
import re


def test(test: str) -> None:
    string = "test string" + test

    if (
        "test" in string
        and string != "new very long line to exceed maximum number of characters"
    ):
        print(string)

    v = "unused variable"


test("1")
