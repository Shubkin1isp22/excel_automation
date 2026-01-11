import customtkinter as ctk
import jsons, sql, assets
from tkinter import filedialog

class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x390")
        self.title("from excel")

        # Переменные изменяемых строк
        self.path_var = ctk.StringVar(value="")     # Для инпута с путём к excel файлу
        self.sql_var = ctk.BooleanVar(value=False)  # Для значения чекбокса sql
        self.json_var = ctk.BooleanVar(value=False) # Для значения чекбокса json
        self.yaml_var = ctk.BooleanVar(value=False) # Для значения чекбокса yaml
        self.error_var = ctk.StringVar(value="")    # Для надписи с ошибками

        # bind подписывает функцию update_width на событие Configure(Изменение окна)
        self.bind("<Configure>", self.update_width)
        
        # Кнопка выбора excel файла
        self.button_choose_file = ctk.CTkButton(self, text="Выбрать файл", height=40, corner_radius=5, command=self.choose_file)
        self.button_choose_file.pack(side='top', fill='x', pady=20, padx=20)

        # Поле вывода пути к файлу excel
        self.excel_file_path_entry = ctk.CTkEntry(self, placeholder_text="Путь к excel файлу", textvariable=self.path_var, height=40, corner_radius=5)
        self.excel_file_path_entry.pack(side='top', fill='x', padx=20)

        # Строка для вывода ошибок
        self.errors_label = ctk.CTkLabel(self, text_color="red", justify='left', textvariable=self.error_var)
        self.errors_label.pack(pady=5, padx=20, side='top', fill='x')

        # Кнопка создать файлы (sql, json, yaml)
        self.main_button = ctk.CTkButton(self, text = "Создать файлы", height=40, corner_radius=5, command=self.main_command)
        self.main_button.pack(side='bottom', fill='x', pady=20, padx=20)

        # Фрейм с чекбоксами - класс CheckBoxFrame
        self.checkbox_frame = CheckBoxFrame(master=self, sql_var=self.sql_var, json_var=self.json_var, yaml_var=self.yaml_var)
        self.checkbox_frame.pack(pady=(5, 20),padx=20, ipady=2, ipadx=5, side='top', anchor='w')

    # Изменяет настроийки переноса строки в error_label
    def update_width(self, event):
        self.errors_label.configure(wraplength = event.width - 40)

    # Обрабатывает нажатие на кнопку "Создать файлы"
    def main_command(self):
        if self.path_var.get() != "":
            self.filtered_data, self.filteres_2list, error = assets.get_lists(self.path_var.get())
            try:
                if not error:
                    checkboxes = [
                        self.is_sql(),
                        self.is_json(),
                        self.is_yaml()
                    ]
                    parsing_files = [
                        sql.get_sql(self.filtered_data, self.filteres_2list),
                        jsons.get_jsons(self.filtered_data),
                        "pass"
                    ]
                    for i in range(len(checkboxes)):
                        if checkboxes[i]:
                            parsing_files[i]
                else:
                    self.error_var.set(error)
            except AttributeError as e:
                self.error_var.set(f"Ошибка: {e}")


    # Функция окна выбора файла
    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path != "":
            self.excel_file_path_entry.delete(0, "end")
            self.path_var.set(file_path)

    # Функции возвращающие статус чекбоксов
    def is_sql(self):
        return self.sql_var.get()
    
    def is_json(self):
        return self.json_var.get()
    
    def is_yaml(self):
        return self.yaml_var.get()
    
    # Выводят в консоль  bool срабатывание чекбоксов
    def is_sql_checkbox(self):
        print(self.is_sql())
    
    def is_json_checkbox(self):
        print(self.is_json())
    
    def is_yaml_checkbox(self):
        print(self.is_yaml())

# Класс с чекбоксами sql | json |yaml
class CheckBoxFrame(ctk.CTkFrame):
    def __init__(self, master, sql_var, json_var, yaml_var, **kwargs):
        super().__init__(master, **kwargs)

        # Изменяемые строки состояния чекбоксов(sql, json, yaml)
        self.sql_var = sql_var
        self.json_var = json_var
        self.yaml_var = yaml_var

        # Чекбокс sql
        checkbox_sql = ctk.CTkCheckBox(self, text='Sql', font=("Arial", 17), checkbox_width=20, checkbox_height=20, corner_radius=3, border_width=2, variable=self.sql_var, onvalue=True, offvalue=False, command=master.is_sql_checkbox)
        checkbox_sql.pack(pady=5, padx=(5,20))

        # Чекбокс json
        checkbox_json = ctk.CTkCheckBox(self, text='Json', font=("Arial", 17), checkbox_width=20, checkbox_height=20, corner_radius=3, border_width=2, variable=self.json_var, onvalue=True, offvalue=False, command=master.is_json_checkbox)
        checkbox_json.pack(pady=5, padx=(5,20))
        
        # Чекбокс yaml
        checkbox_yaml = ctk.CTkCheckBox(self, text='Yaml', font=("Arial", 17), checkbox_width=20, checkbox_height=20, corner_radius=3, border_width=2, variable=self.yaml_var, onvalue=True, offvalue=False, command=master.is_yaml_checkbox)
        checkbox_yaml.pack(pady=5, padx=(5,20))




app = Gui()
app.mainloop()