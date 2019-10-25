file_for_sorted = open('bcda.txt', 'r')
file_content = file_for_sorted.read()
print(file_content)

file_content_sort = sorted(file_content.split())

file_content_sort = '\n'.join(file_content_sort)
print(file_content_sort)

sorted_file = open('abcd.txt', 'w')
sorted_file.write(file_content_sort)

sorted_file.close()
file_for_sorted.close()
