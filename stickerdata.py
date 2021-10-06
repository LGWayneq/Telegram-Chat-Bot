from random import randint

penguinid1 = "CAACAgQAAxkBAAIB1GCo4Jza4yqdLt_1JkLNvTHNwWz-AAInAQACRWLRAYKKLxJy0UliHwQ"
penguinid2 = "CAACAgQAAxkBAAIB2mCo5004cUM6ql96rAriL2tCZgnqAAIsAQACRWLRAZ29uBQSbSpJHwQ"
penguinid3 = "CAACAgQAAxkBAAIB22Co53sD3JWIrnMN7v4MvpnVl4Z9AAITAQACRWLRAZCAooz1PvdXHwQ"
penguinid4 = "CAACAgQAAxkBAAIB3GCo56n4IlFOMvlZFrcW9fD83T00AAIyAQACRWLRAQ88uDQPKZxzHwQ"
penguinid5 = "CAACAgQAAxkBAAIB3WCo57__qceZCTC-UoRCrz6p9DgfAAIcAQACRWLRAXLdhJSCB_D4HwQ"  
penguinids = [penguinid1, penguinid2, penguinid3, penguinid4, penguinid5]

fooddanceid = "CAACAgIAAxkBAAIB3mCpJFrCiTt4DzLG4wyYdTK8uXY_AAJcEgAC6NbiEr5Jo5N45fhsHwQ"

def randomstickerid():
    global penguinlist
    return penguinlist[randint(0,len(penguinlist)-1)]
