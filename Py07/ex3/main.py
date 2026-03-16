from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def get_available_type(data: dict[str, dict[str, str | int]],
                       available: dict, typ: str) -> None:
    for key in data.keys():
        available[typ].append(key)


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print('Configuring Fantasy Card Game...')

    factory = FantasyCardFactory()
    print("Factory: FantasyCardFactory")

    strategy = AggressiveStrategy()
    print(f"Strategy: {strategy.get_strategy_name()}")

    available_type = {'creatures': [], 'spells': [], 'artifacts': []}
    get_available_type(factory.creatures, available_type, "creatures")
    get_available_type(factory.spells, available_type, "spells")
    get_available_type(factory.artifacts, available_type, "artifacts")
    print(f"Available types: {available_type}\n")

    engine = GameEngine("jsam", "Ennemy Player")
    engine.configure_engine(factory, strategy)
    engine.setup_ennemy_board()
    engine.setup_deck()
    engine.draw(7)

    print('Simulating aggressive turn...')
    print(f"Hand: [{', '.join(engine.get_hand())}]")

    print('\nTurn execution:')
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {engine.simulate_turn()}")

    print('\nGame Report:')
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy "
          "Pattern: Maximum flexibility achieved!")


if __name__ == '__main__':
    main()
