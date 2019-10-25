import requests

host = 'http://pulse-rest-testing.herokuapp.com/'
book_url = 'books'

body_created_book = {"title": "Iliad", "author": "Homer"}

# создаем книгу
book_response = requests.post(url=host + book_url, data=body_created_book)
my_book = book_response.json()
book_id = my_book['id']
print(my_book)
print(book_id)

# создаем персонажей
role_url = 'roles'
body_created_role = {'name': 'Achilles', 'type': 'Warrior', 'level': 1000, 'book': host + book_url + '/' + str(book_id)}
role_response = requests.post(url=host + role_url, data=body_created_role)
person1 = role_response.json()
person_id = person1['id']
print(person_id)
print(person1)

person_check_response = requests.get(host + role_url + '/' + str(person_id))
person_check = person_check_response.json()

# проверяем наличие
assert body_created_role['name'] == person_check['name']

# вносим изменения
body_updated_role = {'name': 'Achilles', 'type': 'The Best Warrior', 'book': host + book_url + '/' + str(book_id)}
updated_role_response = requests.put(url=host + role_url + '/' + str(person_id), data=body_updated_role)
updated_role = updated_role_response.json()
print(updated_role)

# удаляем персонажа
delete_role_response = requests.delete(url=host + role_url + '/' + str(person_id))
check_deleted_role_response = requests.get(url=host + role_url + '/' + str(person_id))
print(check_deleted_role_response.status_code)
assert check_deleted_role_response.status_code == 404
print('Not found')







