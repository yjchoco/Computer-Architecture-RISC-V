import sys

reg = [0x00000000] * 32
PC = 0x00000000


def decode_I_format(inst):
    global PC
    opcode = inst & 0x7F
    rd = (inst >> 7) & 0x1F
    funct3 = (inst >> 12) & 0x7
    rs1 = (inst >> 15) & 0x1F
    imm = (inst >> 20) & 0xFFF
    funct7 = (inst >> 25) & 0x7F

    if imm & 0x800:  
        imm = imm - (1 << 12)


    f = ""

    if opcode == 0x03:
        if funct3 == 0x0:
                f = 'lb'
                print(f"{f} x{rd}, {imm}(x{rs1})")
        elif funct3 == 0x1:
                f = 'lh'
                print(f"{f} x{rd}, {imm}(x{rs1})")
        elif funct3 == 0x2:
                f = 'lw'
                #print(f"{f} x{rd}, {imm}(x{rs1})")
                add = reg[rs1] + imm
                if (add == 0x20000000):
                      user_input = input()
                      user_input = int(user_input)
                      reg[rd] = user_input
                else:
                      reg[rd] = DATA_MEMORY[add]
                PC += 4
        elif funct3 == 0x3:
                f = 'ld'
                print(f"{f} x{rd}, {imm}(x{rs1})")
        elif funct3 == 0x4:
                f = 'lbu'
                print(f"{f} x{rd}, {imm}(x{rs1})")
        elif funct3 == 0x5:
                f = 'lhu'
                print(f"{f} x{rd}, {imm}(x{rs1})")
        elif funct3 == 0x6:
                f = 'lwu'
                print(f"{f} x{rd}, {imm}(x{rs1})")
        else:
              print("unknown instruction")

    elif opcode == 0x13:
        if funct3 == 0x0 or funct3 == 0x2 or funct3 == 0x3 or \
        funct3 == 0x4 or funct3 == 0x6 or funct3 == 0x7: 
            if funct3 == 0x0:
                    f = 'addi'
                    #print(f"{f} x{rd}, x{rs1}, {imm}")
                    reg[rd] = reg[rs1] + imm
                    PC += 4
            elif funct3 == 0x2:
                    f = 'slti'
                    #print(f"{f} x{rd}, x{rs1}, {imm}")
                    if reg[rs1] < imm:
                      reg[rd] = 1
                      PC += 4
                    else:
                        reg[rd] = 0
                        PC += 4
            elif funct3 == 0x3:
                    f = 'sltiu'
                    print(f"{f} x{rd}, x{rs1}, {imm}")
            elif funct3 == 0x4:
                    f = 'xori'
                    #print(f"{f} x{rd}, x{rs1}, {imm}")
                    reg[rd] = reg[rs1] ^ imm
                    PC += 4
            elif funct3 == 0x6:
                    f = 'ori'
                    #print(f"{f} x{rd}, x{rs1}, {imm}")
                    reg[rd] = reg[rs1] | imm
                    PC += 4
            elif funct3 == 0x7:
                    f = 'andi'
                    #print(f"{f} x{rd}, x{rs1}, {imm}")
                    reg[rd] = reg[rs1] & imm
                    PC += 4
            
        elif funct3 == 0x1 or funct3 == 0x5:
            shamt = imm & 0x1F
            if funct3 == 0x1:
                f = 'slli'
                reg[rd] = reg[rs1] << shamt
                PC += 4
            elif funct3 == 0x5:
                if funct7 == 0x00:
                        f = 'srli'
                        reg[rd] = (reg[rs1] % 0x100000000) >> shamt
                        PC += 4
                elif funct7 == 0x20:
                        f = 'srai'
                        reg[rd] = reg[rs1] >> shamt
                        PC += 4

            #print(f"{f} x{rd}, x{rs1}, {shamt}")
        else:
              print("unknown instruction")
    elif opcode == 0x67 and funct3 == 0x0:    ########check
        f = 'jalr'
        #print(f"{f} x{rd}, {imm}(x{rs1})")
        reg[rd] = PC + 4
        PC = reg[rs1] + imm
    else:
        print("unknown instruction")
                        


def decode_R_format(inst):
    global PC
    opcode = inst & 0x7F
    rd = (inst >> 7) & 0x1F
    funct3 = (inst >> 12) & 0x7
    rs1 = (inst >> 15) & 0x1F
    rs2 = (inst >> 20) & 0x1F
    funct7 = (inst >> 25) & 0x7F

    f = ""

    if funct3 == 0x0:
        if funct7 == 0x00:
                f = "add"
                #print(f"{f} x{rd}, x{rs1}, x{rs2}")
                reg[rd] = reg[rs1] + reg[rs2]
                PC += 4
        elif funct7 == 0x20:
                f = 'sub'
                #print(f"{f} x{rd}, x{rs1}, x{rs2}")
                reg[rd] = reg[rs1] - reg[rs2]
                PC += 4
    elif funct3 == 0x1:
        if funct7 == 0x00:
                f = 'sll'
                #print(f"{f} x{rd}, x{rs1}, x{rs2}")
                reg[rd] = reg[rs1] << (reg[rs2] & 0x0000001F)
                PC += 4
    elif funct3 == 0x2:
        if funct7 == 0x00:
                f = 'slt'
                #print(f"{f} x{rd}, x{rs1}, x{rs2}")
                if reg[rs1] < reg[rs2]:
                      reg[rd] = 1
                      PC += 4
                else:
                      reg[rd] = 0
                      PC += 4
