# KIRANA STORE BILLING AND STOCK REGISTER
# Simple Functions Version
# B.Sc. IT Sem-I | UDP-131 Project

def add_item():
    f = open("stock.txt", "a")
    
    code = input("Enter item code: ")
    name = input("Enter item name: ")
    unit = input("Enter unit: ")
    rate = float(input("Enter rate: "))

    while rate <= 0:
        print("Rate must be positive")
        rate = float(input("Enter rate again: "))

    qty = int(input("Enter quantity: "))

    while qty <= 0:
        print("Quantity must be positive")
        qty = int(input("Enter quantity again: "))

    gst = float(input("Enter GST percentage: "))

    f.write(code + "," + name + "," + unit + "," +
            str(rate) + "," + str(qty) + "," + str(gst) + "\n")

    f.close()
    print("Item added successfully.")


def display_stock():
    print("\n------------- STOCK -------------")

    f = open("stock.txt", "r")

    print("Code\tName\tUnit\tRate\tQty\tGST")

    for line in f:
        data = line.strip().split(",")

        print(data[0], "\t", data[1], "\t", data[2],
              "\t", data[3], "\t", data[4], "\t", data[5])

    f.close()


def update_rate():
    search_code = input("Enter item code: ")
    new_rate = float(input("Enter new rate: "))

    while new_rate <= 0:
        print("Rate must be positive")
        new_rate = float(input("Enter new rate: "))

    f = open("stock.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("stock.txt", "w")

    found = False

    for line in lines:
        data = line.strip().split(",")

        if data[0] == search_code:
            data[3] = str(new_rate)
            found = True

        f.write(data[0] + "," + data[1] + "," + data[2] + "," +
                data[3] + "," + data[4] + "," + data[5] + "\n")

    f.close()

    if found == True:
        print("Rate updated successfully.")
    else:
        print("Item not found.")


def create_bill():
    bill = []
    total = 0

    while True:
        code = input("Enter item code (0 to finish): ")

        if code == "0":
            break

        f = open("stock.txt", "r")
        found = False

        for line in f:
            data = line.strip().split(",")

            if data[0] == code:
                found = True

                name = data[1]
                rate = float(data[3])
                available = int(data[4])
                gst = float(data[5])

                print("Item:", name)
                print("Available quantity:", available)
                print("Rate:", rate)

                qty = int(input("Enter quantity: "))

                if qty <= 0:
                    print("Quantity must be positive.")

                elif qty > available:
                    print("Not enough stock.")

                else:
                    amount = rate * qty
                    gst_amount = amount * gst / 100
                    final_amount = amount + gst_amount

                    bill.append([code, name, qty, rate,
                                 gst_amount, final_amount])

                    total = total + final_amount

                    print("Item added.")

        f.close()

        if found == False:
            print("Item not found.")

    if len(bill) == 0:
        print("Bill cancelled.")
        print("Stock is unchanged.")

    else:
        print("\n==========================================")
        print("              KIRANA STORE")
        print("==========================================")
        print("Item\tQty\tRate\tGST\tAmount")

        for item in bill:
            print(item[1], "\t", item[2], "\t", item[3],
                  "\t", item[4], "\t", item[5])

        print("------------------------------------------")
        print("Grand Total =", total)

        conform = input("Conform bill? (y/n): ")

        if conform == "y":

            # Update stock only after bill is confirmed
            f = open("stock.txt", "r")
            lines = f.readlines()
            f.close()

            f = open("stock.txt", "w")

            for line in lines:
                data = line.strip().split(",")

                for item in bill:
                    if data[0] == item[0]:
                        old_qty = int(data[4])
                        new_qty = old_qty - item[2]
                        data[4] = str(new_qty)

                f.write(data[0] + "," + data[1] + "," + data[2] + "," +
                        data[3] + "," + data[4] + "," + data[5] + "\n")

            f.close()

            # Save bill
            f = open("bills.txt", "a")

            for item in bill:
                f.write(item[0] + "," + str(item[2]) + "," +
                        str(item[5]) + "\n")

            f.close()

            print("Bill confirmed.")
            print("Stock updated.")

        else:
            print("Bill cancelled.")
            print("Stock is unchanged.")

def daily_sales():
    total_sales = 0

    f = open("bills.txt", "r")

    for line in f:
        data = line.strip().split(",")
        total_sales = total_sales + float(data[2])

    f.close()

    print("Today's Sales =", total_sales)


def reorder_list():
    f = open("stock.txt", "r")

    print("\n--------- REORDER LIST ---------")

    found = False

    for line in f:
        data = line.strip().split(",")
        qty = int(data[4])

        if qty < 5:
            print(data[0], data[1], "Quantity =", qty)
            found = True

    f.close()

    if found == False:
        print("No item needs reorder.")


def main():
    while True:
        print("\n=======================================")
        print("          KIRANA STORE")
        print("  B.Sc. IT Sem-I | UDP-131 Project")
        print("=======================================")
        print("1. Add Item")
        print("2. Display Stock")
        print("3. Update Rate")
        print("4. Create Bill")
        print("5. Daily Sales")
        print("6. Reorder List")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_item()

        elif choice == 2:
            display_stock()

        elif choice == 3:
            update_rate()

        elif choice == 4:
            create_bill()

        elif choice == 5:
            daily_sales()

        elif choice == 6:
            reorder_list()

        elif choice == 7:
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()
