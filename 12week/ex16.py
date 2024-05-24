# 연속적으로 나타나는 같은 숫자 제거

# while문을 이용해서 현재 문자와 다음 문자가 같으면 다음 문자를 지우기
# for문을 이용해서 현재 문자와 다음 문자가 다르면 현재 문자를 결과 리스트에 추가 (추천!)

# arr = [1,1,3,3,0,1,1]
# arr[0] == arr[1] ?  같으므로 추가 X
# arr[1] == arr[2] ?  다르므로 추가 O
# ...
# arr[len(arr)-2] == arr[len(arr)-1] ?

def solution(arr):
    arr.append('@')
    result = []
    for idx in range(len(arr)-1):
        if arr[idx] != arr[idx+1]:
            result.append(arr[idx])

    return result

arr = [1,1,3,3,0,1,1]
print(solution(arr))
arr = [4,4,4,3,3]
print(solution(arr))