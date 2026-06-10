# PDF-countier

Ноутбук считает частоты терминов из PDF-статей, строит CSV-таблицы, частотные графики и матрицы связей терминов.

## Что входит в папку

- `PDF-countier.ipynb` - основной Jupyter notebook.
- `term_dictionary.xlsx` - словарь терминов, лист `terms`, колонки `level`, `label`, `aliases`.
- `requirements.txt` - Python-зависимости.
- `verify_setup.py` - быстрая проверка, что файлы и зависимости на месте.

`PDF-countier.ipynb` уже сохранен выполненным: в файле есть итоговые таблицы и графики.

Исходные PDF-файлы не включены в репозиторий из-за большого размера. Их можно скачать с Google Drive:

[Папка PDF на Google Drive](https://drive.google.com/drive/folders/1wN5CNiVv-mYsG3-5-Uhd8PV1qFyOjURW?usp=sharing)

## Проверенная структура данных

- В исходном наборе данных находится 801 PDF-файл.
- Файл `term_dictionary.xlsx` содержит лист `terms`.
- В словаре 118 непустых терминов.
- Выходные папки `texts/`, `frequency_outputs/`, `matrix_outputs/`, `tables/` создаются ноутбуком автоматически и не обязательны для GitHub, потому что результаты уже встроены в выполненный `.ipynb`.

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Перед повторным запуском ноутбука скачайте PDF-файлы с Google Drive и положите их в папку `PDF/` рядом с файлом `PDF-countier.ipynb`:

```text
PDF-countier.ipynb
term_dictionary.xlsx
PDF/
  article_1.pdf
  article_2.pdf
  ...
```

После запуска откройте `PDF-countier.ipynb` и выполните ячейки сверху вниз.

## Важные замечания

- Папка `PDF/` весит около 2.8 GB, поэтому она хранится отдельно на Google Drive и добавлена в `.gitignore`.
- Отдельных PDF-файлов больше 95 MB не найдено.
- Ноутбук использует параллельную обработку через `multiprocessing` с режимом `fork`, поэтому рассчитан на macOS/Linux. На Windows лучше запускать его через WSL/Linux.
- Генерируемые результаты не нужно хранить в Git: они добавлены в `.gitignore` и пересоздаются при запуске ноутбука.
