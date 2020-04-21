
from snake import*
from playground import*



body_parts=[(400,300),(411,300),(422,300),(433,300),(444,300),(455,300)]
my_snake=snake(INITIAL_SPEED,'R',body_parts)
play=playground(my_snake)
play.play()
