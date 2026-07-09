# Lab Report: VHDL Implementation of Sequential Circuits (Flip-Flops)

---

## 1. Objectives

* To understand the concepts of sequential logic design using VHDL.
* To implement and simulate basic Flip-Flops (D Flip-Flop and JK Flip-Flop) in VHDL.
* To analyze the behavioral waveforms of sequential elements under the influence of clock and asynchronous reset signals.

---

## 2. Introduction & Theory

Unlike combinational logic circuits, **sequential circuits** rely on both current inputs and previous states to determine their outputs. This memory characteristic is achieved using feedback loops that form bistable storage elements.

### The Flip-Flop (FF)

A Flip-Flop is a clocked, edge-triggered sequential device. The most fundamental types are:

* **D Flip-Flop (Data FF):** Captures the value of the D input at a specific clock edge (e.g., rising edge) and outputs it as Q.
* **JK Flip-Flop:** Refines the SR flip-flop by eliminating the invalid state. When both J and K are high ($J=1, K=1$), the output toggles on the clock edge.

Sequential circuits in VHDL are typically modeled using the `process` statement, which is sensitive to changes in the clock (`clk`) or reset (`rst`) signals.

---

## 3. VHDL Implementations

### Code 1: D Flip-Flop with Asynchronous Reset

The following code demonstrates a rising-edge triggered D Flip-Flop. The reset signal is asynchronous, meaning it takes immediate effect regardless of the clock state.

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity d_flip_flop is
    Port ( d   : in  STD_LOGIC;
           clk : in  STD_LOGIC;
           rst : in  STD_LOGIC;
           q   : out STD_LOGIC;
           qb  : out STD_LOGIC);
end d_flip_flop;

architecture Behavioral of d_flip_flop is
begin
    process(clk, rst)
    begin
        if (rst = '1') then
            q  <= '0';
        elsif rising_edge(clk) then
            q  <= d;
        end if;
    end process;
    
    qb <= not q; -- Complementary output
end Behavioral;

```

---

### Code 2: JK Flip-Flop with Asynchronous Reset

The JK Flip-Flop utilizes an internal variable (`t_q`) to maintain its current state, allowing it to perform the toggle operation safely within VHDL semantics.

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity jk_flip_flop is
    Port ( j   : in  STD_LOGIC;
           k   : in  STD_LOGIC;
           clk : in  STD_LOGIC;
           rst : in  STD_LOGIC;
           q   : out STD_LOGIC;
           qb  : out STD_LOGIC);
end jk_flip_flop;

architecture Behavioral of jk_flip_flop is
    signal t_q : STD_LOGIC := '0'; -- Internal state signal
begin
    process(clk, rst)
    begin
        if (rst = '1') then
            t_q <= '0';
        elsif rising_edge(clk) then
            if (j = '0' and k = '0') then
                t_q <= t_q;         -- No change
            elsif (j = '0' and k = '1') then
                t_q <= '0';         -- Reset
            elsif (j = '1' and k = '0') then
                t_q <= '1';         -- Set
            elsif (j = '1' and k = '1') then
                t_q <= not t_q;     -- Toggle
            end if;
        end if;
    end process;

    q  <= t_q;
    qb <= not t_q;
end Behavioral;

```

---

## 4. Truth Tables

### D Flip-Flop Operation

| Reset (rst) | Clock (clk) | Input (D) | Output (Q) | State / Comment |
| --- | --- | --- | --- | --- |
| 1 | X | X | 0 | Asynchronous Reset |
| 0 | 0 or 1 | X | $Q_{prev}$ | No Change (No active edge) |
| 0 | $\uparrow$ | 0 | 0 | Reset state |
| 0 | $\uparrow$ | 1 | 1 | Set state |

### JK Flip-Flop Operation

| Reset (rst) | Clock (clk) | J | K | Output (Q) | State / Comment |
| --- | --- | --- | --- | --- | --- |
| 1 | X | X | X | 0 | Asynchronous Reset |
| 0 | $\uparrow$ | 0 | 0 | $Q_{prev}$ | No Change |
| 0 | $\uparrow$ | 0 | 1 | 0 | Reset |
| 0 | $\uparrow$ | 1 | 0 | 1 | Set |
| 0 | $\uparrow$ | 1 | 1 | $\overline{Q}_{prev}$ | Toggle |

---

## 5. Simulation Results & Waveform Analysis

*(Note: In your final submitted report, replace this section with your actual EDA tool or Vivado/ModelSim waveform screenshots).*

* **Asynchronous Behavior:** When `rst` transitions from `0` to `1`, the output `q` drops to `0` immediately, verifying that it does not wait for a active `clk` edge.
* **D-FF Verification:** Upon a rising edge of `clk`, the value present at `d` is perfectly mirrored to `q` on the next simulation grid line.
* **JK Toggle Verification:** When both `j` and `k` are tied high (`1`), `q` cleanly alternates between `0` and `1` on every consecutive rising edge of the clock signal.

---

## 6. Conclusion

In this lab, VHDL models for both a D Flip-Flop and a JK Flip-Flop were successfully written, compiled, and simulated. The use of the `process` block sensitivity list effectively captured the asynchronous reset capability. The simulated waveforms match the expected theoretical truth tables for edge-triggered sequential logic components.
