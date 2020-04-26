PART_SIZE=10  # size of each body part, a square of side PART_SIZE, in pixels

FRAME_WIDTH=800

FRAME_HEIGHT=600

SPEED_INCREMENT=1
class snake:
    """Class representing a snake in the Snake-Game."""
    def __init__(self,initial_speed,initial_orientation,body_parts):
        """
        Initialize the Snake object.
        Args:
        initial_speed: initial speed set for the snake, in blocks per second.
        
        initial_orientation: initial direction for the snake, can be any of the four directions Left,Right,Up, or Down.
        
        body_parts: body blocks constituting the snake. It is list of tuples representing the x and y
                    coordinates of each block from tail to head.
        """
        self.body=body_parts
        self.speed=initial_speed
        self.orientation=initial_orientation
    
    def __str__(self):
        return("Snake object of size {}, a speed of {}, and direction {}.\n"
              .format(
                  len(self.body),
                  self.speed,
                  self.orientation,))
    
    def get_new_head(self):
        """Returns the new head position of the snake, based on the current orientation (Under construction)"""

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

        new_head=((new_head[0]+FRAME_WIDTH)%FRAME_WIDTH,(new_head[1]+FRAME_HEIGHT)%FRAME_HEIGHT)

        return new_head
        
    def move(self):
        """Performs movement of a single step of the snake, by inserting the new head and poping the tail (Under construction)"""

        # new head coordinates
        new_head=self.get_new_head() 

        # take out the tail
        self.body.pop(0)

        # append the new head
        self.body.append(new_head)

    def grow(self):

        new_head=self.get_new_head()

        self.body.append(new_head)

        self.speed+=SPEED_INCREMENT
