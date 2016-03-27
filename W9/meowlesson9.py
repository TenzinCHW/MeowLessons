# Week 9 cohort

# Problem 1
from libdw import sm


class CM(sm.SM):
    startState = 0  # Special to SM class. Must have initial value

    def getNextValues(self, state, inp):  # Next state function
        if inp != 100 and inp != 50:  # Handles cases when an unknown coin is inserted
            nextstate = state
            output = (0, '--', inp)
            return nextstate, output
        elif state == 0:  # Handles case when state is 0
            if inp == 50:
                nextstate = 1
                output = (50, '--', 0)
            elif inp == 100:
                nextstate = 0
                output = (0, 'coke', 0)
            return nextstate, output
        elif state == 1:  # Handles cases when state is 1
            if inp == 50:
                nextstate = 0
                output = (0, 'coke', 0)
            elif inp == 100:
                nextstate = 0
                output = (0, 'coke', 50)
            return nextstate, output


# c = CM()
# c.start()
# print c.getNextValues(c.state, 50)
# meow = [50,50,100,3]
# print c.transduce(meow)
# print c.step(100)