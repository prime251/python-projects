import time
import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def reaction_game():
    print("🕹️ Reaction Skill Game 시작!")
    print("지금 Enter를 누르지 마세요...")
    time.sleep(2)

    print("\n준비...")
    time.sleep(random.uniform(2, 5))  # 2~5초 랜덤 대기

    print("지금! [ENTER]를 최대한 빠르게 누르세요!")
    start = time.time()
    input()
    end = time.time()

    reaction_time = round((end - start) * 1000)  # ms로 변환

    if reaction_time < 100:
        print("❗너무 빨랐어요! 반칙입니다.")
    else:
        print(f"✅ 반응 속도: {reaction_time}ms")

# 게임 실행
reaction_game()
