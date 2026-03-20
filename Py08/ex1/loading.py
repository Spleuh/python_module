from importlib import import_module
from sys import exit
from typing import Any


def get_version(depend_name: str) -> str:
    module = import_module(depend_name)
    version = module.__version__
    return version

def check_dependencies(lst_depend: list[str]) -> bool:
    check_all = True
    for depend_name in lst_depend:
        version = safe_exec(get_version, depend_name=depend_name)
        if version:
            print(f'[OK] {depend_name} ({version})')
        else:
            check_all = False
            print(f'[KO] {depend_name} is missing')
    return check_all

def safe_exec(func: callable, **kwargs) -> Any:
     try:
        return func(**kwargs)
     except FileNotFoundError as e:
        print(f'File error: {e}')
        return None
     except ImportError as e:
        print(f'Import error: ', end='')
        return None
     except Exception as e:
        print(f'{e}')
        return None



def get_lst_depend(file: str) -> list[str]:
    lst_depend = []
    with open(file, 'r') as f:
        lst_depend = f.read().split('\n')
    return lst_depend

def demo_gen_data() -> None:
    from pandas import DataFrame
    from numpy.random import randn
    print('\nAnalyzing Matrix data...')
    print('Processing 1000 data points...')
    print('Generating visualization...')
    data = randn(1000)
    data_frame = DataFrame(data, columns=['data'])
    print(data_frame)

    print('\nAnalysis complete!')

def main():
    print('LOADING STATUS: Loading programs...\n')
    print('Checking dependencies:')
    lst_depend = None
    lst_depend = safe_exec(get_lst_depend, file='requirements.txt')
    if not lst_depend:
        exit(1)
    check_all = check_dependencies(lst_depend)
    if not check_all:
        print('Please install missing dependencies then run this program again.\n')
        print('with pip: ')
        print('create venv : python3 -m venv matrix_env')
        print('activate venv : source matrix_env/bin/activate')
        print('install requirements : pip install -r requirments.txt\n')
        print('with poetry:')
        print('create and install dependencies: poetry install')
        print("activate venv manually: -get path to env with ('poetry env info --path') then activate with ('source <path>/bin/activate')")
        print("OR execute programme with this command: poetry run python loading.py")
        exit(1)
    else:
        demo_gen_data()

if __name__ == '__main__':
    main()