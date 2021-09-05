# Automate Cookie

A tool to automate cookie production in Cookie Clicker.

## How it works

This tool uses PyAutoGui and in-game images to identify the coordinates to be manipulated.

## Functionalities

This tool automatically

* click golden cookies
* click the main cookie, which you usually hit repeatedly using your mouse
* buy available idleverse facilities
* exit when you move your mouse to the upper left corner
  - within 100px x 100px in the screen


## Note

This tool is not so stable.

* Some required packages may be missing from `requirements.txt`.
* You may need to adjust the parameters because the images it use are dependent on my environment.
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
