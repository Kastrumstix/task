import requests
import numpy as np
import pandas as pd

response = requests.get('https://api.github.com/events')
print(response.status_code)
print(response.json())
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.json())
params = {'q': 'requests+language:python'}
response = requests.get('https://api.github.com/search/repositories', params=params)
print(response.json())


df = pd.read_csv('test.txt')
print("Первые строки DataFrame:\n", df.head())
print("\nИнформация о DataFrame:")
print(df.info())
print("\nСтатистическое описание:")
print(df.describe())
unique_n = df['один'].value_counts()
print("\nКоличество типов\n", unique_n)


array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
sum_result = array_a + array_b
print("Сумма:", sum_result)
diff_result = np.subtract(array_b, array_a)
print("Разность:", diff_result)
product_result = np.multiply(array_a, array_b)
print("Произведение:", product_result)
reshaped = array_a.reshape((3,1))
print("Измененный размер:", reshaped)
transposed = reshaped.T
print("Транспонированный массив:", transposed)