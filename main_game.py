from snake import*
from playground import*

class main_game:
    """This class is used for displaying main menu and settings"""
    
    def __init__(self):
        """Initialize pygame and some parameters"""
        
        pygame.init()
        pygame.display.set_caption('SNAKE-GAME Gilberto Jimenez 00261433')

        # initialize the display object, this is to be used for displaying everything
        self.surface=pygame.display.set_mode((FRAME_WIDTH,FRAME_HEIGHT+BAR))

        # initialize the board, which will be used to store the chosen obstacles by the user. Default is no obstacles board (empty list)
        self.board=[]
        # initialize the speed parameters of the game to store user choices, with default values.
        self.initial_speed=10
        self.speed_increment=1


#################################################### helper functions ########################################################
        
    def draw_arrows(self):
        """This function is used once, to draw arrows in the board-choosing menu, as a design for notifying the user to use right and left arrows for navigating boards"""
        
        x=FRAME_WIDTH-40
        y=(FRAME_HEIGHT-50)/2
        for i in range(21):
            self.surface.fill((0,0,0),rect=(x+i,y+i,20,1))
            self.surface.fill((0,0,0),rect=(x+i,y+40-i,20,1))
            self.surface.fill((0,0,0),rect=(20-i,y+i,20,1))
            self.surface.fill((0,0,0),rect=(20-i,y+40-i,20,1))



    def button_frame(self,button):
        """Drawing a 1-pixel thickness frame around a given button"""
        
        self.surface.fill((0,0,0),rect=(button[0]-1,button[1]-1,button[2]+2,1))
        self.surface.fill((0,0,0),rect=(button[0]-1,button[1]+button[3],button[2]+2,1))
        self.surface.fill((0,0,0),rect=(button[0]-1,button[1],1,button[3]))
        self.surface.fill((0,0,0),rect=(button[0]+button[2],button[1],1,button[3]))

        
    def draw_button(self,button_rect,button_name,font_color,font_size,rect_color,only_text=False):
        """
        This function is to draw a button with specified parameters.
        args:
        button_rect: a 4-elemnt tuple: (starting point abscissa, starting point ordinate, width, height).

        buttom_name: text to print in the button.

        font_color: color of text.

        font_size: size of text.

        rect_color: color of the button

        only_text: false by default. When true, no button will be printed, just a text. In this case, rect_color and the last two elemnts of button_rect will be ignored.
        
        """

        # setting the font
        font = pygame.font.SysFont('Consolas', font_size)

        # case not only text:
        if not only_text:
            # draw the button frame
            self.button_frame(button_rect)
            # draw the button
            self.surface.fill(rect_color,rect=button_rect)
        # print the text. if no text is needed to be printed, button_name will be set as empty string ("") when the function is called.
        self.surface.blit(font.render(button_name, True,font_color), (button_rect[0]+5,button_rect[1]+5))
        
    
        
    def check_pressed(self,pos,button):
        """
        returns a boolean to know if a certain button is pressed by the user
        args:
        pos: (x,y) coordinates representing the current mouse position

        button: the rect object representing the button: a 4-elemnt tuple: (starting point abscissa, starting point ordinate, width, height)

        """
        
        return (pos[0]>=button[0] and pos[0]<=button[0]+button[2] and pos[1]>=button[1] and pos[1]<=button[1]+button[3])

    def assign_board(self,index):
        """ given an index, returns the list of obstacles corresponding to the chosen board index. index will be 0,1 or 2"""
        
        if index==0:
            return []
        if index==1:
            listt=[]
            for i in range(0,800,10):
                listt.append((i,0))
                listt.append((i,590))
            for i in range(10,600,10):
                listt.append((0,i))
                listt.append((790,i))
            return listt
        else:
            listt=[]
            for i in range(0,800,10):
                if i not in range(350,450):
                    listt.append((i,0))
                    listt.append((i,590))
                else:
                    listt.append((i,300))
                    listt.append((i,290))
            for i in range(10,600,10):
                if i not in range(250,350):
                    listt.append((0,i))
                    listt.append((790,i))
                elif i not in [290,300]:
                    listt.append((390,i))
                    listt.append((400,i))
                if i>30 and i<270:    
                    listt.append((i,i))
                    listt.append((i+10,i))
                    listt.append((780-i,i))
                    listt.append((790-i,i))
                    listt.append((i,580-i))
                    listt.append((i+10,580-i))
                    listt.append((780-i,580-i))
                    listt.append((780-i+10,580-i))
            return listt

