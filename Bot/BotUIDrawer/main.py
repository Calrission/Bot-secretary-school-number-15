import pathlib
from pathlib import Path
from tkinter import *


class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title('Секретарь школы №15 С УИОП г. Электросталь')
        self.root.geometry('700x500')
        self.root.wm_iconbitmap(bitmap=str(Path(pathlib.Path.cwd(), "media_files", "icon.ico")))
        self.root.resizable(width=False, height=False)

        # top frame
        self.input_frame = Frame(self.root, height=100, pady=25, padx=5)
        self.input_frame.pack(fill=X)

        # bottom frame
        self.info_frame = Frame(self.root, height=400, padx=15)
        self.info_frame.pack(fill=X)

        self.lbl_name = Label(self.input_frame, text='Что вы хотите узнать', font=12)
        self.lbl_name.pack(side=LEFT)

        self.ent_name = Entry(self.input_frame, font=15, width=50)
        self.ent_name.focus()  # поле ввода сразу становится активным
        self.ent_name.pack(side=LEFT)

        Frame(self.root, width=10).pack(side=LEFT)  # Для отступа между полем ввода и кнопкой

        self.btn_search = Button(self.input_frame, text='Узнать', width=10)
        self.btn_search.pack(side=LEFT)

        # Scroll фрагмента
        self.scrollbar = Scrollbar(self.info_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.txt_widget = Text(self.info_frame, yscrollcommand=self.scrollbar.set, font=15)
        self.txt_widget.configure(state='disabled')  # для отмены возможности изменения текста
        self.txt_widget.pack(fill='both')
        self.scrollbar.config(command=self.txt_widget.yview)

    def get_text_user_input(self):
        return self.ent_name.get()

    def clear_text_user_input(self):
        return self.ent_name.delete(0, END)

    def set_text_output(self, text: str):
        self.txt_widget.insert('end', text)

    def set_new_text_output(self, text: str):
        self.clear_text_output()
        self.set_text_output(text)

    def clear_text_output(self):
        self.txt_widget.delete(0, END)

    def show_choose_variants(self, variants: list):
        str_list = "/n".join(f"{index + 1} " + variant for index, variant in enumerate(variants))
        self.set_new_text_output(f"Выберите вариант\n{str_list}")

    def show_object_variant(self, object_str: str):
        self.set_new_text_output(object_str)

    def set_click_button(self, function):
        self.btn_search.bind('<Button-1>', function)
        self.ent_name.bind("<Return>", function)

    def set_image(self, image_src: str):
        # Замена картинки персонажа
        pass

    def set_image_gif(self, gif_src: str):
        # Замена картинки персонажа на gif
        pass

    def run_app(self):
        # запуск приложения
        self.root.mainloop()
