import tkinter as tk

def finish(): 
    root.destroy()


# Define the quest structure as a dictionary
story = {
    "start": {
        "text": "Where are you going?",
        "choices": {
            "Go Left": "cave",
            "Go Right": "river"
        }
    },
    "cave": {
        "text": "You find a cave with strange symbols. Do you enter or go back?",
        "choices": {
            "Enter": "treasure",
            "Go Back": "start"
        }
    },
    "river": {
        "text": "A raging river blocks your path. Do you try to swim or turn back?",
        "choices": {
            "Swim": "drown",
            "Turn Back": "start"
        }
    },
    "treasure": {
        "text": "Inside the cave, you find a treasure chest filled with gold. You win!",
        "choices": {}
    },
    "drown": {
        "text": "The current is too strong. You drown. Game Over.",
        "choices": {}
    }
}

class main:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Quest Adventure")
        self.root.geometry("1920x1080")
        self.root.configure(bg="black")

        self.menu()

    def menu(self):
        self.clear_screen()
        self.title_label = tk.Label(self.root, text="Baldur's Gate 4: Viruses and Registration Edition", font=("Arial", 40, "bold"), fg="Yellow", bg="black")
        self.title_label.pack(pady=50)

        self.start_button = tk.Button(self.root, text="Start", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", font=("Arial", 14), command=self.root.quit)
        self.exit_button.pack(pady=10)
    def start_game(self):
        """Begins the game by showing the first scene."""
        self.current_scene = "start"
        self.show_scene()
    def show_scene(self):
        """Displays the current scene's text and choices."""
        self.clear_screen()

        scene = story[self.current_scene]
        self.story_label = tk.Label(self.root, text=scene["text"], wraplength=400, font=("Arial", 14), fg="white", bg="black")
        self.story_label.pack(pady=20)

        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack()

        for choice, next_scene in scene["choices"].items():
            btn = tk.Button(self.button_frame, text=choice, font=("Arial", 12),command=lambda next_scene=next_scene: self.change_scene(next_scene))
            btn.pack(pady=5)

        # Add a "Main Menu" button if the player loses or wins
        if not scene["choices"]:
            self.menu_button = tk.Button(self.root, text="Main Menu", font=("Arial", 12), command=self.menu)
            self.menu_button.pack(pady=10)
    
    def change_scene(self, scene):
        """Moves to the next scene."""
        self.current_scene = scene
        self.show_scene()

    def clear_screen(self):
        """Removes all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()
# Run the game
root = tk.Tk()
game = main(root)
root.mainloop()
