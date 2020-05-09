from parameters import *
class snake:
    """Class representing a snake in the Snake-Game."""
    def __init__(self,initial_speed,initial_orientation,speed_increment,body_parts):
        """
        Initialize the Snake object.
        Args:
        initial_speed: initial speed set for the snake, in blocks per second.
        
        initial_orientation: initial direction for the snake, can be any of the four directions Left,Right,Up, or Down.

        speed_increment: speed increment for each unit growth in size
        
        body_parts: body blocks constituting the snake. It is list of tuples representing the x and y
                    coordinates of each block from tail to head.
        """
        self.speed_inc=speed_increment
        self.body=body_parts
        self.speed=initial_speed
        self.orientation=initial_orientation
    
    def get_new_head(self):
        """Returns the new head position of the snake, based on the current orientation """

        # the shift in coordinates for a new head
        shift=PART_SIZE

        #get the head coordinates
        head=self.body[-1]
        
        if self.orientation=='R':
            new_head= (head[0]+shift,head[1])
        if self.orientation=='L':
            new_head= (head[0]-shift,head[1])
        if self.orientation=='U':
            new_head= (head[0],head[1]-shift)
        if self.orientation=='D':
            new_head= (head[0],head[1]+shift)

        # in case the movement is into frame borders, make the snake emerge from the opposite border
        new_head=((new_head[0]+FRAME_WIDTH)%FRAME_WIDTH,(new_head[1]+FRAME_HEIGHT)%FRAME_HEIGHT)

        return new_head
        
    def move(self):
        """Performs movement of a single step of the snake, by inserting the new head and poping the tail"""

        # new head coordinates
        new_head=self.get_new_head() 

        # append the new head
        self.body.append(new_head)

        # take out and return the tail
        return(self.body.pop(0))

    def grow(self):
        """Performs the act of growth of the snake, by inserting the new head and keeping the tail"""
        
        # new head coordinates
        new_head=self.get_new_head()

        # append the new head
        self.body.append(new_head)

        # increase speed
        self.speed+=self.speed_inc
        
