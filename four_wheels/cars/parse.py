import requests

# from pprint import pprint


URL = 'https://cars-base.ru/api/cars'

resp = requests.get(URL)
# print(resp.status_code)
json_resp = resp.json()
CAR_MODEL = [el['id'] for el in json_resp]

# print(CAR_MODEL)


# def say_hello(first_name, last_name):
#     return '{1}/{0}'.format(first_name, last_name)


# print(say_hello('Vitalii', 'Lukianov'))
