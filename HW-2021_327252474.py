import random
import time



                                    # 1 vs 1 #
# Race between two horses
def HorseRace(horse_name1, horse_name2, competition_name, race_range=500):
    # Checking the winner
    def RangeCheck(horse1, horse2, rnd1, rnd2, race_range):
        sum_range1, sum_range2 = 0, 0
        while sum_range1 < race_range:
            sum_range1 += rnd1
            sum_range2 += rnd2
            print('Name:{}    [{}]  ||  Name:{}    [{}]'.format(horse1, sum_range1, horse2, sum_range2))
            time.sleep(0.2)
        if sum_range1 > sum_range2:
            print('     *' * 7)
            print('Congragulations {} won the race!!\n{} ended second place'.format(horse_name1[0], horse_name2[0]))
            print('     *' * 7)
            print('\n')
            return horse_name1
        else:
            print('     *' * 7)
            print('Congragulations {} won the race!!\n{} ended second place'.format(horse_name2[0], horse_name1[0]))
            print('     *' * 7)
            print('\n')
            return horse_name2

    # The main function for the race
    print('\n')
    print('         {}'.format(competition_name))
    print('    ************************')
    print('\n')
    print('RACE STARTS NOW!\n      <<< {}  vs  {} >>>'.format(horse_name1[0], horse_name2[0]))
    if race_range > 500:
        rnd_h1 = random.randint(race_range // 20, race_range // 10)
        rnd_h2 = random.randint(race_range // 20, race_range // 10)
    else:
        rnd_h1 = random.randint(race_range // 20, race_range // 10)
        rnd_h2 = random.randint(race_range // 20, race_range // 10)
    rnd1, rnd2 = rnd_h1, rnd_h2
    return RangeCheck(horse_name1[0], horse_name2[0], rnd1, rnd2, race_range)


# ==================================================================================================
                                    # Random Horses
def ChoiceHorses(horse_list, number_horses):
    new_horse_list = []
    previous = []
    for i in range(number_horses):
        random_index = random.randrange(0, len(horse_list))
        while random_index in previous:
            random_index = random.randrange(0, len(horse_list))
        new_horse_list.append(horse_list[random_index])
        previous.append(random_index)
    return new_horse_list


# ==================================================================================================
                                        # Horse Racing
def HorseRacing(horse_list, competition_name, race_range=500, number_horses=2 ** 2):
    horses_of_choice, winner = [], []
    horses_of_choice.extend(ChoiceHorses(horse_list, number_horses))  # בניית רצף של הסוסים שניבחרו לתחרות

    print(horses_of_choice)

    for i in range(0, len(horses_of_choice), 2):
        name1 = horses_of_choice[i]
        name2 = horses_of_choice[i + 1]
        if HorseRace(name1, name2, competition_name, race_range) == name1: 
            name1[2] += 1
            name1[3] += 5
            winner.append(name1)
        else:  
            name2[2] += 1
            name2[3] += 5
            winner.append(name2)

    while len(winner) > 1:
        name1 = winner[0]
        name2 = winner[1]
        if HorseRace(name1, name2, competition_name, race_range) == name1:
            name1[2] += 1
            name1[3] += 5
            winner_of_all = name1
        else:
            name1[2] += 1
            name1[3] += 5
            winner_of_all = name2
        winner.insert(len(winner), winner_of_all)
        winner.remove(winner[1])
        winner.remove(winner[0])

    print()
    print('AND THE WINNER ISSSS:\n          {}\n    {}'.format(winner_of_all[0], winner_of_all))

#======================================================================================================
                                        # PrintList
def PrintList (horse_list, num = 0):
    col = ('name ', 'age ', 'wins ', 'points ')
    lname, lage, lwins, lpoints=[], [], [], []
    i=0
    while i != len(horse_list):
        name = horse_list[i]
        lname.append(name[0])
        lage.append(name[1])
        lwins.append(name[2])
        lpoints.append(name[3])
        i += 1
    if num < 0:
        horse_list.reverse()
        num *= -1
    for i in range(len(horse_list)):
        print('{:15}{:5}{:5}{:8}'.format(horse_list[i][0],horse_list[i][1],horse_list[i][2],horse_list[i][3]))
        if i == num - 1:
            break
 #====================================================================================================
                                       #SortHorses
def SortHorses (horse_list, choice = 'points', num = 2):
    def SortPoints (list1):
        index = list1[3]
        return index
    def SortWins (list1):
        index = list1[2]
        return index
    def SortAge (list1):
        index = list1[1]
        return index

    if choice == 'points':
        for _ in range(len(horse_list)):
            horse_list.sort(key=SortPoints)
            if num == 2:
                horse_list.reverse()
        PrintList(horse_list, 0)
        return horse_list
    if choice == 'wins':
        for _ in range(len(horse_list)):
            horse_list.sort(key=SortWins)
            if num == 2:
                horse_list.reverse()
        PrintList(horse_list, 0)
        return horse_list
    if choice == 'age':
        for _ in range(len(horse_list)):
            horse_list.sort(key=SortAge)
            if num == 2:
                horse_list.reverse()
        PrintList(horse_list, 0)
        return horse_list
#==================================================================================================
                                    # AddHorse
def AddHorse (horse_list):
    new_horse = []
    name = input('\nEnter horse name: ')
    age = int(input('Enter horse age: '))
    wins = int(input('Enter amount of wins the horse have: '))
    points = int(input('Enter amount of points the horse have: '))
    new_horse = [name, age, wins, points]
    horse_list.append(new_horse)
    SortHorses (horse_list, choice = 'points', num = 2)
    return horse_list
#==================================================================================================
                                    # RemoveHorse
def RemoveHorse (horse_list):
    SortHorses(horse_list)
    last = horse_list[len(horse_list)-1]
    horse_list.remove(last)
    return horse_list

#==================================================================================================
                                    # Menu
def Menu (horse_list):
    flag = True
    decoration = lambda y: y*60
    while flag == True:
        print('\n',decoration('*'))
        print('\n####### Menu #######\n')
        print('Press 1 to add horse.\nPress 2 to delete horse.\nPress 3 to sort horses list.\nPress 4 to print the list.\nPress 5 for horse race.\nPress 9 to exit.')
        print(decoration('*')) 
        choice = int(input('Enter here your choice: '))
        if choice > 5 and choice < 9 or choice > 9 or choice < 1 :
            print('\n      Error\nPlease Choose other option !')
        elif choice == 1:
            AddHorse (horse_list)
        elif choice == 2:
            RemoveHorse (horse_list)
        elif choice == 3:
            asking_user = input('Do you want to make a selection nor you want to skip?\nPlease enter:\n* selection\n* skip\nEnter here: ')
            if asking_user == 'selection':
                num = int(input('\nEnter here number of sorting:\n1. Growing\n2. Up side down\n'))
                user_choice = input('Write by what you want the sort:\n1. By points\n2. By wins\n3. By horse age\n')
                SortHorses (horse_list, user_choice, num)
            elif asking_user == 'skip':
                num = 2
                user_choice = 'points'
                SortHorses(horse_list, user_choice, num)

        elif choice == 4:
            num = int(input('\nEnter how do you want to see the horses:\n* Press 0 to normal list\n* Press number lower than zero to amount of horses from end\n* Press number higher than zero to amount of horses from start\n'))
            PrintList (horse_list, num)
        elif choice == 5:
            amount_of_horses_to_compite = int(input('\nEnter amount of horses that you want to see in the competition 2**n: '))
            race_range = int(input('Enter race distance: '))
            competition_name = 'EU Championship'
            HorseRacing(horse_list, competition_name, race_range, 2 ** amount_of_horses_to_compite)
        elif choice == 9:
            flag = False
        
            
# --------------------------------------------------------------------------------------------------
# * Main Function !*********||
# --------------------------------------------------------------------------------------------------

horse_list = [['Khal', 4, 2, 25],
              ['Jhon', 6, 4, 50],
              ['Bob', 8, 4, 60],
              ['Jerry', 7, 6, 86],
              ['Billi', 9, 7, 65],
              ['Tom', 3, 9, 152],
              ['Jelly', 6, 0, 40],
              ['Leon', 8, 2, 30]]

Menu(horse_list)
