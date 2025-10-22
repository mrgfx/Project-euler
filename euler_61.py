from collections import defaultdict
import itertools

# Polygonal number generators
def triangle(n): return n * (n + 1) // 2
def square(n): return n * n
def pentagonal(n): return n * (3 * n - 1) // 2
def hexagonal(n): return n * (2 * n - 1)
def heptagonal(n): return n * (5 * n - 3) // 2
def octagonal(n): return n * (3 * n - 2)

# Map function names to types
polygonal_funcs = {
    'triangle': triangle,
    'square': square,
    'pentagonal': pentagonal,
    'hexagonal': hexagonal,
    'heptagonal': heptagonal,
    'octagonal': octagonal,
}

# Generate 4-digit numbers for each type
def generate_polygonals():
    polygonals = defaultdict(list)
    for name, func in polygonal_funcs.items():
        n = 1
        while True:
            val = func(n)
            if val >= 10000:
                break
            if val >= 1000:
                polygonals[name].append(val)
            n += 1
    return polygonals

# Check if number is cyclic with another
def is_cyclic(a, b):
    return str(a)[-2:] == str(b)[:2]

# Recursive search for valid chain
def find_cyclic_chain(chain, remaining_types, polygonals):
    if not remaining_types:
        if is_cyclic(chain[-1][1], chain[0][1]):
            return chain
        return None

    last_number = chain[-1][1]
    last_suffix = str(last_number)[-2:]

    for ptype in remaining_types:
        for number in polygonals[ptype]:
            if str(number)[:2] == last_suffix:
                new_chain = chain + [(ptype, number)]
                new_remaining = remaining_types - {ptype}
                result = find_cyclic_chain(new_chain, new_remaining, polygonals)
                if result:
                    return result
    return None

def solve():
    polygonals = generate_polygonals()
    types = set(polygonal_funcs.keys())

    # Try all starting types and numbers
    for start_type in types:
        for number in polygonals[start_type]:
            chain = [(start_type, number)]
            result = find_cyclic_chain(chain, types - {start_type}, polygonals)
            if result:
                print("Cyclic chain:", result)
                return sum(num for _, num in result)

# Run
print("Sum of cyclic set:", solve())
