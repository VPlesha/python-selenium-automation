
def unique(string: str):
    string = string.lower()   #google
    d = {}
    for letter in string:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    print(d)

    for k,v in d.items():
        if v == 1:
            return k  # print first letter with value == 1
            # print(k)   # print all key with value == 1
            # print(k) return  # print first letter with value  ==1 and stop

print(unique('google'))
#edge cases
# print(unique('Google'))
# print(unique(''))
# print(unique('gogo'))
