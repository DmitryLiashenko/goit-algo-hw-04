from pathlib import Path

def total_salary(path = None):
    with open('file.txt', 'r') as fh:
        line = [el.strip() for el in fh.readlines()]
        