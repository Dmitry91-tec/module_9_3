first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x)-len(y) for x,y in zip(first,second) if not len(x) == len(y)) #высчитывает разницу длин строк first и second
print(list(first_result))
second_result = (True if len(first[x]) == len(second[x]) else False for x in range(0,len(first)))  #генераторная сборка, которая содержит результаты сравнения
print(list(second_result))                                                                                       # длин строк в одинаковых позициях из списков first и second