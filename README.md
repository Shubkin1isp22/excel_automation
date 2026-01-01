# Excel маппинг - ddl таблицы, <br> json,<br>  yaml.

## Для запуска:
#### В консоли выполняем следующие команды:
```
python -m venv myenv
```
```
source myenv/bin/activate
```
```
pip install pandas
```
#### Запуск скрипта через:
```
python sql.py
```

## После выполнения скрипта:
#### В корневой директории должен появиться каталог tables_sql, а в неём все ddl таблицы, сформированные из excel-файла.
```
excel_automation
    |__sql.py
    |
    |__tables_sql
        |
        |__filename.sql
        |
        |__anotherfilename.sql
```
#### by shekspii