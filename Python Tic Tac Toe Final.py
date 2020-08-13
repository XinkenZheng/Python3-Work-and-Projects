#!/usr/bin/env python
# coding: utf-8

# In[7]:


from IPython.display import clear_output

board = ['#','1','2','3','4','5','6','7','8','9']
def display_board(board):
    clear_output()
    print( '   |''   |')
    print( ' '+ board[7] +' | '+  board[8] + ' |' +' ' +board[9])
    print( '   |''   |')
    print(  '-----------')
    print( '   |''   |')
    print( ' '+ board[4] +' | '+  board[5] + ' |' +' ' +board[6])
    print( '   |''   |')
    print(  '-----------')
    print( '   |''   |')
    print( ' '+ board[1] +' | '+  board[2] + ' |' +' ' +board[3])
    print( '   |''   |')
    

test_board = ['X','O','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[8]:


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player1, choose X or O: ").upper()
    
    if marker == 'X':
        print("player1 will be X. ")
        print("player2 will be O. ")
        return ('X','O')
    elif marker == 'O':
        print("player1 will be O. ")
        print("player2 will be X. ")
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker


# In[9]:


player1_marker


# In[10]:


def win_check(board, mark):
    if board[7] == mark:
        if board[7] == board[8] == board[9]:
            return True
        if board[7] == board[4] == board[1]:
            return True
        if board[7] == board[5] == board[3]:
            return True
       
    if board[1] == mark:
        if board[1] == board[2] == board[3]:
            return True
        if board[1] == board[5] == board[9]:
            return True
    
    if board[8] == board[5] == board[2]:
            return True
    
    if board[9] == board[6] == board[3]:
            return True
    
    if board[4] == board[5] == board[6]:
        return True
    return False
    

win_check(test_board,'X')


# In[11]:


import random

def choose_first():
    first = random.randint(1,2)
    if first == 1:
        return(True, False)
        print("player 1 goes first.")
    else:
        return(False, True)   
        print("player 2 goes first.")
        
player1_turn, player2_turn = choose_first()


# In[12]:


player1_turn


# In[13]:


player2_turn


# In[14]:


def full_board_check(board):
    for num in range(len(board)):
        if board[num] != 'X' and board[num] != 'O':
            return False
    return True

        
        
full_board_check(test_board)


# In[15]:


player1_turn


# In[16]:


player2_turn


# In[17]:


def player_choice(player1_turn, player2_turn):
    choose_first()
    while(full_board_check(board) == False): 
        if player1_turn == True:
            choice = int (input("Player 1 make your move: "))
            board[choice] = player1_marker;
            display_board(board);
            if(win_check(board,board[choice]) == True):
                print("player1 wins")
                break
            player1_turn = False;
            player2_turn = True
        
        if player2_turn == True:
            choice = int (input("Player 2 make your move: "))
            board[choice] = player2_marker;
            display_board(board);
            win_check(board,board[choice])
            if(win_check(board,board[choice]) == True):
                print("player2 wins")
                break
            player1_turn = True;
            player2_turn = False;
        
        if(full_board_check(board) == True):
            print("its a tie")


# In[18]:


def replay():
    user_input  = input("Do you wish to replay? If Yes, press 1. If not, press any key to exit. : ")
    if user_input == 'yes':
        return True
    return False


# In[ ]:


print("Welcome to Tic Tac Toe")

while(True):
    board = ['X','1','2','3','4','5','6','7','8','9']
    player1_marker, player2_marker = player_input()
    display_board(board)
    player_choice(player1_turn,player2_turn)
    if(not replay()):
        break


