import tkinter as tk
#Main Window
root=tk.Tk()
root.title("Quiz Application")
root.geometry("600x400")
answer=tk.StringVar()
result=tk.Label(root,text="",font=("Arial",16))
result.pack(pady=15)
def check_answer():
        if answer.get()=="A":
            result.config(text="Correct!")
        else:
            result.config(text="Incorrect!")
def start_quiz():
    question=tk.Label(root,text="Question1: What is python?",font=("Arial",18))
    question.pack (pady=20)
    option1=tk.Radiobutton(root,text="A.Programming language",variable=answer,value="A")
    option1.pack(pady=5)
    option2=tk.Radiobutton(root,text="B.A Snake",variable=answer,value="B")
    option2.pack(pady=4)
    option3=tk.Radiobutton(root,text="C.Game",variable=answer,value="C")
    option3.pack(pady=3)
    option4=tk.Radiobutton(root,text="D.Hardware",variable=answer,value="D")
    option4.pack(pady=2)
    check=tk.Button(root,text="Check Answer",command=check_answer)
    check.pack()
#Heading
heading=tk.Label(root,text="Welcome to Quiz",font=("Arial",22,"bold"))
heading.pack(pady=40)
#Start Button
start_button=tk.Button(root,text="Start Quiz",font=("Arial",14),command=start_quiz)
start_button.pack(pady=20)
#Run Application
root.mainloop()
    

