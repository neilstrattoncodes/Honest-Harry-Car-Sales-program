# Honest Harrys Car program
# Created by Neil Stratton, February 17, 2022
import datetime


def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    Number_Display = f"{Number_Display:10}"
    return Number_Display


def Logo_display():
    print(f"HONEST HARRYS CAR PROGRAM")
    print(f"_________________________")
    print("")


# Constants
LICENCE_FEE_LOW = 75
LICENCE_FEE_HIGH = 165
TRANSFER_FEE_PER = .01
ZERO = 0
LUXURY_TAX = .016
REG_TAX = .15
FINANCE_FEE = 39.99
DATE_FORMAT = "%Y-%m-%d"
CAR_YEAR = "%Y"
CAR_SELL_LIMIT = 50000
CAR_5K = 5000
CAR_20K = 20000
MONTH_12 = 12
TITLE = "Honest Harry Car Sales "
TYPE = "Used Car sale and Receipt"
BOT_MSG = "Best used cars at the best price!"
DASHES = ("-"*10)

# Validation lists
numbers_list = (1, 2, 3, 4)
provinces = ("AB", "NL", "ON", "QC", "MN", "SK", "NB", "NS", "BC", "YT", "NT", "PE", "NU")

while True:
    Logo_display()
#Data inputs
    while True:
        try:
            cust_inv_date = input("Enter the invoice date : YYYY-MM-DD format: ")
            cust_inv_date = datetime.datetime.strptime(cust_inv_date, "%Y-%m-%d")
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
        else:
            break

    while True:
        try:
            cust_first_name = str(input("Enter your first name: ")).upper()
            if cust_first_name.isalpha():
                print("Valid First Name")
            else:
                raise TypeError
        except TypeError:
            print("Invalid First Name")
        else:
            break

    while True:
        try:
            cust_last_name = str(input("Enter your last name: ")).upper()
            if cust_last_name.isalpha():
                print("Valid Last Name")
            else:
                raise TypeError
        except TypeError:
            print("Invalid Last Name")
        else:
            break

    while True:
        try:
            cust_address = str(input("Enter your Street Address: ")).upper()
            if cust_address:
                print("valid Address")

            elif cust_address == "":
                raise TypeError

            else:
                raise TypeError
        except TypeError:
            print(" inValid Address")
        else:
            break

    while True:
        try:
            cust_city = str(input("Enter your City: ")).upper()
            if cust_city.isalpha():
                print("Valid City name")

            elif cust_city == "":
                raise TypeError
            else:
                raise TypeError
        except TypeError:
            print("Invalid City name")
        else:
            break

    while True:
        try:
            cust_prov = str(input("Enter your Province in XX format: ")).upper()
            if cust_prov.isalpha() \
                    and cust_prov in provinces:
                print("Valid Province")
            else:
                raise TypeError
        except TypeError:
            print("Invalid Province")
        else:
            break

    while True:
        cust_postal = str(input("Enter your licence plate number 6 digits X9X-9X9 format:  ")).upper()
        length = len(cust_postal)
        if length == 7 \
                and cust_postal[0].isalpha() \
                and cust_postal[1].isdigit() \
                and cust_postal[2].isalpha() \
                and cust_postal[3] == "-" \
                and cust_postal[4].isdigit() \
                and cust_postal[5].isalpha() \
                and cust_postal[6].isdigit():
            print("Valid Postal Code")
        else:
            print("Invalid Postal Code")
            continue
        break

    while True:
        cust_phone_number = str(input("Enter your phone number 10 digits 999-999-9999 format: ")).upper()
        length = len(cust_phone_number)
        if length == 12 \
                and cust_phone_number[3] == "-" \
                and cust_phone_number[7] == "-" \
                and cust_phone_number[:3].isdigit() \
                and cust_phone_number[4:7].isdigit() \
                and cust_phone_number[8:].isdigit():
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            continue
        break

    while True:
        cust_plate_number = str(input("Enter your licence plate number 6 digits XXX999 format:  ")).upper()
        length = len(cust_plate_number)
        if length == 6 \
                and cust_plate_number[0:2].isalpha() \
                and cust_plate_number[3:5].isdigit():
            print("Valid Licence plate Number")
        else:
            print("Invalid Licence plate Number")
            continue
        break

    while True:
        try:
            cust_car_buy_make = str(input('Enter the vehicle make ex: "Honda": ')).upper()
            if not cust_car_buy_make == "":
                print("Valid Car Make")

            else:
                raise TypeError
        except TypeError:
            print("Invalid Car Make")
        else:
            break

    while True:
        try:
            cust_car_buy_model = str(input('Enter the vehicle model ex: "CRV": ')).upper()
            if not cust_car_buy_model == "":
                print("Valid Car Model")
            else:
                raise TypeError
        except TypeError:
            print("Invalid Car Model")
        else:
            break

    while True:
        try:
            cust_car_buy_year = str(input("Enter the vehicle year: "))
            datetime.datetime.strptime(cust_car_buy_year, CAR_YEAR)
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY")
        else:
            break

    while True:

        cust_car_selling_price = float(input("New Vehicle sell Price: "))
        if cust_car_selling_price <= CAR_SELL_LIMIT:
            print("Valid Selling price")

        elif cust_car_selling_price <= ZERO:
            print("Price is too low")

        elif cust_car_selling_price > CAR_SELL_LIMIT:
            print("Price is too High")
            continue
        break


    while True:
        try:
            cust_car_trade_value = float(input("Vehicle trade in value: "))
            if cust_car_trade_value < cust_car_selling_price:
                print("Valid trade in price")
            else:
                print("Error: Trade in value is higher or equal to the selling price")
                raise ValueError
        except ValueError:
            print("Enter a Number")
            continue
        break

    while True:
        try:
            sales_name = str(input("Enter your Sales person name: ")).upper()
            if not sales_name == "":
                print("Valid Salesperson name")
            else:
                raise TypeError
        except TypeError:
            print("Invalid Sales person name")
        else:
            break

    while True:
        credit_card_num = str(input("Enter credit card number(16 digits): "))
        length = len(credit_card_num)
        if length >= 16 \
                and credit_card_num[0:15].isdigit():
            print("Valid Credit Card number")
        else:
            print("Invalid Credit Card Number")
            continue
        break

    while True:
        try:
            credit_card_exp = str(input("Credit card expiry date YYYY-MM-DD format: "))
            datetime.datetime.strptime(credit_card_exp, DATE_FORMAT)
        except ValueError:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
        else:
            break
