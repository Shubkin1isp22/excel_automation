import pandas as pd
import os

def get_sql(filtered_data, filteres_2list):
    last_table_11 = "keyy"
    os.makedirs("tables_sql", exist_ok=True)
    for _, string in filtered_data.iterrows():
        if string['Колонка 11'] != last_table_11:
            with open(f"./tables_sql/{string['Колонка 11']}.sql", "w", encoding="utf-8") as f:
                
                # Дата-фрейм для каждой отдельной таблицы приёмника
                tgt_table_filter = filtered_data[filtered_data["Колонка 11"] == string['Колонка 11']]
                attr_data = tgt_table_filter

                # Атрибуты
                attrs = "\n,".join(
                    f"{string['Колонка 13']} {string['Колонка 14']} {string['Колонка 15'] if pd.notna(string['Колонка 15']) else "null"}"
                    for _, string in attr_data.iterrows()
                )
                
                keys = "noup"
                date_1str = filteres_2list[filteres_2list['Колонка 6'] == str(string['Колонка 11'])]
                if (string['Колонка 3'] == date_1str['Колонка 3'].iloc[0]) & (str(string['Колонка 4']).strip() == str(date_1str['Колонка 4'].iloc[0]).strip()):
                    keys = f"{date_1str["Колонка 13"].iloc[0]}"


                # Запись в sql
                f.write(f"DROP TABLE if exists {string['Колонка 11']} cascade;\n\nCREATE TABLE {string['Колонка 11']} (\n{attrs}\n)\nWITH (\n\tappendonly=true,\n\torientation=column,\n\tcompresstype=zstd,\n\tcompresslevel=1\n)\nDISTRIBUTED BY ({keys});\n\n")
                last_table_11 = string['Колонка 11']
        