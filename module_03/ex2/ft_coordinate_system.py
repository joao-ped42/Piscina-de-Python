import sys
import math


def ft_len(lst: list[str]) -> int:
    i: int = 0
    for str in lst:
        i += 1
    return (i)


def calc_3D_distance(nums1: tuple[int], nums2: tuple[int]) -> float:
    x: int = ((nums2[0] - nums1[0]) ** 2)
    y: int = ((nums2[1] - nums1[1]) ** 2)
    z: int = ((nums2[2] - nums1[2]) ** 2)
    return (math.sqrt(x + y + z))


def main(argv: list[str]) -> None:
    try:
        if (ft_len(argv) == 2):
            print(f"Parsing coordinates: {argv[1]}")
            coord2: tuple[int] = tuple(int(n) for n in argv[1].split(","))
        else:
            coord2: tuple[int] = tuple(int(n) for n in argv[1:])
        coord1 = tuple([0, 0, 0])
        print(f"Position created: {coord2}")
        print(f"Distane between {coord1} and {coord2}: "
              f"{calc_3D_distance(coord1, coord2):.2f}")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: {error.args}")


if (__name__ == "__main__"):
    print("=== Game Coordinate System ===\n")
    main(sys.argv)
