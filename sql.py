import pandas as pd
import os
file_name = '/Users/shekspii/Desktop/excel_py/excel_fyles/Маппинг_ЦЕХ_RDV_OVRP_v2.0 (1).xlsx'

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

dd = pd.read_excel(file_name, sheet_name="Детали загрузок Src-RDV", header=None) #объект листа "Детали загрузок Src-RDV"
dd.columns = column_names

df = pd.read_excel(file_name, sheet_name="Перечень загрузок Src-RDV", header=None)
df.columns = column_names_2

filtered_data = dd[dd["Колонка 2"].isnull() | (dd["Колонка 2"].astype(str).str.strip() == "")].sort_values(by="Колонка 11", ascending=True)
filteres_2list = df[df["Колонка 2"].isnull() | (df["Колонка 2"].astype(str).str.strip() == "")]


for index_of_string, string in filtered_data.iterrows():
    last_table_11 = "keyy"
    if string['Колонка 11'] != last_table_11:
        with open(f"./tables_sql/{string['Колонка 11']}.sql", "w", encoding="utf-8") as f:
            # Дата-фрейм для каждой отдельной таблицы приёмника
            tgt_table_filter = filtered_data[filtered_data["Колонка 11"] == string['Колонка 11']]
            attr_data = tgt_table_filter

            # Атрибуты
            attrs = "\n".join(
                f"{string['Колонка 13']} {string['Колонка 14']} {string['Колонка 15'] if pd.notna(string['Колонка 15']) else "null"},"
                for _, string in attr_data.iterrows()
            )
            
            keys = "noup"
            date_1str = filteres_2list[filteres_2list['Колонка 6'] == str(string['Колонка 11'])]
            if (string['Колонка 11'] == date_1str['Колонка 6'].iloc[0]) & (string['Колонка 3'] == date_1str['Колонка 3'].iloc[0]) & (str(string['Колонка 4']).strip() == str(date_1str['Колонка 4'].iloc[0]).strip()):
                keys = f"{date_1str["Колонка 13"].iloc[0]}"


            # Запись в txt
            f.write(f"Строка {index_of_string + 1}\n")
            f.write(f"DROP TABLE if exists {string['Колонка 11']} cascade;\n\nCREATE TABLE {string['Колонка 11']} (\n{attrs}\n)\nWITH (\n\tappendonly=true,\n\torientation=column,\n\tcompresstype=zstd,\n\tcompresslevel=1\n)\nDISTRIBUTED BY ({keys});\n\n")
            last_table_11 = string['Колонка 11']
        