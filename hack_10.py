"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""


def fn_hack_10():
    result = "fooziman"
    # ...
    result = result.replace("o", "0")
    result = result.replace("i", "1")
    result = result.replace("a", "@")
    result = result.upper()
    result = list(result)
    return result