#################################################### End helper functions ########################################################


    def play(self):
        """using the playground and snake classes, start the game and return results (score and time) when finish"""

        # initiate the snake object with initial speed, initial direction, speed increment, and body parts.
        # copy is used so that the initial body parts list is not changed while playing.
        my_snake=snake(self.initial_speed,'R',self.speed_increment,BODY_PARTS.copy())

        # Initiate the playground object with the snake and the game display object
        play=playground(my_snake,self.surface)

        # add obstacles 
        play.add_obstacles(self.board)
        # generate food
        play.generate_food()

        # return results while calling the play method of the playground class, to start the game.
        return(play.play())


    def main_menu(self):
        """ main menu of the game"""

        # load, rescale, and display the background image
        background=pygame.image.load(BACKGROUND)
        background=pygame.transform.scale(background, (FRAME_WIDTH,FRAME_HEIGHT+BAR))
        self.surface.blit(background,(0,0))

        # assign rects to the buttons: start, options, help, and exit
        start_rect=(FRAME_WIDTH/2-45,FRAME_HEIGHT/2-50,90,40)
        options_rect=(FRAME_WIDTH/2-45,FRAME_HEIGHT/2+10,90,40)
        help_rect=(FRAME_WIDTH/2-45,FRAME_HEIGHT/2+70,90,40)
        exit_rect=(FRAME_WIDTH/2-45,FRAME_HEIGHT/2+130,90,40)

        # draw the buttons
        self.draw_button(start_rect,"Start",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(options_rect,"Options",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(help_rect,"Help",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(exit_rect,"Exit",(0,0,0),FONT_SIZE,(0,180,0))

        # update display to show the drawings
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                # terminate if user exits
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                # if the user pressed the mouse button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get the mouse curser pos
                    pos=pygame.mouse.get_pos()
                    # case start button is pressed
                    if self.check_pressed(pos,start_rect):
                        # when game is over, the user can play again. so iterate indefinetly until the user and python get bored.
                        while True:

                            # get the score and time results while calling the play function
                            score,time_elapsed=self.play()
                            # call game_over function to prompt the user that the game is over and to let him choose to play again or go to main menu.
                            play_again=self.game_over(score,time_elapsed)

                            # if play again is false, recall main menu and return. if play again is true, the loop will continue and initiate the game again
                            if(not play_again):
                                self.main_menu()
                                return

                    # case options is pressed, call the option menu then main menu again.
                    elif self.check_pressed(pos,options_rect):
                        self.options_menu()
                        self.main_menu()
                        return

                    # case help is pressed, call the help menu then main menu again
                    elif self.check_pressed(pos,help_rect):
                        self.help_menu()
                        self.main_menu()
                        return

                    # case exit is pressed, quit and terminate
                    elif self.check_pressed(pos,exit_rect):
                        pygame.quit()
                        sys.exit(0)


    def help_menu(self):
        """ menu displayed when help is clicked"""
        
        # load, rescale, and display the instructions image
        background=pygame.image.load(INSTRUCTIONS)
        background=pygame.transform.scale(background, (FRAME_WIDTH,FRAME_HEIGHT+BAR))
        self.surface.blit(background,(0,0))

        # assign rect to back button
        back_rect=(FRAME_WIDTH/2-40,FRAME_HEIGHT-20,80,40)

        # draw button
        self.draw_button(back_rect,"Back",(0,0,0),FONT_SIZE,(0,180,0))

        # update display
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                # if user exits, terminate
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                # if mouse button is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get mouse cursor position
                    pos=pygame.mouse.get_pos()

                    # case back is pressed,return, so main menu is displayed again
                    if self.check_pressed(pos,back_rect):
                        return
                    
        
    def options_menu(self):
        """ menu displayed when options is clicked"""

        # load, rescale, and display the background image
        background=pygame.image.load(BACKGROUND)
        background=pygame.transform.scale(background, (FRAME_WIDTH,FRAME_HEIGHT+BAR))
        self.surface.blit(background,(0,0))

        # assign rects to buttons: board,speed, and back
        board_rect=(FRAME_WIDTH/2-40,FRAME_HEIGHT/2-50,80,40)
        speed_rect=(FRAME_WIDTH/2-40,FRAME_HEIGHT/2+10,80,40)
        back_rect=(FRAME_WIDTH/2-40,FRAME_HEIGHT/2+70,80,40)

        # draw buttons
        self.draw_button(board_rect,"Board",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(speed_rect,"Speed",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(back_rect,"Back",(0,0,0),FONT_SIZE,(0,180,0))

        # update display
        pygame.display.update()

        
        while True:
            for event in pygame.event.get():
                # if user exits, terminate
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                # if mouse button is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get mouse cursor position
                    pos=pygame.mouse.get_pos()

                    # case board pressed, display board menu then options menu
                    if self.check_pressed(pos,board_rect):
                        self.board_menu()
                        self.options_menu()
                        return
                    # if speed pressed, display speed menu then options menu
                    elif self.check_pressed(pos,speed_rect):
                        self.speed_menu()
                        self.options_menu()
                        return
                    # if back is pressed, return, so that the main menu will be displayed again
                    elif self.check_pressed(pos,back_rect):
                        return
        

    
    def board_menu(self):
        """ Board choosing menu"""

        # load, rescale, and display background
        background=pygame.image.load(BACKGROUND)
        background=pygame.transform.scale(background, (FRAME_WIDTH,FRAME_HEIGHT+BAR))
        self.surface.blit(background,(0,0))

        # draw the arrows to notify user how to  navigate boards
        self.draw_arrows()

        # load the three default boards, rescale them, and put them in the boards list below
        boards=[]
        
        board=pygame.image.load(BOARD1)
        board=pygame.transform.scale(board, (FRAME_WIDTH-100,FRAME_HEIGHT-100))
        boards.append(board)

        board=pygame.image.load(BOARD2)
        board=pygame.transform.scale(board, (FRAME_WIDTH-100,FRAME_HEIGHT-100))
        boards.append(board)

        board=pygame.image.load(BOARD3)
        board=pygame.transform.scale(board, (FRAME_WIDTH-100,FRAME_HEIGHT-100))
        boards.append(board)


        # use this list to store captions to be printed under each board, respecting order.
        captions=["Classic","Borders","Complex"]


        # assign rects to buttons: ok,custom board, caption, and index.
        ok_rect=(FRAME_WIDTH-65,FRAME_HEIGHT-25,35,25)
        custom_rect=(FRAME_WIDTH/2+150,FRAME_HEIGHT-25,150,25)
        caption_rect=(FRAME_WIDTH/2-48,FRAME_HEIGHT-40,96,25)
        index_rect=(FRAME_WIDTH/2-30,FRAME_HEIGHT-10,60,25)

        # draw ok and custom buttons
        self.draw_button(ok_rect,"Ok",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(custom_rect,"Custom Board",(0,0,0),FONT_SIZE,(0,180,0))

        # this variable will store the user choice, as the index corresponding to the board in the boards list. (0,1, or 2)
        index=0
        while True:
            for event in pygame.event.get():
                # if user quit, terminate
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                # if keyboard button is pressed
                if event.type == pygame.KEYDOWN:
                    # if left arrow is pressed, change the index as: 2->1->0->2...
                    if event.key == pygame.K_LEFT:
                        index=(index+2)%3

                    # if right arrow is pressed, change index as : 0->1->2->0...
                    if event.key == pygame.K_RIGHT:
                        index=(index+1)%3
                # if mouse button is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get mouse cursor position
                    pos=pygame.mouse.get_pos()
                    # if ok is pressed, save the chosen board and return
                    if self.check_pressed(pos,ok_rect):
                        self.board=self.assign_board(index)
                        return
                    # if custom board is pressed, call the custom board menu and return
                    if self.check_pressed(pos,custom_rect):
                        self.user_board()
                        return

            # display the chosen board
            self.surface.blit(boards[index],(50,50))

            # draw the caption button with specified caption according to index
            self.draw_button(caption_rect,captions[index],(0,0,0),FONT_SIZE,(0,180,0))
            # draw the index button, with a number between 1 and 3 ( use +1 to change 0 1 2 to 1 2 3 just for display)
            self.draw_button(index_rect,"<{}/3>".format(index+1),(0,0,0),FONT_SIZE,(0,180,0))
            # update display
            pygame.display.update()
        
    def speed_menu(self):
        """choosing speed parameters menu"""
        
        # load, rescale, and display background
        background=pygame.image.load(BACKGROUND)
        background=pygame.transform.scale(background, (FRAME_WIDTH,FRAME_HEIGHT+BAR))
        self.surface.blit(background,(0,0))

        # assign rects to buttons: "+" buttons (p1 and p2), "-" buttons (m1 and m2), and value buttons (e1 and e2),  for speed and increment.
        m1_rect=(FRAME_WIDTH/2+80,200,20,25)
        p1_rect=(FRAME_WIDTH/2+105,200,20,25)
        e1_rect=(FRAME_WIDTH/2+30,200,30,25)
        m2_rect=(FRAME_WIDTH/2+80,250,20,25)
        p2_rect=(FRAME_WIDTH/2+105,250,20,25)
        e2_rect=(FRAME_WIDTH/2+30,250,30,25)
        # assign rects to buttons: back, speed, and increment.
        back_rect=(FRAME_WIDTH/2-30,FRAME_HEIGHT-30,60,25)
        speed_rect=(FRAME_WIDTH/2-150,200,200,25)
        inc_rect=(FRAME_WIDTH/2-150,250,200,25)

        # draw buttons
        self.draw_button(m1_rect,'-',(0,0,0),FONT_SIZE,(160,160,160))
        self.draw_button(m2_rect,'-',(0,0,0),FONT_SIZE,(160,160,160))
        self.draw_button(p1_rect,'+',(0,0,0),FONT_SIZE,(160,160,160))
        self.draw_button(p2_rect,'+',(0,0,0),FONT_SIZE,(160,160,160))
        self.draw_button(e1_rect,str(self.initial_speed),(0,0,0),FONT_SIZE,(255,255,255))
        self.draw_button(e2_rect,str(self.speed_increment),(0,0,0),FONT_SIZE,(255,255,255))
        
        self.draw_button(back_rect,"Back",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(speed_rect,"Initial Speed",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(inc_rect,"Speed Increment",(0,0,0),FONT_SIZE,(0,180,0))

        # update display
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                # if user exits, terminate
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                # if mouse button is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get mouse cursor position
                    pos=pygame.mouse.get_pos()
                    # check pressing and perform the necessary changes. When a value reaches limits, changes will happen.
                    if self.check_pressed(pos,m1_rect):
                        if(self.initial_speed>SPEED_LIMIT[0]):
                            self.initial_speed-=1
                    elif self.check_pressed(pos,p1_rect):
                        if(self.initial_speed<SPEED_LIMIT[1]):
                            self.initial_speed+=1
                    elif self.check_pressed(pos,m2_rect):
                        if(self.speed_increment>INC_LIMIT[0]):
                            self.speed_increment-=1
                    elif self.check_pressed(pos,p2_rect):
                        if(self.speed_increment<INC_LIMIT[1]):
                            self.speed_increment+=1
                    # if back is pressed, return, so the options menu will re-appear
                    elif self.check_pressed(pos,back_rect):
                        return


            # print the new initial speed value which was modified by user pressing + or -
            self.draw_button(e1_rect,str(self.initial_speed),(0,0,0),FONT_SIZE,(255,255,255))

            # if the minimum speed limit is not yet reached, draw the minus button with grey, else draw it with red
            if self.initial_speed!=SPEED_LIMIT[0]:
                self.draw_button(m1_rect,'-',(0,0,0),FONT_SIZE,(160,160,160))
            else:
                self.draw_button(m1_rect,'-',(0,0,0),FONT_SIZE,(255,0,0))

            # if the maximum speed limit is not yet reached, draw the plus button with grey, else draw it with red
            if self.initial_speed!=SPEED_LIMIT[1]:
                self.draw_button(p1_rect,'+',(0,0,0),FONT_SIZE,(160,160,160))
            else:
                self.draw_button(p1_rect,'+',(0,0,0),FONT_SIZE,(255,0,0))


            # print the new initial speed value which was modified by user pressing + or -
            self.draw_button(e2_rect,str(self.speed_increment),(0,0,0),FONT_SIZE,(255,255,255))

            # if the minimum speed increment limit is not yet reached, draw the minus button with grey, else draw it with red
            if self.speed_increment!=INC_LIMIT[0]:
                self.draw_button(m2_rect,'-',(0,0,0),FONT_SIZE,(160,160,160))
            else:
                self.draw_button(m2_rect,'-',(0,0,0),FONT_SIZE,(255,0,0))

            # if the maximum speed increment limit is not yet reached, draw the plus button with grey, else draw it with red
            if self.speed_increment!=INC_LIMIT[1]:
                self.draw_button(p2_rect,'+',(0,0,0),FONT_SIZE,(160,160,160))
            else:
                self.draw_button(p2_rect,'+',(0,0,0),FONT_SIZE,(255,0,0))

            # update display
            pygame.display.update()

        
    def user_board(self):
        """ this is the menu of custom board drawing"""

        # load, rescale, and display background
        background=pygame.image.load(BACKGROUND)
        background=pygame.transform.scale(background, (FRAME_WIDTH,FRAME_HEIGHT+BAR))
        self.surface.blit(background,(0,0))

        # assign rect to the area in which the user will draw custom board
        filling_rect=(FRAME_WIDTH/4,FRAME_HEIGHT/4,FRAME_WIDTH/2,FRAME_HEIGHT/2)
        # assign rects to buttons: confirm and reset
        confirm_rect=(FRAME_WIDTH/2-100,3*FRAME_HEIGHT/4+135,90,25)
        reset_rect=(FRAME_WIDTH/2+10,3*FRAME_HEIGHT/4+135,80,25)
        # assign rect to the snake position, the user is not permitted to draw in this area
        snake_rect=(BODY_PARTS[0][0]/2+FRAME_WIDTH/4,BODY_PARTS[0][1]/2+FRAME_HEIGHT/4,5*6,5)
        # assign rects to two lines of comment, telling the user how to draw
        comment1_rect=(FRAME_WIDTH/2-200,3*FRAME_HEIGHT/4+10,0,0)
        comment2_rect=(FRAME_WIDTH/2-200,3*FRAME_HEIGHT/4+30,0,0)

        # draw buttons
        self.draw_button(filling_rect,"",(0,0,0),FONT_SIZE,(255,255,255))
        self.draw_button(confirm_rect,"Confirm",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(reset_rect,"Reset",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(snake_rect,"",(0,0,0),FONT_SIZE,(0,255,0))
        self.draw_button(comment1_rect,"Left click and hold to generate obstacles",(0,0,0),FONT_SIZE,(0,180,0),True)
        self.draw_button(comment2_rect,"Right click and hold to remove obstacles",(0,0,0),FONT_SIZE,(0,255,0),True)

        # update display
        pygame.display.update()

        # initialize the list that will store the obstacles positions drawn by the user.
        # NOTE: the list will store the scaled positions of obstacles. The drawing area is half-size of the game frame, and translated right and down.
        #       when saving the list to self.board, the positions are re scaled: multiplied by 2 and translated back left and up.
        
        listt=[]
        # this variable will be used to keep track of the mouse state; if the user is holding the mouse button or not
        hold=False
        
        while True:
            for event in pygame.event.get():
                # if user exits, terminate
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                # if mouse button is pressed, set hold to true. hold will stay true unless the mouse button is released
                if event.type == pygame.MOUSEBUTTONDOWN:
                    hold=True

                # if the mouse button is released, set hold to false.
                if event.type == pygame.MOUSEBUTTONUP:
                    hold=False

                # if the mouse is pressed
                if hold:
                    # get position of mouse cursor
                    pos=pygame.mouse.get_pos()
                    # if reset button is pressed
                    if self.check_pressed(pos,reset_rect):
                        # clear the list of obstacles
                        listt=[]
                        # fill the drawing area with white(i.e. erasing)
                        self.draw_button(filling_rect,"",(0,0,0),FONT_SIZE,(255,255,255))
                        # re-draw the snake 
                        self.draw_button(snake_rect,"",(0,0,0),FONT_SIZE,(0,255,0))

                    # if confirm is pressed, store the list in self.board, and return. (remember to rescale and translate)
                    elif self.check_pressed(pos,confirm_rect):
                        self.board=[(2*b[0]-FRAME_WIDTH/2,2*b[1]-FRAME_HEIGHT/2) for b in listt]
                        return

                    # round the mouse pos to the nearest multiple of s, where s is half part size. ( in order to treat positions in the drawing area as discrete)
                    s=PART_SIZE/2
                    pos=(s*int(pos[0]/s),s*int(pos[1]/s))
                    
                    # if the user is pressing inside the drawing area, and not in the snake area, take suitable action.
                    if self.check_pressed(pos,(filling_rect[0],filling_rect[1],filling_rect[2]-5,filling_rect[3]-5)) and not self.check_pressed(pos,(snake_rect[0],snake_rect[1],snake_rect[2]-5,snake_rect[3]-5)):
                        
                        # get_pressed method is a pygame built-in method to know which mouse button is pressed. it returns tuple of three bools: (left_click,middle,right_click)
                        
                        # if left click
                        if pygame.mouse.get_pressed()[0]:
                            # if the position clicked is not yet in the list, fill it black and add it to the list
                            if pos not in listt:
                                self.surface.fill((0,0,0),rect=(pos[0],pos[1],5,5))
                                listt.append(pos)

                        # if right click
                        elif pygame.mouse.get_pressed()[2]:
                            # if the obstacle clicked is in the list, fill the position with white and remove it from the list
                            if pos in listt:
                                self.surface.fill((255,255,255),rect=(pos[0],pos[1],5,5))
                                listt.remove(pos)
                
                # update display
                pygame.display.update()


    def game_over(self,score,time_elapsed):
        """Game over screen, showing cscore and time"""

        # for better animation, delay 3 seconds when the user loses
        time.sleep(2)
        # load the gameover sound
        game_over_sound=pygame.mixer.Sound(OVERSOUND)
        # play the sound
        pygame.mixer.Sound.play(game_over_sound)

        # load,rescale, and display background
        background=pygame.image.load(BACKGROUND)
        background=pygame.transform.scale(background, (FRAME_WIDTH,FRAME_HEIGHT+BAR))
        self.surface.blit(background,(0,0))

        # assign rects to : game over text, score text, time text, and "play again" and "main menu" buttons
        game_over_rect=(FRAME_WIDTH/4-40,FRAME_HEIGHT/4,0,0)
        score_rect=(FRAME_WIDTH/2-70,1.2*FRAME_HEIGHT/3+20,0,0)
        time_rect=(FRAME_WIDTH/2-70,1.2*FRAME_HEIGHT/3+20+25+20,0,0)
        again_rect=(FRAME_WIDTH/4+60,0.6*FRAME_HEIGHT,120,25)
        menu_rect=(FRAME_WIDTH/4+220,0.6*FRAME_HEIGHT,120,25)

        # draw buttons
        self.draw_button(game_over_rect,"Game Over!",(180,0,0),4*FONT_SIZE,(0,0,0),True)
        self.draw_button(score_rect,"Your Score: {}".format(score),(0,0,0),FONT_SIZE,(0,180,0),True)
        self.draw_button(time_rect,"Time: {}".format(time_elapsed),(0,0,0),FONT_SIZE,(0,180,0),True)
        self.draw_button(again_rect,"Play Again",(0,0,0),FONT_SIZE,(0,180,0))
        self.draw_button(menu_rect,"Main Menu",(0,0,0),FONT_SIZE,(0,180,0))

        # update display
        pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                # if use exits, terminate
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                # if mouse button is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get mouse cursor position
                    pos=pygame.mouse.get_pos()
                    # if main menu is pressed, return false. this will assign false to the variable "play_again" defined in "main_menu" function.
                    if self.check_pressed(pos,menu_rect):
                        return False
                    # if play again is pressed, return true. this will assign true to the variable "play_again" defined in "main_menu" function.
                    if self.check_pressed(pos,again_rect):
                        return True
