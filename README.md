# Python 100 days of code

## Environments

We are going to use the python-100-days virtual environment for the project.
We are going to create a folder per day and in case we need to install
something really different to the virtual environment global for the project
then we can create a new virtual environment for that day.

## Setup Global Environment

> [!IMPORTANT]
> If you are on Mac OS you need to install first `tcl-tk`
> before you install your python version 3.12.3

```bash
 brew install tcl-tk
```

1. Install pyenv and pyenv-virtualenv
2. Install Python 3.12.7

   ```bash
   pyenv install 3.12.7
   ```

3. Create a virtual environment for the project

   ```bash
   pyenv virtualenv 3.12.7 python-100-days
   ```

4. set as local python version

   ```bash
   pyenv local python-100-days
   ```

> [!NOTE]
> In case you haven't installed `tcl-tk` then you need to uninstall
> your python version and reinstall after install `tcl-tk`

```bash
 pyenv uninstall 3.12.3
 brew install tcl-tk
 pyenv install 3.12.3
```

## How to manage dependencies

- Use pip to install new packages

```bash
pip install <name-package>
```

- List dependencies

```bash
pip list
```

- Search packages

```bash
pip index versions <name-package>
```

- Update pip

```bash
python -m pip install --upgrade pip
```

## Linter y formater

We are using [ruff](https://docs.astral.sh/ruff/)

To check violations run

```bash
ruff check
```

To fix them

```bash
ruff check --fix
```

To include sort imports run

```bash
ruff check --select I --fix
```

To format the project

```bash
ruff format
```

## Index

- [Day 15](/day-15/main.py): Expresso Machine (functional programming)
- [Day 16](/day-16/main.py): Expresso Machine (with classes)
- [Day 17](/day-17/main.py): Question bank and use of lists
- [Day 18](/day-18/main.py): Multiple challengues with Turtle and color challengue
- [Day 19](/day-19/main.py): Turtle competition
- [Day 20](/day-20/main.py): Snake game using Turtle library
- [Day 22](/day-22/main.py): Pong game using Turtle library
- [Day 23](/day-23/main.py): Car game using Turtle library
- [Day 24](/day-24/main.py): Letter problem with Files
- Day 25:
  - [squirrel stats](/day-25/squirrel/main.py): Use of pandas to collect stats
  - [US states game](/day-25/us-states-game/main.py): GUI game with files and pandas
- [Day 26](/day-26/main.py): Nato Game - List and dict compresion to build data
  read from csv
- [Day 27](/day-26/main.py): Build GUI with Tkinter module and build miles to km converter
- [Day 28](/day-28/main.py): Build a Pomodoro GUI with Tkinter
- [Day 29](/day-29/main.py): Password Manager GUI with Tkinter
- [Day 30](/day-30/playground.py): Management of Exceptions, Errors and JSON data
- [Day 31](/day-31/main.py): Flash cards to translate beetween French and English --Pandas, tkinter --
- [Day 32](/day-32/main.py): Send birthday emails --smtplib and datetime--
   you need to create a "Password aplication" from your google administration
   account. Be sure you have rows with a birthday that correspond to today.
- Day 33: Build an API(Application Programming Interfaces)
  - Resources:
      - [status codes](https://www.webfx.com/web-development/glossary/http-status-codes/)
      - [requests library](https://docs.python-requests.org/en/latest/)
      - [location per coordenates](https://www.latlong.net/)
  - Code:
      - [Kanye GUI](/day-33/kanye-quotes-start/main.py): Use Kanye API to get
      quotes and show them in a GUI with tkinter
      - [ISS overhead email](/day-33/issoverhead/main.py): send and email when
      iss over our head (depending where you are lat,long)  
      - [Play with lat|long](/day-33/main.py)
- [Day 34](/day-34/main.py): Creating a GUI quiz that grab questions from an API(tkinter)
- [Day 35](/day-35/main.py): API Keys, Authentication & env variables -SMS usign Twilio-

   - Commands:

      ```shell
      env                       # list environment variables set in your terminal
      env | grep YOUR_VARIABLE   # look for YOUR_VARIABLE 
      export YOUR_VARIABLE=value # set YOUR_VARIABLE to value
      ```

   - Resources:
      - [Weather API](https://openweathermap.org/api)
      - [Json viewer](https://jsonviewer.stack.hu/)
      - [Weather Map](https://www.ventusky.com/)
      - [Whatsapp Sandbox](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn)
      