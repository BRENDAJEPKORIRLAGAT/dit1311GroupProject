import tkinter as tk
from tkinter import messagebox

# Dummy credentials for login
credentials = {
    'student1': 'password1',
    'student2': 'password2',
}

# Function to check login credentials
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in credentials and credentials[username] == password:
        messagebox.showinfo("Login Successful", "Welcome!")
        login_window.destroy()
        open_home_page()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to display information about wind turbines
def show_wind_turbine_info():
    info = """
    Wind Turbines Education Summary:

    - Wind turbines convert wind energy into electrical energy.
    - They have blades that spin when wind blows.
    - The spinning blades turn a rotor connected to a generator.
    - The generator produces electricity.

    Benefits:
    - Renewable energy source
    - Reduces carbon footprint
    - Can be installed on land or offshore
    """
    messagebox.showinfo("Wind Turbines", info)
    
    
def open_home_page():
    home_page = tk.Toplevel()
    home_page.title("Wind Turbine Education Kiosk")

    project_summary = """
    Welcome to the Wind Turbine Education Kiosk!

    This project aims to educate children about wind turbines.
    Wind turbines are devices that convert wind energy into electrical energy.
    They are an important part of renewable energy technology, helping to reduce our reliance on fossil fuels.

    Explore the kiosk to learn more about how wind turbines work, their benefits, and challenges.
    You can also test your knowledge with a fun quiz!
    """

    summary_label = tk.Label(home_page, text=project_summary, font=("Helvetica", 14), justify="left")
    summary_label.pack(pady=20)

    info_button = tk.Button(home_page, text="Learn about Wind Turbines", command=show_wind_turbine_info, font=("Helvetica", 14))
    info_button.pack(pady=10)

    quiz_button = tk.Button (home_page, text="Take Wind Turbine Quiz", command=start quiz, font=("Helvetica", 14))
    quiz_button.pack(pady=10) 


login_window = tk.Tk()
login_window.title("Login")

login_label = tk.Label(login_window, text="Enter your username and password to login", font=("Helvetica", 14))
login_label.pack(pady=10)

username_label = tk.Label(login_window, text="Username:", font=("Helvetica", 12))
username_label.pack(pady=5)
username_entry = tk.Entry(login_window, font=("Helvetica", 12))
username_entry.pack(pady=5)

password_label = tk.Label(login_window, text="Password:", font=("Helvetica", 12))
password_label.pack(pady=5)
password_entry = tk.Entry(login_window, show='*', font=("Helvetica", 12))
password_entry.pack(pady=5)

login_button = tk.Button(login_window, text="Login", command=check_login, font=("Helvetica", 12))
login_button.pack(pady=10)

login_window.mainloop()
