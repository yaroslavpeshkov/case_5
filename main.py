# Part of case-study #5
# Developers: Khramchikhina A., Peshkov Y., Sanzhanova A., Yurshenaite A.
#

import ru_local as ru
import random


def draw():
    '''
    The function conducts a draw of the game.
    :return: None
    '''
    team = [1, 2, 3, 4]
    team_1 = random.choice(team)
    team.remove(team_1)
    team_2 = random.choice(team)
    team.remove(team_2)
    team_3 = random.choice(team)
    team.remove(team_3)
    team_4 = random.choice(team)
    print(f'{ru.TEAMS_1}{team_1}{ru.AND}{team_2}.')
    print(f'{ru.TEAMS_2}{team_3}{ru.AND}{team_4}')


def patron():
    '''
    The function shuffles the bullets in the clip.
    :return: list with the order of bullets in the clip
    '''
    patrons = [ru.EMPTY_BULLET, ru.EMPTY_BULLET, ru.EMPTY_BULLET, ru.EMPTY_BULLET, ru.EMPTY_BULLET,
               ru.COMBAT_BULLET, ru.COMBAT_BULLET, ru.COMBAT_BULLET, ru.COMBAT_BULLET, ru.COMBAT_BULLET]
    random.shuffle(patrons)
    return patrons


def arsenal():
    '''
    The function gives out four random objects in the beginning of the moves.
    :return: list with the selected objects
    '''
    arsenal_1 = [ru.GLASSES, ru.SAW, ru.HANDCUFFS, ru.MILKSHAKE, ru.TARGET]
    arsenal_i = []
    for i in range(4):
        i = random.randint(0, 4)
        arsenal_i.append(arsenal_1[i])
    arsenal_i.append(ru.NOTHING)
    return arsenal_i


def arsenal_2(arsenal_i):
    '''
    The function makes the order of selected objects.
    :param arsenal_i: list with the selected objects
    :return: numbered list of selected objects
    '''
    arsenal_3 = (f'''{ru.YOUR_ARSENAL}
    1. {arsenal_i[0]}
    2. {arsenal_i[1]}
    3. {arsenal_i[2]}
    4. {arsenal_i[3]}
    5. {arsenal_i[4]}''')
    return arsenal_3


def glasses(list_1):
    '''
    The function shows the next bullet in the clip.
    :param list_1: list with the order of bullets in the clip
    :return: type of the next bullet in the clip
    '''
    return list_1[0]


def saw(harm):
    '''
    The function doubles harm after shot for a one shot.
    :param harm: original value of harm (usually 1)
    :return: doubled value of harm
    '''
    harm *= 2
    return harm


def handcuffs(skip):
    '''
    The function skips a move of another player.
    :param skip: parameter of skipping (originally 0)
    :return: parameter of skipping after using handcuffs
    '''
    skip += 1
    return skip


def milkshake(hp):
    '''
    The function recovers one health point.
    :param hp: current health points
    :return: increased health points
    '''
    hp += 1
    return hp


def target(list_1):
    '''
    The function removes the next bullet in the clip.
    :param list_1: list with the order of bullets in the clip
    :return: type of the removed bullet in the clip
    '''
    patron_1 = f'{ru.THROW_AWAY}{list_1[0].lower()}.'
    list_1.pop(0)
    return patron_1


