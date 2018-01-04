import time

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
import pytest

from cnguitestcase import GUITestApp


@pytest.fixture()
def app():
    app = GUITestApp()
    yield app
    app.tearDown()

def testTestRecorderUnderstanding(app):
    document = app.document
    document_controller = document.controller()
    toolbar = app.window.main_toolbar
    action_select_tool = toolbar.widgetForAction(app.window.action_global_select)
    action_create_tool = toolbar.widgetForAction(app.window.action_global_create)
    action_break_tool = toolbar.widgetForAction(app.window.action_path_break)
    action_paint_tool = toolbar.widgetForAction(app.window.action_path_paint)
    action_insertion_tool = toolbar.widgetForAction(app.window.action_path_insertion)
    action_skip_tool = toolbar.widgetForAction(app.window.action_path_skip)
    action_add_seq_tool = toolbar.widgetForAction(app.window.action_path_add_seq)

    action_new_honeycomb = toolbar.widgetForAction(app.window.action_new_dnapart_honeycomb)
    action_new_square = toolbar.widgetForAction(app.window.action_new_dnapart_square)

    action_export = toolbar.widgetForAction(app.window.action_export_staples)
    action_SVG = toolbar.widgetForAction(app.window.action_SVG)

    action_filter_helix = toolbar.widgetForAction(app.window.action_filter_helix)
    action_filter_endpoint = toolbar.widgetForAction(app.window.action_filter_endpoint)
    action_filter_xover = toolbar.widgetForAction(app.window.action_filter_xover)

    action_filter_scaf = toolbar.widgetForAction(app.window.action_filter_scaf)
    action_filter_stap = toolbar.widgetForAction(app.window.action_filter_stap)
    action_filter_fwd = toolbar.widgetForAction(app.window.action_filter_fwd)
    action_filter_rev = toolbar.widgetForAction(app.window.action_filter_rev)

    print('toolbar is %s' % toolbar)
    print('nhb is %s' % action_new_honeycomb)


    time.sleep(2)
    from PyQt5.QtTest import QTest
    print('About to click create')
    QTest.mouseClick(action_break_tool, Qt.LeftButton, delay=100)
    app.processEvents()
    time.sleep(2)
#    print('About to click xover')
#    QTest.mouseClick(action_filter_xover, Qt.LeftButton, delay=100)
#    app.processEvents()
#    time.sleep(2)
    print('About to click new part button')
    QTest.mouseClick(action_new_honeycomb, Qt.LeftButton, delay=100)
    app.processEvents()
    time.sleep(2)
    print('Clicked new part button')

    document_window = document_controller.win

    from PyQt5.QtTest import QTest
    from PyQt5.QtCore import QPoint
#        pos = QPoint(0, 0)

#    print(document_window.slice_graphics_view)

    time.sleep(2)

    print('About to click first time')
    pos = QPoint(11, 18)
    app.graphicsItemClick(document_window.slice_graphics_view, Qt.LeftButton, pos=pos, delay=100)

    print('About to click second time')
    pos = QPoint(0, 0)
    app.graphicsItemClick(document_window.slice_graphics_view, Qt.LeftButton, pos=pos, delay=100)

    print('About to click third time')
    pos = QPoint(177, 103)
    app.graphicsItemClick(document_window.slice_graphics_view, Qt.LeftButton, pos=pos, delay=100)

    print('About to click fourth time')
    pos = QPoint(177, 110)
    app.graphicsItemClick(document_window.slice_graphics_view, Qt.LeftButton, pos=pos, delay=100)

    print('About to click fifth time')
    pos = QPoint(170, 103)
    app.graphicsItemClick(document_window.slice_graphics_view, Qt.LeftButton, pos=pos, delay=100)

    app.processEvents()

    time.sleep(2)

#        part = document.activePart()
#        assert len(part._virtual_helices_set) > 0
