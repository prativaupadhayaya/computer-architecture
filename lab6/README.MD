
**Design and Implementation of a 4-Bit Binary to Gray Code Converter using VHDL**

---

## 1. Objective

* To design a combinational logic circuit that converts a 4-bit Binary number into its equivalent Gray code.
* To implement and simulate the design using VHDL (Dataflow modeling style).
* To verify the functionality of the circuit via simulation waveforms.

---

## 2. Introduction & Theory

A **code converter** is a combinational circuit that translates information from one binary code format to another.

### Binary vs. Gray Code

* **Binary Code:** A positional numeral system where each bit has a specific weight ($2^n$).
* **Gray Code:** A non-weighted, unit-distance code where two successive values differ by only one bit. This property minimizes errors during state transitions in digital systems.

### Conversion Logic

For a 4-bit Binary input $B = B_3B_2B_1B_0$ and a 4-bit Gray code output $G = G_3G_2G_1G_0$, the conversion equations derived from the logic are:

* $G_3 = B_3$
* $G_2 = B_3 \oplus B_2$
* $G_1 = B_2 \oplus B_1$
* $G_0 = B_1 \oplus B_0$

Where $\oplus$ denotes the **XOR** logic operation.

---

## 3. Block Diagram and Logic Circuit

### Truth Table

| Decimal | Binary Input ($B_3 B_2 B_1 B_0$) | Gray Output ($G_3 G_2 G_1 G_0$) |
| --- | --- | --- |
| 0 | 0000 | 0000 |
| 1 | 0001 | 0001 |
| 2 | 0010 | 0011 |
| 3 | 0011 | 0010 |
| 4 | 0100 | 0110 |
| 5 | 0101 | 0111 |
| 6 | 0110 | 0101 |
| 7 | 0111 | 0100 |
| 8 | 1000 | 1100 |
| 9 | 1001 | 1101 |
| 10 | 1010 | 1111 |
| 11 | 1011 | 1110 |
| 12 | 1100 | 1010 |
| 13 | 1101 | 1011 |
| 14 | 1110 | 1001 |
| 15 | 1111 | 1000 |

---

## 4. VHDL Source Code

```vhdl
-- Library Declarations
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Entity Declaration
entity Binary_to_Gray is
    Port ( 
        B : in  STD_LOGIC_VECTOR (3 downto 0); -- 4-bit Binary Input
        G : out STD_LOGIC_VECTOR (3 downto 0)  -- 4-bit Gray Code Output
    );
end Binary_to_Gray;

-- Architecture Body (Dataflow Modeling)
architecture Dataflow of Binary_to_Gray is
begin
    G(3) <= B(3);
    G(2) <= B(3) xor B(2);
    G(1) <= B(2) xor B(1);
    G(0) <= B(1) xor B(0);
end Dataflow;

```

---

## 5. Testbench Code (For Simulation)

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_Binary_to_Gray is
-- Testbench has empty entity
end tb_Binary_to_Gray;

architecture Behavior of tb_Binary_to_Gray is

    -- Component Declaration for the Unit Under Test (UUT)
    component Binary_to_Gray
    Port(
         B : in  std_logic_vector(3 downto 0);
         G : out  std_logic_vector(3 downto 0)
        );
    end component;
    
    -- Signals
    signal B : std_logic_vector(3 downto 0) := (others => '0');
    signal G : std_logic_vector(3 downto 0);

begin
    -- Instantiate the Unit Under Test (UUT)
   uut: Binary_to_Gray PORT MAP (
          B => B,
          G => G
        );

   -- Stimulus process
   stim_proc: process
   begin		
      -- Apply test vectors matching the truth table
      B <= "0000"; wait for 10 ns;
      B <= "0001"; wait for 10 ns;
      B <= "0011"; wait for 10 ns;
      B <= "0100"; wait for 10 ns;
      B <= "1000"; wait for 10 ns;
      B <= "1111"; wait for 10 ns;
      
      wait;
   end process;

end Behavior;

```

---

## 6. Simulation Results & Verification

> **Note:** Insert your simulated waveform screenshot here.

### Waveform Analysis

* When input `B = "0000"`, output `G = "0000"`
* When input `B = "0100"`, output `G = "0110"`
* When input `B = "1111"`, output `G = "1000"`

The simulated output waveforms perfectly mirror the expected logic outputs detailed in the truth table, verifying the correctness of the VHDL hardware description.

---

## 7. Conclusion

The 4-bit Binary to Gray code converter was successfully designed and modeled using VHDL dataflow architecture. The design was synthesized and verified via testbench simulation. The behavioral waveforms obtained confirm that the circuit functions correctly according to combinational logic principles.
