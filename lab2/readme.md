# LAB REPORT

## Title

Realization of Basic Logic Gates Using VHDL

## Objective

To design, simulate, and verify the operation of basic logic gates (AND, OR, NOT, NAND, NOR, XOR, and XNOR) using VHDL.

## Apparatus/Software Required

* Computer System
* VHDL Simulator (Xilinx ISE / ModelSim / Vivado)
* VHDL Compiler

## Theory

Logic gates are the fundamental building blocks of digital circuits. VHDL (VHSIC Hardware Description Language) is used to describe the behavior and structure of digital systems. Basic logic gates perform logical operations on binary inputs and produce a binary output.

### Truth Tables

#### AND Gate

| A | B | Y |
| - | - | - |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

#### OR Gate

| A | B | Y |
| - | - | - |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

#### NOT Gate

| A | Y |
| - | - |
| 0 | 1 |
| 1 | 0 |

## VHDL Code

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity logic_gates is
    Port (
        A, B : in STD_LOGIC;
        AND_OUT  : out STD_LOGIC;
        OR_OUT   : out STD_LOGIC;
        NOT_OUT  : out STD_LOGIC;
        NAND_OUT : out STD_LOGIC;
        NOR_OUT  : out STD_LOGIC;
        XOR_OUT  : out STD_LOGIC;
        XNOR_OUT : out STD_LOGIC
    );
end logic_gates;

architecture Behavioral of logic_gates is
begin
    AND_OUT  <= A and B;
    OR_OUT   <= A or B;
    NOT_OUT  <= not A;
    NAND_OUT <= A nand B;
    NOR_OUT  <= A nor B;
    XOR_OUT  <= A xor B;
    XNOR_OUT <= A xnor B;
end Behavioral;
```

## Procedure

1. Open the VHDL simulation software.
2. Create a new project.
3. Write the VHDL code for logic gates.
4. Compile the code and remove any errors.
5. Create a testbench and apply different input combinations.
6. Run the simulation.
7. Observe and verify the output waveforms with the truth tables.

## Observation

The simulated outputs matched the expected truth tables for all logic gates.

## Result

The basic logic gates (AND, OR, NOT, NAND, NOR, XOR, and XNOR) were successfully realized using VHDL and verified through simulation.

## Conclusion

The experiment demonstrated the implementation and verification of basic logic gates using VHDL. The simulation results confirmed the correct functioning of all logic gates according to their respective truth tables.
