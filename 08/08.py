#!/usr/bin/python3

checkList = []

with open('input') as f:
    program = [line.rstrip() for line in f]

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

checkList = zerolistmaker(len(program))

sum = 0
pc = 0
while pc < len(program):
    instr = program[pc]
    instrList = instr.split()
    op = instrList[0]
    arg = int(instrList[1])
    if checkList[pc] == 1:
        break
    checkList[pc] = 1
    if op == 'nop':
        pc += 1
    if op == 'jmp':
        pc += arg
    if op == 'acc':
        pc += 1
        sum += arg

print('Part 1',sum)


def opSwitcher(pc):
    instr = program[pc]
    instrList = instr.split()
    op = instrList[0]
    arg = instrList[1]
    if op == 'nop':
        op = 'jmp'
    
    elif op == 'jmp':
        op = 'nop'

    program[pc] = op + ' ' + arg


switcherInd = 0
outerQuit = False

while switcherInd < len(program) and outerQuit == False:
    with open('input') as f:
        program = [line.rstrip() for line in f]

    checkList = zerolistmaker(len(program))
    opSwitcher(switcherInd)

    sum = 0
    pc = 0
    innerQuit = False
    while pc < len(program) and innerQuit == False:
        instr = program[pc]
        instrList = instr.split()
        op = instrList[0]
        arg = int(instrList[1])
        if checkList[pc] == 1:
            innerQuit = True
        else:
            checkList[pc] = 1
            if op == 'nop':
                pc += 1
            if op == 'jmp':
                pc += arg
            if op == 'acc':
                pc += 1
                sum += arg
    if pc == len(program):
        outerQuit = True
    switcherInd += 1
print('Part 2',sum)
