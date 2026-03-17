def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def ft_days(current: int) -> None:
        if (current > days):
            print("Harvest time!")
            return
        print(f"Day {current}")
        ft_days(current + 1)

    ft_days(1)

# ft_count_harvest_recursive()
