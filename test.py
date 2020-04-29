
from snake import*
from playground import*



body_parts=[(400,300),(410,300),(420,300),(430,300),(440,300),(450,300)]
my_snake=snake(INITIAL_SPEED,'R',body_parts)
play=playground(my_snake)

listt=[]
for i in range(0,800,10):
    if i not in range(350,450):
        listt.append((i,0))
        listt.append((i,590))
for i in range(10,600,10):
    if i not in range(250,350):
        listt.append((0,i))
        listt.append((790,i))
        
play.add_obstacles(listt)
play.play()
