import sys


def ft_count_item(items: dict[str, int]) -> int:
    item_count: int = 0
    for key in items:
        item_count += items[key]
    return (item_count)


def item_max(items: dict[str, int]) -> str:
    max_key: str
    max_value: int = 0
    for key in items:
        if (items[key] > max_value):
            max_key = key
            max_value = items[key]
    return (max_key)


def item_min(items: dict[str, int]) -> str:
    min_key: str
    min_value: int = 2147483647
    for key in items:
        if (items[key] < min_value):
            min_key = key
            min_value = items[key]
    return (min_key)


def inventory_gen(item_lst: list[str]) -> dict[str, int]:
    unsorted_items: dict[str, int] = dict()
    key_value: list[str] = []
    for string in item_lst[1:]:
        key_value = string.split(":")
        unsorted_items.update({f"{key_value[0]}": int(key_value[1])})
    items_tuples: list[tuple[str, int]] = list(unsorted_items.items())
    i: int = len(items_tuples)
    for n in range(i):
        for j in range(0, i - n - 1):
            if items_tuples[j][1] < items_tuples[j+1][1]:
                items_tuples[j], items_tuples[j+1] = \
                    items_tuples[j+1], items_tuples[j]
    ret: dict[str, int] = dict()
    for key, value in items_tuples:
        ret.update({key: value})
    return (ret)


def categorize(dic: dict[dict[str, int], str], items: dict[str, int]) -> None:
    for item in items:
        if (items.get(item) >= 4):
            dic.update({{item: items[item]}: "Moderate"})


def main(argv: list[str]) -> None:
    if (len(argv) == 1):
        raise Exception("No arguments given.")
    items: dict[str, int] = inventory_gen(argv)
    moderate: dict[str, int] = dict()
    scarce: dict[str, int] = dict()
    restock: list[str] = []
    print(f"Total items in inventory: {ft_count_item(items)}")
    print(f"Unique item types: {len(items.keys())}\n")
    print("=== Current Inventory ===")
    for key in items:
        print(f"{key}: {items[key]} units ("
              f"{((items[key] * 100) / ft_count_item(items)):.1f}%)")
    print("\n=== Inventory Statistics ===")
    print(f"More abundant: {item_max(items)} ({items[item_max(items)]} units)")
    print(f"More abundant: {item_min(items)} ({items[item_min(items)]} units)")
    print("\n=== Item Categories ===")
    for item in items:
        if (items[item] >= 4):
            moderate.update({item: items[item]})
    for item in items:
        if (items[item] < 4):
            scarce.update({item: items[item]})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print("\n=== Management Suggestions ===")
    print("Restock needed: ", end="")
    for item in items:
        if (items[item] == 1):
            restock.append(item)
    print(", ".join(restock))
    print("\n=== Dictionary Properties Demo ===")
    keys: list[str] = list(items.keys())
    values: list[int] = list(items.values())
    print("Dictionary keys: ", end="")
    print(", ".join(keys))
    print("Dictionary values: ", end="")
    print(", ".join(str(number) for number in values))
    print("Sample lookup - 'sword' in inventory: ", end="")
    print("sword" in items)


if (__name__ == "__main__"):
    print("=== Inventory System Analysis ===")
    try:
        main(sys.argv)
    except Exception as error:
        print(f"An error has occured: {error}")
