class Player(object):

    def __init__(self, theName, thePos=0):
        self._name = theName
        self._pos = thePos

    @property
    def Name(self):
        return self._name

    @property
    def Pos(self):
        return self._pos

    @Pos.setter
    def Pos(self, thePos):
        self._pos = thePos
