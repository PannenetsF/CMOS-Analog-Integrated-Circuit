//Verilog HDL for hw11, sar, verilog 
module sar (
    clk,
    reset,
    en,
    start,
    intr,
    hold,
    cmp,
    data
);

// the timing signal and control signal 
input clk, reset, en, start;
// the interrupt and discharge 
output reg intr, hold;

// the result of comparator 
input cmp;
// the output of SAR 
output reg [4:0] data;

reg [3:0] status;
reg [3:0] cnt;
reg [4:0] bit_flag; 
`define idle 0 
`define init 1 
`define compare 2  
`define check 3  
`define ready 4
`define bitwidth 5  

always @(posedge clk or reset) begin
    if (reset | !en) begin
        data <= 0;
        intr <= 0;
        status <= `idle;
        cnt <= 0;
        hold <= 0;
        bit_flag <= 5'b10000;
    end    
    else begin
        case (status)
            `idle : begin
                if (start) begin
                    status <= `init;
                end
                hold <= 0;
                intr <= 0;
            end
            `init: begin
                // do sampling
                data <= 5'b11111;
                cnt <= 0;
                bit_flag <= 5'b10000;
                status <= `ready;
            end
            `ready: begin
                hold <= 1;
                data <= 0;
                status <= `compare;
            end
            `compare: begin
                data <= data | bit_flag;
                cnt <= cnt + 1;
                status <= `check;
                // hold <= 0;
            end
            `check: begin
                if (cmp) begin 
                    // if the original data is larger, keep the bit
                    data <= data;
                end
                else begin
                    // else, discard the bit 
                    data <= data & ~(bit_flag);
                end
                if (cnt == `bitwidth) begin
                    cnt <= 0;
                    bit_flag <= 5'b10000;
                    intr <= 1;
                    hold <= 0;
                    status <= `idle;
                end
                else begin
                    bit_flag <= (bit_flag) >> 1;
                    status <= `compare;
                end
            end
        endcase
    end
end



endmodule
