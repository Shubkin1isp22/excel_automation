import pandas as pd
import os

column_names = ['Колонка 1', 'Колонка 2', 'Колонка 3', 'Колонка 4', 'Колонка 5', 
                'Колонка 6', 'Колонка 7', 'Колонка 8', 'Колонка 9', 'Колонка 10', 
                'Колонка 11', 'Колонка 12', 'Колонка 13', 'Колонка 14', 'Колонка 15', 
                'Колонка 16', 'Колонка 17', 'Колонка 18', 'Колонка 19', 'Колонка 20', 
                'Колонка 21', 'Колонка 22', 'Колонка 23', 'Колонка 24', 'Колонка 25', 
                'Колонка 26', 'Колонка 27', 'Колонка 28', 'Колонка 29', 'Колонка 30', 
                'Колонка 31', 'Колонка 32', 'Колонка 33', 'Колонка 34']
column_names_2 = ['Колонка 1', 'Колонка 2', 'Колонка 3', 'Колонка 4', 'Колонка 5', 
                'Колонка 6', 'Колонка 7', 'Колонка 8', 'Колонка 9', 'Колонка 10', 
                'Колонка 11', 'Колонка 12', 'Колонка 13', 'Колонка 14', 'Колонка 15', 
                'Колонка 16', 'Колонка 17', 'Колонка 18', 'Колонка 19', 'Колонка 20', 
                'Колонка 21', 'Колонка 22', 'Колонка 23']

def get_lists(file_name : str):
    if is_excel_file(file_name):
        try:
            dd = pd.read_excel(file_name, sheet_name="Детали загрузок Src-RDV", header=None) #объект листа "Детали загрузок Src-RDV"
            dd.columns = column_names
        except ValueError as e:
            list1_error = f"Файл {file_name} не прочитан\nОшибка: {e}"
            return None, None, list1_error
        
        try:
            df = pd.read_excel(file_name, sheet_name="Перечень загрузок Src-RDV", header=None)
            df.columns = column_names_2
        except ValueError as e:
            list2_error = f"Файл {file_name} не прочитан\nОшибка: {e}"
            return None, None, list2_error
        
        filtered_data = dd[dd["Колонка 2"].isnull() | (dd["Колонка 2"].astype(str).str.strip() == "")].sort_values(by="Колонка 11", ascending=True)
        filteres_2list = df[df["Колонка 2"].isnull() | (df["Колонка 2"].astype(str).str.strip() == "")]
        no_error = False
        return filtered_data, filteres_2list, no_error
    else:
        error_no_excel_file = f"Файл {file_name} не индетифицирован как excel-файл"
        return None, None, error_no_excel_file

def is_excel_file(filename):
    if os.path.isfile(filename):
        valid_extensions = (".xlsx", ".xlsm", ".xls", ".xlsb")
        return filename.lower().endswith(valid_extensions)
    else:
        return False