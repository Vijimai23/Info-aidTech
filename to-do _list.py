from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
#creating root window

root = Tk()
root.geometry("700x600")
root.title('To-Do List')

#defining function

def add_task():
    task = Entry.get(text_field)
    if task:
        list_box.insert(END, task)
        text_field.delete(0,END)  
        messagebox.showinfo("success",f"Task is added successfully") 
            

def cross_task():
    list_box.itemconfig(list_box.curselection(),fg="#dedede")
    list_box.selection_clear(0,END)
    messagebox.showinfo("success",f"Task is completed successfully")
    

def delete_task():
    selected_task_index = list_box.curselection()[0]
    list_box.delete(selected_task_index)
    messagebox.showinfo("success",f"Task  is deleted successfully")
   

def uncross_task():
    list_box.itemconfig(list_box.curselection(),fg="#464646")
    list_box.selection_clear(0,END)
    messagebox.showinfo("success",f"Task  is notCompleted")

def save_task():
        tasks = list_box.get(0,END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as file:
                for task in tasks:
                    file.write(task+"\n")    
  
#creating main_frame
    
main_frame=Frame(root,highlightbackground='black',highlightthickness=5,bg='lavender',width=650,height=500)
main_frame.place(x=10,y=70)
 
#creating label_field

label_name=Label(main_frame,bg='lavender',text='ENTER THE TASK',font=('bold',18))
label_name.place(x=10,y=50)

#creating text_field

text_field=Entry(main_frame,highlightbackground='black',highlightthickness=3,bd=3,font=('roman',20),width=30)
text_field.place(x=222,y=45)

#creating list_box

list_box=Listbox(main_frame,selectmode=SINGLE,font=('roman',22),bd=5,highlightbackground='black',width=30,height=7)
list_box.place(x=195,y=120)

#creating buttons

button1=Button(main_frame,text='Add',font=('bold',18),bg='royal blue',width=10,command=add_task)
button1.place(x=10,y=120)

button2=Button(main_frame,text='Cross',font=('bold',18),bg='royal blue',width=10,command=cross_task)
button2.place(x=10,y=190)

button3=Button(main_frame,text='Uncross',font=('bold',18),bg='royal blue',width=10,command=uncross_task)
button3.place(x=10,y=260)

button4=Button(main_frame,text='delete',font=('bold',18),bg='royal blue',width=10,command=delete_task)
button4.place(x=10,y=330)

save_button=Button(main_frame,text='Save',font=('bold',18),bg='green',width=43,command=save_task)
save_button.place(x=10,y=400)

root.mainloop()