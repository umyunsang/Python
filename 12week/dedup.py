# 연속적으로 나타나는 같은 숫자 제거

# while문을 이용해서 현재 문자와 다음 문자가 같으면 다음 문자를 지우기
# for문을 이용해서 현재 문자와 다음 문자가 다르면 현재 문자를 결과 리스트에 추가 (추천!)

# arr = [1,1,3,3,0,1,1]
# arr[0] == arr[1] ?  같으므로 추가 X
# arr[1] == arr[2] ?  다르므로 추가 O
# ...
# arr[len(arr)-2] == arr[len(arr)-1] ?

def solution(arr):
    """
    연속적으로 나타나는 같은 숫자를 제거하고,
    연속되지 않은 숫자만을 포함하는 리스트를 반환합니다.

    Parameters:
    arr (list of int): 입력 리스트

    Returns:
    list of int: 연속된 중복 숫자가 제거된 리스트
    """

    # 리스트의 끝에 임의의 값('@')을 추가하여 마지막 요소의 비교를 용이하게 합니다.
    arr.append('@')

    # 결과를 저장할 리스트 초기화
    result = []

    # 리스트를 순회하며 현재 요소와 다음 요소를 비교
    for idx in range(len(arr) - 1):
        # 현재 요소와 다음 요소가 다를 경우, 현재 요소를 결과 리스트에 추가
        if arr[idx] != arr[idx + 1]:
            result.append(arr[idx])

    return result


# 테스트 케이스
arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))  # 예상 결과: [1, 3, 0, 1], 연속된 중복 숫자가 제거된 결과

arr = [4, 4, 4, 3, 3]
print(solution(arr))  # 예상 결과: [4, 3], 연속된 중복 숫자가 제거된 결과
