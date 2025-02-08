import tkinter as tk

def finish(): 
    root.destroy()

#Сцены создавать по шаблону Название сцены(Текст сцены) - выбор choices - опции - выбор опции перенаправляет на следующую сцену
story = {
    "start": {
        "text": "Ты приходишь в себя в темной камере подземелья. Единственный источник света — факел, мерцающий на стене. В углу видна старая деревянная дверь. Что ты будешь делать?",
        "choices": {
            "Взять факел и осмотреться": "look_around",
            "Подойти к двери": "door"
        }
    },
    "look_around": {
        "text": "Ты поднимаешь факел и видишь на стенах странные руны. В полу что-то блестит — возможно, это ключ.",
        "choices": {
            "Взять ключ": "take_key",
            "Игнорировать руны и подойти к двери": "door"
        }
    },
    "take_key": {
        "text": "Ты поднимаешь ключ, но внезапно слышишь щелчок — ловушка! Стрелы вылетают из стен.",
        "choices": {
            "Прыгнуть в сторону": "dodge_arrows",
            "Закрыться факелом": "hit_by_arrows"
        }
    },
    "dodge_arrows": {
        "text": "Ты успеваешь уклониться от стрел, но одна всё же царапает твою руку. Теперь у тебя есть ключ и лёгкая рана.",
        "choices": {
            "Подойти к двери": "door_with_key"
        }
    },
    "hit_by_arrows": {
        "text": "Ты пытаешься закрыться факелом, но это не помогает. Стрелы пронзают тебя. Ты погибаешь в этом подземелье.",
        "choices": {
            # Конец игры
        }
    },
    "door": {
        "text": "Ты подходишь к двери и пытаешься открыть её. Она заперта. Кажется, нужен ключ.",
        "choices": {
            "Вернуться и осмотреть комнату": "look_around",
            "Попробовать выбить дверь": "break_door"
        }
    },
    "break_door": {
        "text": "Ты пытаешься выбить дверь, но срабатывает магическая ловушка. Вспышка ослепляет тебя, и ты теряешь сознание. Это конец.",
        "choices": {
            # Конец игры
        }
    },
    "door_with_key": {
        "text": "Ты используешь ключ, и дверь открывается с громким скрипом. За ней тёмный коридор, откуда доносится шорох.",
        "choices": {
            "Войти в коридор": "corridor",
            "Закрыть дверь и остаться в комнате": "stay_room"
        }
    },
    "stay_room": {
        "text": "Ты решаешь остаться в комнате, но через некоторое время слышишь, как дверь ломают с другой стороны. Монстры нашли тебя. Конец.",
        "choices": {
            # Конец игры
        }
    },
    "corridor": {
        "text": "Коридор ведет вглубь подземелья. На стенах — следы когтей. Ты слышишь странные звуки впереди.",
        "choices": {
            "Следовать за звуками": "monster_encounter",
            "Повернуть налево в узкий проход": "trap_room"
        }
    },
    "monster_encounter": {
        "text": "Ты выходишь в большую пещеру, где сталкиваешься с огромным троллем. У тебя нет оружия, чтобы сразиться с ним.",
        "choices": {
            "Попытаться убежать": "run_away",
            "Спрятаться за камнями": "hide"
        }
    },
    "run_away": {
        "text": "Ты пытаешься убежать, но тролль догоняет тебя и разрывает на части. Конец.",
        "choices": {
            # Конец игры
        }
    },
    "hide": {
        "text": "Ты прячешься за камнями, и тролль, пройдя мимо, не замечает тебя. Когда всё стихает, ты продолжаешь путь.",
        "choices": {
            "Пойти дальше по туннелю": "exit_path"
        }
    },
    "trap_room": {
        "text": "Ты входишь в узкий проход, но вдруг пол под тобой начинает проваливаться. Ты видишь рычаг на стене.",
        "choices": {
            "Прыгнуть к рычагу": "lever_save",
            "Попытаться перепрыгнуть через провал": "fall_to_pit"
        }
    },
    "lever_save": {
        "text": "Ты успеваешь дотянуться до рычага, и пол стабилизируется. Ты спасён.",
        "choices": {
            "Идти дальше": "exit_path"
        }
    },
    "fall_to_pit": {
        "text": "Ты не успеваешь перепрыгнуть и падаешь в шипастую яму. Это конец.",
        "choices": {
            # Конец игры
        }
    },
    "exit_path": {
        "text": "Ты находишь старую деревянную лестницу, ведущую наверх. Виднеется свет — это выход! Ты свободен... пока.","choices": {
            # Победа!
        }
    }
}
class main():
    def __init__(self, root):
        self.root = root
        self.root.title("Text Quest Adventure")
        self.root.geometry("1920x1080")

        self.menu()

    def menu(self):
        self.clear_screen()
        self.title_label = tk.Label(self.root, text="Baldur's Gate 4: Viruses and Registration Edition", font=("Arial", 40, "bold"), fg="Yellow", bg="black")
        self.title_label.pack(pady=50)

        self.start_button = tk.Button(self.root, text="Start", font=("Arial", 14), relief="raised", command=self.start_game)
        self.start_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", font=("Arial", 14), relief="raised", command=self.root.quit)
        self.exit_button.pack(pady=10)
    def start_game(self):
        self.current_scene = "start"
        self.show_scene()
    def show_scene(self):
        self.clear_screen()
        #создает сцену
        self.bg_image = Image.open("dungeon.png")  
        self.bg_image = self.bg_image.resize((1920,1080))  
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1) 
        scene = story[self.current_scene]
        self.story_label = tk.Label(self.root, text=scene["text"], wraplength=400, font=("Arial", 14), fg="white", bg="black")
        self.story_label.pack(pady=20)
        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack()
        #создает кнопки выбора
        for choice,next_scene in scene["choices"].items():
            btn = tk.Button(self.button_frame, text=choice, font=("Arial", 12), relief="raised",command=lambda next_scene=next_scene: self.change_scene(next_scene))
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
