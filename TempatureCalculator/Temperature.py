from tkinter import *
import statistics

MIN_TEMP:float = -50.0
MAX_TEMP:float = 150.0

def on_enter(e): add_reading()
def add_reading():
    user_in:str = user_var.get()
    try: 
        validate_temperature(float(user_in))
        submit_temps()
    except ValueError: 
        error_label.config(text=f"Invlid Entry")

def validate_temperature(value:float):
    if (value >= MIN_TEMP and value <= MAX_TEMP):
        temps.append(value)
        temp_var.set(temps)
        user_var.set("")
        error_label.config(text="")
    else: error_label.config(text=f"Out of Bounds")

def submit_temps():
    if (len(temps) > 0):
        min_temp = min(temps)
        max_temp = max(temps)
        avg_temp = round(statistics.mean(temps), 2)
        display_stats(min_temp, max_temp, avg_temp)
    else: display_stats(0,0,0)

def clear():
    temps.clear()
    temp_var.set(temps)
    error_label.config(text="")
    user_entry.delete(0, END)
    display_stats(0,0,0)

def display_stats(min:float, max:float, avg:float):
    out_display.config(state="normal")
    out_display.delete(0.0, END)
    out_display.insert(0.0,f"Min: {min:.2f}°C\nMax: {max:.2f}°C\nAvg: {avg:.2f}°C")
    out_display.config(state="disabled")

def remove_item(e):
    temps.remove(float(list_box.selection_get()))
    list_box.delete(list_box.curselection())
    submit_temps()


## INTERFACE IMPLEMENTATION ##
FONT = "rockwell 11"
HEADER_TEXT = f"Temperature Readings (c)\n( {MIN_TEMP} - {MAX_TEMP} )"
BGC_MAIN = "#232323"

root = Tk()
root.config()
root.minsize(260, 412)
root.config(padx=24)
root.title("Temperature Calculator")

header = Label(root, text=HEADER_TEXT, font=FONT)
header.pack(pady=8)

list_con = Frame(root)
list_con.pack(fill="x")

list_sb = Scrollbar(list_con)
list_sb.pack(side="right", fill="y", pady=4)

temps = []
temp_var = StringVar(value=temps)
list_box = Listbox(list_con, listvariable=temp_var, font=FONT, activestyle="dotbox")
list_box.config(yscrollcommand=list_sb.set, width=20, height=6)
list_box.bind("<Delete>", remove_item)
list_box.pack(fill="both")

list_sb.config(command=list_box.yview)

display_con = Frame(root)
display_con.pack(fill="x")

out_sb = Scrollbar(display_con)
out_sb.pack(side="right", fill="y", pady=4)

out_display = Text(display_con, font=FONT, spacing1=2)
out_display.config(yscrollcommand=out_sb.set, width=22, height=4, state="disabled")
out_display.pack(fill="x",pady=8)

out_sb.config(command=out_display.yview)

input_frame = Frame(root)
input_frame.pack()

error_label = Label(input_frame, font=FONT)
error_label.pack()

user_var = StringVar()
user_entry = Entry(input_frame, textvariable=user_var)
user_entry.config(justify="center", font=FONT)
user_entry.bind("<Return>", on_enter)
user_entry.pack(pady=6, ipady=2)

spacer = Frame(input_frame, height=8)
spacer.pack()

add_BTN = Button(input_frame, text=" Add ", font=FONT)
add_BTN.config(command=add_reading)
add_BTN.pack(fill="x")

clear_BTN = Button(input_frame, text=" Clear ", font=FONT)
clear_BTN.config(command=clear)
clear_BTN.pack(fill="x")

display_stats(0,0,0)
root.mainloop()