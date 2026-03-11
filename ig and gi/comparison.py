import math
from collections import Counter

# ---------- ENTROPY ----------
def entropy(labels):
    total = len(labels)
    counts = Counter(labels)

    ent = 0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)

    return ent


# ---------- GINI ----------
def gini(labels):
    total = len(labels)
    counts = Counter(labels)

    g = 1
    for c in counts.values():
        p = c / total
        g -= p ** 2

    return g


# ---------- INFORMATION GAIN ----------
def information_gain(parent, splits):

    parent_entropy = entropy(parent)
    total = len(parent)

    weighted_entropy = 0

    for subset in splits:
        weight = len(subset) / total
        weighted_entropy += weight * entropy(subset)

    return parent_entropy - weighted_entropy


# ---------- WEIGHTED GINI ----------
def weighted_gini(parent, splits):

    total = len(parent)
    wg = 0

    for subset in splits:
        weight = len(subset) / total
        wg += weight * gini(subset)

    return wg


# ---------- PRINT COMPARISON ----------
def compare(parent, splits, name):

    print("\n----------------------------")
    print("Split:", name)
    print("----------------------------")

    for i, subset in enumerate(splits):
        print(f"Node {i+1} labels:", subset)
        print("Entropy:", round(entropy(subset),4))
        print("Gini:", round(gini(subset),4))
        print()

    ig = information_gain(parent, splits)
    gini_value = weighted_gini(parent, splits)

    print("Information Gain:", round(ig,4))
    print("Weighted Gini:", round(gini_value,4))


# ---------- DATA ----------
parent = [0,0,0,1,1,1]

splitA = [
    [0,0,0],
    [1,1,1]
]

splitB = [
    [0,1,0],
    [1,0,1]
]


# ---------- PARENT INFO ----------
print("Parent labels:", parent)
print("Parent Entropy:", round(entropy(parent),4))
print("Parent Gini:", round(gini(parent),4))


# ---------- COMPARISON ----------
compare(parent, splitA, "A")
compare(parent, splitB, "B")