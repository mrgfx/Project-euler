import itertools

def is_special_sum_set(seq):
    """
    Check if the list seq (distinct positive integers) is a special sum set.
    Condition 1: For any two non‑empty disjoint subsets B and C: sum(B) ≠ sum(C).
    Condition 2: If |B| > |C| then sum(B) > sum(C).
    """
    seq = sorted(seq)
    n = len(seq)
    # Quick check for Condition 2 (size vs sum) via minimal checks:
    # If sum of smallest k+1 elements <= sum of largest k elements for any k, fails.
    # Because then a subset of size k+1 can have sum ≤ subset of size k.
    for k in range(1, (n//2)+1):
        sum_small = sum(seq[:k+1])
        sum_large = sum(seq[-k:])
        if sum_small <= sum_large:
            return False

    # Now check Condition 1: no two non‑empty disjoint subsets share the same sum.
    # We can generate all subset sums grouped by subset size.
    # But we only need to compare subsets of **equal size**? Actually any sizes but disjoint.
    # A simpler way: generate all subset sums, track by (mask) or using combinations.
    # For speed we’ll generate sums for all subsets, but record disjointness via masks.
    # For these sets (size ~7‑12) this is feasible.
    sum_by_mask = {}  # mask → sum
    full_mask = (1 << n) - 1
    for mask in range(1, full_mask+1):
        s = 0
        bits = 0
        for i in range(n):
            if (mask >> i) & 1:
                s += seq[i]
                bits += 1
        # check sums seen before
        if s in sum_by_mask:
            # We found another subset with same sum. But we must check if they are disjoint.
            # sum_by_mask[s] may be a list of masks or single mask.
            prev_masks = sum_by_mask[s]
            if isinstance(prev_masks, list):
                for pm in prev_masks:
                    if (pm & mask) == 0:
                        # disjoint and equal‑sum → violation
                        return False
                prev_masks.append(mask)
            else:
                pm = prev_masks
                if (pm & mask) == 0:
                    return False
                sum_by_mask[s] = [pm, mask]
        else:
            sum_by_mask[s] = mask
    # If all good
    return True

def main(filename="sets.txt"):
    total = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # parse numbers separated by comma or space
            # in the Project Euler file they are comma-separated maybe
            parts = line.split(',')
            if len(parts) == 1:
                # maybe space separated
                parts = line.split()
            seq = [int(p) for p in parts]
            if is_special_sum_set(seq):
                total += sum(seq)
    print("Sum of S(A_i) for all special sum sets:", total)

if __name__ == "__main__":
    main()
