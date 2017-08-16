class Gear(object):

    DIRECT = 0
    TURN = 1

    @staticmethod
    def getDict():
        return {Gear.DIRECT: None,
                Gear.TURN: None}
