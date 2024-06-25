### Hexlet tests and linter status:
[![Actions Status](https://github.com/Demidb/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Demidb/python-project-50/actions)

### Github Actions
[![hexlet-check](https://github.com/Demidb/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Demidb/python-project-50/actions/workflows/hexlet-check.yml)

### Main Actions
[![main-check](https://github.com/Demidb/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Demidb/python-project-50/actions/workflows/main.yml)

### Maintainability Badge
[![Maintainability](https://api.codeclimate.com/v1/badges/fca6b4618e70a644cdb8/maintainability)](https://codeclimate.com/github/Demidb/python-project-50/maintainability)

### Test Coverage Badge
<a href="https://codeclimate.com/github/Demidb/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/fca6b4618e70a644cdb8/test_coverage" /></a>

# Второй проект для Хекслет
Проект называется "Вычислитель отличий". В данном проекте мы сравниваем файлы между собой и в результате получаем  результат. Файлы разной сложности, в том числе с вложениями, поэтому выводы могут быть разными по длине.

- **Для установки проекта используйте команду**:
```
python3 -m pip install --user git+https://github.com/Xrustic/gendiff.git
```

## **Технологии**

Для создания данного проекта использовался Python версии 3.10. Чтобы установить последнюю версию нужно использовать команду:
```sh
sudo apt install python3
```

- Так же в проекте используется pip 19 версии и выше. Чтобы установить pip нужно использовать команду:
```sh
sudo apt -y install python3-pip
```

- Если необходимо обновить pip введите команду:
```sh
python3 -m pip install --upgrade --user pip
```

- Ещё в проекте используется poetry 1.2.0 версии и выше. Для установки poetry необходимо ввести команду:
```sh
pipx install poetry
```

### Как использовать?
Чтобы получить сравнение файлов, используйте команду с выбранным разрешением:
```
gendiff <file_name_1> <file_name_2>  -f <stylish/plain/json>
```

### Установка и билд
После изменения файлов с играми, вы можете проверить линтером:
```sh
make lint
```

- Так же необходимо пересобрать весь проект с помощью команд: 
```sh
make build

make publish

make package-install
```

## Команда проекта
Автор:
- [Демид Алексеев](https://github.com/Demidb)

### Аскинемы 
Аскинема 3 части проекта (Сравнение плоских файлов JSON): 
<a href="https://asciinema.org/a/FlaWXY4jqhAslGzxfaUf5XtrG" target="_blank"><img src="https://asciinema.org/a/FlaWXY4jqhAslGzxfaUf5XtrG.svg" /></a>

Аскинема 5 части проекта (Сравнение плоских файлов YAML): 
<a href="https://asciinema.org/a/j6cIBIrU2hYU3uTxiwaAOnOSL" target="_blank"><img src="https://asciinema.org/a/j6cIBIrU2hYU3uTxiwaAOnOSL.svg" /></a>

Аскинема 6 части проекта (Рекурсивное сравнение): 
<a href="https://asciinema.org/a/1XJxfxqmQIKQVM3u2rWoqrcnD" target="_blank"><img src="https://asciinema.org/a/1XJxfxqmQIKQVM3u2rWoqrcnD.svg" /></a>

Аскинема 7 части проекта (Плоский формат): 
<a href="https://asciinema.org/a/svrv5gXlj1bdjVbfZhsHQ4PGI" target="_blank"><img src="https://asciinema.org/a/svrv5gXlj1bdjVbfZhsHQ4PGI.svg" /></a>

Аскинема 8 части проекта (Вывод в JSON):
<a href="https://asciinema.org/a/FfvDKilDMY7H7IzNdpHvldUXz" target="_blank"><img src="https://asciinema.org/a/FfvDKilDMY7H7IzNdpHvldUXz.svg" /></a>
