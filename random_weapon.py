from random import randint

def main(extended_limits):
    r_stars = randint(1,10)
    r_type = randint(1, 5)
    r_mainstat = randint(40, 100) / 100 if extended_limits == 0 else randint(0, 100 * (extended_limits + 1)) / 100
    r_substattype = randint(1, 8)
    r_substat = randint(60, 100) / 100 if extended_limits == 0 else randint(0, 100 * (extended_limits + 1)) / 100

    if r_stars <= 7:
        w_stars = 5
    elif r_stars <= 9:
        w_stars = 4
    else:
        w_stars = 3

    if r_type == 1:
        w_type = "Catalyst"
    elif r_type == 2:
        w_type = "Bow"
    elif r_type == 3:
        w_type = "Polearm"
    elif r_type == 4:
        w_type = "Sword"
    elif r_type == 5:
        w_type = "Claymore"

    w_mainstat = round((15 * r_type * w_stars + 375) * r_mainstat)

    if r_substattype == 1:
        w_substattype = "ATK"
    elif r_substattype == 2:
        w_substattype = "Crit DMG"
    elif r_substattype == 3:
        w_substattype = "Crit Rate"
    elif r_substattype == 4:
        w_substattype = "DEF"
    elif r_substattype == 5:
        w_substattype = "Elemental Mastery"
    elif r_substattype == 6:
        w_substattype = "Energy Recharge"
    elif r_substattype == 7:
        w_substattype = "HP"
    elif r_substattype == 8:
        w_substattype = "Physical DMG Bonus"

    if r_substattype == 5: # EM
        w_substat = round(90 * (w_stars - 2) * r_substat)
    elif r_substattype in [2, 3]: # crit
        w_substat = round((10 * (4 - r_substattype) * (w_stars - 2) + 30) * r_substat, 1)
    elif r_substattype in [4, 6, 8]: # DEF / ER / phys dmg bonus
        w_substat = round((20 * (w_stars - 2) + 10) * r_substat, 1)
    else: # ATK / HP
        w_substat = round((15 * (w_stars - 2) + 15) * r_substat, 1)

    # return f"{w_stars}* {w_type}", f"ATK {w_mainstat}{' '*4}{w_substattype} {w_substat}{'%' if r_substattype != 5 else ''}"
    return w_stars, w_type, w_mainstat, w_substattype, w_substat
