# def rem_dup(spisok):
#     novyi_spisok = []
#     for chislo in spisok:
#         if chislo not in novyi_spisok:
#             novyi_spisok.append(chislo)
#     return novyi_spisok
#
#
#
# def test1():
#     print([1, 1, 2])
#     print(rem_dup([1, 1, 2]))
#
#
# def test2():
#     print([1, 2, 1, 1, 3, 2])
#     print(rem_dup([1, 2, 1, 1, 3, 2]))
#
# test1()
# test2()

# def slovo(stroka):
#     novoe_slovo = []
#     for bukva in stroka:
#         novoe_slovo.append(bukva)
#         novoe_slovo.append(bukva)
#     return ''.join(novoe_slovo)
#
# print(slovo('string'))

# def reverse_negative_number(number:int):
#     string = str('n')
#     if string[0] == '-':
#         return int("-" + string[:0:-1])
#     else:
#         return int(str[::-1])
#
#
# print(reverse_negative_number(-234))
#
# def anagram(s1:str, s2:str):
#     if len(s1) != len(s2):
#         return False
#     if sorted(s1)==sort(s2):
#         return True
#     else:
#         return False
#
# print(anagram(s1:"cat", s2:"act))
