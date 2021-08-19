
#game_list = ['',1,2,3,4,5,6,7,8,9,10]
game_list = ['','X','O','X','X','X','O','O','O',9]

def players():
    marker = ''
    #keep asking player1 
    while marker != 'X' and marker != 'O':
        marker = input('Player1 choose X or O: ').upper()     
    #assign player2
        player1 = marker

        if player1 =='X':
            player2 = 'O'
        else:
            player2 = 'X'  
    
    return player1, player2

def display_game ():
    print('')
    print(game_list[7],'|',game_list[8],'|',game_list[9])
    print('---------')
    print(game_list[4],'|',game_list[5],'|',game_list[6])
    print('---------')
    print(game_list[1],'|',game_list[2],'|',game_list[3])
    
def position_choice ():
    
    #import os 
    #os.system("clear") 
       
    choice = ''
    filled = ['X','O']
    within_range = False
    postion_range = range(1,10)
    
    while choice.isdigit() == False or within_range == False:
        #display_game()
        print('')
        choice = input('Player postion to replace(1~9): ')
        
        
        if choice.isdigit() == False:
            #print('\n'*100)
            #print('\033[H\033[J', end='')
            print('')
            print('Sry! It isnt a digit or out of range!')
            
            
        elif choice.isdigit() == True:
            if int(choice) in postion_range:
                within_range = True
            else:
                within_range = False
                #print('\033[H\033[J', end='')
                print('')
                print('Its out of range!')
                
    return int(choice)

def replacement_choice (playerletter):
    
    filled = ['X','O']
    
    display_game()
    position = position_choice()
    
    while game_list[position] in filled:
        print('Sry! Its filled!')
        position = position_choice()
        
    game_list[position] = playerletter.upper()

def checkgame ():
 
    triple_o = ['O','O','O']
    triple_x = ['X','X','X']
    
    ##LINE
    line1 = game_list[7:10]
    line2 = game_list[4:7] 
    line3 = game_list[1:4]
    

    ## COLUMN
    ## between (()) its transforme into tuple
    column1 = game_list[7:0:-3]
    column2 = game_list[8:0:-3]
    column3 = game_list[9:0:-3]
    
    
    ## DIAGONAL
    diagonal0 = game_list[7:1:-2]
    diagonal1 = game_list[9:0:-4]


    x = game_list.count('X')
    o = game_list.count('O')
    
    if x >= 3 or 3 <=o:
    
        #LINE CHECKER3
        if triple_o in ( line1 , line2 , line3 ):
            return True , 'O line'
        elif triple_x in ( line1 , line2 , line3 ):
            return True, 'X line'

        # COLUMN CHECKER
        elif triple_o in (column1 , column2 , column3):
            return True, 'O column'
        elif triple_x in (column1 , column2 , column3):
            return True, 'X column'

        ## DIAGONAL CHECKER
        elif  triple_o in (diagonal0 , diagonal1):
            return True, 'O diagonal'
        elif  triple_x in (diagonal0 , diagonal1):
            return True, 'X diagonal'
        elif game_list.count('O') == 5 or game_list.count('X') == 5:
            return False, "Game over! It's a tie!"
        else:
            return False
    
    else:
        return False

def swap():
    player1, player2 = players()
    
    p1turn = True
    p2turn = False
      
    swap_player = True
    
    #while swap_player and result == False:

    while swap_player and checkgame() == False:
        while p1turn and checkgame () == False:
            playerletter = player1
            print('')
            print('-------P1-------')
            replacement_choice (playerletter)
            
            if checkgame() == True:
                return
            else:
                p1turn = False
                p2turn = True
            
            
        
        while p2turn and checkgame () == False:
            playerletter = player2
            print('')
            print('-------P2-------')
            replacement_choice (playerletter)
                       
            if checkgame() == True:
                return
            else:
                p1turn = True
                p2turn = False
                
    display_game()
    print('')
    return checkgame ()[1]
            
print(swap())

def  gaming ():
    
    game_on = True
        
    while game_on:
        
        #print('\033[H\033[J', end='')
        
        game_list = replacement_choice()
        #print('\033[H\033[J', end='')

        display_game()

        game_on = gameon_choice()
        
#gaming ()

def gameon_choice ():
    choice = "Y"
    result = checkgame()
    
    if result == False:
        while choice.upper() not in ['Y','N']:

            #choice = input("Would you like to keep playing? Y or N: ")

            if choice.upper() not in ['Y','N']:
                print("Please make sure to choose Y or N: ")

        if choice.upper() == 'Y':
            return True
        else:
            return False
    else:
        print('')
        print(f'Winner - {result[1]}')  