names_from_line = line[17:]

names_from_line = names_from_line.replace(" and", ",")

line = "Adieu, adieu, to "

line = line + names_from_line + ", and " + name

print(line)