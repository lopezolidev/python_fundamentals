def romanToInt(s: str):
    num_dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    
    if(len(s) == 1):
        return num_dic[s]
    i = 0
    first = ''
    second = ''
    value = 0
    while i < len(s):
        first = s[i]
        if(i != len(s) - 1):
            second = s[i+1]
        if (first + second) in num_dic:
            value = value + num_dic[first + second]
            i += 2
            continue
        value = value + num_dic[first]
        i += 1
    return value

print(romanToInt("LVIII"))