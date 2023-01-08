# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

fname = input('Файл: ')
f = open(fname,'w')
while True:
    s = input()
if s == '': break
    f.write(s+'\n')
    f.close()

# Решение 2

lst = ['abc', '123', 'sldk', 'abc', 'dsfj', '123', '654', 'abc']
count = 0
i = 0
index = 0
st = 'abc'
for elem in lst:
i +=1
if st == elem:
count +=1
if count == 2:
index = i
break
elif count < 2:
continue
if index<2:
print(f'Второго вхождения строки {st} нет')
else:
print(index)