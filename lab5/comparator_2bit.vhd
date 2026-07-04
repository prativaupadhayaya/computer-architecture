library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity COMPARATOR_2BIT is
    port (
        A  : in std_logic_vector(1 downto 0);
        B  : in std_logic_vector(1 downto 0);
        EQ : out std_logic; -- A = B
        GT : out std_logic; -- A > B
        LT : out std_logic  -- A < B
    );
end entity COMPARATOR_2BIT;

architecture Dataflow of COMPARATOR_2BIT is
    signal eq1, eq0 : std_logic;
begin
    -- XNOR for bit equality
    eq1 <= not (A(1) xor B(1));
    eq0 <= not (A(0) xor B(0));

    -- Equations based on Boolean expressions
    EQ <= eq1 and eq0;

    GT <= (A(1) and not B(1)) or (eq1 and (A(0) and not B(0)));

    LT <= ((not A(1)) and B(1)) or (eq1 and ((not A(0)) and B(0)));
end architecture Dataflow;