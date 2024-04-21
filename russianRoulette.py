import random as rng
"""
implement class system
powerups
armor system
"""
chamberRoll = lambda a,b : True if rng.randint(1,a) == 1 else False
""" CLASSES
mage inflicts burn as attacker
paladin has all shields multiplied *2 but hp increasers are %50 percent effective
rogue has a %chance to dodge incoming attacks, and all armor bought is converted into dodge chance with a 1*1 exhcange rate 
"""
""" ITEMS
Items can be bought with gold from the shop, and they have three tiers: normal, epic and mythic. normal items increase only one stat,
epic items increase multiple stats and mythic items increase multiple stats and have passive abilities.
"""
def damageCalc(takenDmg,armor,aClass,dClass):
    dmg = armor - takenDmg
    return dmg
player = {
    "hp" : 5,
    "damage" : 2,
    "class" : "starter",
    "burnStacks" : 0,
    "attackSpeed" : 1,
    "armor" : 0,
    "gold" : 0
}
