# 爬取国家社科基金涉东南亚项目信息
Python 3.12.4 is used. It is recommended to create a virtual environment (venv) and install `requirements.txt`.

## How to create virtual environment

Run the following command in the terminal at the root of the project:
```bash
python3 -m venv .
```

## How to install the dependencies to a virtual environment

Run the following command in the terminal at the root of the project:
```bash
pip install -r requirements.txt
```

## How to generate `requirements.txt` (note to self)
Only run this if you know what you're doing
```bash
pipreqs --ignore bin,etc,include,lib,lib64 --force
```

## How to rerun the scraper from scratch (only when necessary)
1. Back up and delete `job_info.json`.
2. Back up and delete `SEAASEAN.csv`.
3. Run `main.py`.

# How to change add more keywords to scraper

1. Add keywords in `main.py`
2. Run `main.py`
