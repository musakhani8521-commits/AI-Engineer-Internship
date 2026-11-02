def remove_duplicates(items):
    return list(dict.fromkeys(items))

print(remove_duplicates([1, 2, 2, 3, 3, 4]))