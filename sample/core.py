from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser

root = Tk()
root.title('note-orius')
# root.iconbitmap('./assets/icons/slice_of_pizza.ico')
# root.geometry("1200x700")

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
        
        nameArr = name.split('/')

        if (len(nameArr) > 0):
            name = nameArr[len(nameArr) - 1]

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
        save_as_file(e)

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
    
    # Check to see whether the board shortcut was used
    if e:
        selected = root.clipboard_get()
    # Update global selection
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

def select_all_text(e): 
    # Add sel tag to select all text 
    my_text.tag_add('sel', '1.0', 'end')

def clear_all_text(e): 
    my_text.delete(1.0, END)

def bold_it(): 
    # Create Font
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    # Configure and Define Tags
    my_text.tag_configure("bold", font=bold_font)
    current_tags = my_text.tag_names("sel.first")

    # Check if the "bold" Tag has been set
    if "bold" in current_tags: 
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else: 
        my_text.tag_add("bold", "sel.first", "sel.last")

# Italics Text
def italics_it(): 
     # Create Font
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    # Configure and Define Tags
    my_text.tag_configure("italic", font=italics_font)
    current_tags = my_text.tag_names("sel.first")

    # Check if the "bold" Tag has been set
    if "italic" in current_tags: 
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else: 
        my_text.tag_add("italic", "sel.first", "sel.last")

# Change Selected Text Color
def change_selected_text_color(): 
    # Prompt the user for a color
    my_color = colorchooser.askcolor()[1]
    
    if my_color:
        # Create Font
        color_font = font.Font(my_text, my_text.cget("font"))
        
        # Configure and Define Tags
        my_text.tag_configure("colored", font=color_font, foreground=my_color)
        current_tags = my_text.tag_names("sel.first")
        
        # Check if the "bold" Tag has been set
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")

def change_all_text_color(): 
    my_color = colorchooser.askcolor()[1]
    if my_color: 
        my_text.config(fg=my_color)

def change_bg_color(): 
    my_color = colorchooser.askcolor()[1]
    if my_color: 
        my_text.config(bg=my_color)

s = ttk.Style()
s.theme_use('classic')

# Create Toolbar Frame 
toolbar_frame = ttk.Frame(root, padding="3 3 12 12")
toolbar_frame.pack(fill=X)

#Create Main Frame
my_frame = ttk.Frame(root, padding="3 3 12 12")
my_frame.pack(pady=5)

# Scrollbar for the TextBox
text_scroll = ttk.Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y, padx=5, pady=5)

hor_scroll = ttk.Scrollbar(my_frame, orient="horizontal")
hor_scroll.pack(side=BOTTOM, fill=X, padx=5, pady=5)

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
my_text.pack(pady=5, padx=5)

# Configure Vertical and Horizontal Scroll Bars
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New          Ctrl+n", command=lambda: new_file(False))
file_menu.add_command(label="Open         Ctrl+o", command=lambda: open_file(False))
file_menu.add_command(label="Save         Ctrl+s", command=lambda: save_file(True))
file_menu.add_command(label="Save As", command=lambda: save_as_file(True))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut          Ctrl+x", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy         Ctrl+c", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste        Ctrl+v", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo         Ctrl+z", command=my_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo         Ctrl+y", command=my_text.edit_redo, accelerator="(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label="Select All   Ctrl+a", command=lambda: select_all_text(False))
# edit_menu.add_command(label="Clear        Ctrl+y", command=lambda: clear_all_text(False))

# Add Color Menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text", command=change_selected_text_color)
color_menu.add_command(label="All Text", command=change_all_text_color)
color_menu.add_command(label="Background", command=change_bg_color)

# Saved Status Bar
status_bar = ttk.Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# File Bindings
root.bind('<Control-Key-n>', new_file)
root.bind('<Control-Key-o>', open_file)
root.bind('<Control-Key-s>', save_file)

# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)

root.bind('<Control-Key-a>', select_all_text)
# root.bind('<Control-Key-y>', clear_all_text)

# Create Buttons

# Bold Button
bold_button = ttk.Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx = 5, pady=5)

# Italics Button
italics_button = ttk.Button(toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=1, padx = 5, pady=5)

# Undo/Redo Button
undo_button = ttk.Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx = 5, pady=5)
redo_button = ttk.Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx = 5, pady=5)

# Text Color Button 
color_text_button = ttk.Button(toolbar_frame, text='Text Color', command=change_selected_text_color)
color_text_button.grid(row=0, column=4, padx=5, pady=5)

root.mainloop()