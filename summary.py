import tkinter as tk
from tkinter import messagebox


credentials = {
    'student1': 'password1',
    'student2': 'password2',
}


def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in credentials and credentials[username] == password:
        messagebox.showinfo("Login Successful", "Welcome!")
        login_window.destroy()
        open_home_page()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def show_wind_turbine_info():
    info = """
    Wind Turbines Education Summary:

    - Wind turbines harness wind energy to produce electricity.
    - They consist of blades, a rotor, and a generator.
    - When wind blows, it turns the blades, which spin the rotor and generate electricity.

    Benefits:
    - Clean and renewable energy
    - Reduces greenhouse gas emissions
    - Can be deployed in various locations

    Challenges:
    - Wind variability
    - Initial setup costs
    - Environmental impact on wildlife
    """
    messagebox.showinfo("Wind Turbines", info)



login_window.mainloop()
