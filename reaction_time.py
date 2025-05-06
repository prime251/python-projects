import time
import random

print("준비되면 엔터를 누르세요.")
input()

# 랜덤 대기 시간
wait_time = random.randint(2, 5)
print("...")
time.sleep(wait_time)

print("지금! 스페이스바 또는 엔터를 누르세요!")
start = time.time()

try:
    # 3초 안에 입력 받기
    key = input(">> ")
    end = time.time()
    reaction_time = end - start

    # 메시지 출력되기 전에 누른 경우 (반응시간이 비정상적으로 짧음)
    if reaction_time < 0.05:
        print("❌ 너무 일찍 눌렀어요! 실격!")
    elif key != " " and key != "":
        print("❌ 스페이스바나 엔터가 아닙니다. 실패!")
    elif reaction_time > 3:
        print(f"⏱ {reaction_time:.2f}초 - 너무 늦었어요!")
    else:
        print(f"🎉 {reaction_time:.2f}초 - 성공!")

except:
    print("❌ 입력 오류!")
