import simpleguitk as simplegui
def draw_handler(canvas):
	r = 0
	g = 0
	b = 0
	canvas.draw_text("Click to go back!", (0, 390), 20, "red")
	canvas.draw_text("Chime's student portfolio",(0,40),35,"blue")
	for g in range(256):
		color="rgb("+ str(r) + ", " + str(g) + ", " + str(b) + ")"
		canvas.draw_text("chime", (50,50 + g), g/2 + 10, color)
frame = simplegui.create_frame("yo", 500, 400)
frame.set_draw_handler(draw_handler)
frame.start()
