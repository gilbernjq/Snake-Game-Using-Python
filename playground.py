from parameters import*
import pygame
import time
from random import choice
import sys

class playground:
    """Class representing the enviroment where the snake is moving."""
    def __init__(self,snake,game_display):
        """
        Initializing the enviroment.
        Args:
        snake: snake object.

        game_display: pygame object used for visualization
        
        """
        
        
        self.snake=snake
        
        # initiate the variable holding the display object; used for displaying
        self.game_display = game_display

        # initiate the variable holding the coordinates of obstacles
        self.obstacles=[]

        # initiate the variable holding the coordinates of food
        self.food=None

        # This time variable is used for visualization of the snake speed
        self.time=pygame.time.get_ticks()

        # this time variable is used for printing the time elapsed
        self.start_time=self.time
        
        self.block_image = pygame.image.load(BLOCK_IMAGE)
        self.food_image=pygame.image.load(FOOD_IMAGE)
        
        # this variable is used for storing the obstacle hit by the snake ( and then game is over)
        self.hit_block=None
        
    def generate_food(self):
        """Generates a random valid block as a food portion."""

        # initiate an empty list to be packed with available possible food locations
        to_choose_from=[]
        
        for i in range(0,FRAME_WIDTH,PART_SIZE):
            for j in range(0,FRAME_HEIGHT,PART_SIZE):
                # iterating over the whole frame by stepping coordinates with a step of PART_SIZE, and add a possible location for the food after excluding snake body parts and obstacles
                if (i,j) not in self.obstacles and (i,j) not in self.snake.body:
                    to_choose_from.append((i,j))
                    
        # assign a location for the food randomly from possible locations
        self.food=choice(to_choose_from)


    def update_snake_orientation(self,orientation):
        """
        Updates the snake orientation, to visualize turns.
        args:
        orientation: a letter R,L,U, or D corresponding to the new direction of motion.
        """
        
        self.snake.orientation=orientation

    def add_obstacles(self,list_of_obstacles):
        """Takes a list of obstacles and adds them"""
        
        self.obstacles=list_of_obstacles
    
    def update(self,turning=False):
        """
        Updates the frame properies of the game.
        args:
        turning: this boolean is used to know if this update will be an auto-update(just moving according to time) or update due to user input( to turn)
                 It is false by default. If set true, the update will happen instantly without waiting for the specific time duration specified according
                 to snake speed.
        """

        # font to use for printing time
        font = pygame.font.SysFont('Consolas', FONT_SIZE)
        
        # in case a duration of time compatible with the snake's speed has been passed, or in case the "turning" flag is true
        if pygame.time.get_ticks()-self.time>1000/self.snake.speed or turning:

            # case the snake reached a food portion
            if self.snake.get_new_head()==self.food:
                # load the growing sound       
                grow_sound=pygame.mixer.Sound(GROWSOUND)
                # start playing the sound
                pygame.mixer.Sound.play(grow_sound)
                # draw the new head on the food portion
                self.game_display.blit(self.block_image, self.food)
                # modify the snake body
                self.snake.grow()
                # generate new food
                self.generate_food()
                # draw new food
                self.game_display.blit(self.food_image,self.food)
                
                # update the score
                # fill the location of the score text with green (to erase)
                self.game_display.fill((0,255,0),rect=(100, FRAME_HEIGHT+7,150,20))
                # print new score. the score is the amount of food eaten, so it is snake body size minus initial size (6)
                self.game_display.blit(font.render("Score: {}".format(len(self.snake.body)-6), True, (0,0,0)), (100, FRAME_HEIGHT+7))

            # case the snake is hitting an obstacle or itself
            elif self.snake.get_new_head() in (self.obstacles+self.snake.body):
                # update the hit_block variable and store the hit block
                self.hit_block=self.snake.get_new_head()
                # draw a red circle on the hit block
                pygame.draw.circle(self.game_display,(255,0,0),(self.hit_block[0]+5,self.hit_block[1]+5),5)
            
            # case no growth and no obstacle hit
            else:
                # move the snake and get the tail
                tail=self.snake.move()
                # draw the new head
                self.game_display.blit(self.block_image, self.snake.body[-1])
                # erase the tail by filling its location with white
                self.game_display.fill((255,255,255),rect=(tail[0],tail[1],10,10))
                
            # reset timer to the current time
            self.time=pygame.time.get_ticks();


        # get the time elapsed ,which is current time minus start time. Transform it to seconds while keeping one decimal place after the point
        text=str(int((pygame.time.get_ticks()-self.start_time)/100)/10)

        # fill teh location of the time text with green (to erase)
        self.game_display.fill((0,255,0),rect=(FRAME_WIDTH-200, FRAME_HEIGHT+7,150,20))
        # print the time elapsed
        self.game_display.blit(font.render("Time: "+text, True, (0,0,0)), (FRAME_WIDTH-200, FRAME_HEIGHT+7))

        # this is called to update all display modifications done
        pygame.display.update()
        
    def visualize(self):
        """Displays the entire frame of the game. This function is used once, at the start."""
        
        font = pygame.font.SysFont('Consolas', FONT_SIZE)
        # fill the screen entirely with white
        self.game_display.fill((255,255,255))
        # draw a border of 1 pixel thickness to divide the screen as the playing screen and the bar on which time and score will be printed
        self.game_display.fill((0,0,0),rect=(0,FRAME_HEIGHT,FRAME_WIDTH,1))
        # draw each block in the snake's body
        for block in self.snake.body:
            self.game_display.blit(self.block_image, block)
        # draw each obstacle
        for obs in self.obstacles:
            self.game_display.fill((0,0,0),rect=(obs[0],obs[1],10,10))

        # draw the food portion
        self.game_display.blit(self.food_image,self.food)

        # fill the bottom bar with green
        self.game_display.fill((0,255,0),rect=(0, FRAME_HEIGHT+1,FRAME_WIDTH,29))
        # print the score initially zero
        self.game_display.blit(font.render("Score: {}".format(len(self.snake.body)-6), True, (0,0,0)), (100, FRAME_HEIGHT+7))
    
    def play(self):
        """ This is where the game starts"""


        # load the starting game sound       
        start_sound=pygame.mixer.Sound(STARTSOUND)
        # start playing the sound
        pygame.mixer.Sound.play(start_sound)
        # define a font for the 3,2,1,GO 
        font = pygame.font.SysFont('Consolas', 10*FONT_SIZE)
        # loop to display the starting screen(3,2,1)
        for i in range(3):
            # delay 1 sec
            time.sleep(1)
            # display obstacles, food, snake...
            self.visualize()
            # display integer 3 or 2 or 1
            self.game_display.blit(font.render(str(3-i), True, (255,0,0)), (FRAME_WIDTH/3+100, FRAME_HEIGHT/3))
            # update display
            pygame.display.update()
        # delay 1 sec
        time.sleep(1)
        # display obstacles, food, snake...
        self.visualize()
        # display the GO! and update display
        self.game_display.blit(font.render("Go!", True, (255,0,0)), (FRAME_WIDTH/3, FRAME_HEIGHT/3))
        pygame.display.update()
        # delay 1 sec
        time.sleep(1)
        # display obstacles, food, snake... Again and update
        self.visualize()
        pygame.display.update()
        # stop the sound
        pygame.mixer.music.stop()
        # add 5 seconds to the starting time, in order to display the timer correctly
        self.start_time+=5000

        
        # variable used to store the state of the game.(paused, unpaused)
        paused=False

        # this time variable is used to stop time counting when the game is paused. it stores the instant when the game is paused.
        paused_instant=0
        # iterate indefinitly unless the user quits or loses
        while True:

            # check if the snake hit obstacle or itself. If yes, return the current score and time elapsed
            if self.hit_block:
                # load the hit sound       
                hit_sound=pygame.mixer.Sound(HITSOUND)
                # start playing the sound
                pygame.mixer.Sound.play(hit_sound)
                
                return str(len(self.snake.body)-6),str(int((pygame.time.get_ticks()-self.start_time)/100)/10)

            
            # iterate for every event
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # case of quitting event, terminate pygame and return
                    sys.exit(0)
                
                # event type keydown means a keyboard key is pressed
                # note that updating directions from right to left immediately
                # is forbidden, the same for up to down.
                if event.type == pygame.KEYDOWN:
                    # take user arrows input just in case the game is not paused
                    # recall that true argument is passed to update instantly (turning=True now)
                    if not paused:
                        if event.key == pygame.K_LEFT:
                            if self.snake.orientation in 'UD':
                                self.update_snake_orientation('L')
                                self.update(True)
                        elif event.key == pygame.K_RIGHT:
                            if self.snake.orientation in 'UD':
                                self.update_snake_orientation('R')
                                self.update(True)
                        elif event.key == pygame.K_UP:
                            if self.snake.orientation in 'RL':
                                self.update_snake_orientation('U')
                                self.update(True)
                        elif event.key == pygame.K_DOWN:
                            if self.snake.orientation in 'RL':
                                self.update_snake_orientation('D')
                                self.update(True)
                    # if P is pressed, pause or unpause the game
                    if event.key == pygame.K_p:
                        # invert the paused variable state
                        paused= not paused
                        # if pausing now, store the paused instant variable
                        if paused:
                            paused_instant=pygame.time.get_ticks()
                        # if unpausing now, increase the start time variable by the amount of pausing duration; to keep a continuos time running on the screen.
                        else:
                            self.start_time+=pygame.time.get_ticks()-paused_instant
            # case game unpaused, update by moving the snake(no True flag, this update is automatic and thus it will happen according to the snake speed.
            if not paused:
                self.update()
