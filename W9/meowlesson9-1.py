# Homework

# Problem 3

from libdw import sm


class CommentsSM(sm.SM):
    startState = 'No comment'

    def getNextValues(self, state, inp):
        if state == 'No comment':
            if inp == '#':
                nextstate = 'Comment present'
                return nextstate, inp
            else:
                return state, None
        elif state == 'Comment present':
            if inp == '\n':
                nextstate = 'No comment'
                return nextstate, None
            else:
                return state, inp


# string = 'def f(x): # comment\n   return 1'
# m = CommentsSM()
# print m.transduce(string)

# Problem 4
mystr = []
class FirstWordSM(sm.SM):
    startState = 'First word'  # fix this

    def getNextValues(self, state, inp):
        if state == 'First word':
            if inp != ' ' and inp != '\n':
                nextstate = state
                out = inp
                mystr.append(inp)
            elif inp == ' ': # and prev != ' ' or prev != '\n'
                if mystr[-1] not in [' ','\n']:
                    nextstate = 'Not first word'
                    out = None
                    mystr.append(inp)
                else:
                    nextstate = state
                    out = None
                    mystr.append(inp)
            elif inp == '\n':
                nextstate = state
                out = None
                mystr.append(inp)
            return nextstate,out
        if state == 'Not first word':
            if inp != '\n':
                nextstate = state
                mystr.append(inp)
            else:
                nextstate = 'First word'
                mystr.append(inp)
            return nextstate,None


string = 'def f(x): # comment\n   return 1'
m = FirstWordSM()
print m.transduce(string)
