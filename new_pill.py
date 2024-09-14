import tkinter as tk
from tkinter import ttk
import random

def take_pill():
    global balance, pills_left, pills
    if pills_left > 0:
        pill = pills.pop()
        pills_left -= 1
        if pill == 'deadly':
            result_label.config(text="💀 You took the deadly pill! Game over.", fg='red')
            take_pill_button.config(state='disabled')
            restart_button.config(state='normal')
        else:
            balance += 500000
            balance_label.config(text=f"Balance: ${balance:,}")
            pills_left_label.config(text=f"Pills left: {pills_left}")
            progress['value'] = pills_left
    else:
        result_label.config(text="🎉 No more pills left! You survived!", fg='green')
        take_pill_button.config(state='disabled')
        restart_button.config(state='normal')

def restart_game():
    global balance, pills_left, pills
    balance = 0
    pills_left = 100
    pills = ['safe'] * 99 + ['deadly']
    random.shuffle(pills)
    balance_label.config(text=f"Balance: ${balance}")
    pills_left_label.config(text=f"Pills left: {pills_left}")
    result_label.config(text="")
    progress['value'] = pills_left
    take_pill_button.config(state='normal')
    restart_button.config(state='disabled')

# Initialize the main window
root = tk.Tk()
root.title("Pill Game")
root.geometry("400x300")

# Initialize game variables
balance = 0
pills_left = 100
pills = ['safe'] * 99 + ['deadly']
random.shuffle(pills)

# Create a custom style for the red buttons
style = ttk.Style()
style.configure("Red.TButton", background="red", foreground="white", font=('Helvetica', 16), padding=10)

# Create GUI elements
title_label = tk.Label(root, text="💊 Pill Survival Game 💊", font=('Helvetica', 18, 'bold'))
title_label.pack(pady=10)

balance_label = tk.Label(root, text=f"Balance: ${balance}", font=('Helvetica', 14))
balance_label.pack()

pills_left_label = tk.Label(root, text=f"Pills left: {pills_left}", font=('Helvetica', 14))
pills_left_label.pack()

progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate', maximum=100)
progress['value'] = pills_left
progress.pack(pady=10)

# Create the red buttons using ttk and the custom style
take_pill_button = ttk.Button(root, text="Take a Pill", command=take_pill, style="Red.TButton")
take_pill_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Helvetica', 14))
result_label.pack()

restart_button = ttk.Button(root, text="Restart Game", command=restart_game, style="Red.TButton", state='disabled')
restart_button.pack(pady=5)

# Start the main loop
root.mainloop()
