# PavaniArmoor_EcommerceOrderEngineHackathon
# 🛒 Ecommerce Order Engine (CLI-Based)

## 📌 Overview

This project is a **menu-driven CLI application** that simulates a real-world e-commerce backend system.
It handles products, inventory, multi-user carts, and order processing with advanced backend concepts like concurrency, transactions, and failure handling.

---

## 🚀 Features

### 🧾 Product Management

* Add new products
* Prevent duplicate product IDs
* View all products
* Ensure stock is not negative

---

### 📦 Inventory Management

* Real-time stock updates
* Stock reservation when adding to cart
* Stock release when removing from cart
* Low stock alerts

---

### 👥 Multi-User Cart System

* Separate cart for each user
* Add/remove/update items
* Prevent adding beyond available stock

---

### ⚙️ Order Placement Engine

* Validate cart
* Calculate total
* Apply discounts and coupons
* Convert cart → order
* Clear cart after order

---

### 💳 Payment Simulation

* Random success/failure
* Failure triggers rollback

---

### 🔄 Transaction & Rollback

* Ensures atomic operations
* Restores stock on failure
* Maintains data consistency

---

### 🔐 Concurrency & Locking

* Simulates multiple users
* Prevents race conditions using locks

---

### 🏷️ Discount & Coupon Engine

* Auto discount rules:

  * Total > 71000 → 10% off
  * Quantity > 3 → extra 5%
* Coupons:

  * SAVE10 → 10% off
  * FLAT200 → ₹200 off

---

### 📑 Order Management

* View all orders
* Cancel orders
* Return products

---

### 📜 Audit Logging

* Tracks all actions with timestamps
* Immutable logs

---

### 🚨 Fraud Detection

* Detects suspicious activity
* High-value order alerts

---

### ⚠️ Failure Handling

* Simulates system failures
* Ensures safe recovery

---

### 🔁 Idempotency Handling

* Prevents duplicate transactions

---

### 🧵 Concurrency Simulation

* Multi-threaded execution

---

## 🧠 Concepts Used

* Python Data Structures
* Threading & Locks
* Transactions & Rollbacks
* Event Simulation
* CLI Design

---

## 💻 Technologies

* Python 3
* Threading module
* UUID module

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📋 CLI Menu

1. Add Product
2. View Products
3. Add to Cart
4. Remove from Cart
5. View Cart
6. Place Order
7. Cancel Order
8. View Orders
9. Low Stock Alert
10. Return Product
11. Simulate Concurrent Users
12. View Logs
13. Trigger Failure Mode
14. Idempotency Handling
15. Exit

---

## 🎯 Objective

To simulate real-world backend behavior including:

* Inventory consistency
* Concurrent user handling
* Transaction safety
* Order lifecycle management

---

## 👩‍💻 Author

**Pavani Armoor**

---

## ⭐ Note

This is a **simulation project** for learning and hackathon purposes only.
