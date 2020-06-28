def recip_book():
    cook_book = {}
    with open("recipes.txt", encoding="utf-8") as book:
        while True:
            dish = book.readline().strip()
            if not dish:
                break
            cook_book[dish] = []
            num_ingrid = int(book.readline().strip())
            food = [book.readline().strip().split("|") for repeat in range(num_ingrid)]
            # print(food) это для  моего понимания список позиций ингридиентов
            for element in food:
                cook_book[dish].append({"ingridient_name": element[0].strip(),
                                        "quantity": int(element[1].replace(' ', '')),
                                        "measure": element[2].lstrip()})
            # print(cook_book[dish]) это для  моего понимания список с вложенным словарем
            book.readline()
        print(cook_book)


recip_book()
