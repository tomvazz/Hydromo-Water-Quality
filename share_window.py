from tkinter import *
import share_result

def open_window(quality_score, quality_result):
    root = Tk()
    root.title("")
    w = 250
    h = 340
    # to place screen in center
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # City (Label & Entry)
    city = Label(root, text="City", fg="#16013B", font=("futura", 20))
    city.place(x=23, y=10)
    city_entry = Entry(root, width=12, fg="#00E37C", font=("futura", 25))
    city_entry.place(x=23, y=45)

    # Full Name (Label & Entry)
    name = Label(root, text="Full Name", fg="#16013B", font=("futura", 20))
    name.place(x=23, y=100)
    name_entry = Entry(root, width=12, fg="#00E37C", font=("futura", 25))
    name_entry.place(x=23, y=135)

    def go():
        city = city_entry.get()
        name = name_entry.get()
        share_result.selenium_webdriver(quality_score, quality_result, name, city, 0, "")
    share_btn = Button(root, text="Share", font=("Futura", 20), bg="gray18", fg="#6173E5", padx=60, pady=10, command=go)
    share_btn.place(x=35, y=200)


    # Help Section
    zip_entry = Entry(root, width=14, fg="#00E37C", font=("futura", 18))
    zip_entry.place(x=35, y=260)
    def help():
        zip_code = zip_entry.get()
        share_result.selenium_webdriver(0, 0, " ", " ", 1, zip_code)
    help_btn = Button(root, text="Need help? Enter Zip Code to Connect With an Agent", font=("Futura", 8), bg="gray18", fg="indianred", padx=6, pady=4, command=help)
    help_btn.place(x=30, y=295)

    root.mainloop()  # running loop required