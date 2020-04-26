
from snake import*
from playground import*



body_parts=[(400,300),(410,300),(420,300),(430,300),(440,300),(450,300)]
my_snake=snake(INITIAL_SPEED,'R',body_parts)
play=playground(my_snake)
play.play()


