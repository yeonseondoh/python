import pickle
import os

def save_scores(scores, filename='score.bin'):
    """학생 점수 저장"""
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

def load_scores(filename='score.bin'):
    """파일에서 학생 점수 불러옴"""
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            scores = pickle.load(f)
        return scores
    else:
        print(f"No existing score file found at {filename}. Starting with an empty score list.")
        return []

def main():
    scores = load_scores()

    if scores:
        print("[파일 읽기]")
        for score in scores:
            print(score)
    else:
        print("No scores loaded, you can enter new scores.")

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
        print("Please enter numeric values for scores.")

    save_scores(scores)

if __name__ == "__main__":
    main()
