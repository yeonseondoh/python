import pickle
import os

def save_scores(scores, filename='score.bin'):
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)
    print(f"Scores saved to {filename}.")

def load_scores(filename='score.bin'):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            scores = pickle.load(f)
        print(f"Scores loaded from {filename}.")
        return scores
    else:
        print(f"{filename}에 점수가 없습니다.")
        return []

def main():
    scores = load_scores()

    print("[파일 읽기]")
    if scores:
        print(scores)
    else:
        print("No scores found.")

    print("[점수 입력]")
    score_1 = input("#1: ")
    score_2 = input("#2: ")
    score_3 = input("#3: ")

    try:
        score_1 = float(score_1)
        score_2 = float(score_2)
        score_3 = float(score_3)
        average_score = (score_1 + score_2 + score_3) / 3
        print("[점수 출력]")
        print(f"평균: {average_score:.2f}")
    except ValueError:
        print("정수로 다시 입력하세요")

    # 프로그램 종료 전에 새로운 점수를 기존 점수에 추가하고 저장
    scores.extend([score_1, score_2, score_3])
    save_scores(scores)

if __name__ == "__main__":
    main()
