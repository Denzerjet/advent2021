drawnNumbersInput = open("DrawnNumbers.txt", "r").readline()
drawnNumbers = drawnNumbersInput.split(",")

boardsInput = open("Boards.txt", "r").read().splitlines()
board_list = [] #3D array
board = []

k = 0
for i in boardsInput:
    if (i == ""):
        board_list.append(board)
        board = []
        k = 0
        continue
    
    boardLine = i.split(" ")
    board.append([])
    for j in boardLine:
        if (j == ""):
            continue
        board[k].append(int(j))
    k += 1

#print("board_list: " + str(board_list))

#print("l_iterator: " + str(board_list[0]))
#print("m_iterator: " + str(board_list[0][0]))
#print("n_iterator: " + str(board_list[0][0][0]))





l_iterator = 0
m_iterator = 0
n_iterator = 0
drawnNumber_iterator = 0
found = 0

#L corresponds to the 2D array which is a board
#M corresponds to a 1D array which makes up 1/5 of the board
#N correspnd to a string number which makes up 1/25 of the board

a_iter= 0
b_iter = 0
c_iter = 0

#print("new board")
for a in board_list:
    for b in board_list[a_iter]:
        for c in board_list[a_iter][b_iter]:
            #print(str(board_list[a_iter][b_iter][c_iter]))

            #checking by row
            for d in board_list[a_iter][b_iter]:
                pass
                #print(str(int(d)))
            #print("exit")

            for e in range(5): #CHANGE BACK TO 5
                pass
                #print(str(int(board_list[a_iter][e][c_iter])))
            #print("new")
                


            c_iter += 1
        b_iter += 1
        c_iter = 0
    #print("new board")
    a_iter += 1
    b_iter = 0

bigfarts = 0
for boardChungus in board_list:
    bigfarts += 1

winners = []
first = 1
for o in drawnNumbers:
    for l in board_list:
        for m in board_list[l_iterator]:
            for n in board_list[l_iterator][m_iterator]:
                currentDrawnNum = int(drawnNumbers[drawnNumber_iterator])
                #print("Grabbed from board_list: " + str(board_list[l_iterator][m_iterator][n_iterator]))

                if currentDrawnNum == board_list[l_iterator][m_iterator][n_iterator]:
                    board_list[l_iterator][m_iterator][n_iterator] = -1
                
                ###
                # go through and check if any boards have a bingo, if so stop and grab that board
                if not bool(found):
                    bingohorizontal = "true"
                    for p in board_list[l_iterator][m_iterator]:
                        #print ("int(p): " + str(int(p)))
                        if int(p) != -1:
                            bingohorizontal = "false"
                    
                    bingovertical = "true"
                    for q in range(5): #CHANGE BACK TO 5
                        if int(board_list[l_iterator][q][n_iterator]) != -1:
                            bingovertical = "false"

                if ((bingohorizontal == "true" or bingovertical == "true")):
                    #found = 1

                    dupe = 0
                    for fart in winners:
                        if int(fart) == l_iterator:
                            dupe = 1
                    
                    if not dupe == 1:
                        winners.append(l_iterator)
                        if (len(winners) == bigfarts):
                            print("amongus: " + str(l_iterator))

                            realanswer = 0
                            for quop in range(5):
                                for glizzy in range(5):
                                    redsus = int(board_list[l_iterator][quop][glizzy])

                                    if redsus != -1:
                                        realanswer += redsus
                            realanswer = realanswer * currentDrawnNum
                            print(realanswer)

                    
                    
                    answer = 0
                    for g in range(5):
                        for h in range(5):
                            element = int(board_list[l_iterator][g][h])

                            if element != -1:
                                answer += element
                    #print(answer)
                    answer = answer * currentDrawnNum
                    #print(currentDrawnNum)
                    #print(str(l_iterator))
                    #print("answer: " + str(answer))


                ###
                n_iterator += 1
            m_iterator += 1
            n_iterator = 0
        l_iterator += 1
        m_iterator = 0
    drawnNumber_iterator += 1
    l_iterator = 0

#print("updated board_list: " + str(board_list))gi
