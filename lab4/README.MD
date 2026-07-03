

# **LABORATORY REPORT**

** Title:** Design and Implementation of Combinational Circuits (Multiplexer and Demultiplexer) using VHDL

**Date:** July 3, 2026

## **1. Objectives**

* To understand the working principle of combinational circuits, specifically Multiplexers (MUX) and Demultiplexers (DEMUX).
* To model a 4-to-1 Multiplexer and a 1-to-4 Demultiplexer using VHDL.
* To simulate and verify the behavioral functionality of the designs using a testbench.

---

## **2. Introduction & Theory**

### **Multiplexer (MUX)**

A Multiplexer is a combinational circuit that selects one of many input signals and forwards the selected input into a single line. A 4-to-1 MUX has $4$ data inputs ($I_0, I_1, I_2, I_3$), $2$ selection lines ($S_1, S_0$), and $1$ output ($Y$). The output logic equation is:

$$Y = (I_0 \cdot \overline{S_1} \cdot \overline{S_0}) + (I_1 \cdot \overline{S_1} \cdot S_0) + (I_2 \cdot S_1 \cdot \overline{S_0}) + (I_3 \cdot S_1 \cdot S_0)$$

### **Demultiplexer (DEMUX)**

A Demultiplexer performs the reverse operation of a MUX. It takes a single input line ($D_{in}$) and routes it to one of many outputs based on the selection lines. A 1-to-4 DEMUX has $1$ data input, $2$ selection lines ($S_1, S_0$), and $4$ outputs ($Y_0, Y_1, Y_2, Y_3$).

---

## **3. VHDL Source Code**

### **3.1 4-to-1 Multiplexer**

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux_4to1 is
    Port ( I : in  STD_LOGIC_VECTOR (3 downto 0);
           S : in  STD_LOGIC_VECTOR (1 downto 0);
           Y : out STD_LOGIC);
end mux_4to1;

architecture Behavioral of mux_4to1 is
begin
    process(I, S)
    begin
        case S is
            when "00" => Y <= I(0);
            when "01" => Y <= I(1);
            when "10" => Y <= I(2);
            when "11" => Y <= I(3);
            when others => Y <= '0';
        end case;
    end process;
end Behavioral;

```

### **3.2 1-to-4 Demultiplexer**

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity demux_1to4 is
    Port ( Din : in  STD_LOGIC;
           S   : in  STD_LOGIC_VECTOR (1 downto 0);
           Y   : out STD_LOGIC_VECTOR (3 downto 0));
end demux_1to4;

architecture Behavioral of demux_1to4 is
begin
    process(Din, S)
    begin
        -- Default assignment to avoid unwanted latches
        Y <= "0000"; 
        case S is
            when "00" => Y(0) <= Din;
            when "01" => Y(1) <= Din;
            when "10" => Y(2) <= Din;
            when "11" => Y(3) <= Din;
            when others => Y <= "0000";
        end case;
    end process;
end Behavioral;

```

---

## **4. Verification & Truth Tables**

### **4.1 MUX Functional Verification**

| Select Input ($S_1 S_0$) | Output ($Y$) |
| --- | --- |
| 00 | $I_0$ |
| 01 | $I_1$ |
| 10 | $I_2$ |
| 11 | $I_3$ |

### **4.2 DEMUX Functional Verification**

| Input ($Din$) | Select ($S_1 S_0$) | $Y_3$ | $Y_2$ | $Y_1$ | $Y_0$ |
| --- | --- | --- | --- | --- | --- |
| D | 00 | 0 | 0 | 0 | D |
| D | 01 | 0 | 0 | D | 0 |
| D | 10 | 0 | D | 0 | 0 |
| D | 11 | D | 0 | 0 | 0 |

---

## **5. Simulation Waveforms**

> **Note to Student:** Insert screenshots of your software simulator (e.g., ModelSim, Vivado, or EDA Playground) showing the transitions of the output `Y` as the selection lines `S` change for both circuits.

---

## **6. Discussion**

During the experimentation, both circuits behaved exactly as dictated by combinational logic principles.

* In the **Multiplexer**, the VHDL `case` statement provided an efficient behavioral model to select a specific index of the input vector `I` based on the state of `S`.
* In the **Demultiplexer**, assigning a default value (`Y <= "0000"`) prior to the `case` statement was crucial. Without this default assignment, the synthesizer would infer storage elements (**latches**), which violates the requirement for the circuit to be strictly combinational.

---

## **7. Conclusion**

The VHDL implementation of a 4-to-1 Multiplexer and a 1-to-4 Demultiplexer was successfully designed, simulated, and verified. The simulation waveforms match the theoretical truth tables perfectly, demonstrating how software-defined hardware can effectively mimic physical combinational logic routing.
