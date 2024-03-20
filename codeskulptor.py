import simplegui
counter=0
def sun():
    red=[]
    def draw_handler(canvas):
        global counter
        x=10
        y=10
        if counter<5:
            canvas.draw_circle((100,300),5,3,"white")
        elif(counter>5 or counter<10):
            canvas.draw_circle((200,200),10,7,"blue")
        else:
            counter=0
        for i in range(10):
            counter=counter+1
            x=x+5
            y=y+3
    frame=simplegui.create_frame(" hime "  , 500,500)
    frame.set_canvas_background("green")
    frame.set_draw_handler(draw_handler)
    frame.start()
sun()