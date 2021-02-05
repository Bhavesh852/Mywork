import random
def fun():
    # reading from the file words.txt
    with open('words.txt', "r") as file:
        all = file.read()
        r_word = all.split()

    print("Selecting the word......")

    # selecting the random word
    word = random.choice(r_word)
    w_len = len(word)
    print(f"The selected word length is {w_len}")

    while(True):
        # taking attempts from the user
        n = input("How many incorrect attempt do you want? [1-25] :")
        # checking the attempts that is integer or notz
        try:
            attempt = int(n)
            if attempt < 26 and attempt > 0:
                break
            else:
                print("Choose the attempt between 1 to 25")
        except:
            print(f"{n} is not an integer between 1 to 25...")

    remain = attempt
    list1 = []
    list2 = []
    str1 = ""
    user = ""
    # list contain * format of word
    for k in range(w_len):
        list1.append("*")

    print('\n')
    # main logic for game
    for i in range(1, (attempt+1)):
        # printing word in star format
        print(f"Word : {str1}")
        # empty the str1
        str1 = ""

        # user previous input
        print("Previous Guess :", user)

        # reamining attempt
        print("Attempts Remaining :", remain)

        # user input
        user = input("Choose the letter :")

        # logic of checking, the letter of word
        if user in word:
            for j in range(w_len):
                if user == word[j]:
                    list1[j] = user
        else:
            print(f'{user} is not in a word!')

        # Remaining attempt logic
        remain = attempt - i

        # storing the guess word by the user
        for m in list1:
            str1 = str1 + m

        # all guess word storing in list2
        list2.append(str1)
        lenth = len(list2) #length of list2

        # checking the guess word
        for z in range(lenth):
            if list2[z] == word:
                print("You won the game...")
                print(f'The word is : {list2[z]}')
                return 0

        print('\n')

    if remain == 0:
        print('...............GAME OVER...............')
        return

if __name__=='__main__':
    fun()
