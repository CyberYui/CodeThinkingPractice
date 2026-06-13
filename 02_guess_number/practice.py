import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess_input = input("1-100之间猜个数: ")

        if not guess_input.isdigit():
            print("请输入一个数字！")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < number:
            print("太小了！")
        elif guess > number:
            print("太大了！")
        else:
            print(f"恭喜你！你在 {attempts} 次尝试中猜中了数字。")
            play_again = input("你想再玩一次吗？ (yes/no): ").lower()
            if play_again == 'yes':
                guess_number()
            break

if __name__ == "__main__":
    guess_number()
