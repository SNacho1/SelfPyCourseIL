def sort_prices(list_of_tuples):
    def get_price(item):
        return float(item[1])
    
    sorted_list = sorted(list_of_tuples, key=get_price, reverse=True)
    return sorted_list

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))
