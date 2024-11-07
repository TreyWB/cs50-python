import inflect

p = inflect.engine()

minutes = 525600

output = p.number_to_words(minutes, andword="")

print(f'\n{output.capitalize()} minutes')