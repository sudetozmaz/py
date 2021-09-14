def can_pile_cubes(cube_lengths):
    cube_on_top = None
    left_index = 0
    right_index = len(cube_lengths) - 1

    while left_index < right_index:  # Avoid corner case of `cube_lengths` being an empty list
        left_cube = cube_lengths[left_index]
        right_cube = cube_lengths[right_index]

        if cube_on_top is None:
            if left_cube > right_cube:
                cube_on_top = left_cube
                left_index += 1
            else:
                cube_on_top = right_cube
                right_index -= 1
        else:
            if left_cube > right_cube:
                if left_cube > cube_on_top:
                    return False
                cube_on_top = left_cube
                left_index += 1
            else:
                if right_cube > cube_on_top:
                    return False
                cube_on_top = right_cube
                right_index -= 1

    return True


def parse_test_case():
    input()  # Throw away number of cubes
    return [int(x) for x in input().split()]


if __name__ == '__main__':
    num_tests = int(input())
    for _ in range(num_tests):
        can_pile = can_pile_cubes(parse_test_case())
        print('Yes' if can_pile else 'No')
