# Setting Up

Firstly, your machine needs to have conda.

## Installation

We create and activate a new conda environment. We will use the packages that are available in the requirements.txt

```bash
conda create --name alotech python=3.5
conda activate alotech
conda install pip
pip install -r requirements.txt

```

In the root folder:

## Usage

```python
python manage.py runserver
```

URL: https://localhost:8000
