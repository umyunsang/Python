# 샘플 데이터: 사람들의 정보를 담고 있는 딕셔너리 리스트
people = [
    {"name": "Eva", "age": 40, "job": "Engineer", "city": "Chicago"},
    {"name": "Alice", "age": 25, "job": "Engineer", "city": "New York"},
    {"name": "Bob", "age": 30, "job": "Doctor", "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "job": "Teacher", "city": "Los Angeles"},
    {"name": "Devid", "age": 28, "job": "Designer", "city": "New York"},
    {"name": "CCCC", "age": 30, "job": "Engineer", "city": "BBBB"}
]

def filter_and_sort(data, sort_key, filter_key, filter_value):
    """
    주어진 기준에 따라 리스트를 필터링하고 정렬하는 함수

    매개변수:
    data (list): 필터링 및 정렬할 딕셔너리 리스트
    sort_key (str): 정렬할 때 사용할 키
    filter_key (str): 필터링할 때 사용할 키
    filter_value (str): 필터링할 때 사용할 값

    반환값:
    list: 필터링 및 정렬된 딕셔너리 리스트
    """
    # filter_key와 filter_value에 따라 데이터를 필터링
    filtered_data = [person for person in data if person[filter_key] == filter_value]

    # 필터링된 데이터를 sort_key에 따라 정렬 (버블 정렬 사용)
    for i in range(len(filtered_data)):
        for j in range(i + 1, len(filtered_data)):
            if filtered_data[i][sort_key] > filtered_data[j][sort_key]:
                # 잘못된 순서일 경우 요소를 교환
                filtered_data[i], filtered_data[j] = filtered_data[j], filtered_data[i]

    return filtered_data

# 함수 호출: "Engineer" 직업을 가진 사람들을 나이 순으로 필터링하고 정렬
result = filter_and_sort(people, "age", "job", "Engineer")

# 결과 출력
print(result)
# 예상 출력:
# [
# {"name" :"Alice", "age" : 25, "job" : "Engineer", "city" :"New York"},
# {"name":"CCCC", "age": 30, "job": "Engineer", "city": "BBBB"},
# {"name":"Eva", "age": 40, "job": "Engineer", "city": "Chicago"}
# ]
