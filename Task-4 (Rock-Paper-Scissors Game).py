import random

def rock_paper_scissors(you, comp):
    if you == comp:
        return 0
    if you == 'r' and comp == 'p':
        return -1
    elif you == 'p' and comp == 'r':
        return 1
    if you == 'r' and comp == 's':
        return 1
    elif you == 's' and comp == 'r':
        return -1
    if you == 'p' and comp == 's':
        return -1
    elif you == 's' and comp == 'p':
        return 1

def main():
    choices = ['r', 'p', 's']
    comp = random.choice(choices)
    
    print("Enter 'r' for rock, 'p' for paper and 's' for scissor")
    you = input()
    
    result = rock_paper_scissors(you, comp)
    
    if result == 0:
        print("Game draw!")
    elif result == 1:
        print("You won the game!")
    else:
        print("You lose the game!")
    
    print(f"You choose {you} and Computer choose {comp}")

if __name__ == "__main__":
    main()
