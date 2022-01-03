import random

# min and max of the dice throws
min = 1
max = 6


def battle(attack, defense):
    battle = True
    attackwins = 0
    defendwins = 0
    for x in range(10000):
        attacktroops = attack
        defendtroops = defense
        battle = True
        
        while (battle):
            attackerrolls = []
            defenderrolls = []
            if (attacktroops > 2):
                for y in range(3):
                    attackerrolls.append(random.randint(min, max))
            elif (attacktroops > 1):
                for y in range(2):
                    attackerrolls.append(random.randint(min, max))
            else:
                attackerrolls.append(random.randint(min, max))

            if (defendtroops > 1):
                for z in range(2):
                    defenderrolls.append(random.randint(min, max))
            elif (defendtroops > 0):
                for z in range(1):
                    defenderrolls.append(random.randint(min, max))
            else:
                defenderrolls.append(random.randint(min, max))

            attackerrolls.sort(reverse=True)
            defenderrolls.sort(reverse=True)
            #print(attackerrolls)
            #print(defenderrolls)

            if (len(defenderrolls) > len(attackerrolls)):
                length = len(attackerrolls)

            else:
                length = len(defenderrolls)
            
            for a in range(length):
                if (attackerrolls[a] > defenderrolls[a]):
                    defendtroops -= 1
                    if (defendtroops == 0):
                        battle = False
                        attackwins += 1
            
                else:
                    attacktroops -= 1
                    if (attacktroops == 0):
                        battle = False
                        defendwins += 1

    



    print("the attack won " + str(attackwins) + " the defense won " + str(defendwins))
    print("The win probability is " + str(attackwins/(attackwins+defendwins)))  


#the input to this function battle(num_attack_troops, num_defense_troops)
battle(6,6)