def round_1():
    '''
    The function conducts a first round of the game.
    :return: None
    '''
    print(ru.ROUND, 1)
    skip = 0
    hp_1 = 3
    hp_2 = 3
    break_flag = False
    shuffle_patrons = patron()
    while hp_1 > 0 and hp_2 > 0:
        harm = 1
        if skip == 0:
            print(f'{ru.HEALTH} {hp_1}:{hp_2}')
            print(ru.MOVE_1)
            arsenal_3 = arsenal()
            print(arsenal_2(arsenal_3))
            arsenal_choice = input(ru.OBJECT)
            while arsenal_choice not in arsenal_3:
                print(ru.MISTAKE)
                arsenal_choice = input(ru.OBJECT)
            match arsenal_choice:
                case ru.GLASSES:
                    print(glasses(shuffle_patrons))
                case ru.SAW:
                    harm = saw(harm)
                case ru.HANDCUFFS:
                    skip = handcuffs(skip)
                case ru.MILKSHAKE:
                    hp_1 = milkshake(hp_1)
                case ru.TARGET:
                    print(target(shuffle_patrons))
                case ru.NOTHING:
                    pass
            print(ru.MOVES)
            shot_choice = int(input(ru.SHOT_CHOICE))
            while shot_choice == 1:
                if len(shuffle_patrons) == 0:
                    shuffle_patrons = patron()
                    print(ru.RELOADING)
                if shuffle_patrons[0] == ru.COMBAT_BULLET:
                    hp_1 -= harm
                    print(ru.SHOT_COMBAT_1)
                else:
                    print(ru.SHOT_EMPTY_1)
                print(f'{ru.HEALTH} {hp_1}:{hp_2}')
                shuffle_patrons.pop(0)
                if hp_1 > 0:
                    shot_choice = int(input(ru.SHOT_CHOICE))
                else:
                    print(ru.DEATH_1)
                    break_flag = True
                    break
            if break_flag:
                break
            if len(shuffle_patrons) == 0:
                shuffle_patrons = patron()
                print(ru.RELOADING)
            if shuffle_patrons[0] == ru.COMBAT_BULLET:
                hp_2 -= harm
                print(ru.SHOT_COMBAT_2)
            else:
                print(ru.SHOT_EMPTY_2)
            if hp_2 <= 0:
                print(ru.DEATH_2)
                break
            shuffle_patrons.pop(0)
        else:
            skip = 0

        print(f'{ru.HEALTH} {hp_1}:{hp_2}')
        harm = 1
        print(ru.MOVE_2)
        if skip == 0:
            arsenal_4 = arsenal()
            print(arsenal_2(arsenal_4))
            arsenal_choice = input(ru.OBJECT)
            while arsenal_choice not in arsenal_4:
                print(ru.MISTAKE)
                arsenal_choice = input(ru.OBJECT)
            match arsenal_choice:
                case ru.GLASSES:
                    print(glasses(shuffle_patrons))
                case ru.SAW:
                    harm = saw(harm)
                case ru.HANDCUFFS:
                    skip = handcuffs(skip)
                case ru.MILKSHAKE:
                    hp_2 = milkshake(hp_2)
                case ru.TARGET:
                    print(target(shuffle_patrons))
                case ru.NOTHING:
                    pass
            print(ru.MOVES)
            shot_choice = int(input(ru.SHOT_CHOICE))
            while shot_choice == 1:
                if len(shuffle_patrons) == 0:
                    shuffle_patrons = patron()
                    print(ru.RELOADING)
                if shuffle_patrons[0] == ru.COMBAT_BULLET:
                    hp_2 -= harm
                    print(ru.SHOT_COMBAT_1)
                else:
                    print(ru.SHOT_EMPTY_1)
                print(f'{ru.HEALTH} {hp_1}:{hp_2}')
                shuffle_patrons.pop(0)
                if hp_2 > 0:
                    shot_choice = int(input(ru.SHOT_CHOICE))
                else:
                    print(ru.DEATH_2)
                    break_flag = True
                    break
            if break_flag:
                break
            if len(shuffle_patrons) == 0:
                shuffle_patrons = patron()
                print(ru.RELOADING)
            if shuffle_patrons[0] == ru.COMBAT_BULLET:
                hp_1 -= harm
                print(ru.SHOT_COMBAT_2)
            else:
                print(ru.SHOT_EMPTY_2)
            if hp_1 <= 0:
                print(ru.DEATH_1)
                break
            shuffle_patrons.pop(0)
        else:
            skip = 0


