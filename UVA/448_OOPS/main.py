from sys import stdin

instructions = (
    ('ADD', 2), ('SUB', 2), ('MUL', 2), ('DIV', 2), ('MOV', 2),
    ('BREQ', 1), ('BRLE', 1), ('BRLS', 1), ('BRGE', 1), ('BRGR', 1), ('BRNE', 1), ('BR', 1),
    ('AND', 3), ('OR', 3), ('XOR', 3), ('NOT', 1)
)
operand_modifs = ('R', '$', 'PC+', '')

def parse_operand(hexdump):
    code = int(hexdump, 16)
    mode = (code & (3 << 14)) >> 14
    value = code & ((1 << 14) - 1)
    return operand_modifs[mode] + str(value)

def parse_instruction(hexdump, pos):
    opcode = int(hexdump[pos], 16)
    instruction = instructions[opcode]
    new_pos = pos + (instruction[1] * 4) + 1
    operands = ','.join(
        parse_operand(hexdump[i:i + 4]) for i in range(pos + 1, new_pos, 4))
    assembly = instruction[0] + ' ' + operands
    return assembly, new_pos

hexdump = ''.join(map(str.strip, stdin.readlines()))

pos = 0
while pos < len(hexdump):
    assembly, pos = parse_instruction(hexdump, pos)
    print(assembly)
