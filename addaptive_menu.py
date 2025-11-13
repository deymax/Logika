from customtkinter import *

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Adaptive Menu")

        self.menu = CTkFrame(self, width=30, height=300)
        self.menu.place(x=0, y=0)
        self.is_open = False
        self.speed = 5

        self.toggle_btn = CTkButton(self, text="▶️", width=30, command=self.toggle_menu)
        self.toggle_btn.place(x=0, y=0)

    def toggle_menu(self):
        self.is_open = not self.is_open
        self.toggle_btn.configure(text="◀️" if self.is_open else "▶️")
        self.animate_menu()

    def animate_menu(self):
        width = self.menu.winfo_width()
        if self.is_open and width < 200:
            self.menu.configure(width=width + self.speed)
            self.after(10, self.animate_menu)
        elif not self.is_open and width > 30:
            self.menu.configure(width=width - self.speed)
            self.after(10, self.animate_menu)

App().mainloop()
