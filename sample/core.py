from tkinter import *
from tkinter import filedialog
# from tkinter import font

root = Tk()
root.title('note-orius')
# root.iconbitmap('./assets/slice_of_pizza.ico')

global open_status_name
open_status_name = False

global selected
selected = False


def new_file(e):
    # Delete previous text
    my_text.delete("1.0", END)

    # Update status bars
    root.title('New File - note-orius')
    status_bar.config(text="New File        ")

    global open_status_name
    open_status_name = False


def open_file(e):
    # Get Filename
    text_file = filedialog.askopenfilename(
        initialdir="/Users/sanshitsagar/Desktop",
        title="Open File",
        filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"),
                   ("Python Files", "*.py"), ("All Files", "*.*")))

    global open_status_name
    open_status_name = text_file

    if text_file:
        # Delete previous text
        my_text.delete("1.0", END)

        # Update Status Bars
        name = text_file
        status_bar.config(text=f'{name} SAVED  ')
        nameArr = name.split('/')

        if (len(nameArr) > 0):
            name = nameArr[len(nameArr) - 1]

        root.title(f'{name} - note-orius')

        # Open the file
        text_file = open(text_file, 'r')
        file_data = text_file.read()
        my_text.insert(END, file_data)
        text_file.close()


def save_as_file(e):
    # get user's desired output location
    prefix = "/Users/sanshitsagar/Desktop/"
    text_file = filedialog.asksaveasfilename(
        defaultextension=".*",
        initialdir=prefix,
        title="Save File",
        filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"),
                   ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Update Status Bars
        name = text_file
        status_bar.config(text=f'{name}        ')
        name = name.replace(prefix, "")
        root.title(f'{name} - note-orius')

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))

        # Close the file
        text_file.close()


def save_file(e):
    global open_status_name
    if open_status_name:
        #Save the file
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))

        #Close the file
        text_file.close()
        status_bar.config(text=f'Saved: {name}        ')
    else:
        save_as_file()


def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            #Grab Selected Text
            selected = my_text.selection_get()
            #Delete Selected Text from text box
            my_text.delete("sel.first", "sel.last")
            #Clear the clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)


def copy_text(e):
    global selected
    
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        # Grab Selected Text
        selected = my_text.selection_get()
        # Clear the clipboard and append
        root.clipboard_clear()
        root.clipboard_append(selected)


def paste_text(e):
    global selected
    # Check to see whether the board shortcut was used
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)


#Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=15)

# Scrollbar for the TextBox
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

hor_scroll = Scrollbar(my_frame, orient="horizontal")
hor_scroll.pack(side=BOTTOM, fill=X)

#Create Text Box
my_text = Text(my_frame,
               width=100,
               height=25,
               font=('Helvetica', 16),
               selectbackground="yellow",
               selectforeground="black",
               undo=True,
               yscrollcommand=text_scroll.set,
               wrap="none",
               xscrollcommand=hor_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)
# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New       Ctrl+n", command=lambda: new_file(False))
file_menu.add_command(label="Open       Ctrl+o", command=lambda: open_file(False))
file_menu.add_command(label="Save       Ctrl+s", command=lambda: save_file(False))
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut       Ctrl+x",
                      command=lambda: cut_text(False),
                      accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy    Ctrl+c",
                      command=lambda: copy_text(False),
                      accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste   Ctrl+v",
                      command=lambda: paste_text(False),
                      accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo    Ctrl+z",
                      command=my_text.edit_undo,
                      accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo    Ctrl+y",
                      command=my_text.edit_redo,
                      accelerator="(Ctrl+y)")
# Saved Status Bar
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# File Bindings
root.bind('<Control-Key-n>', new_file);
root.bind('<Control-Key-o>', open_file);
root.bind('<Control-Key-s>', save_file);

#Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

root.mainloop()
