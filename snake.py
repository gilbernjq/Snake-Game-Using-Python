PART_SIZE=10  # size of each body part, a square of side PART_SIZE, in pixels
BETWEEN_PARTS=0 # distance between body parts in pixels
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
        shift=PART_SIZE+BETWEEN_PARTS

        #get the head coordinates
        head=self.body[-1]
        
        if self.orientation=='R':
            return (head[0]+shift,head[1])
        if self.orientation=='L':
            return (head[0]-shift,head[1])
        if self.orientation=='U':
            return (head[0],head[1]-shift)
        if self.orientation=='D':
            return (head[0],head[1]+shift)
        
    def move(self):
        """Performs movement of a single step of the snake, by inserting the new head and poping the tail (Under construction)"""

        # new head coordinates
        new_head=self.get_new_head() 

        # take out the tail
        self.body.pop(0)

        # append the new head
        self.body.append(new_head)
    
   