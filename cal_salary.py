def CalSalary(num):
    week =  num * 4
    day = (1.6 * 2) * 4
    hk_one_day = 34 + 35 + 5                      #HK pricing
    rent = 1000
    month = (week - day) * 4 - rent 
    return ("月薪：", month)

if __name__ == "__main__":
    print(CalSalary(100))