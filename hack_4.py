"""
text: "fooziman" output => "foozimaN"
"""


def fn_hack_4():
    result = "fooziman"
    result = result.replace("n", "N")
    return result
