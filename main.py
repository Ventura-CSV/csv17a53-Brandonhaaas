from __future__ import annotations


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None if injective."""
    # === TODO ===
    
    hashmap = dict()
    for x, y in mapping.items():
        if y in hashmap:
            return (hashmap[y], x)
        hashmap[y] = x
    return None
    
    # === END TODO ===


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None if surjective."""
    # === TODO ===
    
    output_values = set(mapping.values())

    for element in target:
        if element not in output_values:
            return element
    
    return None

    # === END TODO ===


def my_floor(x: float) -> int:
    """Return floor(x) without using math.floor."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===


def my_ceil(x: float) -> int:
    """Return ceil(x) without using math.ceil."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===
