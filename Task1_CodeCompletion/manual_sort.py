def sort_list_of_dicts(data, key):
    return sorted(data, key=lambda x: x[key])

# Example
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 22},
    {'name': 'Charlie', 'age': 30}
]

sorted_data = sort_list_of_dicts(data, 'age')
print(sorted_data)
