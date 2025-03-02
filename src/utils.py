"""Some external functions module"""

def longest_str_in_list(lst:list[str]) -> str:
    """Returns longest string in the list"""
    if len(lst) == 0:
        return ""
    longest_str = lst[0]
    for string in lst:
        if len(string) > len(longest_str):
            longest_str = string
    return longest_str
