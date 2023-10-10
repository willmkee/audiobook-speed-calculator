# Write your code here :-)
import tkinter as tk

def calculate_duration():
    try:
        hours_left = int(hours_entry.get())
        minutes_left = int(minutes_entry.get())
        speed = float(speed_entry.get())

        # Calculate the total time required
        total_time_minutes = (hours_left * 60 + minutes_left) / speed
        hours_required = int(total_time_minutes // 60)
        minutes_required = int(total_time_minutes % 60)

        # Display the result
        result_label.config(text=f'Time required to finish: {hours_required} hours and {minutes_required} minutes')
    except ValueError:
        result_label.config(text='Please enter valid numbers for hours left, minutes left, and speed.')

# Create the main application window
app = tk.Tk()
app.title('Audiobook Time Calculator')

# Add padding around the entire app
app.geometry("350x250")
app.configure(padx=10, pady=10)

# Create and configure widgets
hours_label = tk.Label(app, text='Hours Left:')
hours_label.pack()

hours_entry = tk.Entry(app)
hours_entry.pack()

minutes_label = tk.Label(app, text='Minutes Left:')
minutes_label.pack()

minutes_entry = tk.Entry(app)
minutes_entry.pack()

speed_label = tk.Label(app, text='Speed (1x, 1.5x, 2x, etc.):')
speed_label.pack()

speed_entry = tk.Entry(app)
speed_entry.pack()

calculate_button = tk.Button(app, text='Calculate Time', command=calculate_duration)
calculate_button.pack()

result_label = tk.Label(app, text='')
result_label.pack()

# Start the main loop
app.mainloop()
