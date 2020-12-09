#!/usr/bin/python3

# I do not do recursion

def RuleParser(rule):
    ruleList      = rule.split(' bags contain ')
    container     = ruleList[0]
    content       = ruleList[1]
    content       = ruleList[1].split(', ')
    return container, content

with open('input') as f:
    lines = [line.rstrip() for line in f]

bagsWithGold = 0
bagsInsideGold = 0
knownBags = {}

while len(lines) > 0:
    i = 0
    while i < len(lines):
        line = lines[i]
        unknownBagsFound = False
        bagVal_bags_and_gold = [0, 0]
        container, content = RuleParser(line)

        if content[0] == 'no other bags.':
            knownBags[container] = [0, 0]
            del lines[i]
        else:
            for con in content:
                num = int(con[0])
                clr = con[2:]
                clr = clr.split(' bag')
                clr = clr[0]
                if clr in knownBags.keys():
                    subContent = knownBags[clr]
                    bagVal_bags_and_gold[0] += num * (1 + subContent[0])
                    if clr == 'shiny gold' or subContent[1] == 1:
                        bagVal_bags_and_gold[1] = 1

                else:
                    unknownBagsFound = True
                    break
            if unknownBagsFound == False:
                if bagVal_bags_and_gold[1] == 1:
                    bagsWithGold += 1
                if container == 'shiny gold':
                    bagsInsideGold = bagVal_bags_and_gold[0]
                    
                knownBags[container] = bagVal_bags_and_gold
                del lines[i]
            else:
                i += 1

print("Bags with gold inside", bagsWithGold)
print("Bags inside gold", bagsInsideGold)
