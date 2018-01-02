from PyQt5 import Qt
import pytest

from cntestcase import CNTestApp


@pytest.fixture()
def cnapp():
    app = CNTestApp()
    yield app
    app.tearDown()

def testTestRecorderUnderstanding(cnapp):
    doc = cnapp.document
    document_controller = doc.controller()

#    part = doc.activePart()

    if document_controller:
        document_window = document_controller.win

        from PyQt5.QtTest import QTest
        from PyQt5.QtCore import QPoint
        pos = QPoint(177, 103)
#        pos = QPoint(0, 0)
        QTest.mouseClick(document_window.slice_graphics_view, Qt.LeftButton, pos=pos, delay=100)
