import pandas as pd
import os


def get_jsons(filtered_data):
    print("Jsons are making!")
    last_table_11 = "keyy"
    os.makedirs("jsons", exist_ok=True)
    for _, string in filtered_data.iterrows():
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