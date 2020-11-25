`include "sar.v"

module teset (
);
    
reg clk, reset, en, start, cmp;
wire intr, hold;
wire [4:0] data;

sar u(  
    clk,
    reset,
    en,
    start,
    intr,
    hold,
    cmp,
    data
);

always #1 clk = ~clk;

initial begin
    $dumpfile("test.vcd");
    $dumpvars;
    clk = 0;
    reset = 1;
    en = 1;
    start = 1;
    cmp = 1;
    #2 reset = 0;
    #50;
    $finish;
end

endmodule