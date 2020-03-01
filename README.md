# Code Shortener

> **This application intended for internal usage**

Code Shortener is simple CLI application to save your money made with [click](https://click.palletsprojects.com/en/7.x/) and [python-docx](https://python-docx.readthedocs.io/en/latest/) library

## Requirement

* Python 3
* Click
* Python-docx
* Requests

```
pip install click python-docx requests
```

## Bug / Missing Feature

* Automated page numbering on footer
* Sometimes character 'ï»¿' appears

## Usage

```
Usage: main.py [OPTIONS] PATH

  Simple program that save your money

Options:
  --markup                 Indicate code is markup
  --max-char INTEGER       Maximum character in a line.
  --max-semicolon INTEGER  Maximum semicolon in a line.
  --to-docx                Generate .docx contains shortened code
  --docx-name TEXT
  --docx-id TEXT
  --docx-title TEXT
  --help                   Show this message and exit.
```

### Basic example

* Shorten single semicolon file

```
python main.py ./index.php
```

* Shotern single markup file

```
python main.py ./index.html --format=markup
```

* Shorten semicolon files in directory

```
python main.py ./model
```

* Shorten markup files in directory

```
python main.py ./view --format=markup
```

* **Only** create docs from directory

```
python main.py ./src --format=same --to-docx
```

### Advance example

* Shorten single semicolon file, configure max char & configure max semicolon

```
python main.py ./index.php --max_char=120 --max_semicolon=4
```

* Create .docx from semicolon

```
python main.py ./src --to-docx --docx-name="Bob" --docx-id=123 --docx-title="Fibonacci Code"
```

* Create .docx from markup & specify filename

```
python main.py ./view --format=markup --to-docx --docx-filename=result.docx --docx-name="Bob" --docx-id=123 --docx-title="Web UI"
```
