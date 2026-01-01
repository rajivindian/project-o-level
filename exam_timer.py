import tkinter as tk
from datetime import datetime

def update_timer():
    # Target Exam Date: Jan 15, 2026, 9:00 AM
    exam_date = datetime(2026, 1, 15, 9, 0, 0)
    now = datetime.now()
    remaining = exam_date - now

    if remaining.total_seconds() > 0:
        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Format the time string
        time_str = f"{days}d : {hours}h : {minutes}m : {seconds}s"
        label_time.config(text=time_str)
        
        # Change color to RED if less than 5 days left!
        if days < 5:
            label_time.config(fg="#ff5555") # Red warning color
        
        # Update every 1000ms (1 second)
        root.after(1000, update_timer)
    else:
        label_time.config(text="EXAM STARTED!", fg="red")

# --- GUI SETUP ---
root = tk.Tk()
root.title("Mission: Jan 15th")
root.geometry("400x250")
root.configure(bg="#1e1e1e") # Dark Grey Background

# Label 1: The Title
label_title = tk.Label(root, text="TIME LEFT TO STUDY:", font=("Arial", 14), fg="#aaaaaa", bg="#1e1e1e")
label_title.pack(pady=(30, 5))

# Label 2: The Countdown
label_time = tk.Label(root, text="", font=("Courier New", 30, "bold"), fg="#50fa7b", bg="#1e1e1e")
label_time.pack(pady=10)

# Label 3: Motivation
label_quote = tk.Label(root, text="Keep Pushing. You got this!", font=("Arial", 12, "italic"), fg="#f1fa8c", bg="#1e1e1e")
label_quote.pack(side="bottom", pady=20)

update_timer()
root.mainloop()