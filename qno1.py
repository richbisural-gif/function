def keep_alphabetic(items):
    return list(filter(lambda x: x.isalpha(), items))

items = ['sql', '123', 'python']
result = keep_alphabetic(items)
print(result)