import pgzrun

HEIGHT = 700
WIDTH = 1200
w, h = WIDTH, HEIGHT

music.play('remix')

P = Actor('ironman',(w//2, h//2))
e = Actor('alien',(w//2,  200))
c = Actor('coin',(w//2, h-100))


def draw ():
    screen.fill('yellow')
    P.draw()
    e.draw()
    c.draw()

def player_update():
    if keyboard.left:
        P.x -=5
    elif keyboard.right: 
        P.x +=5  
    elif keyboard.up: 
        P.y -=5  
    elif keyboard.down: 
        P.y +=5         

def enemy_update ():
    e.x += 5
    if e.x > w:
        e.x = 0

def update ():
    enemy_update()
    player_update()

pgzrun.go()