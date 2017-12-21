from PyQt5.QtCore import QEvent, Qt


class TestRecorder():
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        _id = str(id(self))[-4:]
        _name = self.__class__.__name__
        return '%s_%s_%s' % (_name, -1, _id)

    def sliceSceneEvent(self, event, sender):
        # TODO:  Handle scrolling/zooming
        if event.type() == QEvent.GraphicsSceneHoverMove:
            coordiantes = self._getScenePosCoordinates(event)
        elif event.type() == QEvent.GraphicsSceneMousePress:
            coordiantes = self._getScenePosCoordinates(event)
        elif event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Shift:
                pass
            elif event.key() == Qt.Key_Escape:
                pass
            else:
                print('Received unhandled keyrelease %s' % event.key())
        elif event.type() == QEvent.KeyRelease:
            if event.key() == Qt.Key_Shift:
                pass
            elif event.key() == Qt.Key_Escape:
                pass
            else:
                print('Received unhandled keypress %s' % event.key())
        else:
            print('Received unhandled event type %s' % event.type())

    def gridSceneEvent(self, event, sender):
        print('Received a grid scene event')

    def pathSceneEvent(self, event, sender):
        print('Received a path scene event')

    def simSceneEvent(self, event, sender):
        print('Received a sim scene event')

    def consoleSceneEvent(self, event, sender):
        print('Received a console scene event')

    def undoEvent(self):
        print('Received an undo event')

    def redoEvent(self):
        print('Received a redo event')

    def _getScenePosCoordinates(self, event):
        return event.scenePos().x(), event.scenePos().y()
