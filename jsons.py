import pandas as pd

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

last_table_11 = "keyy"
for index_of_string, string in filtered_data.iterrows():
    if string['Колонка 11'] != last_table_11:
        with open(f"./jsons/ceh.{string['Колонка 11']}.json", "w", encoding="utf-8") as f:
            
            # Дата-фрейм для каждой отдельной таблицы приёмника
            tgt_table_filter = filtered_data[filtered_data["Колонка 11"] == string['Колонка 11']]
            attr_data = tgt_table_filter
            ceh_name = f"ceh.{string['Колонка 11']}"

            columns = ",\n".join(
                f'{"\t" * 4}{"{"}\n{"\t" * 5}"name": "{string["Колонка 13"]}",\n{"\t" * 5}"type": "{string["Колонка 14"]}",\n{"\t" * 5}"primary_key": {"true" if string["Колонка 12"] == "PK" else "false"},\n{"\t" * 5}"nullable": {"true" if string["Колонка 15"] == "null" else "false"}\n{"\t" * 4}{"}"}'
                for _, string in attr_data.iterrows()
            )

            f.write(f'{"{\n"}\t"resource_desc": "table {ceh_name}",\n\t"tags": [\n{"\t" * 2}"",\n{"\t" * 2}""\n\t],\n\t"features": {{\n{"\t" * 2}"domain": "rdv"\n\t}},\n\t"metrics": {{\n{"\t" * 2}"{"istok"}_actual_dttm": {{\n{"\t" * 3}"id": "{ceh_name}",\n{"\t" * 3}"query": "[.last_sources[].conf.by_src | select(. != null) | .[] | to_entries | .[] | select(.key == \\"{"istok"}_actual_dttm\\" and .value != \\"default_value\\" and .value != null).value] | min",\n{"\t" * 3}"default": "default_value"\n{"\t" * 2}}}\n\t}},\n\t"resource_cd": "{ceh_name}",\n\t"is_readonly": false,\n\t"is_deleted": false,\n\t"datasets": [\n{"\t" * 2}{"{"}\n{"\t" * 3}"name": "{string["Колонка 11"][4:]}",\n{"\t" * 3}"schema_name": "rdv",\n{"\t" * 3}"filter": "",\n{"\t" * 3}"columns": {"["}\n{"\t" * -1}{columns}\n{"\t" * 3}{"]"}\n{"\t" * 2}{"}"}\n\t{"]"}\n{"}"}')
            
            last_table_11 = string["Колонка 11"]