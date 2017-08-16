from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import style_from_dict
from prompt_toolkit.token import Token
# import click
from fuzzyfinder import fuzzyfinder
from pygments.lexers.sql import SqlLexer
import sys
from game import Game
import shlex
import time


class GameCompleter(Completer):

    GameKeywords = ['exit', 'start', 'move', 'next', 'status']

    def get_completions(self, document, completeEvent):
        wordBeforeCursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(wordBeforeCursor, GameCompleter.GameKeywords)
        for m in matches:
            yield Completion(m, start_position=-len(wordBeforeCursor))


class Play(object):

    test_style = style_from_dict({Token.Toolbar: '#ffffff italic bg:#007777', })

    def __init__(self):
        self._cmdDict = {'exit': self.do_exit,
                         'start': self.do_start,
                         'move': self.do_move,
                         'next': self.do_next,
                         'status': self.do_status, }
        self._toolbarMessage = 'The Road Game'
        self._game = None

    @property
    def ToolbarMessage(self):
        return self._toolbarMessage

    @ToolbarMessage.setter
    def ToolbarMessage(self, theValue):
        self._toolbarMessage = theValue

    def getBottomToolbarTokens(self, thePlay):
        return [(Token.Toolbar, self.ToolbarMessage), ]

    def isCommand(self, theCmd):
        return theCmd in self._cmdDict.keys()

    def execCommand(self, theCmd, theUserInput):
        self._cmdDict[theCmd](theUserInput)

    def do_exit(self, theLine):
        sys.exit(0)

    def do_start(self, theLine):
        self.ToolbarMessage = '[STARTED] The Road Game'
        self._game = Game()
        self._game.init()

    def do_move(self, theLine):
        argos = shlex.split(theLine)
        car = self._game.getPlayerByIndex(int(argos[1]))
        adv, p, left = self._game.move(car)
        print('<{0}> ... {1}'.format(adv, car))

    def do_next(self, theLine):
        argos = shlex.split(theLine)
        if len(argos) == 2:
            repeats = int(argos[1])
        else:
            repeats = 1
        for x in range(repeats):
            for i in range(0, 3):
                car = self._game.getPlayerByIndex(i)
                adv, p, left = self._game.move(car)
                print('<{0}> ... {1}'.format(adv, car))
            if repeats > 1:
                print('----- END ROUND {0} -----'.format(x + 1))
                time.sleep(1)

    def do_status(self, theLine):
        for index in range(self._game.NbrOfPlayers):
            print(self._game.getPlayerByIndex(index))


if __name__ == '__main__':
    play = Play()
    while True:
        userInput = prompt('The Road Game> ',
                           history=FileHistory('history.txt'),
                           auto_suggest=AutoSuggestFromHistory(),
                           completer=GameCompleter(),
                           lexer=SqlLexer,
                           get_bottom_toolbar_tokens=play.getBottomToolbarTokens,
                           style=Play.test_style,
                           refresh_interval=1)
        # click.echo_via_pager(userInput)
        print(userInput)
        # message = click.edit()
        if userInput:
            cmd = userInput.split()[0]
            if play.isCommand(cmd):
                play.execCommand(cmd, userInput)
            play.LastCmd = userInput