def round_2():
    '''
    The function conducts a second round of the game.
    :return: None
    '''
    print(ru.ROUND, 2)
    skip = 0
    hp_1 = 3
    hp_2 = 3
    break_flag = False
    shuffle_patrons = patron()
    while hp_1 > 0 and hp_2 > 0:
        harm = 1
        if skip == 0:
            print(f'{ru.HEALTH} {hp_1}:{hp_2}')
            print(ru.MOVE_1)
            arsenal_3 = arsenal()
            print(arsenal_2(arsenal_3))
            arsenal_choice = input(ru.OBJECT)
            while arsenal_choice not in arsenal_3:
                print(ru.MISTAKE)
                arsenal_choice = input(ru.OBJECT)
            match arsenal_choice:
                case ru.GLASSES:
                    print(glasses(shuffle_patrons))
                case ru.SAW:
                    harm = saw(harm)
                case ru.HANDCUFFS:
                    skip = handcuffs(skip)
                case ru.MILKSHAKE:
                    hp_1 = milkshake(hp_1)
                case ru.TARGET:
                    print(target(shuffle_patrons))
                case ru.NOTHING:
                    pass
            print(ru.MOVES)
            shot_choice = int(input(ru.SHOT_CHOICE))
            while shot_choice == 1:
                if len(shuffle_patrons) == 0:
                    shuffle_patrons = patron()
                    print(ru.RELOADING)
                if shuffle_patrons[0] == ru.COMBAT_BULLET:
                    hp_1 -= harm
                    print(ru.SHOT_COMBAT_1)
                else:
                    print(ru.SHOT_EMPTY_1)
                print(f'{ru.HEALTH} {hp_1}:{hp_2}')
                shuffle_patrons.pop(0)
                if hp_1 > 0:
                    shot_choice = int(input(ru.SHOT_CHOICE))
                else:
                    print(ru.DEATH_1)
                    break_flag = True
                    break
            if break_flag:
                break
            if len(shuffle_patrons) == 0:
                shuffle_patrons = patron()
                print(ru.RELOADING)
            if shuffle_patrons[0] == ru.COMBAT_BULLET:
                hp_2 -= harm
                print(ru.SHOT_COMBAT_2)
            else:
                print(ru.SHOT_EMPTY_2)
            if hp_2 <= 0:
                print(ru.DEATH_2)
                break
            shuffle_patrons.pop(0)
        else:
            skip = 0

        print(f'{ru.HEALTH} {hp_1}:{hp_2}')
        harm = 1
        print(ru.MOVE_2)
        if skip == 0:
            arsenal_4 = arsenal()
            print(arsenal_2(arsenal_4))
            arsenal_choice = input(ru.OBJECT)
            while arsenal_choice not in arsenal_4:
                print(ru.MISTAKE)
                arsenal_choice = input(ru.OBJECT)
            match arsenal_choice:
                case ru.GLASSES:
                    print(glasses(shuffle_patrons))
                case ru.SAW:
                    harm = saw(harm)
                case ru.HANDCUFFS:
                    skip = handcuffs(skip)
                case ru.MILKSHAKE:
                    hp_2 = milkshake(hp_2)
                case ru.TARGET:
                    print(target(shuffle_patrons))
                case ru.NOTHING:
                    pass
            print(ru.MOVES)
            shot_choice = int(input(ru.SHOT_CHOICE))
            while shot_choice == 1:
                if len(shuffle_patrons) == 0:
                    shuffle_patrons = patron()
                    print(ru.RELOADING)
                if shuffle_patrons[0] == ru.COMBAT_BULLET:
                    hp_2 -= harm
                    print(ru.SHOT_COMBAT_1)
                else:
                    print(ru.SHOT_EMPTY_1)
                print(f'{ru.HEALTH} {hp_1}:{hp_2}')
                shuffle_patrons.pop(0)
                if hp_2 > 0:
                    shot_choice = int(input(ru.SHOT_CHOICE))
                else:
                    print(ru.DEATH_2)
                    break_flag = True
                    break
            if break_flag:
                break
            if len(shuffle_patrons) == 0:
                shuffle_patrons = patron()
                print(ru.RELOADING)
            if shuffle_patrons[0] == ru.COMBAT_BULLET:
                hp_1 -= harm
                print(ru.SHOT_COMBAT_2)
            else:
                print(ru.SHOT_EMPTY_2)
            if hp_1 <= 0:
                print(ru.DEATH_1)
                break
            shuffle_patrons.pop(0)
        else:
            skip = 0


