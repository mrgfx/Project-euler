def find_smallest_cube_with_five_permutations():
    from collections import defaultdict

    cubes = defaultdict(list)
    n = 1

    while True:
        cube = n ** 3
        key = ''.join(sorted(str(cube)))
        cubes[key].append(cube)

        if len(cubes[key]) == 5:
            return min(cubes[key])

        n += 1

# Run the function
print(find_smallest_cube_with_five_permutations())
