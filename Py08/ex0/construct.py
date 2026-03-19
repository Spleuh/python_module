from sys import base_prefix, prefix, executable
from site import USER_SITE


def check_venv() -> bool:
    if base_prefix == prefix:
        return False
    return True


def get_venv_name() -> str:
    result = base_prefix[1:]
    if check_venv():
        result = prefix.split('/')[-1]
    return result


def main():
    if not check_venv():
        print('\nMATRIX STATUS: You are still plugged in\n')
        print(f'Current Python: {executable}')
        print('Virtual Environment: None detected\n')
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print('To enter the construct, run:')
        print('python -m venv matrix_env')
        print('source matrix_env/bin/activate # On Unix')
        print('matrix_env')
        print('Scripts')
        print('activate # On Windows\n')
        print('Then run this program again.')
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f'Current Python: {executable}')
        print(f'Virtual Environment: {get_venv_name()}')
        print(f'Environment Path: {prefix}\n')
        print("SUCCES: You're in an isolated environment!")
        print("Safe to install package without affecting\n"
              "the global system.\n")
        print('Package installation path:')
        print(USER_SITE)


if __name__ == '__main__':

    main()
