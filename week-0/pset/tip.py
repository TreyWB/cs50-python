def main():
    dollars = remove_doll(input("How much was your meal? "))
    percent = remove_per(input("What percentage to tip? "))
    
    dollars = dollars_to_float(dollars)
    percent = percentage_to_float(percent)
     
    tip = dollars * percent
    
    print(f"Tip: ${tip:.2f}")

def remove_doll(raw_doll):
    if "$" in raw_doll:
        raw_doll = raw_doll.replace("$", "")
    return raw_doll

def remove_per(raw_per):
    if "%" in raw_per:
        raw_per = raw_per.replace("%", "")
    return raw_per

def dollars_to_float(dollar_input):
    dollars = float(dollar_input)
    return dollars

def percentage_to_float(percent_input):
    float_percent = float(percent_input)
    percent = float_percent / 100
    return percent
    
main()