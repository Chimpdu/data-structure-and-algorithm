import math


def sales(cars, customers):
    sales = 0
    #
    # pairs = []
    isPurchased = [False] * len(cars)
    customers.sort()
    cars.sort()
    #
    # print(customers)
    # print(cars)
    if len(customers) > len(cars):
        diff = len(customers) - len(cars)
        for i in range(diff):
            cars.append(math.inf)
# if the customers outnumber the cars, we append infinity numbers to cars
# and make the num of cars equals to the num of customers. This avoids
# index out of range and ensures that the extra customer is compared to cars with smaller index.
    for i in range(len(customers)):

        if (customers[i] - cars[i] >= 0):
            sales += 1
            isPurchased[i] = True
            #
            # pairs.append([customers[i], cars[i]])
        else:
            decrease_index = i
            while decrease_index > 0:
                decrease_index -= 1
                if ((customers[i] - cars[decrease_index] >= 0) and (isPurchased[decrease_index] == False)):
                    sales += 1
                    isPurchased[decrease_index] = True
                #
                #    pairs.append([customers[i], cars[decrease_index]])
                    break
    # print(pairs)
    return sales


if __name__ == "__main__":
    # print(sales([20, 10, 15], [11, 25, 15]))                        # 3
    # print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
    # print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
    # print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5
    # print(sales([184, 158, 176, 116, 150, 185, 113, 143, 169],
    #            [138, 159, 199, 161, 108, 141, 101, 172]))              # 6

    print(sales([154, 134, 105, 186, 135, 190, 173, 173, 174, 160],
                [183, 190, 127, 148, 181, 186, 120, 149, 168, 116, 169]))  # 9
