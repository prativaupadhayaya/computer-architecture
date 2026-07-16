Here is a comprehensive, structured lab report template for a VHDL-based sequential circuit (a synchronous 4-bit binary counter).

You can easily customize the details (such as dates, names, or specific board pin assignments) to match your actual lab requirements.

---

# **LABORATORY REPORT**

**Course:** Digital System Design / VHDL Lab

**Experiment Title:** Design and Implementation of a Sequential Circuit (4-Bit Binary Counter) using VHDL

**Date of Experiment:** July 16, 2026

---

## 1. Objectives

* To understand the concepts of sequential logic design using VHDL.
* To design, simulate, and implement a **4-bit synchronous up-counter** with asynchronous reset and clock enable features.
* To familiarize with the VHDL sequential statements (`process`, `if-then-else`) and edge-detection methods.
* To verify the design functionality using testbench simulation and waveform analysis.

---

## 2. Introduction & Theory

Unlike combinational circuits, **sequential circuits** have memory elements, meaning their outputs depend not only on the current inputs but also on the history of past inputs (state).

A **counter** is a classic sequential circuit that goes through a predetermined sequence of states triggered by a clock ($CLK$) signal. In a *synchronous* counter, all flip-flops are clocked simultaneously by the same common clock signal, preventing propagation delay issues (glitches) associated with ripple (asynchronous) counters.

### Key Features of this Design:

* **Asynchronous Reset ($RST$):** Instantly forces the counter output to `0000`, regardless of the clock signal.
* **Clock Enable ($EN$):** Allows the counter to increment only when active high; otherwise, it holds its current state.
* **4-bit Output ($Q$):** Counts from $0$ to $15$ ($0000$ to $1111$) and then rolls over to $0$.

---

## 3. Block Diagram

---

## 4. VHDL Source Code

Below is the VHDL RTL code implementing the 4-bit synchronous counter. It uses the `IEEE.NUMERIC_STD` library for clean, standard-compliant arithmetic operations.

```vhdl
--------------------------------------------------------------------------------
-- Entity: Counter_4bit
-- Description: 4-Bit Synchronous Up-Counter with Async Reset & Clock Enable
--------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Counter_4bit is
    Port (
        CLK   : in  STD_LOGIC;                     -- Clock Input
        RST   : in  STD_LOGIC;                     -- Asynchronous Reset (Active High)
        EN    : in  STD_LOGIC;                     -- Count Enable
        Q     : out STD_LOGIC_VECTOR (3 downto 0)  -- 4-bit Counter Output
    );
end Counter_4bit;

architecture Behavioral of Counter_4bit is
    -- Internal signal to hold the count value (using unsigned for arithmetic)
    signal r_count : unsigned(3 downto 0) := (others => '0');
begin

    -- Sequential Process
    process(CLK, RST)
    begin
        if RST = '1' then
            r_count <= (others => '0');            -- Asynchronous Reset
        elsif rising_edge(CLK) then
            if EN = '1' then
                r_count <= r_count + 1;            -- Increment counter
            end if;                                -- If EN = '0', state is implicitly held
        end if;
    end process;

    -- Output Assignment (Cast unsigned signal back to std_logic_vector)
    Q <= std_logic_vector(r_count);

end Behavioral;

```

---

## 5. Testbench Code

The testbench generates the clock stimulus, asserts the reset, and toggles the enable signal to verify the counter's behavior over time.

```vhdl
--------------------------------------------------------------------------------
-- Testbench for 4-Bit Counter
--------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity tb_Counter_4bit is
-- Testbench has no ports
end tb_Counter_4bit;

architecture Behavioral of tb_Counter_4bit is

    -- Component Declaration of Unit Under Test (UUT)
    component Counter_4bit
        Port (
            CLK   : in  STD_LOGIC;
            RST   : in  STD_LOGIC;
            EN    : in  STD_LOGIC;
            Q     : out STD_LOGIC_VECTOR (3 downto 0)
        );
    end component;

    -- Stimulus Signals
    signal clk_tb : STD_LOGIC := '0';
    signal rst_tb : STD_LOGIC := '0';
    signal en_tb  : STD_LOGIC := '0';
    signal q_tb   : STD_LOGIC_VECTOR (3 downto 0);

    -- Clock Period Definition
    constant CLK_PERIOD : time := 10 ns;

begin

    -- Instantiate the Unit Under Test (UUT)
    uut: Counter_4bit
        port map (
            CLK => clk_tb,
            RST => rst_tb,
            EN  => en_tb,
            Q   => q_tb
        );

    -- Clock Generation Process
    clk_process : process
    begin
        clk_tb <= '0';
        wait for CLK_PERIOD/2;
        clk_tb <= '1';
        wait for CLK_PERIOD/2;
    end process;

    -- Stimulus Process
    stim_proc: process
    begin		
        -- Step 1: Apply Reset
        rst_tb <= '1';
        en_tb <= '0';
        wait for 20 ns;	
        
        -- Step 2: Release Reset
        rst_tb <= '0';
        wait for 10 ns;
        
        -- Step 3: Enable Counting
        en_tb <= '1';
        wait for 160 ns; -- Let it count up to 1111 and roll over

        -- Step 4: Disable Counter (Hold State)
        en_tb <= '0';
        wait for 40 ns;

        -- Step 5: Enable again, then trigger mid-cycle Async Reset
        en_tb <= '1';
        wait for 30 ns;
        rst_tb <= '1';   -- Test asynchronous reset
        wait for 10 ns;
        rst_tb <= '0';

        wait; -- Stop simulation
    end process;

end Behavioral;

```

---

## 6. Simulation Results & Waveform Analysis

### **Observation Details:**

1. **Reset Phase ($t = 0\text{ ns}$ to $20\text{ ns}$):** While `RST` is active-high, the output `Q` is held steady at `"0000"`, ignoring clock transitions.
2. **Counting Phase ($t = 30\text{ ns}$ onwards):** With `RST` low and `EN` high, the counter increments on every positive edge of `CLK` (e.g., `"0000"` $\rightarrow$ `"0001"` $\rightarrow$ `"0010"`).
3. **Roll-over Behavior:** Once the output reaches `"1111"` ($15$), the next rising clock edge correctly wraps the value back to `"0000"`.
4. **Enable Hold Verification:** When `EN` is set to '0', the counter pauses counting and safely holds its last value until `EN` goes high again.

---

## 7. Conclusion

The 4-bit synchronous up-counter was successfully designed, simulated, and verified. By separating the asynchronous reset logic from the synchronous enable and increment operations inside the VHDL process, we achieved stable, predictable sequential behavior. The simulation waveforms perfectly match the expected behavioral truth table, validating that the VHDL code is ready for FPGA synthesis.