#     elif funct3 == 0x3:
#         if funct7 == 0x00:
#                 f = 'sltu'
#                 print(f"{f} x{rd}, x{rs1}, x{rs2}")
    elif funct3 == 0x4:
        if funct7 == 0x00:
                f = 'xor'
                #print(f"{f} x{rd}, x{rs1}, x{rs2}")
                reg[rd] = reg[rs1] ^ reg[rs2]
                PC += 4
    elif funct3 == 0x5:
        if funct7 == 0x00:
                f = 'srl'
                #print(f"{f} x{rd}, x{rs1}, x{rs2}")
                reg[rd] = (reg[rs1] % 0x100000000) >> (reg[rs2] & 0x0000001F)
                PC += 4
        elif funct7 == 0x20:
                f = 'sra'
                #print(f"{f} x{rd}, x{rs1}, x{rs2}")
                reg[rd] = reg[rs1] >> (reg[rs2] & 0x0000001F)
                PC += 4
    elif funct3 == 0x6:
        if funct7 == 0x00:
                f = 'or'
                #print(f"{f} x{rd}, x{rs1}, x{rs2}")
                reg[rd] = reg[rs1] | reg[rs2]
                PC += 4
    elif funct3 == 0x7:
        if funct7 == 0x00:
                f = 'and'
                #print(f"{f} x{rd}, x{rs1}, x{rs2}")
                reg[rd] = reg[rs1] & reg[rs2]
                PC += 4
    else:
        print("unknown instruction")



def decode_S_format(inst):
    global PC
    opcode = inst & 0x7F
    imm_lower = (inst >> 7) & 0x1F
    funct3 = (inst >> 12) & 0x7
    rs1 = (inst >> 15) & 0x1F
    rs2 = (inst >> 20) & 0x1F
    imm_upper = (inst >> 25) & 0x7F
    offset = (imm_upper << 5) | imm_lower

    if offset & 0x800:  # 부호 확인 
        offset = offset - (1 << 12)

    f = ''

    if funct3 == 0x0:
        f = 'sb'
        print(f"{f} x{rs2}, {offset}(x{rs1})")
    elif funct3 == 0x1:
        f = 'sh'
        print(f"{f} x{rs2}, {offset}(x{rs1})")
    elif funct3 == 0x2:
        f = 'sw'
        #print(f"{f} x{rs2}, {offset}(x{rs1})")
        add = reg[rs1] + offset
        if (add == 0x20000000):
              print(chr(reg[rs2]), end = '')
        else:
              DATA_MEMORY[add] = reg[rs2]
        PC += 4
    else:
        print("unknown instruction")
       
def decode_SB_format(inst):
    global PC
    opcode = inst & 0x7F
    imm11 = (inst >> 7) & 0x1
    imm4_1 = (inst >> 8) & 0xF
    funct3 = (inst >> 12) & 0x7
    rs1 = (inst >> 15) & 0x1F
    rs2 = (inst >> 20) & 0x1F
    imm10_5 = (inst >> 25) & 0x3F
    imm12 = (inst >> 31) & 0x1

    offset = (imm12 << 12) | (imm11 << 11) | (imm10_5 << 5) | (imm4_1 << 1)

    if offset & (1 << 12):
        offset = offset - (1 << 13)

    f = ''
    if funct3 == 0x0:
        f = 'beq'
        #print(f"{f} x{rs1}, x{rs2}, {offset}")
        if reg[rs1] == reg[rs2]:
              PC += offset
        else:
              PC += 4
    elif funct3 == 0x1:
        f = 'bne'
        #print(f"{f} x{rs1}, x{rs2}, {offset}")
        if reg[rs1] != reg[rs2]:
              PC += offset
        else:
              PC += 4
    elif funct3 == 0x4:
        f = 'blt'
        #print(f"{f} x{rs1}, x{rs2}, {offset}")
        if reg[rs1] < reg[rs2]:
              PC += offset
        else:
              PC += 4
    elif funct3 == 0x5:
        f = 'bge'
        #print(f"{f} x{rs1}, x{rs2}, {offset}")
        if reg[rs1] >= reg[rs2]:
              PC += offset
        else:
              PC += 4
#     elif funct3 == 0x6:
#         f = 'bltu'
#         print(f"{f} x{rs1}, x{rs2}, {offset}")
#     elif funct3 == 0x7:
#         f = 'bgeu'
#         print(f"{f} x{rs1}, x{rs2}, {offset}")
    else:
        print("unknown instruction")

