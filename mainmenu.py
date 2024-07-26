import tkinter as tk
from tkinter import messagebox

def show_wind_turbine_info():
    info = """
    Wind turbines are devices that convert the wind's kinetic energy into electrical energy.
    They are a clean and renewable source of power. Wind turbines have blades that spin
    when the wind blows. The spinning blades turn a rotor connected to a generator, which
    produces electricity.
    """
    messagebox.showinfo("Wind Turbines", info)

def start_game():
    game_window = tk.Toplevel()
    game_window.title("Wind Turbine Game")
    
    game_label = tk.Label(game_window, text="Find the Windy Spot!", font=("Helvetica", 14))
    game_label.pack(pady=20)
    

    game_info = tk.Label(game_window, text="Game logic goes here", font=("Helvetica", 12))
    game_info.pack(pady=10)
    
    close_button = tk.Button(game_window, text="Close Game", command=game_window.destroy)
    close_button.pack(pady=10)


def start_quiz():
    quiz_window = tk.Toplevel()
    quiz_window.title("Wind Turbine Quiz")

    question_label = tk.Label(quiz_window, text="What is the primary function of a wind turbine?", font=("Helvetica", 14))
    question_label.pack(pady=10)

    options = [
        ("Convert wind energy to electrical energy", True),
        ("Pump water", False),
        ("Measure wind speed", False),
        ("Generate heat", False)
    ]

    def check_answer(is_correct):
        if is_correct:
            messagebox.showinfo("Quiz", "Correct!")
        else:
            messagebox.showinfo("Quiz", "Incorrect. Try again!")

    for text, is_correct in options:
        button = tk.Button(quiz_window, text=text, command=lambda is_correct=is_correct: check_answer(is_correct), font=("Helvetica", 12))
        button.pack(pady=5)

    close_button = tk.Button(quiz_window, text="Close Quiz", command=quiz_window.destroy)
    close_button.pack(pady=10)

root = tk.Tk()
root.title("Science Museum Interactive Kiosk")

welcome_label = tk.Label(root, text="Welcome to the Wind Turbine Interactive Kiosk!", font=("Helvetica", 16))
welcome_label.pack(pady=20)

info_button = tk.Button(root, text="Learn about Wind Turbines", command=show_wind_turbine_info, font=("Helvetica", 14))
info_button.pack(pady=10)


game_button = tk.Button(root, text="Play Wind Turbine Game", command=start_game, font=("Helvetica", 14))
game_button.pack(pady=10)


quiz_button = tk.Button(root, text="Take Wind Turbine Quiz", command=start_quiz, font=("Helvetica", 14))
quiz_button.pack(pady=10)


root.mainloop()
