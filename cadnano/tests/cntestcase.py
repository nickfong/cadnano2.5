# -*- coding: utf-8 -*-
import os
import io
pjoin = os.path.join

import pytest

from pathsetup import TEST_PATH
from cadnano.extras.dnasequences import sequences


@pytest.fixture()
def cnapp():
    app = CNTestApp()
    yield app
    app.tearDown()


class CNTestApp(object):

    def __init__(self):
        # Document import must be here so as to allow for GUI tests to be run
        from cadnano.document import Document
        self.document = Document()
#        assert self.document.controller() is not None
#        from cadnano.controllers.documentcontroller import DocumentController
        """
        Adding this import by itself triggers:
        ❱ pytest cadnano/tests

        ================================================================================== test session starts ==================================================================================
        platform darwin -- Python 3.6.3, pytest-3.3.1, py-1.5.2, pluggy-0.6.0
        PyQt5 5.9.2 -- Qt runtime 5.9.3 -- Qt compiled 5.9.3
        rootdir: cadnano2.5/cadnano/tests, inifile: pytest.ini
        plugins: qt-2.3.0
        collected 13 items

        cadnano/tests/functionaltest.py Abort trap: 6

        This is due to this error, as shown in an interactive Python session:
        >>> from cadnano.document import Document
        >>> doc = Document()
        >>> from cadnano.controllers.documentcontroller import DocumentController
        QPixmap: Must construct a QGuiApplication before a QPixmap
        Abort trap: 6
        """
#        self.document_controller = DocumentController(self.document)
#        self.document_controller.newDocument()

    def tearDown(self):
        pass

    def getTestSequences(self, designname, sequences_to_apply):
        """
        Called by a sequence-verification functional test to read in a file
        (designname), apply scaffold sequence(s) to that design, and return
        the set of staple sequences."""
        # set up the document
        inputfile = pjoin(TEST_PATH,
                          "data", designname)
        document = self.document
        document.readFile(inputfile)

        part = document.activePart()
        # apply one or more sequences to the design
        for sequence_name, start_id_num, start_idx in sequences_to_apply:
            sequence = sequences.get(sequence_name, None)
            for id_num in part.getIdNums():
                fwd_ss, rev_ss = part.getStrandSets(id_num)
                if id_num == start_id_num:
                    strand = fwd_ss.getStrand(start_idx)
                    strand.oligo().applySequence(sequence)
        generated_sequences = part.getSequences()
        return set(generated_sequences.splitlines())
    # end def

    @staticmethod
    def getRefSequences(designname):
        """docstring for getRefSequences"""
        staple_file = pjoin(TEST_PATH,
                            "data", designname)
        with io.open(staple_file, 'r', encoding='utf-8') as f:
            read_sequences = f.read()
        return set(read_sequences.splitlines())

    @staticmethod
    def writeRefSequences(designname, data):
        """docstring for getRefSequences"""
        staple_file = pjoin(TEST_PATH,
                            "data", designname)
        with io.open(staple_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(data))
# end class
