from importlib import import_module
from sys import exit
from os import path, mkdir
from typing import Any, Callable


def get_version(depend_name: str) -> str:
    module = import_module(depend_name)
    version = getattr(module, "__version__", "unknown")
    return version


def get_info(depend_name: str) -> str:
    info = {
        'pandas': 'Data manipulation ready',
        'requests': 'Network access ready',
        'matplotlib': 'Vizualization ready',
        'numpy': 'Data generation ready'}
    return info[depend_name]


def check_dependencies(lst_depend: list[str]) -> bool:
    check_all = True
    for depend_name in lst_depend:
        version = safe_exec(get_version, depend_name=depend_name)
        if version:
            info = safe_exec(get_info, depend_name=depend_name)
            print(f'[OK] {depend_name} ({version}) - {info}')
        else:
            check_all = False
            print(f'[KO] {depend_name} is missing')
    return check_all


def safe_exec(func: Callable, **kwargs: Any) -> Any:
    try:
        return func(**kwargs)
    except FileNotFoundError as e:
        print(f'File error: {e}')
        return None
    except ImportError as e:
        print(f'Import error: {e}: ', end='')
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
    from pandas import DataFrame  # type: ignore
    from numpy.random import randn  # type: ignore
    from matplotlib import pyplot  # type: ignore
    print('\nAnalyzing Matrix data...')
    print('Processing 1000 data points...')
    print('Generating visualization...')
    data = randn(1000)
    data_frame = DataFrame(data, columns=['data'])
    data_frame['moyenne'] = data_frame['data'].expanding().mean()
    print(data_frame)
    pyplot.plot(data_frame['moyenne'])

    pyplot.title('analysis')
    if not path.exists('matrix'):
        mkdir('matrix')
    pyplot.savefig('matrix/analysis.png')

    print('\nAnalysis complete!')
    print('Results saved to: matrix/analysis.png')


def main():
    print('LOADING STATUS: Loading programs...\n')
    print('Checking dependencies:')
    lst_depend = None
    lst_depend = safe_exec(get_lst_depend, file='requirements.txt')
    if not lst_depend:
        exit(1)
    check_all = check_dependencies(lst_depend)
    if not check_all:
        print('Please install missing dependencies '
              'then run this program again.\n')
        print('with pip: ')
        print('1. create venv : python3 -m venv matrix_env')
        print('2. activate venv : source matrix_env/bin/activate')
        print('3. install requirements : pip install -r requirements.txt\n')
        print('with poetry:')
        print('1. create and install dependencies: poetry install')
        print("2. activate venv manually: -get path to env with "
              "('poetry env info --path') then activate with "
              "('source <path>/bin/activate')")
        print("   OR execute programme with this command: "
              "poetry run python loading.py")
        exit(1)
    else:
        demo_gen_data()


if __name__ == '__main__':
    main()
