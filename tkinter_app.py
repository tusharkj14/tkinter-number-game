from tkinter import *
from tkinter import messagebox
from random import randint
# imported all the necessary libraries and functions in the above 3 commands.

# to initialise a tkinter app, you need to call the Tk() function from tkinter module as below
root = Tk()
root.title("Number Game")   # setting the title of the window
root.geometry("400x300")    # choosing a canvas size

name = StringVar()   
# this variable stores the Name of the Player

# the below 2 variables have the default value of an empty string
level = StringVar()    # this variable stores the size of pizza as inputted from radio buttons
# level.set("Beginner")

get_op = StringVar()    # this variable gets the operation required
get_op.set("+")
ans_in = IntVar()   # to get the inputted answer from the user
global ans  # global variable to store sum of the two random integers
ans = 0

# function invoked whenever the radiobuttons input is changed
def on_sel():
    # call the global varaible
    global ans
    op = get_op.get()
    lbl1.config(text="")    #clear previous text in both labels which would contain 
    lbl2.config(text=get_op.get())  # show which operation is currently selected
    lbl3.config(text="")    # the random integers
    lo, up  = 1, 9      # the lower and upper bounds for the random generator

    # it changes according to the level inputted in the radiobutton
    if level.get() == "Beginner":
        lo, up  = 1, 9
    elif level.get() == "Intermediate":
        lo, up  = 10, 99
    elif level.get() == "Advance":
        lo, up  = 100, 500

    # get the random integers
    x1, x2 = randint(lo, up), randint(lo, up)
    # store the result in global variable based on the op
    if get_op.get()=="+":
        ans = x1+x2 
    elif get_op.get()=="-":
        ans = x1-x2
    elif get_op.get() == "*":
        ans = x1*x2
    elif get_op.get() == "/":
        ans = x1//x2
    print(ans)
    lbl1.config(text=x1)    # display the number on the lbl1 Label
    lbl3.config(text=x2)    # display the number on the lbl2 Label


# function invoked when the check button is called
def on_check():
    res = ans_in.get()  # get the input answer from the user
    uname = name.get()  # get the input name from the user
    msg = str() # string to hold the message

    # if the two integers are equal or not
    if res==ans:
        msg = "Congratulations {0}. Your Answer is Correct".format(uname)
    else:
        msg = "I am sorry {0}. Your Answer is wrong".format(uname)
    
    # change the text in lbl_final label
    lbl_final.config(text=msg)
    


lbl_name = Label(root, text="Name :")
lbl_name.place(x=50, y =20)

# An entry widget used to input name from the user
# this changes the name variable
name_in = Entry(root, textvariable=name)
name_in.place(height=20, width=250)
name_in.place(x=100, y=20) 


# the three radio buttons which ask for the Levels 
# these changes the value of level variable 
# whenever a button is pressed, the  on_sel function is invoked
r1=Radiobutton(root, text="Beginner", variable=level,value="Beginner", command=on_sel)
r2=Radiobutton(root, text="Intermediate", variable=level,value="Intermediate",command=on_sel)
r3=Radiobutton(root, text="Advance", variable=level,value="Advance",command=on_sel)
r1.place(x=20,y=50)
r2.place(x=120, y=50)
r3.place(x=220, y=50)

# the four radio buttons which ask for the operation required by the user 
# these changes the value of get_op variable 
# whenever a button is pressed, the  on_sel function is invoked
o1=Radiobutton(root, text="+", variable=get_op,value="+", command=on_sel)
o2=Radiobutton(root, text="-", variable=get_op,value="-", command=on_sel)
o3=Radiobutton(root, text="*", variable=get_op,value="*", command=on_sel)
o4=Radiobutton(root, text="/", variable=get_op,value="/", command=on_sel)
o1.place(x=20,y=80)
o2.place(x=80, y=80)
o3.place(x=140, y=80)
o4.place(x=200, y=80)


# this is the label for the first random number, which changes whenever the radio button input is changed
# using  the on_sel function
lbl1 = Label(root, bg="yellow")
lbl1.place(x=20, y=120)

# the placeholder for the arithmetic operation required, here it is '+'
lbl2 = Label(root, text=get_op.get())
lbl2.place(x=50, y=120)

# this is the label for the second random number, which changes whenever the radio button input is changed
# using  the on_sel function
lbl3 = Label(root,  bg="yellow")
lbl3.place(x=80, y=120)

ans_check = Entry(root, textvariable=ans_in)
ans_check.place(height=20, width=100)
ans_check.place(x=120, y=120)

# this button invokes the on_check function when pressed and checks whether the inputted answer is correct or not
btn=Button(root, text="Check", command=on_check, fg='blue')
btn.place(x=250, y=120)

# this label displayes whether the user has inputted the correct answer or not
lbl_final = Label(root, text="Enter Your Answer")
lbl_final.place(x=60, y=150)

# this command runs the tkinter window as long as the Python program is executed or the user closes the tkinter window.
root.mainloop()