#Calculations
    car_sale_price = cust_car_selling_price - cust_car_trade_value
    hst_amount = cust_car_selling_price * REG_TAX

    if car_sale_price <= CAR_5K:
        LICENCE_FEE = LICENCE_FEE_LOW

    else:
        LICENCE_FEE = LICENCE_FEE_HIGH

    if car_sale_price <= CAR_20K:
        TRANSFER_FEE = car_sale_price * TRANSFER_FEE_PER

    else:
        TRANSFER_FEE = car_sale_price * (TRANSFER_FEE_PER + LUXURY_TAX)

    total_price = car_sale_price + LICENCE_FEE + TRANSFER_FEE + hst_amount
    receipt_no = (f"{cust_first_name[0]}{cust_first_name[0]}-{cust_plate_number[3:6]}-{cust_phone_number[8:12]}")

    end_date = cust_inv_date + datetime.timedelta(days=30)
    end_date = end_date.strftime("%d-%b-%y")
    inv_date = cust_inv_date.strftime("%B %d, %Y")

    print("")
    print(f"#Years    #Payments    #Financing Fee    Total Price    Monthly Payment    ")
    print(f"-" * 72)

    for year in range(1, 5):
        yearly_cost = total_price
        car_payment = MONTH_12 * year
        financing_fee = FINANCE_FEE * year
        yearly_cost += financing_fee
        monthly_payment = yearly_cost / car_payment

        print(
            f"   {year}          {car_payment}          {As_Dollars(financing_fee)}        {As_Dollars(yearly_cost)}       {As_Dollars(monthly_payment)}")


    while True:
        try:
            pay_choice = int(input("Enter the payment schedule you want to follow (1-4): "))
            if pay_choice == 4:
                for year in range(1, 1):
                    yearly_cost = total_price
                    car_payment = MONTH_12 * year
                    financing_fee = FINANCE_FEE * year
                    yearly_cost += financing_fee
                    monthly_payment = yearly_cost / car_payment

            elif pay_choice == 1:
                for year in range(1, 2):
                    yearly_cost = total_price
                    car_payment = MONTH_12 * year
                    financing_fee = FINANCE_FEE * year
                    yearly_cost += financing_fee
                    monthly_payment = yearly_cost / car_payment

            elif pay_choice == 2:
                for year in range(1, 3):
                    yearly_cost = total_price
                    car_payment = MONTH_12 * year
                    financing_fee = FINANCE_FEE * year
                    yearly_cost += financing_fee
                    monthly_payment = yearly_cost / car_payment

            elif pay_choice == 3:
                for year in range(1, 4):
                    yearly_cost = total_price
                    car_payment = MONTH_12 * year
                    financing_fee = FINANCE_FEE * year
                    yearly_cost += financing_fee
                    monthly_payment = yearly_cost / car_payment

            else:
                if pay_choice not in numbers_list:
                    raise ValueError

        except ValueError:
                print("Enter a valid choice")

        else:
            break





#Printout
    print("")
    print("")
    print(f"      {TITLE:^7}")
    print(f"      {TYPE:^7}")
    print("")
    print(f"Invoice Date: {inv_date:>7}")
    print(f"Receipt No: {receipt_no:>7} ")
    print("")
    print("Sold to:")
    print(f"      {cust_first_name[0]}.{cust_last_name}")
    print(f"      {cust_address}")
    print(f"      {cust_city},{cust_prov},{cust_postal}")
    print(f"")
    print(f"Car Details:")
    print(f"     {cust_car_buy_year} {cust_car_buy_make} {cust_car_buy_model}")
    print("-"*37)
    print(f"Sale Price:               {As_Dollars(cust_car_selling_price)}")
    print(f"Trade Allowance:          {As_Dollars(cust_car_trade_value)}")
    print(f"Price After trade:        {As_Dollars(car_sale_price)}")
    print(f"                          {DASHES}")
    print(f"HST:                      {As_Dollars(hst_amount)}")
    print(f"Licence Fee               {As_Dollars(LICENCE_FEE)}")
    print(f"Transfer Fee              {As_Dollars(TRANSFER_FEE)}")
    print(f"                          {DASHES}")
    print(f"Total Sales Cost:         {As_Dollars(yearly_cost)}")
    print("-"*37)
    print(f"Term: {year}           Total Payments: {car_payment} ")
    print(f"Monthly Payment:           {As_Dollars(monthly_payment)}")
    print(f"First Payment Date:        {end_date}")
    print(f"")
    print(f"        {TITLE:^7}")
    print(f"      {BOT_MSG:^3}")
    print("")





    enter_new_sale = input("Would you like to enter a new sale? Y for Yes: ").upper()
    print("")
    if enter_new_sale == "Y":
        continue
    else:
        break
