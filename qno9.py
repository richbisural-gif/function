def remove_at_idx(lst, idx):
    new_list = []
    for i in range(len(lst)):
        if i != idx:
            new_list.append(lst[i])
    return new_list

# Example usage
data = ['a', 'b', 'c', 'd']
result = remove_at_idx(data, 2)
print(result)