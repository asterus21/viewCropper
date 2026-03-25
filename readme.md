The current script is aimed to automatically crop windows of the PolyAnalyst nodes to save time for the Technincal writers team when making nodes settings windows screenshots (see examples). Only those files starting with "Screenshot_" are processed by default.

The script logic is defined via a use of flags, i.e.

* `-h`, `--help`    – show this help message and exit
* `-w`, `--wizard`  – flag to process only wizards (used by default when no flag is given)
* `-v`, `--view`    – flag to process only views
* `-t`, `--type`    – flag to show types of screenshots
* `-d`, `--dir`     – flag to start the script in the current folder
* `-c`, `--cropped` – flag to process only those screenshots which start with "Cropped_"
* `-b`, `--both`    – flag to process both wizards and views
* `-x`, `--width`   – width value to process views
* `-y`, `--height`  – height value to process views
* `-f`, `--file`    – path value to process a single file
* `-a`, `--all`     – flag to process not only those screenshots which start with "Screenshot_" but all of them (except "Cropped_")

Examples (via Windows PowerShell):

- default (process wizards implicitly):

`py .\main.py`

- process wizards (explicitly):

`py .\main.py -w`

- process only views:

`py .\main.py -v`

- process views by 100 pixels (and 761 high by default):

`py .\main.py -x 100`

- process views 100 pixels high (and 1271 wide by default):

`py .\main.py -y 100`

- process views 100 pixels wide and 100 high:

`py .\main.py -x 100 -y 100`

- process views 200 pixels high and 400 wide:

`py .\main.py -y 200 -x 400`

- process a single file (only a wizard):

`py .\main.py -f D:/folder/Screenshot_1.png`

- process a single file (only a view):

`py .\main.py -f D:/folder/Screenshot_1.png -v`

- process a single view by 200 pixels high and 400 wide:

`py .\main.py -f D:/folder/Screenshot_1.png -y 200 -x 400`

- process a single view by на 600 pixels wide and 300 high:

`py .\main.py -v -x 600 -y 300 -f D:/folder/Screenshot_1.png`

- show screenshot types:

`py .\main.py -t`

- process all wizards in the current folder:

`py .\main.py -d`

- process all views in the current folder:

`py .\main.py -d -v`

- process all views in the current folder by 200 pixels high and 400 wide:

`py .\main.py -d -v -y 200 -x 400`

- process all wizards and views in the current folder:

`py .\main.py -b -d`

- process all view screenshot files that start with "Cropped_":

`py .\main.py -c -v`

- process all wizard screenshot files that start with any character, i.e. not only with "Screenshot_" (but not "Cropped_"):

`py .\main.py -a -w`

---

Данный скрипт используется для автоматического "нарезания" окон узлов в PolyAnalyst, что позволит команде Технических писателей сократить время на ручное "нарезание" скриншотов (см. папку examples). По умолчанию обрабатываются только скриншоты, которые начинаются на "Screenshot_".

Работа скрипта определяется с помощью флагов:

* `-h`, `--help`    – показать флаги и завершить работу
* `-w`, `--wizard`  – флаг для работы только с визардами (используется по умолчанию, если флаг не задан)
* `-v`, `--view`    – флаг для работы только с вьюшками
* `-t`, `--type`    – флаг для отображения типов скриншотов
* `-d`, `--dir`     – флаг для запуска скрипта в текущей папке
* `-c`, `--cropped` – флаг для обработки только тех скриншотов, которые начинаются с "Cropped_"
* `-b`, `--both`    – флаг для обработки как визардов, так и вьюшек
* `-x`, `--width`   – значение ширины для обработки вьюшек
* `-y`, `--height`  – значение высоты для обработки вьюшек
* `-f`, `--file`    – путь к файлу для обработки одного файла
* `-a`, `--all`     – флаг для обработки только всех скриншотов, которые начинаются не только с "Screenshot_" (кроме "Cropped_")

Примеры (через Windows PowerShell):

- по умолчанию (неявно обрезать визарды):

`py .\main.py`

- обрезать визарды (явно):

`py .\main.py -w`

- обрезать только вьюшки:

`py .\main.py -v`

- обрезать вьюшки на 100 пикселей в ширину (и 761 в высоту по умолчанию):

`py .\main.py -x 100`

- обрезать вьюшки на 100 пикселей в высоту (и 1271 в ширину по умолчанию):

`py .\main.py -y 100`

- обрезать вьюшки на 100 пикселей в ширину и 100 в высоту:

`py .\main.py -x 100 -y 100`

- обрезать вьюшки на 200 пикселей в высоту и 400 в ширину:

`py .\main.py -y 200 -x 400`

- обрезать отдельный файл (только визард):

`py .\main.py -f D:/folder/Screenshot_1.png`

- обрезать отдельный файл (только вьюшка):

`py .\main.py -f D:/folder/Screenshot_1.png -v`

- обрезать отдельный файл вьюшки на 200 пикселей в высоту и 400 в ширину:

`py .\main.py -f D:/folder/Screenshot_1.png -y 200 -x 400`

- обрезать отдельный файл вьюшки на 600 пикселей в ширину и 300 в высоту:

`py .\main.py -v -x 600 -y 300 -f D:/folder/Screenshot_1.png `

- показать только типы скриншотов:

`py .\main.py -t`

- сразу обрезать все скриншоты визардов в текущей папке:

`py .\main.py -d`

- сразу обрезать все скриншоты вьюшек в текущей папке:

`py .\main.py -d -v`

- сразу обрезать все скриншоты вьюшек в текущей папке на 200 пикселей в высоту и 400 в ширину:

`py .\main.py -d -v -y 200 -x 400`

- обрезать визарды и вьюшки в текущей папке:

`py .\main.py -b -d`

- обрезать вьюшки, которые начинаются на "Cropped_":

`py .\main.py -c -v`

- обрезать визарды, которые начинаются на любую последовательность символов, включая "Screenshot_" (кроме "Cropped_"):

`py .\main.py -a -w`
