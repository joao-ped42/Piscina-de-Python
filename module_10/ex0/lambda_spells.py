from collections.abc import Callable


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    print("\nSorting...\n")
    func: Callable[[dict], int] = lambda x: x['power']
    ret: list[dict] = sorted(artifacts, key=func, reverse=True)
    return (ret)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    print("\nFiltering...\n")
    func: Callable[[dict], bool] = lambda x: x['power'] >= min_power
    ret: list[dict] = list(filter(func, mages))
    return (ret)


def spell_transformer(spells: list[str]) -> list[str]:
    print("\nTransforming...\n")
    func: Callable[[str], str] = lambda x: f"* {x} *"
    ret: list[str] = list(map(func, spells))
    return (ret)


def display_artifacts(artifacts: list[dict]) -> None:
    for artifact in artifacts:
        print(f" - {artifact['name']} ({artifact['power']})")


def display_mages(mages: list[dict]) -> None:
    for mage in mages:
        print(f" - {mage['name']} ({mage['power']})")


def mage_stats(mages: list[dict]) -> dict:
    print("\nProcessing stats...\n")
    power_func: Callable[[dict], int] = lambda x: x['power']
    power_list: Callable[[list[dict]], list[int]] = lambda x: [y['power']
                                                               for y in x]
    max_power: dict[str, int] = max(mages, key=power_func)
    min_power: dict[str, int] = min(mages, key=power_func)
    avg_power: float = sum(power_list(mages)) / len(mages)
    ret: dict[str, int | float] = {"max_power": max_power['power'],
                                   "min_power": min_power['power'],
                                   "avg_power": avg_power}
    return (ret)


def main() -> None:
    print("==================================================================")
    print("\nTesting artifact sorter...")
    artifacts = [{'name': 'Wind Cloak', 'power': 62, 'type': 'armor'},
                 {'name': 'Ice Wand', 'power': 110, 'type': 'relic'},
                 {'name': 'Fire Staff', 'power': 90, 'type': 'armor'},
                 {'name': 'Wind Cloak', 'power': 75, 'type': 'accessory'}]
    display_artifacts(artifacts=artifacts)
    artifacts = artifact_sorter(artifacts=artifacts)
    display_artifacts(artifacts=artifacts)
    print("==================================================================")
    print("\nTesting power filter...")
    mages = [{'name': 'Luna', 'power': 99, 'element': 'shadow'},
             {'name': 'Alex', 'power': 89, 'element': 'water'},
             {'name': 'Luna', 'power': 100, 'element': 'ice'},
             {'name': 'Kai', 'power': 60, 'element': 'water'},
             {'name': 'Zara', 'power': 64, 'element': 'light'}]
    display_mages(mages=mages)
    mages = power_filter(mages=mages, min_power=80)
    display_mages(mages=mages)
    print("==================================================================")
    print("\nTesting spell transformer...")
    spells = ['lightning', 'tsunami', 'shield', 'tornado']
    print(*spells, sep=', ')
    spells = spell_transformer(spells=spells)
    print(*spells, sep=', ')
    print("==================================================================")
    print("\nTesting mage stats...")
    mages2 = [{'name': 'Luna', 'power': 99, 'element': 'shadow'},
              {'name': 'Alex', 'power': 89, 'element': 'water'},
              {'name': 'Luna', 'power': 100, 'element': 'ice'},
              {'name': 'Kai', 'power': 60, 'element': 'water'},
              {'name': 'Zara', 'power': 64, 'element': 'light'}]
    print(mage_stats(mages=mages2))


if (__name__ == "__main__"):
    main()
