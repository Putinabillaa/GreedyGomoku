''' This module contains function that detect threats in the board. '''

def find_threats(board, defense):
    '''
    Find threats in the board.
    if defense == 1, player 1 defense
    if defense == 2, player 1 offense
    '''
    offense = 1 if defense == 2 else 2
    straight_four = []
    four_in_a_row = []
    broken_four = []
    open_three_in_a_row = []
    closed_three_in_a_row = []
    open_broken_three = []
    closed_broken_three = []
    open_two_in_a_row = []
    closed_two_in_a_row = []
    open_broken_two = []
    closed_broken_two = []
    open_single = []
    closed_single = []
    for row in range(board.height):
        for col in range(board.width):
            # print("here: ", row, col)
            cell = board.states.get(row * board.width + col)
            if cell == offense: 
                # Four in a row / Straight four
                # Horizontal
                if col + 3 < board.width:
                    if board.states.get(row * board.width + col + 1) == offense and \
                       board.states.get(row * board.width + col + 2) == offense and \
                       board.states.get(row * board.width + col + 3) == offense:
                        if  col - 1 >= 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) == defense and \
                            board.states.get(row * board.width + col - 1) is None:
                            four_in_a_row.append((row, col - 1))
                        elif col - 1 < 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) is None:
                            four_in_a_row.append((row, col + 4))
                        elif col - 1 >= 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) is None and \
                            board.states.get(row * board.width + col - 1) == defense:
                            four_in_a_row.append((row, col + 4))
                        elif col - 1 >= 0 and col + 4 >= board.width and \
                            board.states.get(row * board.width + col - 1) is None:
                            four_in_a_row.append((row, col - 1))
                        elif col - 1 >= 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) is None and \
                            board.states.get(row * board.width + col - 1) is None:
                            straight_four.append((row, col - 1))
                            straight_four.append((row, col + 4))
                # Vertical
                if row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col) == offense and \
                       board.states.get((row + 2) * board.width + col) == offense and \
                       board.states.get((row + 3) * board.width + col) == offense:
                        if row - 1 >= 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) == defense and \
                           board.states.get((row - 1) * board.width + col) is None:
                            four_in_a_row.append((row - 1, col))
                        elif row - 1 < 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) is None:
                            four_in_a_row.append((row + 4, col))
                        elif row - 1 >= 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) is None and \
                            board.states.get((row - 1) * board.width + col) == defense:
                            four_in_a_row.append((row + 4, col))
                        elif row - 1 >= 0 and row + 4 >= board.height and \
                            board.states.get((row - 1) * board.width + col) is None:
                            four_in_a_row.append((row - 1, col))
                        elif row - 1 >= 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) is None and \
                            board.states.get((row - 1) * board.width + col) is None:
                            straight_four.append((row - 1, col))
                            straight_four.append((row + 4, col))
                        
                # Down-right
                if col + 3 < board.width and row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col + 1) == offense and \
                       board.states.get((row + 2) * board.width + col + 2) == offense and \
                       board.states.get((row + 3) * board.width + col + 3) == offense:
                        if row - 1 >= 0 and col - 1 >= 0 and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) == defense and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            four_in_a_row.append((row - 1, col - 1))
                        elif (row - 1 < 0 or col - 1 < 0) and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) is None:
                            four_in_a_row.append((row + 4, col + 4))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) is None and \
                            board.states.get((row - 1) * board.width + col - 1) == defense:
                            four_in_a_row.append((row + 4, col + 4))
                        elif row - 1 >= 0 and col - 1 >= 0 and (row + 4 >= board.height or col + 4 >= board.width) and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            four_in_a_row.append((row - 1, col - 1))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) is None and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            straight_four.append((row - 1, col - 1))
                            straight_four.append((row + 4, col + 4))
                # Down-left
                if col - 3 >= 0 and row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col - 1) == offense and \
                       board.states.get((row + 2) * board.width + col - 2) == offense and \
                       board.states.get((row + 3) * board.width + col - 3) == offense:
                        if row - 1 >= 0 and col + 1 < board.width and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) == defense and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            four_in_a_row.append((row - 1, col + 1))
                        elif (row - 1 < 0 or col + 1 >= board.width) and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) is None:
                            four_in_a_row.append((row + 4, col - 4))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) is None and \
                            board.states.get((row - 1) * board.width + col + 1) == defense:
                            four_in_a_row.append((row + 4, col - 4))
                        elif row - 1 >= 0 and col + 1 < board.width and (row + 4 >= board.height or col - 4 < 0) and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            four_in_a_row.append((row - 1, col + 1))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) is None and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            straight_four.append((row - 1, col + 1))
                            straight_four.append((row + 4, col - 4))
                
                # Broken four
                # Horizontal
                if col + 4 < board.width:
                    if board.states.get(row * board.width + col + 1) is None and \
                       board.states.get(row * board.width + col + 2) == offense and \
                       board.states.get(row * board.width + col + 3) == offense and \
                        board.states.get(row * board.width + col + 4) == offense:
                            broken_four.append((row, col + 1))
                    elif board.states.get(row * board.width + col + 1) == offense and \
                        board.states.get(row * board.width + col + 2) is None and \
                        board.states.get(row * board.width + col + 3) == offense and \
                        board.states.get(row * board.width + col + 4) == offense:
                            broken_four.append((row, col + 2))
                    elif board.states.get(row * board.width + col + 1) == offense and \
                        board.states.get(row * board.width + col + 2) == offense and \
                        board.states.get(row * board.width + col + 3) is None and \
                        board.states.get(row * board.width + col + 4) == offense:
                            broken_four.append((row, col + 3))
                        
                # Vertical
                if row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col) is None and \
                       board.states.get((row + 2) * board.width + col) == offense and \
                       board.states.get((row + 3) * board.width + col) == offense and \
                        board.states.get((row + 4) * board.width + col) == offense:
                            broken_four.append((row + 1, col))
                    elif board.states.get((row + 1) * board.width + col) == offense and \
                        board.states.get((row + 2) * board.width + col) is None and \
                        board.states.get((row + 3) * board.width + col) == offense and \
                        board.states.get((row + 4) * board.width + col) == offense:
                            broken_four.append((row + 2, col))
                    elif board.states.get((row + 1) * board.width + col) == offense and \
                        board.states.get((row + 2) * board.width + col) == offense and \
                        board.states.get((row + 3) * board.width + col) is None and \
                        board.states.get((row + 4) * board.width + col) == offense:
                            broken_four.append((row + 3, col))

                        
                # Down-right
                if col + 3 < board.width and row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col + 1) is None and \
                       board.states.get((row + 2) * board.width + col + 2) == offense and \
                       board.states.get((row + 3) * board.width + col + 3) == offense and \
                        board.states.get((row + 3) * board.width + col + 3) == offense:
                            broken_four.append((row + 1, col + 1))
                    elif board.states.get((row + 1) * board.width + col + 1) == offense and \
                        board.states.get((row + 2) * board.width + col + 2) is None and \
                        board.states.get((row + 3) * board.width + col + 3) == offense and \
                        board.states.get((row + 3) * board.width + col + 3) == offense:
                            broken_four.append((row + 2, col + 2))
                    elif board.states.get((row + 1) * board.width + col + 1) == offense and \
                        board.states.get((row + 2) * board.width + col + 2) == offense and \
                        board.states.get((row + 3) * board.width + col + 3) is None and \
                        board.states.get((row + 3) * board.width + col + 3) == offense:
                            broken_four.append((row + 3, col + 3))

                # Down-left
                if col - 3 >= 0 and row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col - 1) is None and \
                       board.states.get((row + 2) * board.width + col - 2) == offense and \
                       board.states.get((row + 3) * board.width + col - 3) == offense and \
                        board.states.get((row + 3) * board.width + col - 3) == offense:
                            broken_four.append((row + 1, col - 1))
                    elif board.states.get((row + 1) * board.width + col - 1) == offense and \
                        board.states.get((row + 2) * board.width + col - 2) is None and \
                        board.states.get((row + 3) * board.width + col - 3) == offense and \
                        board.states.get((row + 3) * board.width + col - 3) == offense:
                            broken_four.append((row + 2, col - 2))
                    elif board.states.get((row + 1) * board.width + col - 1) == offense and \
                        board.states.get((row + 2) * board.width + col - 2) == offense and \
                        board.states.get((row + 3) * board.width + col - 3) is None and \
                        board.states.get((row + 3) * board.width + col - 3) == offense:
                            broken_four.append((row + 3, col - 3))

                # Three in a row
                # Horizontal
                if col + 2 < board.width:
                    if board.states.get(row * board.width + col + 1) == offense and \
                       board.states.get(row * board.width + col + 2) == offense:
                        if col - 1 >= 0 and col + 3 < board.width and \
                            board.states.get(row * board.width + col - 1) == defense and \
                            board.states.get(row * board.width + col + 3) is None:
                            closed_three_in_a_row.append((row, col + 3))
                        elif col - 1 < 0 and col + 3 < board.width and \
                            board.states.get(row * board.width + col + 3) is None:
                            closed_three_in_a_row.append((row, col + 3))
                        elif col - 1 >= 0 and col + 3 < board.width and \
                            board.states.get(row * board.width + col - 1) is None and \
                            board.states.get(row * board.width + col + 3) == defense:
                            closed_three_in_a_row.append((row, col - 1))
                        elif col - 1 >= 0 and col + 3 >= board.width and \
                            board.states.get(row * board.width + col - 1) is None:
                            closed_three_in_a_row.append((row, col - 1))
                        elif board.states.get(row * board.width + col - 1) is None and \
                            board.states.get(row * board.width + col + 3) is None:
                            open_three_in_a_row.append((row, col - 1))
                            open_three_in_a_row.append((row, col + 3))

                # Vertical
                if row + 2 < board.height:
                    if board.states.get((row + 1) * board.width + col) == offense and \
                       board.states.get((row + 2) * board.width + col) == offense:
                        if row - 1 >= 0 and row + 3 < board.height and \
                            board.states.get((row - 1) * board.width + col) == defense and \
                            board.states.get((row + 3) * board.width + col) is None:
                            closed_three_in_a_row.append((row + 3, col))
                        elif row - 1 < 0 and row + 3 < board.height and \
                            board.states.get((row + 3) * board.width + col) is None:
                            closed_three_in_a_row.append((row + 3, col))
                        elif row - 1 >= 0 and row + 3 < board.height and \
                            board.states.get((row - 1) * board.width + col) is None and \
                            board.states.get((row + 3) * board.width + col) == defense:
                            closed_three_in_a_row.append((row - 1, col))
                        elif row - 1 >= 0 and row + 3 >= board.height and \
                            board.states.get((row - 1) * board.width + col) is None:
                            closed_three_in_a_row.append((row - 1, col))
                        elif row - 1 >= 0 and row + 3 < board.height and \
                            board.states.get((row - 1) * board.width + col) is None and \
                            board.states.get((row + 3) * board.width + col) is None:
                            open_three_in_a_row.append((row - 1, col))
                            open_three_in_a_row.append((row + 3, col))

                # Down-right
                if col + 2 < board.width and row + 2 < board.height:
                    if board.states.get((row + 1) * board.width + col + 1) == offense and \
                       board.states.get((row + 2) * board.width + col + 2) == offense:
                        if row - 1 >= 0 and col - 1 >= 0 and row + 3 < board.height and col + 3 < board.width and \
                            board.states.get((row - 1) * board.width + col - 1) == defense and \
                            board.states.get((row + 3) * board.width + col + 3) is None:
                            closed_three_in_a_row.append((row + 3, col + 3))
                        elif (row - 1 < 0 or col - 1 < 0) and row + 3 < board.height and col + 3 < board.width and \
                            board.states.get((row + 3) * board.width + col + 3) is None:
                            closed_three_in_a_row.append((row + 3, col + 3))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 3 < board.height and col + 3 < board.width and \
                            board.states.get((row - 1) * board.width + col - 1) is None and \
                            board.states.get((row + 3) * board.width + col + 3) == defense:
                            closed_three_in_a_row.append((row - 1, col - 1))
                        elif row - 1 >= 0 and col - 1 >= 0 and (row + 3 >= board.height or col + 3 >= board.width) and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            closed_three_in_a_row.append((row - 1, col - 1))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 3 < board.height and col + 3 < board.width and \
                            board.states.get((row - 1) * board.width + col - 1) is None and \
                            board.states.get((row + 3) * board.width + col + 3) is None:
                            open_three_in_a_row.append((row - 1, col - 1))
                            open_three_in_a_row.append((row + 3, col + 3))

                # Down-left
                if col - 2 >= 0 and row + 2 < board.height:
                    if board.states.get((row + 1) * board.width + col - 1) == offense and \
                       board.states.get((row + 2) * board.width + col - 2) == offense:
                        if row - 1 >= 0 and col + 1 < board.width and row + 3 < board.height and col - 3 >= 0 and \
                            board.states.get((row - 1) * board.width + col + 1) == defense and \
                            board.states.get((row + 3) * board.width + col - 3) is None:
                            closed_three_in_a_row.append((row + 3, col - 3))
                        elif (row - 1 < 0 or col + 1 >= board.width) and row + 3 < board.height and col - 3 >= 0 and \
                            board.states.get((row + 3) * board.width + col - 3) is None:
                            closed_three_in_a_row.append((row + 3, col - 3))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 3 < board.height and col - 3 >= 0 and \
                            board.states.get((row - 1) * board.width + col + 1) is None and \
                            board.states.get((row + 3) * board.width + col - 3) == defense:
                            closed_three_in_a_row.append((row - 1, col + 1))
                        elif row - 1 >= 0 and col + 1 < board.width and (row + 3 >= board.height or col - 3 < 0) and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            closed_three_in_a_row.append((row - 1, col + 1))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 3 < board.height and col - 3 >= 0 and \
                            board.states.get((row - 1) * board.width + col + 1) is None and \
                            board.states.get((row + 3) * board.width + col - 3) is None:
                            open_three_in_a_row.append((row - 1, col + 1))
                            open_three_in_a_row.append((row + 3, col - 3))

                # Broken three
                # Horizontal
                if col + 3 < board.width:
                    if board.states.get(row * board.width + col + 1) is None and \
                       board.states.get(row * board.width + col + 2) == offense and \
                       board.states.get(row * board.width + col + 3) == offense:
                        if  col - 1 >= 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) == defense and \
                            board.states.get(row * board.width + col - 1) is None:
                            closed_broken_three.append((row, col + 1))
                            closed_broken_three.append((row, col - 1))
                        elif col - 1 < 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) is None:
                            closed_broken_three.append((row, col + 1))
                            closed_broken_three.append((row, col + 4))
                        elif col - 1 >= 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) is None and \
                            board.states.get(row * board.width + col - 1) == defense:
                            closed_broken_three.append((row, col + 1))
                            closed_broken_three.append((row, col + 4))
                        elif col - 1 >= 0 and col + 4 >= board.width and \
                            board.states.get(row * board.width + col - 1) is None:
                            closed_broken_three.append((row, col + 1))
                            closed_broken_three.append((row, col - 1))
                        elif col - 1 >= 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) is None and \
                            board.states.get(row * board.width + col - 1) is None:
                            open_broken_three.append((row, col + 1))
                            open_broken_three.append((row, col - 1))
                            open_broken_three.append((row, col + 4))
                if col + 3 < board.width:
                    if board.states.get(row * board.width + col + 1) == offense and \
                       board.states.get(row * board.width + col + 2) is None and \
                       board.states.get(row * board.width + col + 3) == offense:
                        if  col - 1 >= 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) == defense and \
                            board.states.get(row * board.width + col - 1) is None:
                            closed_broken_three.append((row, col + 2))
                            closed_broken_three.append((row, col - 1))
                        elif col - 1 < 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) is None:
                            closed_broken_three.append((row, col + 2))
                            closed_broken_three.append((row, col + 4))
                        elif col - 1 >= 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) is None and \
                            board.states.get(row * board.width + col - 1) == defense:
                            closed_broken_three.append((row, col + 2))
                            closed_broken_three.append((row, col + 4))
                        elif col - 1 >= 0 and col + 4 >= board.width and \
                            board.states.get(row * board.width + col - 1) is None:
                            closed_broken_three.append((row, col + 2))
                            closed_broken_three.append((row, col - 1))
                        elif col - 1 >= 0 and col + 4 < board.width and \
                            board.states.get(row * board.width + col + 4) is None and \
                            board.states.get(row * board.width + col - 1) is None:
                            open_broken_three.append((row, col + 2))
                            open_broken_three.append((row, col - 1))
                            open_broken_three.append((row, col + 4))
                # Vertical
                if row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col) is None and \
                       board.states.get((row + 2) * board.width + col) == offense and \
                       board.states.get((row + 3) * board.width + col) == offense:
                        if row - 1 >= 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) == defense and \
                            board.states.get((row - 1) * board.width + col) is None:
                            closed_broken_three.append((row + 1, col))
                            closed_broken_three.append((row - 1, col))
                        elif row - 1 < 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) is None:
                            closed_broken_three.append((row + 1, col))
                            closed_broken_three.append((row + 4, col))
                        elif row - 1 >= 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) is None and \
                            board.states.get((row - 1) * board.width + col) == defense:
                            closed_broken_three.append((row + 1, col))
                            closed_broken_three.append((row + 4, col))
                        elif row - 1 >= 0 and row + 4 >= board.height and \
                            board.states.get((row - 1) * board.width + col) is None:
                            closed_broken_three.append((row + 1, col))
                            closed_broken_three.append((row - 1, col))
                        elif row - 1 >= 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) is None and \
                            board.states.get((row - 1) * board.width + col) is None:
                            open_broken_three.append((row + 1, col))
                            open_broken_three.append((row - 1, col))
                            open_broken_three.append((row + 4, col))
                if row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col) == offense and \
                       board.states.get((row + 2) * board.width + col) is None and \
                       board.states.get((row + 3) * board.width + col) == offense:
                        if row - 1 >= 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) == defense and \
                            board.states.get((row - 1) * board.width + col) is None:
                            closed_broken_three.append((row + 2, col))
                            closed_broken_three.append((row - 1, col))
                        elif row - 1 < 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) is None:
                            closed_broken_three.append((row + 2, col))
                            closed_broken_three.append((row + 4, col))
                        elif row - 1 >= 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) is None and \
                            board.states.get((row - 1) * board.width + col) == defense:
                            closed_broken_three.append((row + 2, col))
                            closed_broken_three.append((row + 4, col))
                        elif row - 1 >= 0 and row + 4 >= board.height and \
                            board.states.get((row - 1) * board.width + col) is None:
                            closed_broken_three.append((row + 2, col))
                            closed_broken_three.append((row - 1, col))
                        elif row - 1 >= 0 and row + 4 < board.height and \
                            board.states.get((row + 4) * board.width + col) is None and \
                            board.states.get((row - 1) * board.width + col) is None:
                            open_broken_three.append((row + 2, col))
                            open_broken_three.append((row - 1, col))
                            open_broken_three.append((row + 4, col))
                # Down-right
                if col + 3 < board.width and row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col + 1) is None and \
                       board.states.get((row + 2) * board.width + col + 2) == offense and \
                       board.states.get((row + 3) * board.width + col + 3) == offense:
                        if row - 1 >= 0 and col - 1 >= 0 and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) == defense and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            closed_broken_three.append((row + 1, col + 1))
                            closed_broken_three.append((row - 1, col - 1))
                        elif (row - 1 < 0 or col - 1 < 0) and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) is None:
                            closed_broken_three.append((row + 1, col + 1))
                            closed_broken_three.append((row + 4, col + 4))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) is None and \
                            board.states.get((row - 1) * board.width + col - 1) == defense:
                            closed_broken_three.append((row + 1, col + 1))
                            closed_broken_three.append((row + 4, col + 4))
                        elif row - 1 >= 0 and col - 1 >= 0 and (row + 4 >= board.height or col + 4 >= board.width) and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            closed_broken_three.append((row + 1, col + 1))
                            closed_broken_three.append((row - 1, col - 1))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) is None and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            open_broken_three.append((row + 1, col + 1))
                            open_broken_three.append((row - 1, col - 1))
                            open_broken_three.append((row + 4, col + 4))
                if col + 3 < board.width and row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col + 1) == offense and \
                       board.states.get((row + 2) * board.width + col + 2) is None and \
                       board.states.get((row + 3) * board.width + col + 3) == offense:
                        if row - 1 >= 0 and col - 1 >= 0 and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) == defense and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            closed_broken_three.append((row + 2, col + 2))
                            closed_broken_three.append((row - 1, col - 1))
                        elif (row - 1 < 0 or col - 1 < 0) and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) is None:
                            closed_broken_three.append((row + 2, col + 2))
                            closed_broken_three.append((row + 4, col + 4))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) is None and \
                            board.states.get((row - 1) * board.width + col - 1) == defense:
                            closed_broken_three.append((row + 2, col + 2))
                            closed_broken_three.append((row + 4, col + 4))
                        elif row - 1 >= 0 and col - 1 >= 0 and (row + 4 >= board.height or col + 4 >= board.width) and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            closed_broken_three.append((row + 2, col + 2))
                            closed_broken_three.append((row - 1, col - 1))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 4 < board.height and col + 4 < board.width and \
                            board.states.get((row + 4) * board.width + col + 4) is None and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            open_broken_three.append((row + 2, col + 2))
                            open_broken_three.append((row - 1, col - 1))
                            open_broken_three.append((row + 4, col + 4))
                # Down-left
                if col - 3 >= 0 and row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col - 1) is None and \
                       board.states.get((row + 2) * board.width + col - 2) == offense and \
                       board.states.get((row + 3) * board.width + col - 3) == offense:
                        if row - 1 >= 0 and col + 1 < board.width and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) == defense and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            closed_broken_three.append((row + 1, col - 1))
                            closed_broken_three.append((row - 1, col + 1))
                        elif (row - 1 < 0 or col + 1 >= board.width) and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) is None:
                            closed_broken_three.append((row + 1, col - 1))
                            closed_broken_three.append((row + 4, col - 4))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) is None and \
                            board.states.get((row - 1) * board.width + col + 1) == defense:
                            closed_broken_three.append((row + 1, col - 1))
                            closed_broken_three.append((row + 4, col - 4))
                        elif row - 1 >= 0 and col + 1 < board.width and (row + 4 >= board.height or col - 4 < 0) and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            closed_broken_three.append((row + 1, col - 1))
                            closed_broken_three.append((row - 1, col + 1))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) is None and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            open_broken_three.append((row + 1, col - 1))
                            open_broken_three.append((row - 1, col + 1))
                            open_broken_three.append((row + 4, col - 4))
                if col - 3 >= 0 and row + 3 < board.height:
                    if board.states.get((row + 1) * board.width + col - 1) == offense and \
                       board.states.get((row + 2) * board.width + col - 2) is None and \
                       board.states.get((row + 3) * board.width + col - 3) == offense:
                        if row - 1 >= 0 and col + 1 < board.width and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) == defense and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            closed_broken_three.append((row + 2, col - 2))
                            closed_broken_three.append((row - 1, col + 1))
                        elif (row - 1 < 0 or col + 1 >= board.width) and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) is None:
                            closed_broken_three.append((row + 2, col - 2))
                            closed_broken_three.append((row + 4, col - 4))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) is None and \
                            board.states.get((row - 1) * board.width + col + 1) == defense:
                            closed_broken_three.append((row + 2, col - 2))
                            closed_broken_three.append((row + 4, col - 4))
                        elif row - 1 >= 0 and col + 1 < board.width and (row + 4 >= board.height or col - 4 < 0) and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            closed_broken_three.append((row + 2, col - 2))
                            closed_broken_three.append((row - 1, col + 1))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 4 < board.height and col - 4 >= 0 and \
                            board.states.get((row + 4) * board.width + col - 4) is None and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            open_broken_three.append((row + 2, col - 2))
                            open_broken_three.append((row - 1, col + 1))
                            open_broken_three.append((row + 4, col - 4))

                # Two in a row
                # Horizontal
                if col + 1 < board.width:
                    if board.states.get(row * board.width + col + 1) == offense:
                        if col - 1 >= 0 and col + 2 < board.width and \
                            board.states.get(row * board.width + col - 1) == defense and \
                            board.states.get(row * board.width + col + 2) is None:
                            closed_two_in_a_row.append((row, col + 2))
                        elif col - 1 < 0 and col + 2 < board.width and \
                            board.states.get(row * board.width + col + 2) is None:
                            closed_two_in_a_row.append((row, col + 2))
                        elif col - 1 >= 0 and col + 2 < board.width and \
                            board.states.get(row * board.width + col - 1) is None and \
                            board.states.get(row * board.width + col + 2) == defense:
                            closed_two_in_a_row.append((row, col - 1))
                        elif col - 1 >= 0 and col + 2 >= board.width and \
                            board.states.get(row * board.width + col - 1) is None:
                            closed_two_in_a_row.append((row, col - 1))
                        elif col - 1 >= 0 and col + 2 < board.width and \
                            board.states.get(row * board.width + col - 1) is None and \
                            board.states.get(row * board.width + col + 2) is None:
                            open_two_in_a_row.append((row, col - 1))
                            open_two_in_a_row.append((row, col + 2))
                
                # Vertical
                if row + 1 < board.height:
                    if board.states.get((row + 1) * board.width + col) == offense:
                        if row - 1 >= 0 and row + 2 < board.height and \
                            board.states.get((row - 1) * board.width + col) == defense and \
                            board.states.get((row + 2) * board.width + col) is None:
                            closed_two_in_a_row.append((row + 2, col))
                        elif row - 1 < 0 and row + 2 < board.height and \
                            board.states.get((row + 2) * board.width + col) is None:
                            closed_two_in_a_row.append((row + 2, col))
                        elif row - 1 >= 0 and row + 2 < board.height and \
                            board.states.get((row - 1) * board.width + col) is None and \
                            board.states.get((row + 2) * board.width + col) == defense:
                            closed_two_in_a_row.append((row - 1, col))
                        elif row - 1 >= 0 and row + 2 >= board.height and \
                            board.states.get((row - 1) * board.width + col) is None:
                            closed_two_in_a_row.append((row - 1, col))
                        elif row - 1 >= 0 and row + 2 < board.height and \
                            board.states.get((row - 1) * board.width + col) is None and \
                            board.states.get((row + 2) * board.width + col) is None:
                            open_two_in_a_row.append((row - 1, col))
                            open_two_in_a_row.append((row + 2, col))
                
                # Down-right
                if row + 1 < board.height and col + 1 < board.width:
                    if board.states.get((row + 1) * board.width + col + 1) == offense:
                        if row - 1 >= 0 and col - 1 >= 0 and row + 2 < board.height and col + 2 < board.width and \
                            board.states.get((row - 1) * board.width + col - 1) == defense and \
                            board.states.get((row + 2) * board.width + col + 2) is None:
                            closed_two_in_a_row.append((row + 2, col + 2))
                        elif (row - 1 < 0 or col - 1 < 0) and row + 2 < board.height and col + 2 < board.width and \
                            board.states.get((row + 2) * board.width + col + 2) is None:
                            closed_two_in_a_row.append((row + 2, col + 2))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 2 < board.height and col + 2 < board.width and \
                            board.states.get((row - 1) * board.width + col - 1) is None and \
                            board.states.get((row + 2) * board.width + col + 2) == defense:
                            closed_two_in_a_row.append((row - 1, col - 1))
                        elif row - 1 >= 0 and col - 1 >= 0 and (row + 2 >= board.height or col + 2 >= board.width) and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            closed_two_in_a_row.append((row - 1, col - 1))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 2 < board.height and col + 2 < board.width and \
                            board.states.get((row - 1) * board.width + col - 1) is None and \
                            board.states.get((row + 2) * board.width + col + 2) is None:
                            open_two_in_a_row.append((row - 1, col - 1))
                            open_two_in_a_row.append((row + 2, col + 2))
                
                # Down-left
                if row + 1 < board.height and col - 1 >= 0:
                    if board.states.get((row + 1) * board.width + col - 1) == offense:
                        if row - 1 >= 0 and col + 1 < board.width and row + 2 < board.height and col - 2 >= 0 and \
                            board.states.get((row - 1) * board.width + col + 1) == defense and \
                            board.states.get((row + 2) * board.width + col - 2) is None:
                            closed_two_in_a_row.append((row + 2, col - 2))
                        elif (row - 1 < 0 or col + 1 >= board.width) and row + 2 < board.height and col - 2 >= 0 and \
                            board.states.get((row + 2) * board.width + col - 2) is None:
                            closed_two_in_a_row.append((row + 2, col - 2))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 2 < board.height and col - 2 >= 0 and \
                            board.states.get((row - 1) * board.width + col + 1) is None and \
                            board.states.get((row + 2) * board.width + col - 2) == defense:
                            closed_two_in_a_row.append((row - 1, col + 1))
                        elif row - 1 >= 0 and col + 1 < board.width and (row + 2 >= board.height or col - 2 < 0) and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            closed_two_in_a_row.append((row - 1, col + 1))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 2 < board.height and col - 2 >= 0 and \
                            board.states.get((row - 1) * board.width + col + 1) is None and \
                            board.states.get((row + 2) * board.width + col - 2) is None:
                            open_two_in_a_row.append((row - 1, col + 1))
                            open_two_in_a_row.append((row + 2, col - 2))
                # Broken two
                # Horizontal
                if col + 2 < board.width:
                    if board.states.get(row * board.width + col + 1) is None and \
                       board.states.get(row * board.width + col + 2) == offense:
                        if col - 1 >= 0 and col + 3 < board.width and \
                            board.states.get(row * board.width + col - 1) == defense and \
                            board.states.get(row * board.width + col + 3) is None:
                            closed_broken_two.append((row, col + 1))
                            closed_broken_two.append((row, col + 3))
                        elif col - 1 < 0 and col + 3 < board.width and \
                            board.states.get(row * board.width + col + 3) is None:
                            closed_broken_two.append((row, col + 1))
                            closed_broken_two.append((row, col + 3))
                        elif col - 1 >= 0 and col + 3 < board.width and \
                            board.states.get(row * board.width + col - 1) is None and \
                            board.states.get(row * board.width + col + 3) == defense:
                            closed_broken_two.append((row, col + 1))
                            closed_broken_two.append((row, col - 1))
                        elif col - 1 >= 0 and col + 3 >= board.width and \
                            board.states.get(row * board.width + col - 1) is None:
                            closed_broken_two.append((row, col + 1))
                            closed_broken_two.append((row, col - 1))
                        elif board.states.get(row * board.width + col - 1) is None and \
                            board.states.get(row * board.width + col + 3) is None:
                            open_broken_two.append((row, col + 1))
                            open_broken_two.append((row, col - 1))
                            open_broken_two.append((row, col + 3))

                # Vertical
                if row + 2 < board.height:
                    if board.states.get((row + 1) * board.width + col) is None and \
                       board.states.get((row + 2) * board.width + col) == offense:
                        if row - 1 >= 0 and row + 3 < board.height and \
                            board.states.get((row - 1) * board.width + col) == defense and \
                            board.states.get((row + 3) * board.width + col) is None:
                            closed_broken_two.append((row + 1, col))
                            closed_broken_two.append((row + 3, col))
                        elif row - 1 < 0 and row + 3 < board.height and \
                            board.states.get((row + 3) * board.width + col) is None:
                            closed_broken_two.append((row + 1, col))
                            closed_broken_two.append((row + 3, col))
                        elif row - 1 >= 0 and row + 3 < board.height and \
                            board.states.get((row - 1) * board.width + col) is None and \
                            board.states.get((row + 3) * board.width + col) == defense:
                            closed_broken_two.append((row + 1, col))
                            closed_broken_two.append((row - 1, col))
                        elif row - 1 >= 0 and row + 3 >= board.height and \
                            board.states.get((row - 1) * board.width + col) is None:
                            closed_broken_two.append((row + 1, col))
                            closed_broken_two.append((row - 1, col))
                        elif row - 1 >= 0 and row + 3 < board.height and \
                            board.states.get((row - 1) * board.width + col) is None and \
                            board.states.get((row + 3) * board.width + col) is None:
                            open_broken_two.append((row + 1, col))
                            open_broken_two.append((row - 1, col))
                            open_broken_two.append((row + 3, col))

                # Down-right
                if col + 2 < board.width and row + 2 < board.height:
                    if board.states.get((row + 1) * board.width + col + 1) is None and \
                       board.states.get((row + 2) * board.width + col + 2) == offense:
                        if row - 1 >= 0 and col - 1 >= 0 and row + 3 < board.height and col + 3 < board.width and \
                            board.states.get((row - 1) * board.width + col - 1) == defense and \
                            board.states.get((row + 3) * board.width + col + 3) is None:
                            closed_broken_two.append((row + 1, col + 1))
                            closed_broken_two.append((row + 3, col + 3))
                        elif (row - 1 < 0 or col - 1 < 0) and row + 3 < board.height and col + 3 < board.width and \
                            board.states.get((row + 3) * board.width + col + 3) is None:
                            closed_broken_two.append((row + 1, col + 1))
                            closed_broken_two.append((row + 3, col + 3))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 3 < board.height and col + 3 < board.width and \
                            board.states.get((row - 1) * board.width + col - 1) is None and \
                            board.states.get((row + 3) * board.width + col + 3) == defense:
                            closed_broken_two.append((row + 1, col + 1))
                            closed_broken_two.append((row - 1, col - 1))
                        elif row - 1 >= 0 and col - 1 >= 0 and (row + 3 >= board.height or col + 3 >= board.width) and \
                            board.states.get((row - 1) * board.width + col - 1) is None:
                            closed_broken_two.append((row + 1, col + 1))
                            closed_broken_two.append((row - 1, col - 1))
                        elif row - 1 >= 0 and col - 1 >= 0 and row + 3 < board.height and col + 3 < board.width and \
                            board.states.get((row - 1) * board.width + col - 1) is None and \
                            board.states.get((row + 3) * board.width + col + 3) is None:
                            open_broken_two.append((row + 1, col + 1))
                            open_broken_two.append((row - 1, col - 1))
                            open_broken_two.append((row + 3, col + 3))

                # Down-left
                if col - 2 >= 0 and row + 2 < board.height:
                    if board.states.get((row + 1) * board.width + col - 1) is None and \
                       board.states.get((row + 2) * board.width + col - 2) == offense:
                        if row - 1 >= 0 and col + 1 < board.width and row + 3 < board.height and col - 3 >= 0 and \
                            board.states.get((row - 1) * board.width + col + 1) == defense and \
                            board.states.get((row + 3) * board.width + col - 3) is None:
                            closed_broken_two.append((row + 1, col - 1))
                            closed_broken_two.append((row + 3, col - 3))
                        elif (row - 1 < 0 or col + 1 >= board.width) and row + 3 < board.height and col - 3 >= 0 and \
                            board.states.get((row + 3) * board.width + col - 3) is None:
                            closed_broken_two.append((row + 1, col - 1))
                            closed_broken_two.append((row + 3, col - 3))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 3 < board.height and col - 3 >= 0 and \
                            board.states.get((row - 1) * board.width + col + 1) is None and \
                            board.states.get((row + 3) * board.width + col - 3) == defense:
                            closed_broken_two.append((row + 1, col - 1))
                            closed_broken_two.append((row - 1, col + 1))
                        elif row - 1 >= 0 and col + 1 < board.width and (row + 3 >= board.height or col - 3 < 0) and \
                            board.states.get((row - 1) * board.width + col + 1) is None:
                            closed_broken_two.append((row + 1, col - 1))
                            closed_broken_two.append((row - 1, col + 1))
                        elif row - 1 >= 0 and col + 1 < board.width and row + 3 < board.height and col - 3 >= 0 and \
                            board.states.get((row - 1) * board.width + col + 1) is None and \
                            board.states.get((row + 3) * board.width + col - 3) is None:
                            open_broken_two.append((row + 1, col - 1))
                            open_broken_two.append((row - 1, col + 1))
                            open_broken_two.append((row + 3, col - 3))
                # Single
                if  row + 1 < board.height and col + 1 < board.width and \
                    row - 1 >= 0 and col - 1 >= 0 and \
                    board.states.get(row * board.width + col + 1) is None and \
                    board.states.get((row + 1) * board.width + col) is None and \
                    board.states.get((row + 1) * board.width + col + 1) is None and \
                    board.states.get((row + 1) * board.width + col - 1) is None and \
                    board.states.get(row * board.width + col - 1) is None and \
                    board.states.get((row - 1) * board.width + col) is None and \
                    board.states.get((row - 1) * board.width + col - 1) is None and \
                    board.states.get((row - 1) * board.width + col + 1) is None:
                        open_single.append((row + 1, col))
                        open_single.append((row, col + 1))
                        open_single.append((row - 1, col))
                        open_single.append((row, col - 1))
                        open_single.append((row + 1, col + 1))
                        open_single.append((row - 1, col - 1))
                        open_single.append((row + 1, col - 1))
                        open_single.append((row - 1, col + 1))
                
                elif (board.states.get(row * board.width + col + 1) == defense or \
                      board.states.get(row * board.width + col + 1) == defense) and \
                    (board.states.get((row + 1) * board.width + col) == defense or \
                     board.states.get((row + 1) * board.width + col) is None) and \
                    (board.states.get((row + 1) * board.width + col + 1) == defense or \
                     board.states.get((row + 1) * board.width + col + 1) == defense is None) and \
                    (board.states.get((row + 1) * board.width + col - 1) == defense or \
                     board.states.get((row + 1) * board.width + col - 1) is None) and \
                    (board.states.get(row * board.width + col - 1) == defense or \
                     board.states.get(row * board.width + col - 1) is None) and \
                    (board.states.get((row - 1) * board.width + col) == defense or \
                     board.states.get((row - 1) * board.width + col) is None) and \
                    (board.states.get((row - 1) * board.width + col - 1) == defense or \
                     board.states.get((row - 1) * board.width + col - 1) is None) and \
                    (board.states.get((row - 1) * board.width + col + 1) == defense or \
                     board.states.get((row - 1) * board.width + col + 1) ==  None):
                        closed_single.append((row + 1, col))
                        closed_single.append((row, col + 1))
                        closed_single.append((row - 1, col))
                        closed_single.append((row, col - 1))
                        closed_single.append((row + 1, col + 1))
                        closed_single.append((row - 1, col - 1))
                        closed_single.append((row + 1, col - 1))
                        closed_single.append((row - 1, col + 1))

    return  straight_four, four_in_a_row, broken_four, open_three_in_a_row, open_broken_three, closed_three_in_a_row, \
            closed_broken_three, open_broken_three, open_two_in_a_row, closed_two_in_a_row, \
            open_broken_two, closed_broken_two, open_single, closed_single