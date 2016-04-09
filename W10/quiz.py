from libdw import sm


class countOdd(sm.SM):
    startState = 0

    def getNextValues(self, state, inp): #state means current state of machine
        if inp % 2 != 0:
            nextstate = state + 1
            output = nextstate
        else:
            nextstate = 0
            output = nextstate
        return nextstate, output


meow = countOdd()
a = [1, 4, 3, 6, 2, 3, 9, 11, 13]
print meow.transduce(a)