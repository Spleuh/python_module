import os
import sys
from typing import Callable, Any


def safe_exec(f: Callable, **kwargs: Any):
    try:
        return f(**kwargs)
    except ModuleNotFoundError as e:
        print(f'{e}')
        return False
    except Exception as e:
        print(f'{e}')
        return None


def check_depend() -> bool:
    import dotenv
    return True


def main():
    if not safe_exec(check_depend):
        print('python-dotenv is missing: '
              'Please intall then run this program again')
        sys.exit(1)

    import dotenv
    print('\nORACLE STATUS: Reading the Matrix...\n')

    dotenv.load_dotenv()
    print('Configuration loaded:')
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print(f"Database: {os.getenv('DATABASE_URL')}")


if __name__ == '__main__':
    main()
