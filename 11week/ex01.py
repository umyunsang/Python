people = [
    {"name": "Eva", "age": 40, "job": "Engineer", "city": "Chicago"},
    {"name": "Alice", "age": 25, "job": "Engineer", "city": "New York"},
    {"name": "Bob", "age": 30, "job": "Doctor", "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "job": "Teacher", "city": "Los Angeles"},
    {"name": "Devid", "age": 28, "job": "Designer", "city": "New York"},
    {"name": "CCCC", "age": 30, "job": "Engineer", "city": "BBBB"}
]


def filter_and_sort(data, sort_key, filter_key, filter_value):
    filtered_data = []

    for person in data:
        if person[filter_key] == filter_value:
            filtered_data.append(person)

    for i in range(len(filtered_data)):
        for j in range(i + 1, len(filtered_data)):
            if filtered_data[i][sort_key] > filtered_data[j][sort_key]:
                tmp = filtered_data[i]
                filtered_data[i] = filtered_data[j]
                filtered_data[j] = tmp

    return filtered_data


result = filter_and_sort(people, "age", "job", "Engineer")

print(result)
# Output:
# [
# {"name" :"Alice", "age" : 25, "job" : "Engineer", "city" :"New York"},
# {"name":"CCCC", "age": 30, "job": "Engineer", "city": "BBBB"},
# {"name":"Eva", "age": 40, "job": "Engineer", "city": "Chicago"}
# ]
