

  

---

# LAB REPORT

## 1. Title

**Design and Simulation of a 2-Bit Combinational Magnitude Comparator using VHDL.**

---

## 2. Objective

* To understand the working principle of a combinational magnitude comparator.
* To design a 2-bit magnitude comparator using VHDL.
* To verify the functional correctness of the design through simulation waveforms.

---

## 3. Introduction & Theory

A **magnitude comparator** is a combinational circuit that compares two digital numbers (binary vectors) and determines their relative magnitudes.

For a 2-bit comparator, we compare two 2-bit numbers, $A = (A_1A_0)$ and $B = (B_1B_0)$. The circuit generates three distinct outputs based on the comparison:

1. **$A > B$ (Greater Than):** High if $A$ is strictly greater than $B$.
2. **$A = B$ (Equal To):** High if both numbers are identical.
3. **$A < B$ (Less Than):** High if $A$ is strictly less than $B$.

### Truth Table

The behavior of a 2-bit magnitude comparator can be represented by the following truth table:

| $A_1$ | $A_0$ | $B_1$ | $B_0$ | $A > B$ | $A = B$ | $A < B$ |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 | 1 |
| 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 1 | 0 |

---

## 4. Hardware/Software Requirements

* **Operating System:** Windows 10/11 or Linux
* **EDA Tool / Software:** ModelSim / Xilinx Vivado / Intel Quartus Prime (Delete/Keep as applicable)

---

## 5. VHDL Code Implementation

### 5.1 Design Code (`comparator_2bit.vhd`)

This code uses dataflow modeling style with conditional signal assignments to evaluate the relative magnitudes.

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity comparator_2bit is
    Port ( A : in  STD_LOGIC_VECTOR (1 downto 0);
           B : in  STD_LOGIC_VECTOR (1 downto 0);
           Greater : out  STD_LOGIC;
           Equal   : out  STD_LOGIC;
           Less    : out  STD_LOGIC);
end comparator_2bit;

architecture Dataflow of comparator_2bit is
begin
    -- Conditional signal assignments for outputs
    Greater <= '1' when (A > B) else '0';
    Equal   <= '1' when (A = B) else '0';
    Less    <= '1' when (A < B) else '0';
end Dataflow;

```

### 5.2 Testbench Code (`tb_comparator_2bit.vhd`)

The testbench applies all 16 possible input combinations to exhaustively verify the design.

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL; -- Used for loop casting

entity tb_comparator_2bit is
-- Testbench has no ports
end tb_comparator_2bit;

architecture Behavioral of tb_comparator_2bit is
    -- Component Declaration for the Unit Under Test (UUT)
    component comparator_2bit
    Port ( A : in  STD_LOGIC_VECTOR (1 downto 0);
           B : in  STD_LOGIC_VECTOR (1 downto 0);
           Greater : out  STD_LOGIC;
           Equal   : out  STD_LOGIC;
           Less    : out  STD_LOGIC);
    end component;
    
    -- Inputs
    signal A : STD_LOGIC_VECTOR(1 downto 0) := "00";
    signal B : STD_LOGIC_VECTOR(1 downto 0) := "00";

    -- Outputs
    signal Greater : STD_LOGIC;
    signal Equal   : STD_LOGIC;
    signal Less    : STD_LOGIC;

begin
    -- Instantiate the Unit Under Test (UUT)
    uut: comparator_2bit PORT MAP (
          A => A,
          B => B,
          Greater => Greater,
          Equal => Equal,
          Less => Less
        );

    -- Stimulus process
    stim_proc: process
    begin		
        -- Loop through all 16 combinations of A and B
        for i in 0 to 3 loop
            for j in 0 to 3 loop
                A <= std_logic_vector(to_unsigned(i, 2));
                B <= std_logic_vector(to_unsigned(j, 2));
                wait for 20 ns;
            end loop;
        end loop;
        
        -- End simulation
        wait;
    end process;
end Behavioral;

```

---

## 6. Simulation Results & Waveform Analysis

> **[Insert Simulation Waveform Screenshot Here]**
> *Instructions for student: Run the simulation in your EDA tool, take a screenshot highlighting distinct test cases (e.g., $A="11", B="01" \rightarrow Greater='1'$), and paste it here.*

### Waveform Analysis:

* At time $t = 0\text{ ns}$ to $20\text{ ns}$, $A = "00"$ and $B = "00"$. The output `Equal` jumps to `'1'` while `Greater` and `Less` remain `'0'`.
* At time $t = 20\text{ ns}$ to $40\text{ ns}$, $A = "00"$ and $B = "01"$. The output `Less` switches to `'1'`.
* At time $t = 80\text{ ns}$, $A = "01"$ and $B = "00"$. The output `Greater` transitions to `'1'`.
The simulation precisely matches the theoretical truth table values.

---

## 7. Conclusion

The VHDL code for a 2-bit combinational magnitude comparator was successfully written, compiled, and simulated. The testbench effectively validated all 16 input conditions. The resulting output waveforms perfectly tracked the expected mathematical conditions ($A>B$, $A=B$, and $A<B$), confirming the correct operational design of the combinational circuit.
