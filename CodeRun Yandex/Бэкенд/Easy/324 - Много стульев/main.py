def main():
    purchase_offers, sale_offers = map(int, input().split())
    purchases_price = sorted(list(map(int, input().split())))
    sales_price = sorted(list(map(int, input().split())), reverse=True)
    min_length = min(purchase_offers, sale_offers)

    profit = 0
    for i in range(min_length):
        max_diff = 0
        for j in range(i, min_length):
            if sales_price[j] > purchases_price[i]:
                diff = sales_price[j] - purchases_price[i]
                if diff > max_diff:
                    max_diff = diff
                    break

        profit += max_diff

    print(profit)


if __name__ == '__main__':
    main()
