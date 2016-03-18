# This is not my code, I merely helped my friend Jun Yi from class 15F04 to write some parts and adapted it to how I
# think in programming. Then I just copied it into my own code :x Also note the path name of his file. You can do this
# too if you are using a Unix based system such as Apple or any of the Linux distributions.
f = open("./data1.txt")


def getSchedule(f):
    info = f.readlines()
    dictionary = {}
    everything = []
    for i in info:
        everything += i.split()
    for i in range(len(everything)):
        day_list = []
        if len(everything[i]) > 2:
            hi = everything[i + 1:]
            for j in range(0, len(hi), 2):
                if len(hi[j]) <= 2:
                    meow = (int(hi[j]), int(hi[j+1]))
                    day_list.append(meow)
                else:
                    break
            dictionary[everything[i]] = day_list
    return dictionary


def dictSchedule(f):
    dictionary = {}
    for key, value in getSchedule(f).iteritems():
        summa = 0
        for i in range(len(value)):
            summa += value[i][1] - value[i][0]
        dictionary[key] = summa
    return dictionary

