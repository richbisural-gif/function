course = [
    {'title': 'Ancient Civilizations', 'genre': 'history'},
    {'title': 'Corporate Finance', 'genre': 'commerce'},
    {'title': 'Modern World History', 'genre': 'history'}
]

# Filter history courses
history_courses = list(filter(lambda c: c['genre'] == 'history', course))

# Display the result
print(history_courses)