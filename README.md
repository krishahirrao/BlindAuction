# 🕵️ Secret Auction Program (Python)

A simple command-line based **Secret Auction system** built using Python.  
This program allows multiple users to place bids privately and determines the highest bidder at the end.

---

## 📌 Features

- 👤 Multiple bidders can participate  
- 💰 Accepts bid amounts from each user  
- 🔒 Keeps bids hidden between participants  
- 🧠 Automatically finds the highest bidder  
- 🧩 Beginner-friendly Python logic  

---

## ⚙️ How It Works

1. User enters their **name**  
2. User enters their **bid amount**  
3. Program asks if there are more bidders  
   - If **yes** → screen clears (simulated)  
   - If **no** → winner is displayed  
4. The program prints the **highest bidder and bid amount**

---

## 🧑‍💻 Code Overview

- Uses a **dictionary** to store bids (`name: bid`)  
- A function `find_highest_bidder()` is used to:
  - Loop through all bids  
  - Compare values  
  - Find the highest bidder  

---
