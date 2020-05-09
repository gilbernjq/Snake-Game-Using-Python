FONT_SIZE=20 # change font according to your OS for good display. Apparently, 30 for linux and 20 for windows are perfect.

FRAME_WIDTH=800
FRAME_HEIGHT=600
PART_SIZE=10    # size of each body part; square of side size PART_SIZE in pixels
BAR=30 # height of the bottom bar in which time and score are printed


BLOCK_IMAGE="ball.png"
FOOD_IMAGE="food.png"
BACKGROUND="back.jpg"   
INSTRUCTIONS="instructions.png"
# images for the three boards to choose from
BOARD1="b1.png"
BOARD2="b2.png"
BOARD3="b3.png"

# inital speed limits
SPEED_LIMIT=(1,30)
# speed increment limits
INC_LIMIT=(0,3)
# starting body parts locations of the snake.
BODY_PARTS=[(100,500),(110,500),(120,500),(130,500),(140,500),(150,500)]

STARTSOUND="start.wav"
GROWSOUND="grow.wav"
HITSOUND="hit.wav"
OVERSOUND="gameOver.wav"
