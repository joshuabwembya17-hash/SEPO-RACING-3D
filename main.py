class SEPORacing3D:
    def __init__(self):
        self.title = "SEPO Racing 3D"
        self.graphics_setting = "Realistic Graphics"

    def show_intro(self):
        print("Developed by Cross")

    def start_game(self):
        self.show_intro()
        print(f"Starting {self.title} with {self.graphics_setting} setting...")


if __name__ == '__main__':
    game = SEPORacing3D()
    game.start_game()