def final_round():
    '''
    The function conducts a final round of the game.
    :return: None
    '''
    print(ru.FINAL_ROUND)
    skip = 0
    hp_1 = 3
    hp_2 = 3
    break_flag = False
    shuffle_patrons = patron()
    while hp_1 > 0 and hp_2 > 0:
        harm = 1
        if skip == 0:
            print(f'{ru.HEALTH} {hp_1}:{hp_2}')
            print(ru.MOVE_1)
            arsenal_3 = arsenal()
            print(arsenal_2(arsenal_3))
            arsenal_choice = input(ru.OBJECT)
            while arsenal_choice not in arsenal_3:
                print(ru.MISTAKE)
                arsenal_choice = input(ru.OBJECT)
            match arsenal_choice:
                case ru.GLASSES:
                    print(glasses(shuffle_patrons))
                case ru.SAW:
                    harm = saw(harm)
                case ru.HANDCUFFS:
                    skip = handcuffs(skip)
                case ru.MILKSHAKE:
                    hp_1 = milkshake(hp_1)
                case ru.TARGET:
                    print(target(shuffle_patrons))
                case ru.NOTHING:
                    pass
            print(ru.MOVES)
            shot_choice = int(input(ru.SHOT_CHOICE))
            while shot_choice == 1:
                if len(shuffle_patrons) == 0:
                    shuffle_patrons = patron()
                    print(ru.RELOADING)
                if shuffle_patrons[0] == ru.COMBAT_BULLET:
                    hp_1 -= harm
                    print(ru.SHOT_COMBAT_1)
                else:
                    print(ru.SHOT_EMPTY_1)
                print(f'{ru.HEALTH} {hp_1}:{hp_2}')
                shuffle_patrons.pop(0)
                if hp_1 > 0:
                    shot_choice = int(input(ru.SHOT_CHOICE))
                else:
                    print(ru.DEATH_1_F)
                    break_flag = True
                    break
            if break_flag:
                break
            if len(shuffle_patrons) == 0:
                shuffle_patrons = patron()
                print(ru.RELOADING)
            if shuffle_patrons[0] == ru.COMBAT_BULLET:
                hp_2 -= harm
                print(ru.SHOT_COMBAT_2)
            else:
                print(ru.SHOT_EMPTY_2)
            if hp_2 <= 0:
                print(ru.DEATH_2_F)
                break
            shuffle_patrons.pop(0)
        else:
            skip = 0

        print(f'{ru.HEALTH} {hp_1}:{hp_2}')
        harm = 1
        print(ru.MOVE_2)
        if skip == 0:
            arsenal_4 = arsenal()
            print(arsenal_2(arsenal_4))
            arsenal_choice = input(ru.OBJECT)
            while arsenal_choice not in arsenal_4:
                print(ru.MISTAKE)
                arsenal_choice = input(ru.OBJECT)
            match arsenal_choice:
                case ru.GLASSES:
                    print(glasses(shuffle_patrons))
                case ru.SAW:
                    harm = saw(harm)
                case ru.HANDCUFFS:
                    skip = handcuffs(skip)
                case ru.MILKSHAKE:
                    hp_2 = milkshake(hp_2)
                case ru.TARGET:
                    print(target(shuffle_patrons))
                case ru.NOTHING:
                    pass
            print(ru.MOVES)
            shot_choice = int(input(ru.SHOT_CHOICE))
            while shot_choice == 1:
                if len(shuffle_patrons) == 0:
                    shuffle_patrons = patron()
                    print(ru.RELOADING)
                if shuffle_patrons[0] == ru.COMBAT_BULLET:
                    hp_2 -= harm
                    print(ru.SHOT_COMBAT_1)
                else:
                    print(ru.SHOT_EMPTY_1)
                print(f'{ru.HEALTH} {hp_1}:{hp_2}')
                shuffle_patrons.pop(0)
                if hp_2 > 0:
                    shot_choice = int(input(ru.SHOT_CHOICE))
                else:
                    print(ru.DEATH_2_F)
                    break_flag = True
                    break
            if break_flag:
                break
            if len(shuffle_patrons) == 0:
                shuffle_patrons = patron()
                print(ru.RELOADING)
            if shuffle_patrons[0] == ru.COMBAT_BULLET:
                hp_1 -= harm
                print(ru.SHOT_COMBAT_2)
            else:
                print(ru.SHOT_EMPTY_2)
            if hp_1 <= 0:
                print(ru.DEATH_1_F)
                break
            shuffle_patrons.pop(0)
        else:
            skip = 0


def main():
    '''
    The main function.
    :return: None
    '''
    print(ru.INFORMATION)
    draw()
    round_1()
    round_2()
    final_round()


if __name__ == '__main__':
    main()
