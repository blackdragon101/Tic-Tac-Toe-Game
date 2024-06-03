def game_3d():
    import random
    print("""
            ***********************
            Welcome To Tic Tac Toe 
            ***********************
            """)
    main_matrix = [[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']],
                   [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                   [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]]
    print("The game begins:")
    print('-------------------------------')
    for matrices in main_matrix:
        print(matrices)
        print("==================================================")
        print()

    enteries = 0

    def winner_checker():
        winner = True
        for matrix in main_matrix:
            if matrix[0][0] == matrix[0][1] and matrix[0][0] == matrix[0][2]:
                print(f"The player {matrix[0][0]} won the game.")
                return winner
            if matrix[1][0] == matrix[1][1] and matrix[1][0] == matrix[1][2]:
                print(f"The player {matrix[1][0]} won the game.")
                return winner
            if matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2]:
                print(f"The player {matrix[2][0]} won the game.")
                return winner
            if matrix[0][0] == matrix[1][0] and matrix[0][0] == matrix[2][0]:
                print(f"The player {matrix[0][0]} won the game.")
                return winner
            if matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1]:
                print(f"The player {matrix[0][1]} won the game.")
                return winner
            if matrix[0][2] == matrix[1][2] and matrix[0][2] == matrix[2][2]:
                print(f"The player {matrix[0][2]} won the game.")
                return winner
            if matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]:
                print(f"The player {matrix[0][0]} has won the game.")
                return winner
            if matrix[0][2] == matrix[1][1] and matrix[0][2] == matrix[2][0]:
                print(f"The player {matrix[0][2]} has won the game.")
                return winner
        matrix1 = main_matrix[0]
        matrix2 = main_matrix[1]
        matrix3 = main_matrix[2]
        if matrix1[0][0] == matrix2[0][0] and matrix1[0][0] == matrix3[0][0]:
            print(f"The player {matrix1[0][0]} has won the game.")
            return winner
        if matrix1[0][1] == matrix2[0][1] and matrix1[0][1] == matrix3[0][1]:
            print(f"The player {matrix1[0][1]} has won the game.")
            return winner
        if matrix1[0][2] == matrix2[0][2] and matrix1[0][2] == matrix3[0][2]:
            print(f"The player {matrix1[0][2]} has won the game.")
            return winner
        if matrix1[1][0] == matrix2[1][0] and matrix1[1][0] == matrix3[1][0]:
            print(f"The player {matrix1[1][0]} has won the game.")
            return winner
        if matrix1[1][1] == matrix2[1][1] and matrix1[1][1] == matrix3[1][1]:
            print(f"The player {matrix1[1][1]} has won the game.")
            return winner
        if matrix1[1][2] == matrix2[1][2] and matrix1[1][2] == matrix3[1][2]:
            print(f"The player {matrix1[1][2]} has won the game.")
            return winner
        if matrix1[2][0] == matrix2[2][0] and matrix1[2][0] == matrix3[2][0]:
            print(f"The player {matrix1[2][0]} has won the game.")
            return winner
        if matrix1[2][1] == matrix2[2][1] and matrix1[2][1] == matrix3[2][1]:
            print(f"The player {matrix1[2][1]} has won the game.")
            return winner
        if matrix1[2][2] == matrix2[2][2] and matrix1[2][2] == matrix3[2][2]:
            print(f"The player {matrix1[2][2]} has won the game.")
            return winner
        if matrix1[0][0] == matrix2[1][1] and matrix1[0][0] == matrix3[2][2]:
            print(f"The player {matrix1[0][0]} has won the game.")
            return winner
        if matrix1[0][2] == matrix2[1][1] and matrix1[0][2] == matrix3[2][0]:
            print(f"The player {matrix1[0][2]} has won the game.")
            return winner
        if matrix1[2][1] == matrix2[1][1] and matrix1[2][1] == matrix3[0][1]:
            print(f"The player {matrix1[2][1]} has won the game.")
            return winner
        if matrix1[0][1] == matrix2[1][1] and matrix1[0][1] == matrix3[2][1]:
            print(f"The player {matrix1[0][1]} has won the game.")
            return winner
        if matrix1[2][2] == matrix2[1][1] and matrix1[2][2] == matrix3[0][0]:
            print(f"The player {matrix1[2][2]} has won the game.")
            return winner
        if matrix1[0][0] == matrix2[0][1] and matrix1[0][0] == matrix3[0][2]:
            print(f"The player {matrix1[0][0]} has won the game.")
            return winner
        if matrix1[2][0] == matrix2[2][1] and matrix1[2][0] == matrix3[2][2]:
            print(f"The player {matrix1[2][0]} has won the game.")
            return winner
        if matrix1[0][0] == matrix2[1][0] and matrix1[0][0] == matrix3[2][0]:
            print(f"The player {matrix1[0][0]} has won the game.")
            return winner
        if matrix1[0][2] == matrix2[1][2] and matrix1[0][2] == matrix3[2][2]:
            print(f"The player {matrix1[0][2]} has won the game.")
            return winner
        if matrix1[0][2] == matrix2[0][1] and matrix1[0][2] == matrix3[0][0]:
            print(f"The player {matrix1[0][2]} has won the game.")
            return winner
        if matrix1[2][0] == matrix2[1][0] and matrix1[2][0] == matrix3[0][0]:
            print(f"The player {matrix1[2][0]} has won the game.")
            return winner
        if matrix1[2][2] == matrix2[2][1] and matrix1[2][2] == matrix3[2][0]:
            print(f"The player {matrix1[2][2]} has won the game.")
            return winner
        if matrix1[2][1] == matrix2[1][1] and matrix1[2][1] == matrix3[0][0]:
            print(f"The player {matrix1[2][1]} has won the game.")
            return winner
        if matrix1[1][0] == matrix2[1][1] and matrix1[1][0] == matrix3[1][2]:
            print(f"The player {matrix1[1][0]} has won the game.")
            return winner
        if matrix1[1][2] == matrix2[1][1] and matrix1[1][2] == matrix3[1][0]:
            print(f"The player {matrix1[1][2]} has won the game.")
            return winner
    def draw_check():
        if winner_checker() is False and enteries == 27:
            print("""
                     ===========================
                     ---------Game Draw---------
                     ===========================
                     """)
            return

    player1 = input("Enter the name of 1st player: ")
    player2 = input("Enter the name of 2nd player: ")
    players = [player1, player2]
    prev_player = None
    selected_player = random.choice(players)
    while enteries < 27:
        if winner_checker() is True:
            break
        else:
            while prev_player == selected_player:
                selected_player = random.choice(players)
            prev_player = selected_player
            global user_input
            user_input = input(f"Enter the number {selected_player} want to mark: ")
            if user_input.isalnum() == False:
                print("Invalid input!!!")
            for matrix in main_matrix:
                for rows in matrix:
                    for column in rows:
                        if column in rows:
                            if user_input == column:
                                user_inp_index = rows.index(column)
                                rows.insert(user_inp_index, selected_player)
                                rows.remove(column)
                                break
            enteries += 1

            for matrix in main_matrix:
                for rows in matrix:
                    print(rows)
                    print("---------------------------")
                print('==================================')
                print()
    draw_check()
game_3d()
restart1 = input("Do you want to restart the game?Yes/No: ")
restart = restart1.lower()
if restart == 'yes':
    game_3d()
else:
    print("You have exit the game without restart.")












