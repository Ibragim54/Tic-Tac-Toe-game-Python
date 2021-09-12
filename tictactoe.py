def tutorial():
    print('Welcome to Tic Tac Toe! \n')

    print("Let's start with the tutorial. \n")

    board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X']

    def board_print(list):
        print("   |   |   ")
        print(" {0} | {1} | {2}".format(board_list[0], board_list[1], board_list[2]))
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(" {0} | {1} | {2}".format(board_list[3], board_list[4], board_list[5]))
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(" {0} | {1} | {2}".format(board_list[6], board_list[7], board_list[8]))
        print("   |   |   ")

    print("The board for 'X's and 'O's will look like this: \n")

    board_print(board_list)

    print("\nTop left cell corresponds to # 1 and bottom right to # 9, similar to the order on an old mobile phone. \n")


tutorial()


def main():
    print("NEW GAME STARTED \n")

    marker_choice_1 = input("Player 1: Do you want to be X or O? \n").upper()

    while not (marker_choice_1 == "X" or marker_choice_1 == "O"):
        print("Wrong input.")
        marker_choice_1 = input("Player 1: Do you want to be X or O? \n").upper()

    if marker_choice_1 == "X":
        marker_choice_2 = "O"
    elif marker_choice_1 == "O":
        marker_choice_2 = "X"

    print("Splendid! Player 1 will go first! \n")

    readiness = input("Are you ready to play? Enter Yes or No. \n").upper()

    while readiness != "YES":

        if readiness == "NO":
            print("Get ready and come back. \n")

        if not (readiness == "YES" or readiness == "NO"):
            print("Only yes or no are accepted as an input. \n")

        readiness = input("Are you ready to play? Enter Yes or No. \n").upper()

    print("Alright, let's commence! \n")

    board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X']

    def board_print(list):
        print("   |   |   ")
        print(" {0} | {1} | {2}".format(board_list[0], board_list[1], board_list[2]))
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(" {0} | {1} | {2}".format(board_list[3], board_list[4], board_list[5]))
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(" {0} | {1} | {2}".format(board_list[6], board_list[7], board_list[8]))
        print("   |   |   ")

    def win_check(list):
        if (board_list[0] == board_list[1] == board_list[2] == "X") or (
                board_list[0] == board_list[1] == board_list[2] == "O"):
            return True
        elif (board_list[3] == board_list[4] == board_list[5] == "X") or (
                board_list[3] == board_list[4] == board_list[5] == "O"):
            return True
        elif (board_list[6] == board_list[7] == board_list[8] == "X") or (
                board_list[6] == board_list[7] == board_list[8] == "O"):
            return True
        elif (board_list[0] == board_list[3] == board_list[6] == "X") or (
                board_list[0] == board_list[3] == board_list[6] == "O"):
            return True
        elif (board_list[1] == board_list[4] == board_list[7] == "X") or (
                board_list[1] == board_list[4] == board_list[7] == "O"):
            return True
        elif (board_list[2] == board_list[5] == board_list[8] == "X") or (
                board_list[2] == board_list[5] == board_list[8] == "O"):
            return True
        elif (board_list[0] == board_list[4] == board_list[8] == "X") or (
                board_list[0] == board_list[4] == board_list[8] == "O"):
            return True
        elif (board_list[2] == board_list[4] == board_list[6] == "X") or (
                board_list[2] == board_list[6] == board_list[6] == "O"):
            return True
        else:
            return False


    def draw_check(list):
        space_count = board_list.count(' ')
        return space_count == 0

    while not win_check(board_list):

        while True:

            marker_position = input('Player 1, choose your next position: (1-9) \n')

            try:
                while not (9 >= int(marker_position) >= 1):
                    print('You can only input numbers 1-9. \n')
                    marker_position = input('Player 1, choose your next position: (1-9) \n')

                if board_list[int(marker_position) - 1] != ' ':
                    print('This position is already taken! \n')
                    continue

                else:
                    break

            except:
                print('Only integers from 1 to 9 are accepted as an input. Please try again. \n')
                continue


        board_list[int(marker_position) - 1] = marker_choice_1

        board_print(board_list)

        if win_check(board_list):
            break

        if draw_check(board_list):
            break

        print('\n')

        while True:

            marker_position = input('Player 2, choose your next position: (1-9) \n')

            try:
                while not (9 >= int(marker_position) >= 1):
                    print('You can only input numbers 1-9. \n')
                    marker_position = input('Player 2, choose your next position: (1-9) \n')

                if board_list[int(marker_position) - 1] != ' ':
                    print('This position is already taken! \n')
                    continue

                else:
                    break

            except:
                print('Only integers from 1 to 9 are accepted as an input. Please try again. \n')
                continue

        board_list[int(marker_position) - 1] = marker_choice_2

        board_print(board_list)

        if win_check(board_list):
            break

        if draw_check(board_list):
            break

        print('\n')

    if win_check(board_list):
        print('Congratulations! One of the players has won the game! \n')

    if draw_check(board_list):
        print("It's a draw! \n")

    restart = input("Would you like to play again? Yes or no?\n").lower()

    while restart != "yes":

        if restart == "no":
            break

        if not restart == "yes" or restart == "no":
            print("Is that a yes or no?")

            restart = input("Would you like to play again? Yes or no?\n").lower()


    if restart == 'yes':

        main()

    else:
        print("Thanks for playing!")
        exit()

main()