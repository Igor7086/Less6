"""
считываем построчно строки из файла и выводим строки,
добавляя в конец этих строк восклицательный знак
"""
all_str = open('la.txt', 'r+')
change_all_str = ''
for line in all_str.readlines(0):
    change_all_str += line[:-1] + '!\n'
print(change_all_str)
all_str.seek(0)
all_str.write(change_all_str)
all_str.close()


