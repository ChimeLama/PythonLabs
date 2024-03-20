import play 
w=300
h=300
@play.when_program_starts
def do():
  play.screen.width = w
  play.screen.height = h


box=play.new_box(
  color="purple",
  x=126,
  y=33,
  width = w,
  height= h,
  
)
play.set_backdrop((200,10,0))


ears_L= play.new_circle(
    color="green",
    x= -4,
    y=-10,
    radius=15,
)
ears_R= play.new_circle(
    color="green",
    x= 57,
    y=-10,
    radius=15,
)
inears_L= play.new_circle(
    color="pink",
    x=-4,
    y=-9,
    radius=8,
)
inears_R= play.new_circle(
    color="pink",
    x= 57,
    y=-8,
    radius=8,
)

c_head = play.new_circle(
 color = "green ",
  x=31,
  y=-48,
  radius=45,
)
eye_C_R=play.new_circle(
  color="yellow",
  x=10,
  y=-42,
   radius=20,
)
eye_C_L=play.new_circle(
  color="yellow",
  x=50,
  y=-42,
   radius=20,
)
eye_CR=play.new_circle(
  color="black",
  x=10,
  y=-42,
   radius=5,
)
eye_CL=play.new_circle(
  color="black",
  x=50,
  y=-42,
   radius=5,
)

mouth_C_L = play.new_box(
    color = "black",
    x = 30,
    y = -70,
    width = 20,
    height = 5,
)
blush_L=play.new_box(
    color="pink",
    x= 0,
    y=-70,
    width= 10,
    height= 5,
)
blush_R=play.new_box(
    color="pink",
    x= 61,
    y=-70,
    width= 10,
    height= 5,
)
nose_C=play.new_circle(
    color="LightSalmon",
    x= 30,
    y=-53,
    radius=5,
)
brow_L=play.new_box(
    color="black",
    x=12,
    y=-17,
    angle=-30,
    width=30,
    height=3,
  
)
brow_R=play.new_box(
    color="black",
    x=48,
    y=-17,
    angle= 30,
    width=30,
    height=3,
  
)

text= play.new_text(
  color="white",
  words="AYE who farted?",
  x=138,
  y=-18,
  font_size =20,

)
@play.repeat_forever
async def speak_slowly():
  await play.timer(seconds=5)
  text.words= "No I didn't fart I swear"
  
mouse_text=play.new_text(
 color="black",
  words="black",
  x=0,
  y=0,
  font_size =20,
)
@play.repeat_forever
def mouse_coords():
  mouse_text.go_to(play.mouse)
  mouse_text.words = str(int(play.mouse.x)) + "," + str(int(play.mouse.y))

play.start_program()