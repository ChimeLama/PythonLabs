import play #loading the  play library 
import random #loading the random libray
#determing a constatt court's width and height
w=300 #determing global variable for horizontal size of court
h=400 #determing global variable for vertical size of court
#determine a constatnt for the middle of the court
halfWidth=w/2 #defining the global variable for half width/height of court
halfHeight=h/2
#defining global variable for the begining score
score=0
#defining global variable for the speed of ball
speed=3
@play.when_program_starts #creates a keyframe to start the game
def do(): #defininf or initializing the function DO
  play.set_backdrop((0,0,0))#sets bg color
court=play.new_box( #declaring the variable that will be the play field (play) calls the library (.) query for a prebuild function (new_box) the prebuild function to create rectangles
  color="red", #initializin the parameter for color to be red
  x=0,#initializing x value (horizontal) coordinates
  y=0, #initializing y value (vertical) coordinates
  width = w, #initializing the width to the pre set value  'w'
  height= h, #initializing the height to the pre set value  'h'
)#close the parameters

ball=play.new_circle( #declaring the variable to hold a function for circle
  color="yellow",#initializing the parameter for the color to be yellow
  x=0, #initializing x value (horizontal) coordinates
  y=halfHeight -30, #initializing the Y with the halfHeight - 30
   radius=10,#initializing the parameter radius of the play circle to be '10'
  angle= random.randint(210,330) #initializing the bouncing angle
)#parenthasis closes parmeter
paddle=play.new_box(#declaring the variable to hold a function for paddle box
  color="green",#initializing the parameter for the color to be green
  width= 50,#initializing the width to the value '50'
  height= 10, #initializing the height to the value '10'
  x=0,#initialize the x value(horizontal) coordinates
  y=-190,#initialize the y value(vertical) coordinates
)#close the parameters

scoretext= play.new_text(#declares the variable to hold a text
  color="white",#initializing the text color to be white
  words="Score: " + str(score),#initializes the word 'score' to be represented by the str((score(an int)))
  x=0,#initialize the x value(horizontal) coordinates
  y=halfHeight + 15,#initializing the Y with the halfHeight + 15
  font_size =40, #initializing the text font size to be 40
)
@play.repeat_forever #creates a kewyframe to make the following program run as long as the game is playing
#declare a padle movement
def do():
  global score #calling for the global variable score
  paddle.x= play.mouse.x #Dot b=notation to recall the x parameterof paddle to reassign value to match the mouse
  #to ensure the paddle isn't off the court
  if (play.mouse.x< -halfWidth + paddle.width/2):#left side
      paddle.x=-halfWidth+paddle.width/2
  if (play.mouse.x>halfWidth -paddle.width/2):#right side
     paddle.x=halfWidth-paddle.width/2
    
  ball.move(speed)
#create bounce
  #top wall
  if(ball.y+ball.radius >halfHeight):
    ball.angle= 360-ball.angle
    #bottom wall
  if(ball.y - ball.radius < -halfHeight):
    ball.angle = 360 - ball.angle
    score -=1 # another way score = score -1
    #bounce off left/riht :180 - angle
    #right wall
  if(ball.x+ball.radius > halfWidth):
     ball.angle=180-ball.angle
    #left wall
  if(ball.x-ball.radius< -halfWidth):
     ball.angle=180 -ball.angle
#make it bounce as if it hit the bottom and give it a littlw change of trajectory
  if(ball.is_touching(paddle)):
      ball.angle=360-ball.angle+random.randint(-30,30)
      ball.angle %= 360 #ensures angle is valid
  #make sure tha ball goes up after hitting the paddle
      if(ball.angle<20):
       ball.angle =20
      elif(ball.angle> 160):
        ball.angle=160
      score +=1
      if(score==5):
         paddle.width -= 5
  ball.angle%= 360#ensure angle valid
  scoretext.words=" SCORE: " + str(score)


@play.repeat_forever
def mouse_coords():
  mouse_text.go_to(play.mouse)
  mouse_text.words = str(int(play.mouse.x)) + "," + str(int(play.mouse.y))

mouse_text=play.new_text(
 color="white",
  words="white",
  x=0,
  y=0,
  font_size =20,
)


play.start_program()