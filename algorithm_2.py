
def are_anagrams(s1: str, s2: str):
    return sorted(s1.lower()) == sorted(s2.lower())

print(are_anagrams('rage', 'ager'))



def reverse_words(sentence: str):
    result = []

    slova = sentence.split(' ')
    for slovo in slova:
        rev_slovo = slovo[::-1]
        result.append(rev_slovo)



    return ' '.join(result)
print(reverse_words(' One of the last steps is the string method'))

def repeat_digits(s: str):
    result = []  # Initialize an empty string to store the result

    for char in s:  # Iterate through each character in the input string
        d = int(char)
        result.append(char * d)

    return ''.join(result)  # Return the final result string

print(repeat_digits('312'))
print(repeat_digits('102'))



def is_vowel(bukva:str):
    glasniye = ['a', 'e', 'i', 'o', 'u']
    return bukva in glasniye

def remove_vowels(slovo:str):
    result = []  # Initialize an empty string to store the result
    for bukva in slovo:
        if not is_vowel(bukva):
            result.append(bukva)

    return ''.join(result)
print(remove_vowels('iurgfboo'))
print(remove_vowels('suhoswohasn'))
