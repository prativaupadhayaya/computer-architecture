# Lab Report: VHDL Code for Combinational Circuit

## Aim

To design and simulate a combinational circuit using VHDL.

## Theory

A combinational circuit is a digital circuit whose output depends only on the present input values. Logic gates such as AND, OR, and NOT are examples of combinational circuits.

## VHDL Code

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity AND_Gate is
    Port (A, B : in STD_LOGIC;
          Y : out STD_LOGIC);
end AND_Gate;

architecture Behavioral of AND_Gate is
begin
    Y <= A and B;
end Behavioral;
```

## Procedure

1. Write the VHDL code.
2. Compile the program.
3. Simulate the circuit.
4. Verify the output.

## Result

The combinational circuit was successfully implemented and verified using VHDL.

## Conclusion

The VHDL code for the combinational circuit worked correctly and produced the expected output.
