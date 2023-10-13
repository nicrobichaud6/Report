from tkinter import *
from tkinter import messagebox
import random


#Naming our variables



grade_out =""
skills_out = ""
Name = "Nic"



root = Tk()
root.title("Report Card Generator")

myLabel = Label(root, text = 'Welcome!').pack()


#### Name of the student

n_title = Label(root, text = "Student's name:").pack()


Name = Entry(root, width = 40)
Name.pack()



#Gender dropbox for pronouns

g_title = Label(root, text = 'Gender').pack()

gender=StringVar()
gender.set("F")
gender_input =OptionMenu(root, gender, 	"M", "F")
gender_input.pack()



if gender == "M":
	gender_out1 = 'he' 
	gender_out2 = 'his'
else:
	gender_out1 = 'she' 
	gender_out2 = 'her'


#Grade level


g_title = Label(root, text = 'Grade').pack()

grade = StringVar()
grade.set("Grade 1")

grade_input = OptionMenu(root, grade, "Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5")
grade_input.pack()


if grade == 'Grade 1':
	grade_out = ''
elif grade == "Grade 2":
	grade_out = ''
elif grade == "Grade 3":
	grade_out = ''
elif grade == "Grade 4":
	grade_out = ''
elif grade == "Grade 5":
	grade_out = ''

#Time to create the dropboxes for skills and also if that comment is going to be positive or negative 

s_title = Label(root, text = 'Skills').pack()

skills = StringVar()


skills.set("Communication")

skills_input = OptionMenu(root, skills, "Communication", "Risk Taker", "Caring", "Thinker")
skills_input.pack()



skills_gi = StringVar()


skills_gi.set("Great")

skills_input2 = OptionMenu(root, skills_gi, "Great", "To Improve")
skills_input2.pack()


if skills == "Communication":
	if skills_gi == "Great":
		skills_out = \
		"{Name} has good communication skills as {gender_out1}\
		 interacts with {gender_out2} classmates well and contributes to class discussions."
	else:
		skills_out= \
		"Moving forward, {Name} is encouraged to develop \
		{gender_out2} communication skills by asking questions, communicating with peers, and responding to artworks."
elif skills == "Risk Taker":
	if skills_gi == 'Great':
		skills_out = \
		"{gender_out1} has shown herself to be a risk taker as \
		{gender_out1} experiments with the elements of art and is confident with {gender_out2} artworks."
	else:
		skills_out:\
		''
elif skills == "Caring":
	if skills_gi == 'Great':
		skills_out = \
		"{Name} is a caring student who interacts well with\
		{gender_out2} classmates and often offers to assist {gender_out2} classmates."
	else:
		skills_out= \
		'{Name} should also develop respect for {gender_out2} classmates, the teacher, and the classroom.\
		To foster caring and kindness in the classroom, {gender_out1} should focus on listening to others, showing empathy,\
		and finding ways to support and uplift their peers.'		
elif skills == "Thinker":
	if skills_gi == 'Great':
		skills_out = \
		"{Name} that {gender_out1} is a thinker as\
		{gender_out1} demonstrates critical thinking skills and creative\
		thinking skills by problem solving, making connections, and applying ideas and concepts to {gender_out2} artworks."
	else:
		skills_out:\
		''

c_title = Label(root, text = "Additional Comments").pack()
#ending statement

#This is for extra comments at the end

Add_comment = Entry(root, width = 40)
Add_comment.pack()

############## Checkbox for comments at the end

enc = [f'Keep up the hard work, {Name}',f'Keep up the good work {Name}!', f'Well done, {Name}.', f'Excellent Work, {Name}']
encourage = random.choice(enc)


## This new function checks the boolean answer from the checkbox 'true, false' and if it's checked(True) then it fills it with the encourage answer

def update_answer():
    if var.get():
        final_answer.set(encourage)
    else:
        final_answer.set("")


final_answer = StringVar()

# Create a Checkbutton and associate it with the variable 'var'
var = BooleanVar()
checkbox = Checkbutton(root, text="Encouragement", variable=var, command=update_answer)
checkbox.pack()



 


#have to create a function to know what will happen when 
def clickbutton():
	global finished_report
	Label_click = Label(root, text= skills_out+grade_out+encourage)
	Label_click.pack()

mybutton = Button(root, text = "Populate Report", command = clickbutton) 
mybutton.pack()







# Having text pop up on the screen

root.mainloop()