
# LAB REPORT

## Title

**Introduction to VHDL Programming and Open-Source Simulation Environment**

## Objective

* To understand the basics of VHDL (VHSIC Hardware Description Language).
* To learn the structure and syntax of a VHDL program.
* To familiarize with an open-source simulation environment for VHDL design and testing.
* To create, compile, and simulate a simple VHDL program.

## Theory

### What is VHDL?

VHDL (VHSIC Hardware Description Language) is a hardware description language used for modeling, designing, and simulating digital electronic systems. It allows designers to describe the behavior and structure of digital circuits before implementing them on hardware such as FPGAs and ASICs.

### Features of VHDL

* Supports hierarchical design.
* Allows concurrent execution of statements.
* Enables simulation before hardware implementation.
* Supports behavioral, dataflow, and structural modeling.

### Basic Structure of a VHDL Program

A VHDL program mainly consists of:

1. **Library Declaration**

   ```vhdl
   library IEEE;
   use IEEE.STD_LOGIC_1164.ALL;
   ```

2. **Entity Declaration**
   Defines inputs and outputs of the circuit.

3. **Architecture Body**
   Describes the functionality of the circuit.

### Open-Source Simulation Environment

An open-source VHDL simulation environment allows users to write, compile, and simulate VHDL code without purchasing commercial software. One commonly used simulator is **GHDL**, which supports VHDL standards and provides waveform analysis when used with tools such as GTKWave.

### Advantages of Open-Source Simulators

* Free to use.
* Platform independent.
* Suitable for educational and research purposes.
* Supports debugging and waveform visualization.

## Experiment

### Problem Statement

Design and simulate a 2-input AND gate using VHDL.

### VHDL Code

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity AND_GATE is
    Port (
        A : in STD_LOGIC;
        B : in STD_LOGIC;
        Y : out STD_LOGIC
    );
end AND_GATE;

architecture Behavioral of AND_GATE is
begin
    Y <= A and B;
end Behavioral;
```

### Testbench Code

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity TB_AND_GATE is
end TB_AND_GATE;

architecture Behavioral of TB_AND_GATE is

    signal A, B, Y : STD_LOGIC;

begin

    UUT: entity work.AND_GATE
        port map (
            A => A,
            B => B,
            Y => Y
        );

    process
    begin
        A <= '0'; B <= '0'; wait for 10 ns;
        A <= '0'; B <= '1'; wait for 10 ns;
        A <= '1'; B <= '0'; wait for 10 ns;
        A <= '1'; B <= '1'; wait for 10 ns;
        wait;
    end process;

end Behavioral;
```

## Procedure

1. Install GHDL and GTKWave.
2. Create a VHDL source file for the AND gate.
3. Create a testbench file.
4. Compile the design using GHDL.
5. Run the simulation.
6. Generate waveform output.
7. View the waveform in GTKWave.
8. Verify the results with the AND gate truth table.

## Observation

| A | B | Y = A AND B |
| - | - | ----------- |
| 0 | 0 | 0           |
| 0 | 1 | 0           |
| 1 | 0 | 0           |
| 1 | 1 | 1           |

The simulation output matched the expected truth table of the AND gate.

## Result

The VHDL program for a 2-input AND gate was successfully designed and simulated using an open-source simulation environment. The obtained waveform verified the correct operation of the circuit.

## Conclusion

This experiment provided an introduction to VHDL programming and demonstrated the use of an open-source simulation environment. VHDL enables efficient digital circuit design and verification before hardware implementation. Open-source tools such as GHDL and GTKWave offer a cost-effective platform for learning and development.

## Viva Questions

1. What does VHDL stand for?
2. What is the purpose of an entity in VHDL?
3. What is an architecture in VHDL?
4. What is the difference between simulation and synthesis?
5. Name two open-source VHDL simulation tools.
6. Why is a testbench required?
7. What is the function of the IEEE library?
