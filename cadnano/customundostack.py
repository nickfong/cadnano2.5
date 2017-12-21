from PyQt5.QtWidgets import QUndoStack

from cadnano.tests.testrecorder import TestRecorder


class CustomUndoStack(QUndoStack):
    def __init__(self, test_recorder=None):
        assert isinstance(test_recorder, TestRecorder) or test_recorder is None

        super().__init__()
        self.test_recorder = test_recorder
    # end def

    def undo(self):
        print('undoing')
        self.test_recorder.undoEvent()
        return super().undo()

    def redo(self):
        print('redoing')
        self.test_recorder.redoEvent()
        return super().redo()

    def push(self, QUndoCommand):
        print('pushed')
        return super().push(QUndoCommand)

    def createRedoAction(self, QObject, prefix=''):
        print('created')
        return super().createRedoAction(QObject, prefix)

    def createUndoAction(self, QObject, prefix=''):
        print('created2')
        return super().createUndoAction(QObject, prefix)

    def index(self):
        print('index')
        return super().index()

    def indexChanged(self, p_int):
        print('changed')
        return super().indexChanged(p_int)

    def beginMacro(self, p_str):
        print('begin')
        return super().beginMacro(p_str)

    def endMacro(self):
        print('end')
        return super().endMacro()
