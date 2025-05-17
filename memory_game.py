import random
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_sequence(length):
    return [random.randint(0, 9) for _ in range(length)]

def get_settings():
    print("난이도 선택: [1] EZ  [2] MID  [3] HD")
    choice = input("선택 (1/2/3): ")
    if choice == '1':
        return {'name': 'EZ', 'delay': 3, 'step': 1}
    elif choice == '2':
        return {'name': 'MID', 'delay': 2.2, 'step': 2}
    elif choice == '3':
        return {'name': 'HD', 'delay': 1.5, 'step': 3}
    else:
        print("잘못된 입력입니다. EZ로 기본 설정됩니다.")
        return {'name': 'EZ', 'delay': 3, 'step': 1}

def play_game():
    settings = get_settings()
    level = 1
    print(f"\n🧠 Memory Game ({settings['name']} 모드) 시작!\n")
    while True:
        sequence_length = level + settings['step'] - 1
        sequence = generate_sequence(sequence_length)
        print(f"\n🔢 Level {level}")
        print("기억하세요:", ''.join(map(str, sequence)))  # 한 줄로 붙여서 보여줌

        time.sleep(settings['delay'])
        clear_console()

        answer = input("입력하세요 (띄어쓰기 없이 입력): ").strip()

        if not answer.isdigit() or len(answer) != len(sequence):
            print("fuck you")
            break

        user_input = [int(char) for char in answer]

        if user_input == sequence:
            print("✅ 정답! 다음 레벨로 갑니다.")
            level += 1
        else:
            print("\n❌ 틀렸어요!")
            print(f"정답은: {''.join(map(str, sequence))}")
            break

    print(f"\n🎉 최종 도달 레벨: {level}")

play_game()
