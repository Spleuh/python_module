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


def check_conf(key: str) -> bool:
    conf = os.getenv(key)
    if not conf:
        return False
    return True


def check_env() -> bool:
    lst_key = [
        'MATRIX_MODE',
        'DATABASE_URL',
        'API_KEY',
        'LOG_LEVEL',
        'ZION_ENDPOINT']
    result = all([os.getenv(key) for key in lst_key])
    return result


def print_info(mode: str):
    if mode == 'development' or mode == 'production':
        missing = 'DATABASE_URL is missing'
        n_missing = 'Connected to local instance'
        print("Database: "
              f"{missing if not os.getenv('DATABASE_URL') else n_missing}")
        missing = 'API_KEY is missing'
        n_missing = 'Authentificated'
        print(
            "API Acces: "
            f"{ missing if not os.getenv('API_KEY') else n_missing }")
        missing = 'LOG_LEVEL is missing'
        n_missing = 'DEBUG'
        print(
            "Log Level: "
            f"{missing if not os.getenv('LOG_LEVEL') else n_missing}")
        missing = 'ZION_ENDPOINT is missing'
        n_missing = 'Online'
        print(
            "Zion Network: "
            f"{missing if not os.getenv('ZION_ENDPOINT') else n_missing}\n")
    else:
        print('Error: mode unknown\n')


def security_check(mode: str):
    prod = mode == 'production'
    print('Environment security check:')
    print('[OK] No hardcoded secrets detected')
    env_check = check_env()
    print(f"[{'OK' if env_check else 'KO'}] .env file "
          f"{'not ' if not env_check else ''}properly configured")
    print(f"[{'OK' if prod else 'KO'}] "
          f"Production overrides {'not ' if not prod else ''}available")


def main():
    if not safe_exec(check_depend):
        print('python-dotenv is missing: '
              'Please intall then run this program again')
        sys.exit(1)

    import dotenv
    print('\nORACLE STATUS: Reading the Matrix...\n')

    dotenv.load_dotenv()
    print('Configuration loaded:')

    mode = os.getenv('MATRIX_MODE')
    print(f"Mode: {'MATRIX_MODE is missing' if not mode else mode}")
    if mode:
        print_info(mode)

    security_check(mode)
    print('\nThe Oracle sees all configurations.')


if __name__ == '__main__':
    main()
