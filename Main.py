#Module Import
import os as o
import time as t
import Maze_generation as gen # <- Custom generation import (Save space)
from pynput.keyboard import Key, Listener
import threading
import tkinter as tk

global generated_level
global new_pos
global moved
global current_pos
global moving
global label0
global label1
global label2
global label3
global label4
global label5
global label6
global label7
global label8
global label9
global label10
global label11
global label12
global label13
global label14
global label15
global label16
global label17
global label18
global label19
global label20
global label21
global label22
global label23
global label24
global label25
global label26
global labeltime
global root
global time

var = None
moving = False
time = 0

#Movement function

def Listener_thread():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def time_thread():
    global time
    while True:
        time += 1
        t.sleep(1)

def movement(maze, move_button):
    global generated_level
    global new_pos
    global moved
    global current_pos
    current_pos = gen.find_player(generated_level) #Find position of player to find walls and calculate new position
    if move_button == "w": #Up movement
        if maze[current_pos[0] - 1][current_pos[1]] != "#":
            new_pos = [current_pos[0] - 1,current_pos[1]]
            moved = True
        else:
            new_pos = "Not possible" #If theres a wall returns not possible
    elif move_button == "s": #Down movement
        if maze[current_pos[0] + 1][current_pos[1]] != "#":
            new_pos = [current_pos[0] + 1,current_pos[1]]
            moved = True
        else:
            new_pos = "Not possible" #If theres a wall returns not possible
    elif move_button == "a": #Left movement
        if maze[current_pos[0]][current_pos[1] - 1] != "#":
            new_pos = [current_pos[0],current_pos[1] - 1]
            moved = True
        else:
            new_pos = "Not possible" #If theres a wall returns not possible
    elif move_button == "d": #Right movement
        if maze[current_pos[0]][current_pos[1] + 1] != "#":
            new_pos = [current_pos[0],current_pos[1] + 1]
            moved = True
        else:
            new_pos = "Not possible" #If theres a wall returns not possible
    else:
        new_pos = "Error" #Catches any errors i.e Calculation error

#Main loop
def main():
    global generated_level
    global moved
    global new_pos
    global moving
    to_play = "0" #Get user input
    if to_play.lower() == "q":
        quit(0) #If the user enters Q the program exits
    o.system("cls")
    playing = True
    valid_move = False
    generated_level = gen.generate_maze() #Generate the maze and store the 2D array in the variable generated_level
    maze_exit = gen.find_exit(generated_level) #Find the exit of the generated Maze
    time_thread_real.start()
    while playing == True: #Keep looping the movement till player reaches the exit
        moved = False
        valid_move = False
        current_pos = gen.find_player(generated_level) #Grab the players current position
        if current_pos == maze_exit: #Check if the player is in the exit
            playing = False
            o.system("cls")
            update_label(True,time)
            t.sleep(3)
            quit(0)
        else:
            while valid_move == False:
                update_label(False,time)
                moved = False
                while moved != True: # Checks if the input is a valid moving character
                    #Delay
                    moving = True
                    1 + 1
                o.system("cls") #Call the function to move
                moving = False
                if new_pos not in ("Not possible", "Error"): #Make sure the returned result from movement is valid
                    print(f"Current = {current_pos}") # Debugging print statements
                    print(f"New = {new_pos}")
                    current_pos = gen.find_player(generated_level)
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
            

# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#             print('You Pressed A Key!')
#     except:
#         break

def on_press(key):
    try:
        if moving:
            if key.char == "w":
                movement(generated_level,"w")
            elif key.char == "s":
                movement(generated_level,"s")
            elif key.char == "a":
                movement(generated_level,"a")
            elif key.char == "d":
                movement(generated_level,"d")
    except:
        return ""

def on_release(key):
    1 + 1

    



