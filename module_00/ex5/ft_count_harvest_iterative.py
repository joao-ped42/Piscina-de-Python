def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    i: int = 1
    while i <= days:
        print(f"Day {i}")
        i = i + 1
    print("Harvest time!")

# ft_count_harvest_iterative()
