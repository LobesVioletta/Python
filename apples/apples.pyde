state = 0
img = 0
qaz=0
x=random(20,480)
y=random(20,480)
class Food:
    def __init__(self):
        self.x=random(0,500)
        self.y=random(0,500)
    def draw_(self):
        image(img, self.x,self.y,10,10)
    def move(self,x,y):
        self.x=x
        self.y=y
food=Food()
class Snake:
    def __init__(self):
        self.x = 250
        self.y = 250
    def draw_(self):
        image(img,self.x,self.y,15,15)
    def move(self, x,y):
        self.x+=x
        self.y+=y
snake = Snake()
def check_collide(x,y,w,h   , x1,y1):
    return x1 >= x and x1 <= x+w and y1 >= y and y1 <= y+h

def rectsCollision(x,y,w,h , x1,y1,w1,h1):
    return check_collide(x,y,w,h , x1,y1) or \
           check_collide(x,y,w,h , x1+w1,y1) or \
           check_collide(x,y,w,h , x1,y1+h1) or \
           check_collide(x,y,w,h , x1+w1,y1+h1)
def setup():
    global img ,gaz,wsx
    img = loadImage(u'морковь 2.jpg')
    qaz=loadImage(u'заяц.jpg')
    wsx=loadImage(u'трава.jpg')
    size(500,500)
def draw():
    global snake,food,x,y,state  
    fill(255)
    if state==0:
        fill(255)
        rect(130,150,250,100)
        fill(0)
        text("START",175,210)
        textSize(50)
        if keyPressed:
            if key==ENTER:
                state=1
    elif state==1:
        image(wsx,0,0,500,500)
        food.draw_()
        snake.draw_()
        if keyPressed:
            if keyCode==UP:
                snake.y-=5
            elif keyCode==DOWN:
                snake.y+=5
            if keyCode==LEFT:
                snake.x-=5
            elif keyCode==RIGHT:
                snake.x+=5
    if rectsCollision(snake.x ,snake.y, 15,15 , food.x ,food.y,8,8):
         food.x=random(20,480)
         food.y=random(20,480)
    if   snake.x>500 or snake.y >500  or snake.x< 0   or  snake.y <0 :
          state=0
          snake.x=250
          snake.y=250
          fill(255,0,0)
          textSize(30)
          text("GameOver",150,50)
          
