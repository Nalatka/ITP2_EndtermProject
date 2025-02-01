import tkinter as tk

def finish(): 
    root.destroy()

#Сцены создавать по шаблону Название сцены(Текст сцены) - выбор choices - опции - выбор опции перенаправляет на следующую сцену
story = {
    "start": {
        "text": "Проснись! Быть выбранным судьбой является большой честью для любой души. Для какой же цели ты был выбран? Сам поймешь, а сейчас выберись хотя-бы из этого подземелья!",
        "choices": {
            "Проснуться": "chamber",
            "Лежать": "dreaming"
        }
    },
    "chamber":{
        "text":"test",
        "choices":{
            }
        }
}
class main():
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
        self.current_scene = "start"
        self.show_scene()
    def show_scene(self):
        self.clear_screen()
        #создает сцену
        scene = story[self.current_scene]
        self.story_label = tk.Label(self.root, text=scene["text"], wraplength=400, font=("Arial", 14), fg="white", bg="black")
        self.story_label.pack(pady=20)

        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack()
        #создает кнопки выбора
        for choice,next_scene in scene["choices"].items():
            btn = tk.Button(self.button_frame, text=choice, font=("Arial", 12),command=lambda next_scene=next_scene: self.change_scene(next_scene))
            btn.pack(pady=5)

        #если нет выбора, создает кнопку выхода в меню
        if not scene["choices"]:
            self.menu_button = tk.Button(self.root, text="Main Menu", font=("Arial", 12), command=self.menu)
            self.menu_button.pack(pady=10)
    
    def change_scene(self, scene):
        #меняет сцену
        self.current_scene = scene
        self.show_scene()

    def clear_screen(self):
        #убирает окно от виджетов(типа кнопок)
        for widget in self.root.winfo_children():
            widget.destroy()
root = tk.Tk()
game = main(root)
root.mainloop()
