import uuid
import time
import threading
import random

# ------------------ GLOBAL DATA ------------------
products = {}
users = {1: {}, 2: {}}
carts = {1: {}, 2: {}}
orders = {}
logs = []
transactions = set()
lock = threading.Lock()

# ------------------ LOGGING ------------------
def log(msg):
    entry = f"{time.strftime('%H:%M:%S')} - {msg}"
    logs.append(entry)
    print(entry)

# ------------------ PRODUCT SERVICE ------------------
def add_product():
    pid = int(input("Enter product ID: "))
    if pid in products:
        print("❌ Product ID exists")
        return
    
    name = input("Name: ")
    price = int(input("Price: "))
    stock = int(input("Stock: "))
    
    if stock < 0:
        print("Stock cannot be negative")
        return
    
    products[pid] = {"name": name, "price": price, "stock": stock}
    log(f"Product {pid} added")

def view_products():
    for pid, p in products.items():
        print(pid, p)

# ------------------ CART SERVICE ------------------
def add_to_cart(user):
    pid = int(input("Product ID: "))
    qty = int(input("Qty: "))
    
    with lock:
        if products[pid]["stock"] < qty:
            print("Not enough stock")
            return
        
        products[pid]["stock"] -= qty  # reserve
        carts[user][pid] = carts[user].get(pid, 0) + qty
        log(f"User {user} added {pid} qty={qty}")

def remove_from_cart(user):
    pid = int(input("Product ID: "))
    
    if pid in carts[user]:
        qty = carts[user][pid]
        products[pid]["stock"] += qty  # release
        del carts[user][pid]
        log(f"User {user} removed {pid}")

def view_cart(user):
    print(carts[user])

# ------------------ COUPON ------------------
def apply_discount(total, qty):
    if total > 71000:
        total *= 0.9
    if qty > 3:
        total *= 0.95
    
    code = input("Coupon: ")
    if code == "SAVE10":
        total *= 0.9
    elif code == "FLAT200":
        total -= 200
    
    return max(total, 0)

# ------------------ FRAUD ------------------
def fraud_check(user):
    return random.choice([False, False, True])

# ------------------ ORDER ENGINE ------------------
def place_order(user):
    if not carts[user]:
        print("Cart empty")
        return
    
    with lock:
        order_id = str(uuid.uuid4())
        total = 0
        qty = 0
        
        for pid, q in carts[user].items():
            total += products[pid]["price"] * q
            qty += q
        
        total = apply_discount(total, qty)
        
        orders[order_id] = {
            "user": user,
            "items": dict(carts[user]),
            "total": total,
            "status": "CREATED"
        }
        
        carts[user].clear()
        log(f"Order {order_id} created")
    
    # Payment simulation
    if random.choice([True, False]):
        orders[order_id]["status"] = "PAID"
        log("Payment success")
    else:
        rollback(order_id)
        return
    
    # Fraud
    if fraud_check(user):
        orders[order_id]["status"] = "FAILED"
        log("Fraud detected")
    
    print("✅ Order placed:", order_id)

# ------------------ ROLLBACK ------------------
def rollback(order_id):
    order = orders[order_id]
    
    for pid, qty in order["items"].items():
        products[pid]["stock"] += qty
    
    order["status"] = "FAILED"
    log("Rollback done")

# ------------------ CANCEL ------------------
def cancel_order():
    oid = input("Order ID: ")
    
    if oid in orders and orders[oid]["status"] != "CANCELLED":
        orders[oid]["status"] = "CANCELLED"
        for pid, qty in orders[oid]["items"].items():
            products[pid]["stock"] += qty
        
        log("Order cancelled")

# ------------------ RETURN ------------------
def return_product():
    oid = input("Order ID: ")
    if oid in orders:
        orders[oid]["status"] = "RETURNED"
        log("Return processed")

# ------------------ ALERT ------------------
def low_stock():
    for p in products.values():
        if p["stock"] < 2:
            print("Low stock:", p)

# ------------------ CONCURRENCY ------------------
def simulate():
    t1 = threading.Thread(target=add_to_cart, args=(1,))
    t2 = threading.Thread(target=add_to_cart, args=(2,))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# ------------------ LOGS ------------------
def view_logs():
    for l in logs:
        print(l)

# ------------------ FAILURE ------------------
def failure():
    if random.choice([True, False]):
        print("Injected failure")
        log("Failure simulated")

# ------------------ IDEMPOTENCY ------------------
def idempotency():
    tid = input("Transaction ID: ")
    
    if tid in transactions:
        print("Duplicate request")
    else:
        transactions.add(tid)
        print("Processed")

# ------------------ MENU ------------------
def menu():
    user = 1
    
    while True:
        print("\n1 Add Product")
        print("2 View Products")
        print("3 Add to Cart")
        print("4 Remove from Cart")
        print("5 View Cart")
        print("6 Place Order")
        print("7 Cancel Order")
        print("8 View Orders")
        print("9 Low Stock Alert")
        print("10 Return Product")
        print("11 Simulate Concurrent Users")
        print("12 View Logs")
        print("13 Trigger Failure")
        print("14 Idempotency")
        print("0 Exit")
        
        ch = input("Choice: ")
        
        if ch == '1': add_product()
        elif ch == '2': view_products()
        elif ch == '3': add_to_cart(user)
        elif ch == '4': remove_from_cart(user)
        elif ch == '5': view_cart(user)
        elif ch == '6': place_order(user)
        elif ch == '7': cancel_order()
        elif ch == '8': print(orders)
        elif ch == '9': low_stock()
        elif ch == '10': return_product()
        elif ch == '11': simulate()
        elif ch == '12': view_logs()
        elif ch == '13': failure()
        elif ch == '14': idempotency()
        elif ch == '0': break

if __name__ == "__main__":
    menu()
