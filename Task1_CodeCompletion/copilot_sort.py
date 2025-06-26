def sort_list_of_dicts(data, key):
    """
    This function sorts a list of dictionaries by a given key.
    """
    return sorted(data, key=lambda x: x[key])