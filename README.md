# Python 100 days of code

## Environments

We are going to use the python-100-days virtual environment for the project.
We are going to create a folder per day and in case we need to install
something really different to the virtual environment global for the project
then we can create a new virtual environment for that day.

## Setup Global Environment

1. Install pyenv and pyenv-virtualenv
2. Install Python 3.12.3

   ```bash
   pyenv install 3.12.3
   ```

3. Create a virtual environment for the project

   ```bash
   pyenv virtualenv 3.12.3 python-100-days
   ```

4. set as local python version

   ```bash
   pyenv local python-100-days
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
