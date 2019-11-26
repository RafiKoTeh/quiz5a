import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
products_db = myclient["products"]
order_management_db = myclient["order_management"]

def get_product(code):
    products_coll = products_db["products"]

    product = products_coll.find_one({"code":code})

    return product

def get_products():
    product_list = []

    products_coll = products_db["products"]

    for p in products_coll.find({}):
        product_list.append(p)

    return product_list

def get_branch(code):
    products_coll = products_db["branches"]
    
    product = products_coll.find_one({"code":code})
    
    return product

def get_branches():
    product_list = []

    products_coll = products_db["branches"]

    for p in products_coll.find({}):
        product_list.append(p)

    return product_list


def get_user(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user

def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)
    
def countorders(username):
    orders_coll = order_management_db['orders']
    numberoforders = orders_coll.count({"username":username})
    return numberoforders

def get_order(code):
    orders_coll = order_management_db['orders']

    orders = orders_coll.find_one({"code":code})

    return orders

def get_orders(username):
    order_list = []

    orders_coll = order_management_db['orders']

    for o in orders_coll.find({"username":username}):
        order_list.append(o)
    return order_list

def changepassword(username):
    

    

    

    