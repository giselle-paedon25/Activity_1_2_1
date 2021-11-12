# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl

import random as rand

import leaderboard as lb

#-----game configuration----
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please input your name: ")

t = trtl.Turtle()

score_writer = trtl.Turtle()

counter =  trtl.Turtle()

sizes = [0.5, 1, 2, 3, 4, 5]
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
counter.goto(-190,190)
counter.pendown()

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False


#-----game functions--------
def manage_leaderboard():
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, t, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, t, score)

def countdown():
	global timer, timer_up
	counter.clear()
	if timer <= 0:
		counter.write("Time's Up", font=font_setup)
		timer_up = True
		manage_leaderboard()
	else:
		counter.write("Timer: " + str(timer), font=font_setup)
		timer -= 1
		counter.getscreen().ontimer(countdown, counter_interval)

colors = ["red", "blue", "purple", "green", "yellow", "pink", "white", "black"]

bgcolor = ["pink", "purple", "green","blue", "white"]

def change_position():
	t.stamp()
	t.fillcolor(rand.choice(colors))
	wn.bgcolor(rand.choice(bgcolor))
	t.penup()
	new_xpos = rand.randint(-200,200)
	new_ypos = rand.randint(-200,200)
	t.goto(new_xpos,new_ypos)
	t.shapesize(rand.choice(sizes))
	
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
# manages the leaderboard for top 5 scorers


wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()