from tkinter import Button, Label, Tk, Entry

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 200, height= 150)
window.config(padx=15, pady=15)

# Function to calculate miles to km
def calculate_miles_to_km():
    miles = float(miles_entry.get())
    km = miles * 1.689
    txt_3.config(text=f"{km}")

# Configuration
caluclate_btn = Button(text="Calculate", command=calculate_miles_to_km)
miles_label = Label(text = "Miles")
miles_entry = Entry(width=10)
txt = Label(text = "is equal to")
txt_2 = Label(text = "Km")
txt_3 = Label(text = "0")



miles_entry.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
txt.grid(row=1, column=0, sticky="news")
txt_2.grid(row=1, column=2, sticky="news")
txt_3.grid(row=1, column=1, sticky="news")
caluclate_btn.grid(row=2, column=1, sticky="news")



window.mainloop()