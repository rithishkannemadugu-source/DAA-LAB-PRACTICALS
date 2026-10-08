# Knapsack Problem (0/1 Knapsack)

##  Overview
The **Knapsack Problem** is a classic **Dynamic Programming** problem.  
You are given:
- `n` items, each with a **weight** and a **value**.
- A knapsack with a maximum **capacity**.

The goal is to **maximize the total value** of items placed in the knapsack **without exceeding its capacity**.

This implementation solves the **0/1 Knapsack Problem** (each item can either be taken or not taken, no fractions allowed).

---

## ⚙️ How the Code Works
1. **Input**
   - Number of items (`n`)
   - List of weights (`w`)
   - List of values (`v`)
   - Knapsack capacity (`capacity`)

2. **Dynamic Programming Table**
   - We use a 1D DP array `dp[capacity+1]`.
   - `dp[j]` stores the **maximum value achievable** with capacity `j`.

3. **Transition Formula**
   For each item `i`:
