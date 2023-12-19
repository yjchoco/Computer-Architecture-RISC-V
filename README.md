# Computer-Architecture-RISC-V

### Project 1
Interpret RISC-V binary code.
The program reads a binary file containing RISC-V machine code and prints the assembly representation of the code.

Support following instructions:
lui, auipc, jal, jalr, beq, bne, blt, bge, bltu, bgeu, lb, lh, lw, lbu, lhu, sb, sh, sw, addi, slti, sltiu, xori, ori, andi, slli, srli, srai, add, sub, sll, slt, sltu, xor, srl, sra, or, and

>> implemented in **riscv-sim_proj1.py**


### Project 2
Simulate a single-cycle CPU.
Implement an instruction simulator that supports a subset of RISC-V instructions. The program reads instructions from the binary file and execute the instructions one-by-one. At the end of the execution, your program prints out the current value of the registers, and that should match with the expected output on a real RISC-V processor.

Support following instructions:
add, sub, addi, xor, or, and, xori, ori, andi, slli, srli, srai, sll, srl, sra, slti, slt, auipc, lui, jal, jalr, beq, bne, blt, bge, lw, sw

>> implemented in **riscv-sim_proj2.py**


### Project 3
Modifying the Spike RISC-V instruction simulator to implement the LRU replacement algorithm.

>> modified **\riscv\cachesim.cc** and **\riscv\cachesim.h**
