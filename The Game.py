print("*" * 59)
print("*" * 9, " Давай сыграем в игру крестики нолики ", "*" * 10)
print("*" * 59)

RANGE_OF_FIELD = 6
board = list(range(1,RANGE_OF_FIELD **2 + 1))
WIN_ROW = 4


def draw_board(board: list):  #Создаем тело игрового поля
    print("█" * 22, "-" * (RANGE_OF_FIELD *4) , "█" * 22) # █ данный символ реализован через сочетание alt+219
    for i in range(RANGE_OF_FIELD):
        row = ""
        for j in range(RANGE_OF_FIELD):
            row += "|"
            row += str(board[j+i*RANGE_OF_FIELD]).ljust(3)
        print("█" * 22, row,  "█" * 22)
        print("█" * 22, "-" * (RANGE_OF_FIELD *4), "█" * 22)

def take_input(player_token: str): #создаем ввод для игроков и проверку ввода
    valid = False
    while not valid:
        player_answer = input(f"Куда поставим  {player_token}" )
        try:
            player_answer = int(player_answer)
        except:
            print("Введен неверный символ")
            continue
        if player_answer < 1 or player_answer > RANGE_OF_FIELD ** 2:
            print(f"Неверный символ. Введите число от 1 до {RANGE_OF_FIELD**2}.")
            continue
        if not board[player_answer-1] in ["X", "O"]:
            board[player_answer-1] = player_token
            valid = True
        else:
            print("Здесь уже есть значение")


def check_list_of_equals(list1: list):
    if len(set(list1)) == 1:
        return True
    return False


def check_win(board : list): #проверка на выигрышь
    win_coord = []
    for i in range(RANGE_OF_FIELD):
        for j in range(RANGE_OF_FIELD - WIN_ROW + 1):
            if check_list_of_equals(board[i*RANGE_OF_FIELD+j:i*RANGE_OF_FIELD+j+ WIN_ROW]):#горизонталь
                return True
            if check_list_of_equals(board[i + j * RANGE_OF_FIELD:i + (j + WIN_ROW)*RANGE_OF_FIELD:RANGE_OF_FIELD]):#вертикаль
                return True
    return False

def main(board): #запуск функций
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > (WIN_ROW + 1):
           if check_win(board):
              print("УРА, Вы выиграли!")
              win = True
              break
        if counter == RANGE_OF_FIELD**2:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Давай сыграем еще разок!")