def decode_U_format(inst):
    global PC
    opcode = inst & 0x7F
    rd = (inst >> 7) & 0x1F
    imm = (inst >> 12) & 0xFFFFF
    f = ''

    if imm & (1 << 19):
        imm = imm | 0xFFF00000
        imm = imm - (1 << 32)
    imm = imm << 12

    if opcode == 0x37:
        f = 'lui'
        #print(f"{f} x{rd}, {imm}")
        reg[rd] = imm
        PC += 4
    elif opcode == 0x17:
        f = 'auipc'
        #print(f"{f} x{rd}, {imm}")
        reg[rd] = PC + imm
        PC += 4
    else:
        print("unknown instruction")

def decode_UJ_format(inst):
    global PC
    opcode = inst & 0x7F    
    rd = (inst >> 7) & 0x1F         
    imm_20 = (inst >> 31) & 0x1     
    imm_10_1 = (inst >> 21) & 0x3FF 
    imm_11 = (inst >> 20) & 0x1     
    imm_19_12 = (inst >> 12) & 0xFF 

    imm = (imm_20 << 20) | (imm_19_12 << 12) | (imm_11 << 11) | (imm_10_1 << 1)
    
    if imm & 0x100000:  # 부호 확인 
        imm = imm | 0xFFE00000
        imm = imm - (1 << 32)

    if opcode == 0x6F:
        #print(f"jal x{rd}, {imm}")
        reg[rd] = PC + 4
        PC = PC + imm

'''
def read_instructions(file_path):
        with open(file_path, 'rb') as file:
                count=0
                while True:
                        data = file.read(4)
                        if not data:
                                break
                        inst = int.from_bytes(data, "little")
                        print(f"inst {count}: {inst:08x}", end = " ")

                        opcode = inst & 0x7F
                        if opcode == 0x33:
                                decode_R_format(inst)
                        elif opcode == 0x03 or opcode == 0x13 or opcode == 0x67:
                                decode_I_format(inst)
                        elif opcode == 0x23:
                                decode_S_format(inst)
                        elif opcode == 0x63:
                                decode_SB_format(inst)
                        elif opcode == 0x37 or opcode == 0x17:
                                decode_U_format(inst)
                        elif opcode == 0x6F:
                                decode_UJ_format(inst)
                        else:
                                print("unknown instruction")

                        count += 1
                        '''

INST_MEMORY = {}
DATA_MEMORY = {}

def execute_instruction_3(input_file_path_instructions, N):
        current_address = 0x00000000
        with open(input_file_path_instructions, "rb") as file:
                while True:
                    data = file.read(4)
                    if not data:
                        break
                    INST_MEMORY[current_address] = int.from_bytes(data, "little")
                    current_address += 4
        # instruction 하나씩 execute
        executed_cnt=0
        global PC
        while executed_cnt < N and PC in INST_MEMORY:
                exe_instruction(INST_MEMORY[PC])
                executed_cnt += 1
        # reg 32개 모두 출력
        for i in range(32):
              print(f"x{i}: 0x{reg[i]&0xFFFFFFFF:08x}")

def execute_instruction_4(input_file_path_instructions, input_file_path_data, N):
        current_address = 0x00000000
        current_data_address = 0x10000000
        end_data_address = 0x1000FFFF
        with open(input_file_path_instructions, "rb") as file:
                while True:
                    data = file.read(4)
                    if not data:
                        break
                    INST_MEMORY[current_address] = int.from_bytes(data, "little")
                    current_address += 4
        with open(input_file_path_data, "rb") as data_file:
              while True:
                    data = data_file.read(4)
                    if not data:
                          break
                    DATA_MEMORY[current_data_address] = int.from_bytes(data, "little", signed = True)
                    current_data_address += 4
                    
        while current_data_address <= end_data_address:
              DATA_MEMORY[current_data_address] = 0xFF
              current_data_address += 4
        
        
        # instruction 하나씩 execute
        executed_cnt=0
        global PC
        while executed_cnt < N and PC in INST_MEMORY:
                exe_instruction(INST_MEMORY[PC])
                executed_cnt += 1
        # reg 32개 모두 출력
        for i in range(32):
              print(f"x{i}: 0x{reg[i]&0xFFFFFFFF:08x}")
      

def exe_instruction(inst):
        opcode = inst & 0x7F
        if opcode == 0x33:
                decode_R_format(inst)
        elif opcode == 0x03 or opcode == 0x13 or opcode == 0x67:
                decode_I_format(inst)
        elif opcode == 0x23:
                decode_S_format(inst)
        elif opcode == 0x63:
                decode_SB_format(inst)
        elif opcode == 0x37 or opcode == 0x17:
                decode_U_format(inst)
        elif opcode == 0x6F:
                decode_UJ_format(inst)
        else:
                print("unknown instruction")
        reg[0] = 0x00000000
      


if __name__ == "__main__":
        if len(sys.argv) == 3:
                input_file_path_instructions = sys.argv[1]
                N = int(sys.argv[2])
                execute_instruction_3(input_file_path_instructions, N)

        elif len(sys.argv) == 4:
              input_file_path_instructions = sys.argv[1]
              input_file_path_data = sys.argv[2]
              N = int(sys.argv[3])
              execute_instruction_4(input_file_path_instructions, input_file_path_data, N)

        else:
                print("input error?")
                sys.exit(1)
