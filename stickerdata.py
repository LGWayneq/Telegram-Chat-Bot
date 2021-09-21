from random import randint

pingupatid = "CAACAgQAAxkBAAIB1GCo4Jza4yqdLt_1JkLNvTHNwWz-AAInAQACRWLRAYKKLxJy0UliHwQ"
pingucuddleid = "CAACAgQAAxkBAAIB2mCo5004cUM6ql96rAriL2tCZgnqAAIsAQACRWLRAZ29uBQSbSpJHwQ"
pinguhugid = "CAACAgQAAxkBAAIB22Co53sD3JWIrnMN7v4MvpnVl4Z9AAITAQACRWLRAZCAooz1PvdXHwQ"
pinguplayid = "CAACAgQAAxkBAAIB3GCo56n4IlFOMvlZFrcW9fD83T00AAIyAQACRWLRAQ88uDQPKZxzHwQ"
pinguhappyid = "CAACAgQAAxkBAAIB3WCo57__qceZCTC-UoRCrz6p9DgfAAIcAQACRWLRAXLdhJSCB_D4HwQ"  
pingulist = [pingupatid, pingucuddleid, pinguhugid, pinguplayid, pinguhappyid]

buttshakeid = "CAACAgIAAxkBAAIB2GCo4murBHqFOwW1i_Jlx1zf1iJFAAJxEgAC6NbiEpNossZGq9nyHwQ"
fooddanceid = "CAACAgIAAxkBAAIB3mCpJFrCiTt4DzLG4wyYdTK8uXY_AAJcEgAC6NbiEr5Jo5N45fhsHwQ"

def randompinguid():
    global pingulist
    return pingulist[randint(0,len(pingulist)-1)]

print(randompinguid())