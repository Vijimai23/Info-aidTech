from tkinter import *
from tkinter import messagebox
import random

#creating root window

root=Tk() 
root.geometry('550x450')
root.title('Number Guessing Game')

random_number = random.randint(1,100)
left_attempts=10

#check function

def start_check():
   result = " "
   guess=int(text_field.get())
   if guess == random_number:
            result_label.config(text="Congratulations!!!! You guessed it right!")
   else:
            global left_attempts
            left_attempts-=1
            if left_attempts == 0:
                messagebox.showinfo("Game Over", f"Sorry, you lost. The number was {random_number}.")
            else:
                if guess < random_number:
                      result_label.config(text=f"wrong, choose high number! You have {left_attempts} guesses left.")
                      text_field.delete(0,END)
                else:
                      result_label.config(text=f"Wrong, choose low number! You have {left_attempts} guesses left.")
                      text_field.delete(0,END)
           
#play_again function
                                            
def play_again():
      global random_number
      random_number = random.randint(1, 100)
      global left_attempts
      left_attempts = 10
      result_label.config(text="")
      text_field.delete(0, END)
      
#quit function
    
def quit():
       root.destroy()
   
#creating main_frame

main_frame = Frame(root,bg='pink',highlightbackground='black',highlightthickness=2,height=400,width=500)
main_frame.place(x=10,y=10)

#creating label_frame

Label_Frame=Label(main_frame,bg='pink',text='Guess the number between 1-100',font=('bold',20))
Label_Frame.place(x=30,y=30)

#creating text_field

text_field=Entry(main_frame,font=('bold',20),width=30)
text_field.place(x=20,y=100)

result_label=Label(main_frame,bg='pink',font=('bold',15))
result_label.place(x=15,y=200)

#creating buttons

check_button=Button(main_frame,bg='yellow',text='Check',font=('bold',20),command=start_check)
check_button.place(x=20,y=300)

play_again_button=Button(main_frame,bg='green',text='Play again',font=('bold',20),command=play_again)
play_again_button.place(x=180,y=300)

quit_button=Button(main_frame,bg='red',text='Quit',font=('bold',20),command=quit)
quit_button.place(x=390,y=300)

root.mainloop() 