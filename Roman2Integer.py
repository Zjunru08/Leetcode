def romanToInt(s: str) -> int:
    symbol = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    rule = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
    
    num = 0
    size = len(s)
    index = 0
    while (index < size-1):
        if s[index: index+2] in rule.keys():
            num = num + rule[s[index:index+2]]
            index += 2
        else:
            num = num + symbol[s[index]]
            index += 1
    if (size-1) > 0:
        if s[size-2: size] not in rule:
            num = num + symbol[s[size-1]]
    # size = 1
    else:
        num = num + symbol[s[size-1]]
    
    return num

print(romanToInt("IV"))
