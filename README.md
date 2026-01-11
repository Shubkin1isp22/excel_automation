# Excel маппинг - ddl таблицы,  json,  yaml.

## Для запуска:
#### В консоли выполняем следующие команды:
##### 
##### Активация в MacOS:
```
source myenv/bin/activate
```
##### Активация в Windows:
```
.\venv\Scripts\activate
```

#### Запуск скрипта через:
```
python main.py
```

## После запуска скрипта:
![Изображение интерфейса программы](image.png)
## После выбора файла, проставления чекбоксов и создания файлов:
#### В корневой директории должны появиться каталоги tables_sql и jsons, а в них соответственно все ddl таблицы и json-файлы, сформированные из excel-файла.
```
excel_automation
    |__sql.py
    |
    |__tables_sql
    |   |
    |   |__filename.sql
    |   |
    |   |__anotherfilename.sql
    |
    |__jsons
        |
        |__filename.json
        |
        |__anotherfilename.json
```
#### by shekspii