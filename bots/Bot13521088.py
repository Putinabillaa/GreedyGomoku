import random
from game import Board
import globals as globals
from bots.threats import find_threats

class Bot13521088(object):
    """
    Bot player
    """

    def __init__(self):
        self.player = None

        """
            TODO: Ganti dengan NIM kalian
        """
        self.NIM = "13521088"

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board, return_var):

        try:
            location = self.get_input(board)
            if isinstance(location, str):  # for python3
                location = [int(n, 10) for n in location.split(",")]
            move = board.location_to_move(location)
        except Exception as e:
            move = -1

        while move == -1 or move not in board.availables:
            if globals.stop_threads:
                return
            try:
                location = self.get_input(board)
                if isinstance(location, str):  # for python3
                    location = [int(n, 10) for n in location.split(",")]
                move = board.location_to_move(location)
            except Exception as e:
                move = -1
        return_var.append(move) 

    def __str__(self):
        return "{} a.k.a Player {}".format(self.NIM,self.player)
    
    def get_input(self, board : Board) -> str:
        """
            Parameter board merepresentasikan papan permainan. Objek board memiliki beberapa
            atribut penting yang dapat menjadi acuan strategi.
            - board.height : int (x) -> panjang papan
            - board.width : int (y) -> lebar papan
            Koordinat 0,0 terletak pada kiri bawah

            [x,0] [x,1] [x,2] . . . [x,y]                               
            . . . . . . . . . . . . . . .  namun perlu diketahui        Contoh 4x4: 
            . . . . . . . . . . . . . . .  bahwa secara internal        11 12 13 14 15
            . . . . . . . . . . . . . . .  sel-sel disimpan dengan  =>  10 11 12 13 14
            [2,0] [2,1] [2,2] . . . [2,y]  barisan interger dimana      5  6  7  8  9
            [1,0] [1,1] [1,2] . . . [1,y]  kiri bawah adalah nol        0  1  2  3  4
            [0,0] [0,1] [0,2] . . . [0,y]          
                                 
            - board.states : dict -> Kondisi papan. 
            Key dari states adalah integer sel (0,1,..., x*y)
            Value adalah integer 1 atau 2:
            -> 1 artinya sudah diisi player 1
            -> 2 artinya sudah diisi player 2

            TODO: Tentukan x,y secara greedy. Kembalian adalah sebuah string "x,y"
        """
        defense = assign_val(board, 1)
        defense_maxval = max(defense.values())
        defense_maxval_list = [k for k, v in defense.items() if v == defense_maxval]
    
        offense = assign_val(board, 2)
        offense_maxval = max(offense.values())
        offense_maxval_list = [k for k, v in offense.items() if v == offense_maxval]
        
        print(defense_maxval, offense_maxval)
        # print(defense,"\n", offense)
        if defense_maxval > offense_maxval:
            idx = len(defense_maxval_list)//2
            (x, y) = defense_maxval_list[idx]
            print(x)
            print(y)
        else:
            idx = len(offense_maxval_list)//2
            x, y = offense_maxval_list[idx]
        return f"{x},{y}"

def assign_val(board: Board, defense):
    dict = {}
    straight_four, four_in_a_row, broken_four, open_three_in_a_row, open_broken_three, closed_three_in_a_row, \
    closed_broken_three, open_broken_three, open_two_in_a_row, closed_two_in_a_row, \
    open_broken_two, closed_broken_two, open_single, closed_single = find_threats(board, defense)
    print("straight four:", straight_four)
    print("four in a row:", four_in_a_row)
    print("broken four:", broken_four)
    print("open three in a row:", open_three_in_a_row)
    print("open broken three:", open_broken_three)
    print("closed three in a row:", closed_three_in_a_row)
    print("closed broken three:", closed_broken_three)
    print("open two in a row:", open_two_in_a_row)
    print("closed two in a row:", closed_two_in_a_row)
    print("broken two:", open_broken_two, closed_broken_two)
    print("open single:", open_single)
    print("closed single:", closed_single)
    for i in range (board.height):
        for j in range (board.width):
            if (i, j) in straight_four:
                dict[(i, j)] = dict.get((i, j), 0) + 10
            if (i, j) in four_in_a_row:
                dict[(i, j)] = dict.get((i, j), 0) + 10
            if (i, j) in broken_four:
                dict[(i, j)] = dict.get((i, j), 0) + 10
            if (i, j) in open_three_in_a_row:
                if defense == 1: dict[(i, j)] = dict.get((i, j), 0) + 9
                else: dict[(i, j)] = dict.get((i, j), 0) + 7
            if (i, j) in open_broken_three:
                if defense == 1: dict[(i, j)] = dict.get((i, j), 0) + 9
                else: dict[(i, j)] = dict.get((i, j), 0) + 7
            if (i, j) in closed_three_in_a_row:
                dict[(i, j)] = dict.get((i, j), 0) + 5
            if (i, j) in closed_broken_three:
                dict[(i, j)] = dict.get((i, j), 0) + 5
            if (i, j) in open_two_in_a_row:
                dict[(i, j)] = dict.get((i, j), 0) + 4
            if (i, j) in open_broken_two:
                dict[(i, j)] = dict.get((i, j), 0) + 4
            if (i, j) in closed_two_in_a_row:
                dict[(i, j)] = dict.get((i, j), 0) + 3
            if (i, j) in closed_broken_two:
                dict[(i, j)] = dict.get((i, j), 0) + 3
            if (i, j) in open_single:
                dict[(i, j)] = dict.get((i, j), 0) + 2
            if (i, j) in closed_single:
                dict[(i, j)] = dict.get((i, j), 0) + 1
            dict[(i, j)] = dict.get((i, j), 0) + 0
    return dict