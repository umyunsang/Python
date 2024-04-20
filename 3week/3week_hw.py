#
# 1. 사용자의 일일 걸음 수가 10,000보 미만이면 "목표에 도달하기 위해 더 많이 움직이세요."라고 조언합니다.
# 2. 일일 걸음 수가 10,000보 이상이고 20,000보 미만일 경우 "훌륭합니다! 목표를 달성했어요."라고 격려합니다.
# 3. 만약 사용자가 20,000보 이상을 걸었다면 "대단해요! 목표를 초과 달성했습니다!"라고 칭찬합니다.
# 4. 추가적으로, 사용자가 일일 권장 수분 섭취량(여성: 2.7L, 남성: 3.7L)을 충족했는지 여부도 확인합니다.
# 수분 섭취량이 권장량에 미치지 못하면 "오늘 물을 많이 마셔야 합니다."라는 메세지를 추가로 제공합니다.
#
# 요구사항
#     사용자로부터 성별(여성/남성), 일일 걸음 수, 그리고 일일 수분 섭취량(L)에 대한 정보를 입력받는다
#
#     위의 조건들을 모두 고려하여 건강 상태와 운동 목표 달성에 대한 피드백을 제공하는 프로그램을 작성하세요.

gender = input("성별을 입력하세요 (여성 또는 남성): ")
steps = int(input("일일 걸음 수를 입력하세요: "))
water_intake = float(input("일일 수분 섭취량(L)을 입력하세요: "))

if steps < 10000:
    print("목표에 도달하기 위해 더 많이 움직이세요.")
elif 10000 <= steps < 20000:
    print("훌륭합니다! 목표를 달성했어요.")
else:
    print("대단해요! 목표를 초과 달성했습니다.")

if gender == "여성" and water_intake < 2.7:
    print("오늘 물을 많이 마셔야 합니다.")
elif gender == "남성" and water_intake < 3.7:
    print("오늘 물을 많이 마셔야 합니다.")