# -*- coding: utf-8 -*-

from cadnano import undocommand, undostack


class ProxyObject(object):
    __slots__ = '_parent', '_signals'

    def __init__(self, parent):
        self._parent = parent
        self._signals = {}
    # end def

    def parent(self):
        return self._parent
    # end def

    def setParent(self, parent):
        self._parent = parent
    # end def

    def connect(self, sender, bsignal, method):
        def f(x, y): return method(x, *y)
        bsignal.connect(method, sender=sender)
        self._signals[(sender, bsignal, method)] = f

    def disconnect(self, sender, bsignal, method):
        f = self._signals[(sender, bsignal, method)]
        bsignal.disconnect(f, sender=sender)
        del self._signals[(sender, bsignal, method)]

    def signals(self):
        return self._signals
    # end def

    def deleteLater(self):
        pass
    # end def
# end class


class DummySignal(object):
    def __init__(self, *args, **kwargs):
        name = kwargs.get('name')
        if name is None:
            raise ValueError("missing name")
        self.targets = []
        self.argtypes = args
        self.name = name

    def connect(self, target):
#        print('cn proxy target is', target)
        self.targets.append(target)
#        if target not in self.targets:
#            self.targets.append(target)
#        else:
#            index = self.targets.index(target)
#            self.targets[index] = target

    def disconnect(self, target):
        while target in self.targets:
            self.targets.remove(target)

    def emit(self, *args):
        for t in self.targets:
            t(*args)
# end class


ProxySignal = DummySignal
BaseObject = ProxyObject
UndoCommand = undocommand.UndoCommand
UndoStack = undostack.UndoStack


class TempApp(object):
    documentWasCreatedSignal = ProxySignal(name='documentWasCreatedSignal')
    is_temp_app = True


tapp = TempApp()
