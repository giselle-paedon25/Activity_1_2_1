# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
t = trtl.Turtle()

score_writer = trtl.Turtle()

import random as rand

counter =  trtl.Turtle()
#-----game configuration----
t.shape("turtle")
t.shapesize(1.5)
t.fillcolor("pink")
t.pencolor("pink")
score = 0
#-----initialize turtle-----
score_writer.penup()
score_writer.goto(190,190)
score_writer.pendown()

counter.penup()
counter.goto(-190,-190)
counter.pendown()

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def change_position():
	t.penup()
	new_xpos = rand.randint(-200,200)
	new_ypos = rand.randint(-200,200)
	t.goto(new_xpos,new_ypos)
	
def update_score():
	global score
	score += 1
	score_writer.clear()
	score_writer.write(score,font=font_setup)

def t_clicked(x,y):
	countdown()
	if timer_up == False:
		update_score()
		change_position()
	else:
		t.hideturtle()
	


t.onclick(t_clicked)
#-----events----------------

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()