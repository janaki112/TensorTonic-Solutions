def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    set_a = set(set_a)
    set_b = set(set_b)
    union_set = set_a | set_b
    if(len(union_set)==0):
        return 0.0
    intersection_set = set_a & set_b
    jaccard_similarity = len(intersection_set) / len(union_set)
    return jaccard_similarity
    # Write code here