def update_label(finished, final):
    global generated_level
    global root
    global var
    global label0
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global label8
    global label9
    global label10
    global label11
    global label12
    global label13
    global label14
    global label15
    global label16
    global label17
    global label18
    global label19
    global label20
    global label21
    global label22
    global label23
    global label24
    global label25
    global label26
    if finished != True:
        list_rows = gen.display_maze(generated_level)
        label0.config(text=list_rows[0])
        label1.config(text=list_rows[1])
        label2.config(text=list_rows[2])
        label3.config(text=list_rows[3])
        label4.config(text=list_rows[4])
        label5.config(text=list_rows[5])
        label6.config(text=list_rows[6])
        label7.config(text=list_rows[7])
        label8.config(text=list_rows[8])
        label9.config(text=list_rows[9])
        label10.config(text=list_rows[10])
        label11.config(text=list_rows[11])
        label12.config(text=list_rows[12])
        label13.config(text=list_rows[13])
        label14.config(text=list_rows[14])
        label15.config(text=list_rows[15])
        label16.config(text=list_rows[16])
        label17.config(text=list_rows[17])
        label18.config(text=list_rows[18])
        label19.config(text=list_rows[19])
        label20.config(text=list_rows[20])
        label21.config(text=list_rows[21])
        label22.config(text=list_rows[22])
        label23.config(text=list_rows[23])
        label24.config(text=list_rows[24])
        label25.config(text=list_rows[25])
        label26.config(text=list_rows[26])
        root.update_idletasks()
    else:
        label0.config(text=f"Congrats on winning \n Thanks for playing \n It took you {time} seconds")
        label1.grid_forget()
        label2.grid_forget()
        label3.grid_forget()
        label4.grid_forget()
        label5.grid_forget()
        label6.grid_forget()
        label7.grid_forget()
        label8.grid_forget()
        label9.grid_forget()
        label10.grid_forget()
        label11.grid_forget()
        label12.grid_forget()
        label13.grid_forget()
        label14.grid_forget()
        label15.grid_forget()
        label16.grid_forget()
        label17.grid_forget()
        label18.grid_forget()
        label19.grid_forget()
        label20.grid_forget()
        label21.grid_forget()
        label22.grid_forget()
        label23.grid_forget()
        label24.grid_forget()
        label25.grid_forget()
        label26.grid_forget()


listeningthread = threading.Thread(target=Listener_thread)
listeningthread.start()
time_thread_real = threading.Thread(target=time_thread)
mainthread = threading.Thread(target=main)
mainthread.start()

# Collect events until released

def main_tk():
    global label0
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global label8
    global label9
    global label10
    global label11
    global label12
    global label13
    global label14
    global label15
    global label16
    global label17
    global label18
    global label19
    global label20
    global label21
    global label22
    global label23
    global label24
    global label25
    global label26
    global root
    # Create the main window
    root = tk.Tk()

    # Create a labels
    label0 = tk.Label(root, text= "", justify="left")
    label0.grid(row=0,column=0)
    label1 = tk.Label(root, text= "", justify="left")
    label1.grid(row=0,column=1)
    label2 = tk.Label(root, text= "", justify="left")
    label2.grid(row=0,column=2)
    label3 = tk.Label(root, text= "", justify="left")
    label3.grid(row=0,column=3)
    label4 = tk.Label(root, text= "", justify="left")
    label4.grid(row=0,column=4)
    label5 = tk.Label(root, text= "", justify="left")
    label5.grid(row=0,column=5)
    label6 = tk.Label(root, text= "", justify="left")
    label6.grid(row=0,column=6)
    label7 = tk.Label(root, text= "", justify="left")
    label7.grid(row=0,column=7)
    label8 = tk.Label(root, text= "", justify="left")
    label8.grid(row=0,column=8)
    label9 = tk.Label(root, text= "", justify="left")
    label9.grid(row=0,column=9)
    label10 = tk.Label(root, text= "", justify="left")
    label10.grid(row=0,column=10)
    label11 = tk.Label(root, text= "", justify="left")
    label11.grid(row=0,column=11)
    label12 = tk.Label(root, text= "", justify="left")
    label12.grid(row=0,column=12)
    label13 = tk.Label(root, text= "", justify="left")
    label13.grid(row=0,column=13)
    label14 = tk.Label(root, text= "", justify="left")
    label14.grid(row=0,column=14)
    label15 = tk.Label(root, text= "", justify="left")
    label15.grid(row=0,column=15)
    label16 = tk.Label(root, text= "", justify="left")
    label16.grid(row=0,column=16)
    label17 = tk.Label(root, text= "", justify="left")
    label17.grid(row=0,column=17)
    label18 = tk.Label(root, text= "", justify="left")
    label18.grid(row=0,column=18)
    label19 = tk.Label(root, text= "", justify="left")
    label19.grid(row=0,column=19)
    label20 = tk.Label(root, text= "", justify="left")
    label20.grid(row=0,column=20)
    label21 = tk.Label(root, text= "", justify="left")
    label21.grid(row=0,column=21)
    label22 = tk.Label(root, text= "", justify="left")
    label22.grid(row=0,column=22)
    label23 = tk.Label(root, text= "", justify="left")
    label23.grid(row=0,column=23)
    label24 = tk.Label(root, text= "", justify="left")
    label24.grid(row=0,column=24)
    label25 = tk.Label(root, text= "", justify="left")
    label25.grid(row=0,column=25)
    label26 = tk.Label(root, text= "", justify="left")
    label26.grid(row=0,column=26)
    
    # Start the GUI event loop
    root.mainloop()


main_tk()