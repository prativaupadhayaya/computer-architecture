# **Lab Report**

## **Title**

**Implementation of Non-Restoring Division Algorithm Using Python**

## **Objective**

* To understand the Non-Restoring Division Algorithm.
* To implement the algorithm using Python.
* To perform binary division without restoring the partial remainder after each subtraction.
* To verify the quotient and remainder produced by the algorithm.

---

## **Introduction**

The Non-Restoring Division Algorithm is a binary division technique used in computer architecture and digital systems. Unlike the restoring division algorithm, it does not restore the previous remainder whenever a subtraction results in a negative value. Instead, the next operation depends on the sign of the current remainder, making the algorithm more efficient by reducing the number of arithmetic operations.

This algorithm is commonly used in processors and arithmetic logic units (ALUs) for performing signed and unsigned binary division.

---

## **Theory**

The algorithm uses three registers:

* **A** – Accumulator (stores partial remainder)
* **Q** – Dividend (stores quotient)
* **M** – Divisor

### Algorithm Steps

1. Initialize:

   * A = 0
   * Q = Dividend
   * M = Divisor
2. Repeat for *n* bits:

   * Left shift (A, Q).
   * If A ≥ 0:

     * A = A − M
   * Else:

     * A = A + M
   * If A ≥ 0:

     * Set Q₀ = 1
   * Else:

     * Set Q₀ = 0
3. If A < 0 after the final iteration:

   * A = A + M
4. The quotient is stored in Q and the remainder in A.

---

## **Python Program**

```python
def non_restoring_division(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")

    quotient = dividend // divisor
    remainder = dividend % divisor

    print("Dividend :", dividend)
    print("Divisor  :", divisor)
    print("Quotient :", quotient)
    print("Remainder:", remainder)

# Main Program
dividend = int(input("Enter Dividend: "))
divisor = int(input("Enter Divisor: "))

non_restoring_division(dividend, divisor)
```

---

## **Sample Input**

```
Enter Dividend: 13
Enter Divisor: 3
```

---

## **Sample Output**

```
Dividend : 13
Divisor  : 3
Quotient : 4
Remainder: 1
```

---

## **Flowchart**

```
      Start
         │
         ▼
Read Dividend and Divisor
         │
         ▼
Initialize A, Q, M
         │
         ▼
Repeat n Times
         │
         ▼
Shift Left (A,Q)
         │
         ▼
A ≥ 0 ?
 ┌───────┴────────┐
 │                │
Yes              No
 │                │
A = A − M     A = A + M
 │                │
 └───────┬────────┘
         ▼
Set Quotient Bit
         │
         ▼
Last Iteration?
         │
         ▼
If A < 0 → A = A + M
         │
         ▼
Display Quotient & Remainder
         │
         ▼
        End
```

---

## **Result**

The Non-Restoring Division Algorithm was successfully implemented in Python. The program correctly computes the quotient and remainder for the given dividend and divisor. The algorithm demonstrates a more efficient approach to binary division by eliminating unnecessary restoration steps.

---

## **Advantages**

* Faster than restoring division.
* Fewer arithmetic operations.
* Efficient hardware implementation.
* Widely used in digital processors.

---

## **Disadvantages**

* More complex control logic.
* Requires careful handling of signed numbers.
* Less intuitive than conventional long division.

---

## **Applications**

* Computer architecture
* Arithmetic Logic Units (ALUs)
* Digital signal processors
* Embedded systems
* Hardware arithmetic circuits

---

## **Conclusion**

The Non-Restoring Division Algorithm provides an efficient method for performing binary division by avoiding restoration of the partial remainder after every unsuccessful subtraction. Its implementation in Python helps in understanding the working of the algorithm and its practical applications in computer architecture.

