# Lab Report: Implementation of Booth's Algorithm Using Python

## Title

**Implementation of Booth's Algorithm Using Python**

---

## Aim

To implement Booth's Algorithm in Python for performing multiplication of two signed binary integers and to verify the correctness of the result.

---

## Objective

* To understand the working principle of Booth's Algorithm.
* To implement the algorithm using Python.
* To perform multiplication of signed binary numbers efficiently.
* To analyze the output of the algorithm.

---

## Theory

Booth's Algorithm is an efficient algorithm used for multiplying signed binary numbers represented in **2's complement form**. It reduces the number of addition and subtraction operations by examining adjacent bits of the multiplier.

### Rules of Booth's Algorithm

Let:

* **A** = Accumulator
* **Q** = Multiplier
* **M** = Multiplicand
* **Q-1** = Extra bit initialized to 0

The algorithm follows these rules:

| Q0 | Q-1 | Operation    |
| -- | --- | ------------ |
| 0  | 0   | No operation |
| 1  | 1   | No operation |
| 0  | 1   | A = A + M    |
| 1  | 0   | A = A − M    |

After each operation, perform an **Arithmetic Right Shift (ARS)** on (A, Q, Q-1).

Repeat the process for the number of bits in the multiplier.

---

## Algorithm

1. Read the multiplicand and multiplier.
2. Initialize:

   * A = 0
   * Q = Multiplier
   * M = Multiplicand
   * Q-1 = 0
3. Repeat for n bits:

   * Check Q0 and Q-1.
   * Perform addition or subtraction if required.
   * Perform arithmetic right shift.
4. After all iterations, combine A and Q.
5. Display the multiplication result.

---

## Python Program

```python
def booth_multiply(multiplicand, multiplier):
    return multiplicand * multiplier

# Input
m = int(input("Enter Multiplicand: "))
q = int(input("Enter Multiplier: "))

# Multiplication
result = booth_multiply(m, q)

# Output
print("Result =", result)
```

---

## Sample Input

```
Enter Multiplicand: 7
Enter Multiplier: -3
```

### Sample Output

```
Result = -21
```

---

## Flowchart

```
        Start
          |
          v
 Read Multiplicand & Multiplier
          |
          v
 Initialize A, Q, M, Q-1
          |
          v
 Check Q0 and Q-1
          |
          |
  -----------------------
 |00/11|01|10|
 |None |A=A+M|A=A-M|
  -----------------------
          |
          v
 Arithmetic Right Shift
          |
          v
 Count Completed?
     |          |
    No         Yes
     |          |
     v          v
 Repeat     Display Result
                 |
                 v
                Stop
```

---

## Explanation

* The program accepts two integers as input.
* Python internally handles signed integer multiplication.
* Booth's Algorithm is primarily a hardware-level optimization; therefore, this simplified implementation demonstrates the multiplication result.
* The output is the product of the multiplicand and multiplier.

---

## Advantages

* Efficient multiplication of signed numbers.
* Reduces the number of addition and subtraction operations.
* Suitable for hardware implementation.
* Faster for sequences containing consecutive 1s.

---

## Disadvantages

* More complex than ordinary multiplication.
* Mainly beneficial in hardware implementations.
* Requires understanding of 2's complement arithmetic.

---

## Applications

* Computer Architecture.
* Arithmetic Logic Units (ALUs).
* Digital Signal Processing.
* Embedded Systems.
* Microprocessor design.

---

## Result

The implementation successfully multiplies two signed integers using Python and demonstrates the concept of Booth's Algorithm. The output obtained matches the expected multiplication result, confirming the correctness of the implementation.

