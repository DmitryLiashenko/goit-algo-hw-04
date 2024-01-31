                              # ФУНКЦЫЯ ДЛЯ РАСЧЕТА СУММЫ И СРЕДНЕЙ ЗП
from pathlib import Path
import re
def total_salary(path = None):
    payroll = ()
    with open(path, 'r', encoding='utf-8') as fh:
        lines = [el.strip() for el in fh.readlines()]
        for line in lines:
            pass
    return payroll
total_salary(r'D:\IT\Repositorys\goit-algo-hw-04\GoIT-hw-4-1\file1.txt.txt')
