# Напишите программу, в которой
# пользователь будет задавать две строки, а программа
# - определять количество вхождений одной строки в
# другую.
# «qwe» «qwertyqwe» -> 2
#1
string1 = input()
string2 = input()
if len(string1) > len(string2):
    print(string1)
    count = 0
    for i in range(len(string1)):
        print(string1[i:i+len(string2)])
        if string2 == string1[i:i+len(string2)]:
            count += 1
    print("количество совпадений строк:", count)

#2
string1 = input()
string2 = input()
print(f"Строка 2 входит в строку 1 {string1.count(string2)} раз(ы)")