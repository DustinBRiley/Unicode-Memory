# INF360 - Programming in Python
# Dustin Riley
# Midterm Project - memory game

import random
import os

board = [['\u2600', '\u2600', '\u2620', '\u2620', '\u2623', '\u2623'],
    ['\u2660', '\u2660', '\u2670', '\u2670', '\u26d0', '\u26d0'],
    ['\u2622', '\u2622', '\u2625', '\u2625', '\u2672', '\u2672'],
    ['\u263a', '\u263a', '\u263f', '\u263f', '\u2602', '\u2602'],
    ['\u2663', '\u2663', '\u2665', '\u2665', '\u2666', '\u2666'],
    ['\u263d', '\u263d', '\u269c', '\u269c', '\u262c', '\u262c']]
boardFace = [['\u2592']*6 for _ in range(6)]
boardList = ['\u2600', '\u2620', '\u2623', '\u2660', '\u2670', '\u26d0', '\u2622', '\u2625', '\u2672', '\u263a', '\u263f', '\u2623', '\u2663', '\u2665', '\u2666', '\u263d', '\u269c', '\u262c', '\u2600', '\u2620', '\u2602', '\u2660', '\u2670', '\u26d0', '\u2622', '\u2625', '\u2672', '\u263a', '\u263f', '\u2602', '\u2663', '\u2665', '\u2666', '\u263d', '\u269c', '\u262c']
matched = ['0']*36
done = False
count = 0
dup = 0
prevspot1 = ''
prevspot2 = ''


def shuffle():
    random.random()
    random.shuffle(boardList)           #shuffle boardlist
    for j in range(6):
        for k in range(6):
            boardFace[j][k] = '\u2592'  #reset boardFace
    i = -1
    for j in range(6):
        for k in range(6):
            i+=1
            board[j][k] = boardList[i]  #place boardList into board
            for l in range(36):
                if(matched[l] == boardList[i]): #check if current boardList item is in matched list
                    temp = matched[l]           #switch position of matched[l] to match newly shuffled boardList
                    matched[l] = matched[i]
                    matched[i] = temp
                    boardFace[j][k] = board[j][k]   #reveal matched items in their newly shuffled place


def printBoard():
    os.system('cls')                    #clear screen
    print('\t1\t2\t3\t4\t5\t6')         #print top cords
    x = ''
    y = ''
    for i in range(6):
        match i:                        #print side cords
            case 0: y += 'A'
            case 1: y += 'B'
            case 2: y += 'C'
            case 3: y += 'D'
            case 4: y += 'E'
            case 5: y += 'F'
        print(y, end = '\t')
        y = ''
        for j in range(6):
            x += boardFace[i][j] + '\t' #add boardFace items to x string for 1 row
        print(x)
        x = ''                          #reset x string


def init():
    global count, board, matched            #reset count board and matched
    count = 0
    matched = ['0']*36
    board = [['\u2600', '\u2600', '\u2620', '\u2620', '\u2623', '\u2623'],
    ['\u2660', '\u2660', '\u2670', '\u2670', '\u26d0', '\u26d0'],
    ['\u2622', '\u2622', '\u2625', '\u2625', '\u2672', '\u2672'],
    ['\u263a', '\u263a', '\u263f', '\u263f', '\u2623', '\u2623'],
    ['\u2663', '\u2663', '\u2665', '\u2665', '\u2666', '\u2666'],
    ['\u263d', '\u263d', '\u269c', '\u269c', '\u262c', '\u262c']]
    shuffle()

def getSpot():
    spotPicked = False
    x = ''
    while(not spotPicked):
        spot = input('Pick a spot (a-f)(1-6): ')                        #get user input
        if(len(spot) != 2):                                             #make sure input is 2 characters long
            print('Error not a valid position'); continue
        else:
            match spot[0].upper():                                      #convert first character to uppercase
                case 'A': x += '0'                                      #store first character to match list index
                case 'B': x += '1'
                case 'C': x += '2'
                case 'D': x += '3'
                case 'E': x += '4'
                case 'F': x += '5'
                case _: print('Error first input not a-f.'); continue   #if anything but abcdef/ABCDEF is entered
            match spot[1]:
                case '1': x += '0'                                      #store second character to match list index
                case '2': x += '1'
                case '3': x += '2'
                case '4': x += '3'
                case '5': x += '4'
                case '6': x += '5'
                case _: print('Error second input not 1-5.'); continue  #if anything but 123456 is entered
            spotPicked = True
    return x

init()
while(not done):
    printBoard()
    x, y, x2, y2 = 0, 0, 0, 0
    spot1 = getSpot()
    x = int(spot1[0])                                   #convert first char of spot1 to integer
    y = int(spot1[1])                                   #convert second char of spot1 to integer
    if(boardFace[x][y] == '\u2592'):                    #check if spot is unmatched
        if(prevspot1 == spot1 or prevspot2 == spot1):   #check if spot 1 is a duplicate spot from last attempt
            dup += 1                                    #dup count up
            if(dup == 2):
                print('You called that spot the last 2 times, thats brute forcing not memorizing. *shake* *shake* *shake*')
                shuffle()
                prevspot1 = ''
                prevspot2 = ''
                dup = 0
                input('Press Enter to continue...')
                continue
        boardFace[x][y] = board[x][y]                   #reveal board spot 1
    else:                                               #spot is already matched
        print('Error spot already matched')
        input('Press Enter to continue...')
        continue
    printBoard()                                        #call printBoard() to display board spot 1
    spot2 = getSpot()                                   #do the same for spot 2
    x2 = int(spot2[0])
    y2 = int(spot2[1])
    if(x == x2 and y == y2):                            #if spot 1 is the same spot as spot 2
        print('Error thats the same spot, try again')
        boardFace[x][y] = '\u2592'                      # reset spot 1
        input('Press Enter to continue...')
        continue
    if(boardFace[x2][y2] == '\u2592'):
        if(prevspot1 == spot2 or prevspot2 == spot2):   #check if spot 2 is a duplicate spot from last attempt
            dup += 1
            if(dup == 2):
                print('You called that spot the last 2 times, thats brute forcing not memorizing. *shake* *shake* *shake*')
                shuffle()
                prevspot1 = ''
                prevspot2 = ''
                dup = 0
                input('Press Enter to continue...')
                continue
        boardFace[x2][y2] = board[x2][y2]
    else:
        print('Error spot already matched')
        input('Press Enter to continue...')
        boardFace[x][y] = '\u2592'                      # reset spot 1
        continue
    printBoard()
    if(boardFace[x][y] == boardFace[x2][y2]):           #check if spot 1 and spot 2 are a match
        print('You got a match!')
        count += 1                                      #count of matches up
        for i in range(36):
            if(boardList[i] == boardFace[x][y]):        #record matched items to matched list
                matched[i] = boardList[i]
        prevspot1 = ''                                  #reset prev spots and dup count
        prevspot2 = ''
        dup = 0
    else:
        boardFace[x][y] = '\u2592'                      # reset spot 1 and 2
        boardFace[x2][y2] = '\u2592'
        print('Not a match')
        prevspot1 = spot1                               #record attempted spot 1 and spot 2
        prevspot2 = spot2
    input('Press Enter to continue...')
    if(count == 18):                                    #if all matches found
        print('You did it!')
        answered = False
        while(not answered):
            ans = input('Play again? (y or n): ')
            if(ans.upper() == 'Y'):
                answered = True
                init()
            elif(ans.upper() == 'N'):
                answered = True
                done = True
            else:
                print('Are your y and n keys broken?')