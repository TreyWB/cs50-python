def main():
    while True:
        mass = input("m (kg): ")
        check = mass.isnumeric()
        if check == True:
            break
        
    num = int(mass)
    
    answer = eqiv(num)
    print("E:", answer)

def eqiv(m):
    c = 300000000
    output = m * pow(c, 2)
    return output


main()