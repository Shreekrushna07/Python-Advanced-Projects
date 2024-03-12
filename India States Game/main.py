# Import the turtle and pandas libraries
import turtle
import pandas

# Create a screen for the turtle graphics and set it up
screen = turtle.Screen()
screen.setup(900, 800)
screen.title("India States Game")

# Set the image for the turtle to use as the background
image = "India States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the data containing the names and coordinates of the states
data = pandas.read_csv("India States Game/list_states_india.csv")
all_states = data.state.to_list()
guessed_states = []

# Loop until all states are guessed or the user exits
while len(guessed_states) < 31:
    # Ask the user for the name of a state
    answer_state = screen.textinput(title=f"{len(guessed_states)}/31 States Correct", prompt="What's another state name?")

    # If the user types "Exit" or "exit", save the remaining states and exit the loop
    if answer_state == "Exit" or answer_state == "exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("India States Game/new.csv")
        break

    # If the guessed state is correct, add it to the list of guessed states and display it on the map
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# Close the screen when the user clicks on it
screen.exitonclick()