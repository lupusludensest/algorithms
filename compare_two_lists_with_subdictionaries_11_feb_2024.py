
# compare input and output. two lists with sub-dictionaries

items_1 = [
    {
      "productId": "fc88cd5d-5049-4b00-8d88-df1d9b4a3ce1",
      "productQuantity": 1
    },
      {
        "productId": "fc88cd5d-5049-4b00-8d88-df1d9b4a3ce2",
        "productQuantity": 2
      }
  ]


items_2 = [
        {
            "id": "86ce06e2-8ab0-4296-935e-a2e84f571b49",
            "productInfo": {
                "id": "fc88cd5d-5049-4b00-8d88-df1d9b4a3ce1",
                "name": "Vanilla Latte",
                "description": "Espresso with Vanilla and Steamed Milk",
                "price": 4.85,
                "quantity": 60,
                "active": True,
                "productFileUrl": None
            },
            "productQuantity": 1
        },
            {
            "id": "86ce06e2-8ab0-4296-935e-a2e84f571b49",
            "productInfo": {
                "id": "fc88cd5d-5049-4b00-8d88-df1d9b4a3ce2",
                "name": "Vanilla Latte",
                "description": "Espresso with Vanilla and Steamed Milk",
                "price": 4.85,
                "quantity": 60,
                "active": True,
                "productFileUrl": None
            },
            "productQuantity": 1
        }
    ]

def cmpr_lsts(items_1, items_2):
    prdcts_ids = []
    for i in items_1:
        prdcts_ids.append(i["productId"])


    ids = []
    for e in items_2:
        ids.append(e["productInfo"]["id"])

    for i in prdcts_ids:
        if i not in ids:
            return False
    return True


print(cmpr_lsts(items_1, items_2))




