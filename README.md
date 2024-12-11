# 爬取国家社科基金涉东南亚项目信息
Python 3.13 is used. It is recommended to create a virtual environment (venv) and install dependencies using [uv](https://docs.astral.sh/uv/).

## How to create virtual environment and install dependencies using uv

If uv is not installed, install uv following the instructions [here](https://docs.astral.sh/uv/getting-started/installation/).

Then, run the following command in the terminal at the root of the project to automatically sync the environment:

```bash
uv sync
```

## How to create virtual environment and install dependencies using the traditional method (not recommended)

Run the following command in the terminal at the root of the project to create a virtual environment:
```bash
python3 -m venv .
```

Run the following command in the terminal at the root of the project to install dependencies:
```bash
pip install -r requirements.txt
```

## How to rerun the scraper from scratch (only when necessary)
1. Back up and delete `job_info.json`.
2. Back up and delete `SEAASEAN_raw.csv`.
3. Run `main.py`.

# How to change add more keywords to scraper

1. Add keywords in `main.py`
2. Run `main.py`

## How to clean the data (after scraping)

You may find that there are duplicate entries in the data, especially when the same project contains multiple keywords of interest. Run `clean.py` to clean the data.