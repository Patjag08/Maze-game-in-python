#Module Import
import os as o
import time as t
import Maze_generation as gen # <- Custom generation import (Save space)

#Movement function
def movement(maze, move_button):
    current_pos = gen.find_player(maze) #Find position of player to find walls and calculate new position
    if move_button == "w": #Up movement
        if maze[current_pos[0] - 1][current_pos[1]] != "#":
            return [current_pos[0] - 1,current_pos[1]]
        else:
            return "Not possible" #If theres a wall returns not possible
    elif move_button == "s": #Down movement
        if maze[current_pos[0] + 1][current_pos[1]] != "#":
            return [current_pos[0] + 1,current_pos[1]]
        else:
            return "Not possible" #If theres a wall returns not possible
    elif move_button == "a": #Left movement
        if maze[current_pos[0]][current_pos[1] - 1] != "#":
            return [current_pos[0],current_pos[1] - 1]
        else:
            return "Not possible" #If theres a wall returns not possible
    elif move_button == "d": #Right movement
        if maze[current_pos[0]][current_pos[1] + 1] != "#":
            return [current_pos[0],current_pos[1] + 1]
        else:
            return "Not possible" #If theres a wall returns not possible
    else:
        return "Error" #Catches any errors i.e Calculation error

#Main loop
def main():
    print("Press enter to play: (Q = Exit)") #Display options for players
    to_play = input() #Get user input
    if to_play.lower() == "q":
        quit(0) #If the user enters Q the program exits
    o.system("cls")
    playing = True
    move = ""
    valid_move = False
    generated_level = gen.generate_maze() #Generate the maze and store the 2D array in the variable generated_level
    maze_exit = gen.find_exit(generated_level) #Find the exit of the generated Maze
    while playing == True: #Keep looping the movement till player reaches the exit
        valid_move = False
        current_pos = gen.find_player(generated_level) #Grab the players current position
        if current_pos == maze_exit: #Check if the player is in the exit
            playing = False
            o.system("cls")
            print("Congrats on completing the maze") #Output a nice message that the maze has been completed
            print("Thanks for playing!")
            t.sleep(2) #Display it for two seconds
            o.system("cls") #Clear the screen after the two seconds
            return "" #Close out the function
        else:
            while valid_move == False:
                move = "" #Clears the move input
                while move.lower() not in ("w","s","a","d"): # Checks if the input is a valid moving character
                    gen.print_maze(generated_level) #Print the maze
                    move = input("(W = Up, S = Down, A = Left, D = Right) Where would you like to go") #Gets the movement input
                    o.system("cls")
                new_pos = movement(generated_level,move) #Call the function to move
                if new_pos not in ("Not possible", "Error"): #Make sure the returned result from movement is valid
                    # print(f"Current = {current_pos}") # Debugging print statements
                    # print(f"New = {new_pos}")
                    generated_level[current_pos[0]][current_pos[1]] = " " #Update the player character
                    current_pos = new_pos
                    generated_level[current_pos[0]][current_pos[1]] = "p"
                    valid_move = True
                    o.system("cls") # Clear the terminal
                elif new_pos == "Not possible": #Check if a wall has been hit
                    o.system("cls") #Clear the terminal to display message
                    print("You hit a wall.") #Print the message
                    t.sleep(2) #Wait two seconds 
                    o.system("cls") # Clear the terminal
                    break
                else:
                    print("Game returned an error (Movement related) NO ERROR CODE")
                    quit(0) #Quit after error returned
            
        
while True:
    main() #Loop the main function