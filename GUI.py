from input_validation import *
from doppler_shift_simulator import *
from tkinter import *
import tkinter.font as tkFont

# Colors:
taupe_grey = "#7a6563"
light_bronze = "#d3a588"
toasted_almond = "#c88e6a"
sand_duno = "#ece2d0"
parchment = "#f9f6f1"
silver = "#d1c8c7"

lam = 0
fd = 0
recieved_freq = 0
tc = 0
classification = ""

conversions = ["Hz", "MHz", "GHz"]


window = Tk()

window.geometry("720x480")
window.resizable(False, False)

def calculate():
    global lam, fd, recieved_freq, tc, classification

    fc_val = fc_input.get()
    speed = speed_input.get()
    angle = angle_input.get()

    fc_is_valid, fc_error_msg, fc = validate_fc(fc_val, X.get())
    speed_is_valid, speed_error_msg = validate_speed(speed)
    angle_is_valid, angle_error_msg = validate_angle(angle)

    if(fc_is_valid and speed_is_valid and angle_is_valid):
        result = compute_doppler(fc, float(speed), float(angle))
        lam = result[0]
        fd = result[1]
        recieved_freq = result[2]
        tc = result[3]
        classification = result[4]
        print(result)
    else:
        lam = 0
        fd = 0
        recieved_freq = 0
        tc = 0
        classification = ""
    
    lambda_label.config(text=f"λ = {lam:.3f}m")
    fd_label.config(text=f"Doppler shift (fD) = {"+" if fd >= 0 else "-"}{fd:.2f}hz")
    recieved_freq_label.config(text=f"Received Frequency = {recieved_freq:.2f}hz")
    tc_label.config(text=f"Coherence Time (Tc) = {tc:.4f}s")
    classification_label.config(text=f"classification = {classification}")

    fc_error.config(text=fc_error_msg)
    speed_error.config(text=speed_error_msg)
    angle_error.config(text=angle_error_msg)

def plot():
    fc = fc_input.get()
    speed = speed_input.get()
    angle = angle_input.get()

    fc_is_valid, fc_error_msg, fc = validate_fc(fc, X.get())
    speed_is_valid, speed_error_msg = validate_speed(speed)
    angle_is_valid, angle_error_msg = validate_angle(angle)

    if(fc_is_valid and speed_is_valid and angle_is_valid):
        plot_fd_angle(fc, float(speed))
        plot_fd_speed(fc, float(angle))

    fc_error.config(text=fc_error_msg)
    speed_error.config(text=speed_error_msg)
    angle_error.config(text=angle_error_msg)


try:
    error_custom_font = tkFont.Font(family="Source Sans Pro", size=12)
    label_custom_font = tkFont.Font(family="Source Sans Pro", size=16, weight="bold")
    button_custom_font = tkFont.Font(family="Source Sans Pro", size=24, weight="bold")
except:
    print("Source Sans Pro not found, using Helvetica as a fallback.")
    error_custom_font = tkFont.Font(family="Helvetica", size=12)
    label_custom_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
    button_custom_font = tkFont.Font(family="Helvetica", size=24, weight="bold")

window.title("Doppler Shifter Simulator")
icon = PhotoImage(file="./smartphone.png")
window.iconphoto(True, icon)

window.config(background=taupe_grey)

# labels:
fc_label = Label(window, text="Carrier Frequency (hz/Mhz)", font=label_custom_font, fg=sand_duno, bg=taupe_grey)
fc_label.place(x=27, y=51)

speed_label = Label(window, text="Speed (m/s)", font=label_custom_font, fg=sand_duno, bg=taupe_grey)
speed_label.place(x=350, y=51)

angle_label = Label(window, text="Angle (deg)", font=label_custom_font, fg=sand_duno, bg=taupe_grey)
angle_label.place(x=552, y=51)

# inputs:
fc_input = Entry(window, 
                    font=button_custom_font, 
                    width=10,
                    bg=light_bronze,
                    fg=parchment,
                    border=0)
fc_input.place(x=30, y=80)

speed_input = Entry(window, 
                    font=button_custom_font, 
                    width=5,
                    bg=light_bronze,
                    fg=parchment,
                    border=0)
speed_input.place(x=350, y=80)

angle_input = Entry(window, 
                    font=button_custom_font, 
                    width=5,
                    bg=light_bronze,
                    fg=parchment,
                    border=0)
angle_input.place(x=552, y=80)

# error messages:
fc_error = Label(window, text="", font=error_custom_font, fg="red", bg=taupe_grey)
fc_error.place(x=15, y=120)

speed_error = Label(window, text="", font=error_custom_font, fg="red", bg=taupe_grey)
speed_error.place(x=330, y=120)

angle_error = Label(window, text="", font=error_custom_font, fg="red", bg=taupe_grey)
angle_error.place(x=530, y=120)

# conversions frame:
conversion_frame = Frame(window, bg=silver, width=100, height=50, padx=20, pady=15)
conversion_frame.place(x=27, y=160)

# radiobuttons:
X = IntVar()

for index in range(len(conversions)):
    radiobutton = Radiobutton(conversion_frame, text=conversions[index], variable=X, value=index, indicatoron=0, font=label_custom_font, bg=silver, fg=taupe_grey)
    radiobutton.pack(side=LEFT, padx=3)

# result frame:
result_frame = Frame(window, bg=silver, width=342, height=230, padx=20, pady=15)
result_frame.place(x=27, y=230)

# result:
lambda_label = Label(result_frame, text="λ = 0m", font=label_custom_font, fg=taupe_grey, bg=silver, anchor='w', pady=5)
lambda_label.pack(fill='both')

fd_label = Label(result_frame, text="Doppler shift (fD) = 0hz", font=label_custom_font, fg=taupe_grey, bg=silver, anchor='w', pady=5)
fd_label.pack(fill='both')

recieved_freq_label = Label(result_frame, text="Received Frequency = 0hz", font=label_custom_font, fg=taupe_grey, bg=silver, anchor='w', pady=5)
recieved_freq_label.pack(fill='both')

tc_label = Label(result_frame, text="Coherence Time (Tc) = 0s", font=label_custom_font, fg=taupe_grey, bg=silver, anchor='w', pady=5)
tc_label.pack(fill='both')

classification_label = Label(result_frame, text="classification = ", font=label_custom_font, fg=taupe_grey, bg=silver, anchor='w', pady=5)
classification_label.pack(fill='both')

# buttons:
calculate_button = Button(window, 
                          text="Calculate", 
                          fg=parchment, 
                          activeforeground=parchment, 
                          bg=light_bronze, 
                          activebackground=toasted_almond, 
                          font=button_custom_font,
                          bd=0,
                          command=calculate)
calculate_button.place(x=500, y=235)

plot_button = Button(window, 
                          text="Plot", 
                          fg=parchment, 
                          activeforeground=parchment, 
                          bg=light_bronze, 
                          activebackground=toasted_almond, 
                          font=button_custom_font,
                          bd=0,
                          padx=38,
                          command=plot)
plot_button.place(x=500, y=391)

window.mainloop()