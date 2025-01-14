from collections import Counter
key = input()
password = input()
key_list = list(key)
password_list = list(password)

if not(key == password):
    equal = Counter(key_list) == Counter(password_list)
    if equal == True:
        answer = 'YES'
    else:
        answer = 'NO'
print(answer)