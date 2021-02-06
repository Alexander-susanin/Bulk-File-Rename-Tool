import os

path = os.chdir('E:\Python\pictures')#изменяет текущий директорию на заданную

i = 0
for file in os.listdir(path):#пробегаемся циклом по списку файлов в папке
	new_file_name = 'pict-{}.jpg'.format(i)#изменяем на нужный шаблон
	os.rename(file, new_file_name)#и наконец переименовываем файлы
	i += 1