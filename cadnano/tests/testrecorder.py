from PyQt5.QtCore import QEvent, QPoint, Qt


SLICE_VIEW = 'document_window.slice_graphics_view'

class TestRecorder():
    def __init__(self):
        self.corpus = []

    def __repr__(self):
        pass

    def __str__(self):
        _id = str(id(self))[-4:]
        _name = self.__class__.__name__
        return '%s_%s_%s' % (_name, -1, _id)

    # Events
    def sliceSceneEvent(self, event, sender):
        # TODO:  Handle scrolling/zooming
        if event.type() == QEvent.GraphicsSceneHoverMove:
            point = QPoint(*self._getScenePosCoordinates(event))
        elif event.type() == QEvent.GraphicsSceneMousePress:
            point = QPoint(*self._getScenePosCoordinates(event))
            self.cgenMouseClick(SLICE_VIEW, point)
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
            pass
#            print('Received unhandled event type %s' % event.type())

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

    def newHoneycombEvent(self):
        print('Received a new honeycomb event')

    def newSquareEvent(self):
        print('Received a new square event')

    def switchSelectTool(self):
        print('Switching to select tool')

    def switchCreateTool(self):
        print('Switching to create tool')

    def switchBreakTool(self):
        print('Switching to break tool')

    def switchPaintTool(self):
        print('Switching to paint tool')

    def switchInsertTool(self):
        print('Switching to insert tool')

    def switchSkipTool(self):
        print('Switching to skip tool')

    def switchSeqTool(self):
        print('Switching to seq tool')

    def actionExportStaples(self):
        print('Exporting staples')

    def actionSVG(self):
        print('Creating a SVG')

    def actionFilterHelix(self):
        print('Helix filter triggered')

    def actionFilterEndpoint(self):
        print('Endpoint filter triggered')

    def actionFilterXover(self):
        print('Xover filter triggered')

    def actionFilterScaf(self):
        print('Scaf filter triggered')

    def actionFilterStap(self):
        print('Stap filter triggered')

    def actionFilterFwd(self):
        print('Fwd filter triggered')

    def actionFilterRev(self):
        print('Rev filter triggered')

    # Event Helpers
    def _getScenePosCoordinates(self, event):
        return event.pos().x(), event.pos().y()

    # Code generation
    def cgenMouseClick(self, view, button=None, pos=None, delay=None):
        click_button = button if button else Qt.LeftButton
        delay = delay if delay else 100
        command = 'app.graphicsItemClick(%s, %s, pos=%s, delay=%s)' % (view, click_button, pos, delay)
        self.corpus.append(command)

    def cgenMouseMove(self):
        raise NotImplementedError
