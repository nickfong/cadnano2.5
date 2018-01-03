from PyQt5.QtCore import Qt
import pytest

from cnguitestcase import GUITestApp


@pytest.fixture()
def cnapp():
    app = GUITestApp()
    yield app
    app.tearDown()

def testTestRecorderUnderstanding(cnapp):
    document = cnapp.document
    document_controller = document.controller()


    if document_controller:
        document_window = document_controller.win

        from PyQt5.QtTest import QTest
        from PyQt5.QtCore import QPoint
        pos = QPoint(177, 103)
#        pos = QPoint(0, 0)

        cnapp.graphicsItemClick(document_window.slice_graphics_view, Qt.LeftButton, pos=pos, delay=100)

        print(document_window.slice_graphics_view)
        QTest.mouseClick(document_window.slice_graphics_view, Qt.LeftButton, pos=pos, delay=100)

        part = document.activePart()
        assert len(part._virtual_helices_set) > 0
