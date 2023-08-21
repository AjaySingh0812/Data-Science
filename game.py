import pgzrun
from random import randint

HEIGHT=600
WIDTH=700
w,h=WIDTH,HEIGHT
music.play('remix')

p=Actor('ironman',(w//2,h//2))
e=Actor('alien',(w//2,200))
c=Actor('coin',(w//2,h-100))
score=0

game_state=0
def draw():
    if game_state==0:
        screen.fill('black')
        p.draw()
        e.draw()
        c.draw()
        screen.draw.text(f'Score:{score}',(10,10),color='white')
    
    elif game_state==1:
        screen.draw.text(f'Game Over',(w//2,h//2),color='red')
    
    elif game_state==2:
        screen.draw.text(f'You Win',(w//2,h//2),color='green')

def player_update():
    if keyboard.left:
        p.x-=10
        if p.x > w:
            p.x=0
        
    elif keyboard.right:
        p.x+=10
    elif keyboard.up:
        p.y-=10
        if p.y > h:
            p.y=0
    elif keyboard.down:
        p.y+=10


def enemy_update():
    if c.x > e.x:
        e.x += 3
    if c.x < e.x:
        e.x -= 3
    if c.y > e.y:
        e.y += 3
    if c.y < e.y :
        e.y -= 3
    if e.colliderect(p):
        p.x=w//2
        p.y=h//2
def score_update():
    global score
    if p.colliderect(c):
        score+=10
        c.x=randint(0,w)
        c.y=randint(0,h)
        sounds.action.play()
    if e.colliderect(c):
        score-=10
        c.x=randint(0,w)
        c.y=randint(0,h)
        sounds.action.play()
def update():
    if game_state==0:
        enemy_update()
        player_update()
        score_update()
pgzrun.go()