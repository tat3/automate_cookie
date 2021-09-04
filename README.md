# Automate Cookie

A tool to automate cookie production in Cookie Clicker.

## How it works

This tool uses PyAutoGui and in-game images to identify the coordinates to be manipulated.

## Note

This tool is not so stable.

* Some required packages may be missing from `requirements.txt`.
* You may need to adjust the parameters because the images it use may be dependent on my environment.
  - especially for `confidence` parameter of idleverse

## Usage

Install requirements.

```bash
$ python -V
Python 3.9.7
$ pip install -r requirements.txt
```

Run tool.

```bash
$ python src/click_cookie.py
```
