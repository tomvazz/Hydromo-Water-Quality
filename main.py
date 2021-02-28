from tkinter import *
import email_update
import score_calculation
import share_window

# APP UI

# starting frame
root = Tk()
root.title("iPhone X")
w = 400
h = 800
# to place screen in center
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# iphone frame
iphone = PhotoImage(file="iphonebackdrop.png")
phone_frame = Label(root, image=iphone)
phone_frame.place(x=-3, y=-3)

time = Label(root, text="9:41", bg="#F6F7F9", fg="#8A919D", font=("Sans Serif", 12))
time.place(x=52, y=36)

date = Label(root, text="Today, 28 Feb 2021", bg="#F6F7F9", fg="#8A919D", font=("futura", 10))
date.place(x=45, y=72)

title = Label(root, text="hydromo", bg="#F6F7F9", fg="#6173E5", font=("futura", 30))
title.place(x=45, y=88)

options = Label(root, text="+", bg="#F6F7F9", fg="#6173E5", font=("futura", 30))
options.place(x=317, y=88)

score = Label(root, text="00", fg="#16013B", font=("futura", 90))
score.place(x=140, y=190)

result_heading = Label(root, fg="#8A919D", text="water quality: ", font=("futura", 15))
result_heading.place(x=145, y=300)

result = Label(root, text="  poor", fg="#6173E5", font=("futura", 17))
result.place(x=163, y=324)


# Ph (Label and Buttons)
ph = Label(root, text="pH Level", fg="#16013B", font=("futura", 12))
ph.place(x=172, y=420)
ph_value = 0
ph_buttons = []

def phClick(num):
    global ph_value
    ph_value = num
    for i in range(15):
        ph_buttons[i].config(fg="#6173E5")
    ph_buttons[num].config(fg="#00E37C")

for i in range(15):
    if (i<10):
        ph_buttons.append(Button(root, text=f" {i} ", font=("futura, 11"), fg="#6173E5", pady=2, command=lambda e=i: phClick(e)))
    else:
        ph_buttons.append(Button(root, text=f"{i}", font=("futura, 11"), fg="#6173E5", pady=2, command=lambda e=i: phClick(e)))

    ph_buttons[i].place(x=(40+(i*21)), y=446)

# Biological Oxygen Demand (Label & Entry)
bod = Label(root, text="B.O.D.", fg="#16013B", font=("futura", 12))
bod.place(x=40, y=477)
bod_entry = Entry(root, width=15, fg="#00E37C", font=("futura", 14))
bod_entry.insert(0, "mg/L")
bod_entry.place(x=40, y=497)

# Dissolved Oxygen (Label & Entry)
do = Label(root, text="Dissolved Oxygen", fg="#16013B", font=("futura", 12))
do.place(x=210, y=477)
do_entry = Entry(root, width=15, fg="#00E37C", font=("futura", 14))
do_entry.insert(0, "%")
do_entry.place(x=210, y=497)

# Fecal Coliform (Label & Entry)
fec = Label(root, text="Fecal Coliform", fg="#16013B", font=("futura", 12))
fec.place(x=40, y=527)
fec_entry = Entry(root, width=15, fg="#00E37C", font=("futura", 14))
fec_entry.insert(0, "c/100ml")
fec_entry.place(x=40, y=547)

# Nitrate (Label & Entry)
nit = Label(root, text="Nitrate", fg="#16013B", font=("futura", 12))
nit.place(x=210, y=527)
nit_entry = Entry(root, width=15, fg="#00E37C", font=("futura", 14))
nit_entry.insert(0, "mg/L")
nit_entry.place(x=210, y=547)

# Temperature (Label & Entry)
temp = Label(root, text="Temperature", fg="#16013B", font=("futura", 12))
temp.place(x=40, y=577)
temp_entry = Entry(root, width=15, fg="#00E37C", font=("futura", 14))
temp_entry.insert(0, "°C")
temp_entry.place(x=40, y=597)

# Total Dissolved Solids (Label & Entry)
tds = Label(root, text="Total Dissolved Solids", fg="#16013B", font=("futura", 12))
tds.place(x=210, y=577)
tds_entry = Entry(root, width=15, fg="#00E37C", font=("futura", 14))
tds_entry.insert(0, "mg/L")
tds_entry.place(x=210, y=597)

# Phosphate (Label & Entry)
phos = Label(root, text="Phosphate", fg="#16013B", font=("futura", 12))
phos.place(x=40, y=627)
phos_entry = Entry(root, width=15, fg="#00E37C", font=("futura", 14))
phos_entry.insert(0, "mg/L")
phos_entry.place(x=40, y=647)

# Turbidity (Label & Entry)
turb = Label(root, text="Turbidity", fg="#16013B", font=("futura", 12))
turb.place(x=210, y=627)
turb_entry = Entry(root, width=15, fg="#00E37C", font=("futura", 14))
turb_entry.insert(0, "NTU")
turb_entry.place(x=210, y=647)

# Button that runs calculation after user enters in information
def runClicked():
    bod_val = float(bod_entry.get())
    do_val = float(do_entry.get())
    fec_val = float(fec_entry.get())
    nit_val = float(nit_entry.get())
    temp_val = float(temp_entry.get())
    tds_val = float(tds_entry.get())
    phos_val = float(phos_entry.get())
    turb_val = float(turb_entry.get())
    overall_score, quality = score_calculation.driver(bod_val, do_val, fec_val, nit_val, temp_val, tds_val, phos_val, turb_val, ph_value)
    score.config(text=f"{overall_score}")
    result.config(text=f"{quality}")

    result.config()
run_button = Label(root, text="u", fg="#6173E5", bg="#F6F7F9", font=("Wingdings 3", 47))
run_button.place(x=175, y=693)
run_button.bind("<Button-1>", lambda e: runClicked())

# Button that sends email summary to user
def emailClicked():
    quality_score = score.cget("text")
    quality_result = result.cget("text")
    subject = "Hydromo Water Quality Score"
    message = f"Your water recieved a score of {quality_score}, which is considered to be {quality_result} water quality. \n" \
              f"\nBe sure to check with others in your area using this link: https://web-build-sidkumar5.vercel.app \n" \
              f"\nCheck out StateFarm's phenomenal customer service at this link: https://www.statefarm.com \n" \
              f"\nHydromo - Drink or Drown\n"
    email_update.send_email(subject, message)
email_button = Label(root, text="✉︎", fg="#8A919D", bg="#F6F7F9", font=("futura", 37))
email_button.place(x=80, y=695)
email_button.bind("<Button-1>", lambda e: emailClicked())

# Button that shares score to forum
def shareClicked():
    quality_score = score.cget("text")
    quality_result = result.cget("text")
    share_window.open_window(quality_score, quality_result)
share_button = Label(root, text="N", fg="#8A919D", bg="#F6F7F9", font=("Wingdings 3", 35))
share_button.place(x=285, y=701)
share_button.bind("<Button-1>", lambda e: shareClicked())



root.mainloop() # running loop required
