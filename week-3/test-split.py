me_date = input("Date: ")
    
splits = me_date.split(" ", 2)

month = splits[0]

day = splits[1]

day = day.replace(",", "")

year = splits[2]

# print(f"Y: {year} M: {month} D: {day}")

print(splits)
