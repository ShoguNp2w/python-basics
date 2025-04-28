products_dic = {"AG32":10, "HT91":20,
                "PL65":30, "OS31":15,
                "KB07":25, "TR48":35}

if "OS31" in products_dic.keys():
    print(True)
else:
    print(False)

if "0S31" not in products_dic.keys():
    print(False)
else:
    print(True)

if "HT91" in products_dic.keys() and min(products_dic.values()) > 5:
    print(True)
else:
    print(False)


if "HT91" in products_dic.keys() or min(products_dic.values()) < 5:
    print(True)
else:
    print(False)


expensive_products =[]

for key, val in products_dic.items():
    if val >=20:
        expensive_products.append(key)

print(expensive_products)
