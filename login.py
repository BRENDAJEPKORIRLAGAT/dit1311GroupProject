import tkinter as tk
from tkinter import messagebox

credentials = {
    'user1': 'password1',
    'user2': 'password2',
}

def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in credentials and credentials[username] == password:
        messagebox.showinfo("Login Successful", "Welcome!")
        login_window.destroy()
        open_main_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def show_wind_turbine_info():
    info = """
    Wind turbines convert wind's kinetic energy into electrical energy.
    They are a clean and renewable energy source.
    The blades spin when wind blows, turning a rotor connected to a generator.
    """
    messagebox.showinfo("Wind Turbines", info)


    close_button = tk.Button( quiz_text ="Close Quiz", command=quiz_text.destroy)
    close_button.pack(pady=10)

def open_main_menu():
    main_menu = tk.Toplevel()
    main_menu.title("Science Museum Interactive Kiosk")

    welcome_label = tk.Label(main_menu, text="Welcome to the Wind Turbine Interactive Kiosk!", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    info_button = tk.Button(main_menu, text="Learn about Wind Turbines", command=show_wind_turbine_info, font=("Helvetica", 14))
    info_button.pack(pady=10)

    quiz_button = tk.Button(main_menu, text="Take Wind Turbine Quiz", command=start_quiz, font=("Helvetica", 14))
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
