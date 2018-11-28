def get_variance(elements):
    """Calculates the variance of a list of numbers."""
    m = sum(elements) / len(elements)
    var = sum([(xi - m) ** 2 for xi in elements]) / len(elements)
    return var
