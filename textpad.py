from tkinter import *
from tkinter import filedialog
from tkinter import font 

root = Tk()
root.title('note-orius')
root.iconbitmap('./assets/slice_of_pizza.ico')

def new_file():
    # Delete previous text
    my_text.delete("1.0", END)

    # Update status bars
    root.title('New File - note-orius')
    status_bar.config(text="New File        ")

def open_file(): 
    # Delete previous text
    my_text.delete("1.0", END)

    # Get Filename 
    text_file = filedialog.askopenfilename(initialdir="/Users/sanshitsagar/Desktop", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py")))
    
    # Update Status Bars 
    name = text_file 
    status_bar.config(text=f'{name}        ')
    nameArr = name.split('/')
    name = nameArr[len(nameArr) - 1]
    name = name.replace('/Users/sanshitsagar/Desktop/', "")
    root.title(f'{name} - note-orius')

    # Open the file 
    text_file = open(text_file, 'r')
    file_data = text_file.read()
    my_text.insert(END, file_data)
    text_file.close()

#Create Main Frame 
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our Scrollbar for the Text Box 
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Create Text Box 
my_text = Text(my_frame, width=97, height=25, font=('Helvetica', 16), selectbackground="yellow",  selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack() 

text_scroll.config(command=my_text.yview)

# Create Menu 
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu 
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu 
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop() 