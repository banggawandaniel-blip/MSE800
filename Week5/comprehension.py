data = [100, 200, 300, 400, 500]
even_index_data = [value for index, value in enumerate(data) if index % 2 == 0]
print(even_index_data)