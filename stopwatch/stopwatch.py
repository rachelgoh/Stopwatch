import simplegui

time = 0

def timer_handler():
    global time
    time = time + 1

def draw_handler(canvas):
    global time
    canvas.draw_text(str(time), (50,50), 20, 'Pink')

def button_handler1():
    timer.stop()

def button_handler2():
    timer.start()

def button_handler3():
    timer.stop()
    global time
    time = 0


frame = simplegui.create_frame('Stopwatch', 200, 200)
button2 = frame.add_button('Start', button_handler2)
button1 = frame.add_button('Stop', button_handler1)
button3 = frame.add_button('Reset', button_handler3)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)
frame.start()

def format(t):
	global time
	time = t[0] + ":" + 