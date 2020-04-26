import pygame
from random import choice


INITIAL_SPEED=20

FRAME_WIDTH=800

FRAME_HEIGHT=600

BLOCK_IMAGE="ball.png"

FOOD_IMAGE="food.png"



class playground:
    """Class representing the enviroment where the snake is moving."""
    def __init__(self,snake):
        """
        Initializing the enviroment.
        snake: snake object.
        """
        pygame.init()
        pygame.display.set_caption('SNAKE-GAME Gilberto Jimenez 00261433')
        
        self.obstacles=[]
        self.snake=snake
        self.score=len(snake.body)
        
        # initialize a variable for storing current time. Will be used to animate the snake's speed.
        
        self.time=pygame.time.get_ticks()
        self.start_time=self.time
        self.block_image = pygame.image.load(BLOCK_IMAGE)
        self.food_image=pygame.image.load(FOOD_IMAGE)
        
        self.generate_food()

        # initiate the variable holding the display object; used for displaying
        self.game_display = pygame.display.set_mode((FRAME_WIDTH,FRAME_HEIGHT))

        # initiate the clock object that manages the framerate of the game
        self.clock = pygame.time.Clock()
        
        
    def __str__(self):
        return("{} by {} frame".format(FRAME_WIDTH,FRAME_HEIGHT))
    
    def generate_food(self):
        """Generates a random valid block as a food portion."""

        # initiate an empty list for food locations
        to_choose_from=[]
        
        for i in range(0,FRAME_WIDTH,10):
            for j in range(0,FRAME_HEIGHT,10):
                # iterating over the whole frame, add a possible location for the food after excluding snake body parts and frame obstacles Under construction
                if (i,j) not in self.obstacles and (i,j) not in self.snake.body:
                    to_choose_from.append((i,j))
                    
        #assign a location for the food randomly
        self.food=choice(to_choose_from)
        #self.food=(10*int(self.food[0]/10),10*int(self.food[1]/10))


    def update_snake_orientation(self,orientation):
        """
        Updates the snake orientation, to visualize turns.
        args:
        orientation: a letter R,L,U, or D corresponding to the new direction of motion.
        """
        self.snake.orientation=orientation

    
    def update(self):
        """ Updates the frame properies of the game."""

        # in case a duration of time compatible with the snake's speed has been passed
        if pygame.time.get_ticks()-self.time>1000/self.snake.speed:

            if self.snake.get_new_head()==self.food:
                self.snake.grow()
                self.generate_food()
            else:
                # move the snake
                self.snake.move()
            # reset timer to the current time
            self.time=pygame.time.get_ticks();

        # display the frame by calling a class method and updating pygame display
            self.visualize()
            pygame.display.update()
        
    def visualize(self):
        """ Displays the entire frame of the game"""

        # fill the screen entirely with white
        self.game_display.fill((255,255,255))

        # draw each block in the snake's body
        for block in self.snake.body:
            self.game_display.blit(self.block_image, block)

        # draw the food portion
        self.game_display.blit(self.food_image,self.food)
        text=str(int((pygame.time.get_ticks()-self.start_time)/10)/100)
        font = pygame.font.SysFont('Consolas', 30)
        self.game_display.blit(font.render(text, True, (0, 0, 0)), (650, 570))
    
    def play(self):
        """ This is where the game starts"""
        self.visualize()
        stop=False

        # iterate indefinitly unless the user quits
        while True:
            # iterate for every event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # case of quitting event, terminate pygame and return
                    return
                
                # even type keydown means a keyboard key is pressed
                # note that updating directions from right to left immediately
                # is forbidden, the same for up to down.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.snake.orientation in 'UD':
                            self.update_snake_orientation('L')
                    elif event.key == pygame.K_RIGHT:
                        if self.snake.orientation in 'UD':
                            self.update_snake_orientation('R')
                    elif event.key == pygame.K_UP:
                        if self.snake.orientation in 'RL':
                            self.update_snake_orientation('U')
                    elif event.key == pygame.K_DOWN:
                        if self.snake.orientation in 'RL':
                            self.update_snake_orientation('D')
                    elif event.key == pygame.K_p:
                         stop= not stop                    
                            
            #call update to move snake and visualize
            if not stop:
                self.update()
            self.clock.tick_busy_loop(60) # maintain a 60 fps display

