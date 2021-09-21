from random import randint

penguinpatid = "CAACAgQAAxkBAAIB1GCo4Jza4yqdLt_1JkLNvTHNwWz-AAInAQACRWLRAYKKLxJy0UliHwQ"
penguincuddleid = "CAACAgQAAxkBAAIB2mCo5004cUM6ql96rAriL2tCZgnqAAIsAQACRWLRAZ29uBQSbSpJHwQ"
penguinhugid = "CAACAgQAAxkBAAIB22Co53sD3JWIrnMN7v4MvpnVl4Z9AAITAQACRWLRAZCAooz1PvdXHwQ"
penguinplayid = "CAACAgQAAxkBAAIB3GCo56n4IlFOMvlZFrcW9fD83T00AAIyAQACRWLRAQ88uDQPKZxzHwQ"
penguinhappyid = "CAACAgQAAxkBAAIB3WCo57__qceZCTC-UoRCrz6p9DgfAAIcAQACRWLRAXLdhJSCB_D4HwQ"  
penguinlist = [pingupatid, pingucuddleid, pinguhugid, pinguplayid, pinguhappyid]

fooddanceid = "CAACAgIAAxkBAAIB3mCpJFrCiTt4DzLG4wyYdTK8uXY_AAJcEgAC6NbiEr5Jo5N45fhsHwQ"

def randomstickerid():
    global penguinlist
    return penguinlist[randint(0,len(penguinlist)-1)]
