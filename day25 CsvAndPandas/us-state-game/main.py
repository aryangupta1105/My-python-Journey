import turtle as t
import pandas

screen = t.Screen()
screen.title("U.S. States Game")
image = "day25 CsvAndPandas/us-state-game/blank_states_img.gif"
screen.addshape(image)

t.shape(image)

states_data = pandas.read_csv("day25 CsvAndPandas/us-state-game/50_states.csv")
all_states = states_data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed! correctly:" , prompt="What's another state name?").title()
    if answer_state == "Exit":
        missed_states = {
            "Missed States" : 
            [state for state in all_states if state not in guessed_states]
        }
        missed_state_names = pandas.DataFrame(missed_states)
        missed_state_names.to_csv("day25 CsvAndPandas/us-state-game/missed_state_names.csv")
        break
    if answer_state in all_states:
        mark = t.Turtle()
        mark.hideturtle()
        mark.penup()
        mark.pencolor("black")
        state = states_data[states_data["state"] == answer_state]
        mark.goto(int(state["x"]),int(state["y"]))
        mark.write(f"{answer_state}" , align="center", font=("Arial" , 10 , "normal"))
        guessed_states.append(answer_state)
        # <--------------item method in panda-------------->
        #The item() METHOD fetches the first item of the row or list
        # mark.write(f"{state.state.item()}" , align="center", font=("Arial" , 10 , "normal"))




# def get_mouse_click_cor(x,y):
#     print(x,y)
# t.onscreenclick(get_mouse_click_cor)
# to get the coordinates of each state by mouse click....


# Alternate way of keeping the screen on even on clicking on it.....
# screen.exitonclick()