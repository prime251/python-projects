import random

# 참가자 목록 (이름, 기록)
participants = [
    ("동현", 13.15),
    ("대협", 12.73),
    ("여욱", 13.89),
    ("지민", 12.44),
    ("태형", 14.01),
    ("정국", 11.92),
    ("남준", 13.00),
    ("석진", 12.85),
    ("일반", 15.20),
    ("거우", 14.33)
]

def print_race_results_with_times(runners):
    random.shuffle(runners)  # 순서를 무작위로 섞음
    runners.sort(key=lambda x: x[1])  # 기록 기준으로 정렬

    print("🏁 100kM 달리기 대회 결과 🏁")
    for i, (name, time) in enumerate(runners, start=1):
        medal = ""
        if i == 1:
            medal = "🥇 "
        elif i == 2:
            medal = "🥈 "
        elif i == 3:
            medal = "🥉 "
        print(f"- {i}등: {medal}{name} ({time:.2f}초)")

# 실행
print_race_results_with_times(participants)
