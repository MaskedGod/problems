def distance(strand_a, strand_b):
    hamm_dist = 0

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                hamm_dist += 1

    return hamm_dist


print(distance("", ""))  # 0
print(distance("A", "A"))  # 0
print(distance("G", "T"))  # 1
print(distance("GGACTGAAATCTG", "GGACTGAAATCTG"))  # 0
print(distance("GGACGGATTCTG", "AGGACGGATTCT"))  # 9
