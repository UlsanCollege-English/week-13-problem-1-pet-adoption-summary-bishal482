def summarize_adoptions(adoptions):
    """
    Given a list of animal type strings, return a dictionary mapping each
    distinct animal type to how many times it appears in the list.

    Example:
    summarize_adoptions(["cat", "dog", "cat"]) -> {"cat": 2, "dog": 1}
    """

    # Step 6: Implement the algorithm in Python
    counts = {}

    for animal in adoptions:
        if animal in counts:
            counts[animal] += 1
        else:
            counts[animal] = 1

    return counts


if __name__ == "__main__":
    # Optional manual test
    sample = ["cat", "dog", "cat", "rabbit", "dog", "cat"]
    print(summarize_adoptions(sample))
