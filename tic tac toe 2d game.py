def game_2d():
    import random
    matrix_game = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
    print("""
            ########################
            Welcome To Tick Tack Toe
            ########################""")
    print(""" 

             1  |  2  |  3
            ----|-----|-----
             4  |  5  |  6
            ----|-----|-----
             7  |  8  |  9  
            ---------------- """)

    def winner_check():
        winner = True
        if matrix_game[0][0] == matrix_game[0][1] and matrix_game[0][0] == matrix_game[0][2]:
            print(f"The player {matrix_game[0][0]} won the game.")
            return winner
        if matrix_game[1][0] == matrix_game[1][1] and matrix_game[1][0] == matrix_game[1][2]:
            print(f"The player {matrix_game[1][0]} won the game.")
            return winner
        if matrix_game[2][0] == matrix_game[2][1] and matrix_game[2][0] == matrix_game[2][2]:
            print(f"The player {matrix_game[2][0]} won the game.")
            return winner
        if matrix_game[0][0] == matrix_game[1][0] and matrix_game[0][0] == matrix_game[2][0]:
            print(f"The player {matrix_game[0][0]} won the game.")
            return winner
        if matrix_game[0][1] == matrix_game[1][1] and matrix_game[0][1] == matrix_game[2][1]:
            print(f"The player {matrix_game[0][1]} won the game.")
            return winner
        if matrix_game[0][2] == matrix_game[1][2] and matrix_game[0][2] == matrix_game[2][2]:
            print(f"The player {matrix_game[0][2]} won the game.")
            return winner
        if matrix_game[0][0] == matrix_game[1][1] and matrix_game[0][0] == matrix_game[2][2]:
            print(f"The player {matrix_game[0][0]} has won the game.")
            return winner
        if matrix_game[0][2] == matrix_game[1][1] and matrix_game[0][2] == matrix_game[2][0]:
            print(f"The player {matrix_game[0][2]} has won the game.")
            return winner

    def game_draw():
        if input_of_game == 9 and winner_check() != True:
            print("""
                     ===========================
                     ---------Game Draw---------
                     ===========================
                     """)
            return

    input_of_game = 0
    player_list = []
    print(

    )
    player1_name = input("Enter the name of player1: ")
    player2_name = input("Enter the name of player2: ")
    player_list.append(player1_name)
    player_list.append(player2_name)
    # set the previous player to none value.This inside while loop is to make sure that same player is not selected.
    prev_player = None
    while input_of_game < 9:
        if winner_check() == True:
            break
        selected_player = random.choice(player_list)
        while selected_player == prev_player:
            selected_player = random.choice(player_list)
        prev_player = selected_player
        global turn
        turn = int(input(f"Enter the number which {selected_player} want to mark: "))
        while turn < 1 or turn > 9 or matrix_game[(turn - 1) // 3][(turn - 1) % 3] in player_list:
            print("Invalid input or position already marked. Please try again.")
            turn = int(input("Enter the number which you want to mark: "))
        for rows in matrix_game:
            for column in rows:
                if column in rows:
                    if turn == column:
                        index_of_turn = rows.index(column)
                        rows.insert(index_of_turn, selected_player)
                        rows.remove(column)
                        break
        input_of_game += 1
        for elements in matrix_game:
            print(elements)
            print('--------------------------')
    game_draw()
game_2d()
restart1 = input("Do you want to restart the game?Yes/No: ")
restart = restart1.lower()
if restart == 'yes':
    game_2d()
else:
    print("You have exit the game without restart.")











