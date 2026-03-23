def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    get_power = lambda x: x['power']
    result = {
        'max_power': max(mages, key=get_power)['power'],
        'min_power': min(mages, key=get_power)['power'],
        'avg_power': round(sum(map(get_power, mages)) / len(mages), 2)
        }
    return result


def print_artifact_sorter(sorted_artifacts: list[dict]) -> None:
    result = [f"{art['name']} ({art['power']} power)" for art in sorted_artifacts]
    result = " comes before ".join(result)
    print(result)


def main():
    artifacts = [{'name': 'Fire Staff', 'power': 119, 'type': 'relic'}, {'name': 'Wind Cloak', 'power': 72, 'type': 'accessory'}, {'name': 'Fire Staff', 'power': 101, 'type': 'relic'}, {'name': 'Earth Shield', 'power': 106, 'type': 'focus'}]
    mages = [{'name': 'Nova', 'power': 87, 'element': 'ice'}, {'name': 'Zara', 'power': 65, 'element': 'fire'}, {'name': 'Sage', 'power': 64, 'element': 'fire'}, {'name': 'Riley', 'power': 76, 'element': 'wind'}, {'name': 'Storm', 'power': 64, 'element': 'ice'}]
    spells = ['shield', 'meteor', 'blizzard', 'tornado']

    print('Testing artifact sorter...')
    print(f'Input: \n{artifacts}')
    print(f'Output: ')
    print_artifact_sorter(artifact_sorter(artifacts))

    print('\nTesting power filter...')
    print(f'Input: \n{mages}')
    print(f'Output: \n{power_filter(mages, 70)}')

    print('\nTesting spell transformer...')
    print(f"Input: \n{spells}")
    print(f"Output: \n{spell_transformer(spells)}")

    print('\nTesting mage stats...')
    print(f'Input: \n{mages}')
    print(f'Output: \n{mage_stats(mages)}')

if __name__ == '__main__':
    main()