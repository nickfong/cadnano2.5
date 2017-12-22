# -*- coding: utf-8 -*-
from collections import deque


class UndoCommand(object):
    def __init__(self, name=None):
        self.name = name
        self.commands = deque()
    # end def

    def redo(self):
        print('redoing***')
        for cmd in self.commands:
            cmd.redo()
    # end def

    def undo(self):
        print('undoing***')
        for cmd in self.commands:
            cmd.undo()
    # end def

    def addCommand(self, cmd):
        self.commands.append(cmd)
