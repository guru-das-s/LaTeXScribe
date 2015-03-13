# ------------------------------------------------------- #
# 			The LaTeXscribe Letter Generator
#
# 	          Please read the README.txt file for details.
# ------------------------------------------------------- #

import os
from Tkinter import *

def gen_letter():
	#Retrieve and process text from all input fields
	subject=e1.get()
	opadd=e2.get()
	myname=e3.get()
	yourname=e4.get()
	closadd=e5.get()    
	contents=context.get('1.0', 'end')
	contmod=contents.replace('\n',"\\\\") 
	fromadd=fromtext.get('1.0', 'end')
	frommod=fromadd.replace('\n',"\\\\")
	toadd=totext.get('1.0', 'end')
	tomod=toadd.replace('\n',"\\\\")
    
	#Make new directory, switch to it and save the text in a .tex file    
	os.system("mkdir LaTeXscribe")
	texfile=open("./letterskeleton.tex", 'r+')
	texfilecontents=texfile.xreadlines()
    
	filecontents=""
    
	for lines in texfilecontents:
		filecontents=filecontents+lines
	
	filecontents=filecontents.replace("MyName",myname) #Substitute field placeholders with entered data
	filecontents=filecontents.replace("YourName",yourname)
	filecontents=filecontents.replace("FromAddress",frommod)
	filecontents=filecontents.replace("ToAddress",tomod)
	filecontents=filecontents.replace("OpeningAddress",opadd)
	filecontents=filecontents.replace("Subject",subject)
	filecontents=filecontents.replace("LetterContents",contmod)
	filecontents=filecontents.replace("ClosingAddress",closadd)

	f=open("./LaTeXscribe/LaTeXscribeLetter.tex",'w')
	f.seek(0)
	f.write(filecontents) #Save the generated TeX file
	f.close()
    
	#Run pdflatex 
	os.system("cd LaTeXscribe; pdflatex LaTeXscribeLetter.tex")

# ------------------------------------------------------- #
# 				Detailing of the GUI follows.
# ------------------------------------------------------- #

root = Tk()
root.title("LaTeXscribe Letter Generator v1.0")

#Frame One
f1 = Frame(root)

Label(f1, text='Subject').grid(row=0, column=0, sticky=W)
Label(f1, text='Opening Address').grid(row=1, column=0, sticky=W)
Label(f1, text='Your Name').grid(row=2, column=0, sticky=W)
Label(f1, text='Addressee\'s Name').grid(row=3, column=0, sticky=W)
e1 = Entry(f1, width=30)
e2 = Entry(f1, width=30)
e3 = Entry(f1, width=30)
e4 = Entry(f1, width=30)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

f1.pack()

#Frame Two
f2=Frame(root)
Label(f2, text="The \"From\" Address").grid(row=0, column=0, sticky=W)
fromtext = Text(f2, wrap=WORD, bd=0, height=5, width=50)
fromtext.grid(row=1, column=0, sticky=N+S+E+W)

Label(f2, text="The \"To\" Address").grid(row=0, column=1, sticky=E)
totext = Text(f2, wrap=WORD, bd=0, height=5, width=50)
totext.grid(row=1, column=1, sticky=N+S+E+W)

f2.pack()

#Frame Three
f3 = Frame(root)
Label(f3, text="Contents of Letter").grid(row=0, column=0, sticky=W)
f3.grid_rowconfigure(1, weight=1)
f3.grid_columnconfigure(1, weight=1)

xscrollbar = Scrollbar(f3, orient=HORIZONTAL)
xscrollbar.grid(row=11, column=0, sticky=E+W)

yscrollbar = Scrollbar(f3)
yscrollbar.grid(row=1, column=1, sticky=N+S)

context = Text(f3, wrap=WORD, bd=0, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set, height=10, width=80)

context.grid(row=1, column=0, sticky=N+S+E+W)

xscrollbar.config(command=context.xview)
yscrollbar.config(command=context.yview)

f3.pack()

#Frame Four
f4=Frame(root)
Label(f4, text="Closing Address").grid(row=0, column=0, sticky=W)
e5 = Entry(f4, width=30)
e5.grid(row=0, column=1)
Button(f4, text='Generate Letter!', bd=5, command=gen_letter).grid(row=3, column=1, sticky=S)
f4.pack()

#Execute GUI loop
root.mainloop()
