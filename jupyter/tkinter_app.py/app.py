import tkinter as tk
from tkinter import messagebox
import cold_email_generator  # Ensure this imports correctly

# Function to be called when the button is clicked
def on_generate_email():
    skills = skills_entry.get()
    email = cold_email_generator.generate_email(skills)
    messagebox.showinfo("Generated Email", email)

# Create the main application window
app = tk.Tk()
app.title("Cold Email Generator")

# Add a label and an entry widget for input
tk.Label(app, text="Enter Skills (comma separated):").pack(pady=10)
skills_entry = tk.Entry(app, width=50)
skills_entry.pack(pady=10)

# Add a button to generate the email
tk.Button(app, text="Generate Email", command=on_generate_email).pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
