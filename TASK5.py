
library = {"Python негіздері": 150, "Машиналық оқыту": 200, "Java 101": 100, "Веб-әзірлеу": 180}
max_name = ""
max_value = 0

for book, total in library.items():
    if total > max_value:
        max_value = total
        max_name = book
print(max_name, max_value)