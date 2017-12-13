<<<<<<< HEAD:cadnano/views/outlinerview/nucleicacidpartitem.py
from PyQt5.QtCore import QItemSelectionModel
from cadnano.proxies.cnenum import ItemType
from cadnano.views import styles
from .cnoutlineritem import CNOutlinerItem
from cadnano.views.abstractitems.abstractpartitem import AbstractPartItem
from cadnano.controllers.nucleicacidpartitemcontroller import NucleicAcidPartItemController
from .oligoitem import OutlineOligoItem
from .virtualhelixitem import OutlineVirtualHelixItem


class OutlineNucleicAcidPartItem(CNOutlinerItem, AbstractPartItem):
    FILTER_NAME = "part"

    def __init__(self, model_part, parent):
        super(OutlineNucleicAcidPartItem, self).__init__(model_part, parent)
        self._controller = NucleicAcidPartItemController(self, model_part)
        self._model_part = model_part
        self.setExpanded(True)
        # properties
        temp_color = model_part.getColor()
        # outlinerview takes responsibility of overriding default part color
        if temp_color == "#000000":
            index = len(model_part.document().children()) - 1
            new_color = styles.PARTCOLORS[index % len(styles.PARTCOLORS)]
            model_part.setProperty('color', new_color)

        # item groups
        self._root_items = {}
        self._root_items['VHelixList'] = self.createRootPartItem('Virtual Helices', self)
        self._root_items['OligoList'] = self.createRootPartItem('Oligos', self)
        # self._root_items['Modifications'] = self._createRootItem('Modifications', self)
        if model_part.is_active:
            print("should be active")
            self.activate()
=======
from cadnano.cnenum import ItemType
from cadnano.gui.controllers.itemcontrollers.nucleicacidpartitemcontroller import NucleicAcidPartItemController
from cadnano.gui.views.abstractitems.abstractpartitem import AbstractPartItem
#from cadnano.gui.views.abstractitems.abstractpartitem import QAbstractPartItem


#class ConsoleNucleicAcidPartItem(QAbstractPartItem):
class ConsoleNucleicAcidPartItem(AbstractPartItem):
    FILTER_NAME = 'part'

    def __init__(self, model_part, viewroot, parent):
        super(ConsoleNucleicAcidPartItem, self).__init__()
#        super(ConsoleNucleicAcidPartItem, self).__init__(model_part, viewroot, parent)
        self._controller = NucleicAcidPartItemController(self, model_part)
        self._model_part = model_part
        self._parent = parent

        self._virtual_helix_item_hash = dict()
>>>>>>> 2.5.0:  Add console support for napartitem:cadnano/gui/views/consoleview/nucleicacidpartitem.py
    # end def

    ### PRIVATE SUPPORT METHODS ###
    def __repr__(self):
<<<<<<< HEAD:cadnano/views/outlinerview/nucleicacidpartitem.py
        return "OutlineNucleicAcidPartItem %s" % self._cn_model.getProperty('name')
=======
        try:
            return 'ConsoleNucleicAcidPartItem %s' % self._model_part.getProperty('name')
        except AttributeError:
            return 'ConsoleNucleicAcidPartItem'
>>>>>>> 2.5.0:  Add console support for napartitem:cadnano/gui/views/consoleview/nucleicacidpartitem.py

    ### PUBLIC SUPPORT METHODS ###
    def log(self, message):
        self._parent.log(message)

    def part(self):
        return self._model_part
    # end def

    def itemType(self):
        return ItemType.NUCLEICACID
    # end def

    def isModelSelected(self, document):
        '''Make sure the item is selected in the model
        TODO implement Part selection

        Args:
            document (Document): reference the the model :class:`Document`
        '''
        return False
    # end def

    ### SLOTS ###
    def partRemovedSlot(self, sender):
        self.log('Part removed')
        self._controller.disconnectSignals()
        self._model_part = None
        self._controller = None
    # end def

    def partOligoAddedSlot(self, model_part, model_oligo):
<<<<<<< HEAD:cadnano/views/outlinerview/nucleicacidpartitem.py
        m_o = model_oligo
        m_o.oligoRemovedSignal.connect(self.partOligoRemovedSlot)
        o_i = OutlineOligoItem(m_o, self._root_items['OligoList'])
        self._oligo_item_hash[m_o] = o_i
=======
        model_oligo.oligoRemovedSignal.connect(self.partOligoRemovedSlot)
        self.log('Added oligo %s' % model_oligo)
#        m_o = model_oligo
#        o_i = ConsoleOligoItem(m_o, self._root_items['OligoList'])
#        self._oligo_item_hash[m_o] = o_i
>>>>>>> 2.5.0:  Add console support for napartitem:cadnano/gui/views/consoleview/nucleicacidpartitem.py
    # end def

    def partOligoRemovedSlot(self, model_part, model_oligo):
        self.log('Removed oligo %s' % model_oligo)
#        m_o = model_oligo
#        o_i = self._oligo_item_hash[m_o]
#        o_i.parent().removeChild(o_i)
#        del self._oligo_item_hash[m_o]
    # end def

    def partVirtualHelixAddedSlot(self, model_part, id_num, virtual_helix, neighbors):
<<<<<<< HEAD:cadnano/views/outlinerview/nucleicacidpartitem.py
        tw = self.treeWidget()
        tw.is_child_adding += 1
        vh_i = OutlineVirtualHelixItem(virtual_helix, self._root_items['VHelixList'])
        self._virtual_helix_item_hash[id_num] = vh_i
        tw.is_child_adding -= 1

    def partVirtualHelixRemovingSlot(self, model_part, id_num, virtual_helix, neigbors):
        vh_i = self._virtual_helix_item_hash.get(id_num)
        # in case a OutlineVirtualHelixItem Object is cleaned up before this happends
        if vh_i is not None:
=======
        self._virtual_helix_item_hash[id_num] = virtual_helix
        self.log('%s added' % virtual_helix)

    def partVirtualHelixRemovingSlot(self, model_part, id_num, virtual_helix, neigbors):
        self.log('%s removed' % virtual_helix)

        if self._virtual_helix_item_hash.get(id_num) is not None:
>>>>>>> 2.5.0:  Add console support for napartitem:cadnano/gui/views/consoleview/nucleicacidpartitem.py
            del self._virtual_helix_item_hash[id_num]
    # end def

    def partPropertyChangedSlot(self, model_part, property_key, new_value):
<<<<<<< HEAD:cadnano/views/outlinerview/nucleicacidpartitem.py
        if self._cn_model == model_part:
            self.setValue(property_key, new_value)
            if property_key == 'virtual_helix_order':
                vhi_dict = self._virtual_helix_item_hash
                self.treeWidget().document()
                new_list = [vhi_dict[id_num] for id_num in new_value]
                # 0. record what was selected
                selected_list = [(x, x.isSelected()) for x in new_list]
                root_vhi = self._root_items['VHelixList']
                # 1. move the items
                root_vhi.takeChildren()
                for vhi in new_list:
                    root_vhi.addChild(vhi)
                # 2. now reselect the previously selected.
                # could also query the model
                for vhi, was_selected in selected_list:
                    if was_selected:
                        vhi.setSelected(True)
    # end def

    def partSelectedChangedSlot(self, model_part, is_selected):
        # print("part", is_selected)
        self.setSelected(is_selected)
=======
        if self._model_part == model_part:
            print('partPropertyChanged', model_part, property_key, new_value)
    # end def

    def partSelectedChangedSlot(self, model_part, is_selected):
        self.log('%s is selected' % model_part) if is_selected else self.log('%s is deselected' % model_part)
>>>>>>> 2.5.0:  Add console support for napartitem:cadnano/gui/views/consoleview/nucleicacidpartitem.py
    # end def

    def partVirtualHelixPropertyChangedSlot(self, sender, id_num, virtual_helix, keys, values):
        print(self._model_part)
        print(sender)
        if self._model_part == sender:
            vh_i = self._virtual_helix_item_hash[id_num]
            for key, val in zip(keys, values):
<<<<<<< HEAD:cadnano/views/outlinerview/nucleicacidpartitem.py
                if key in CNOutlinerItem.PROPERTIES:
                    vh_i.setValue(key, val)
    # end def

    def partVirtualHelicesSelectedSlot(self, sender, vh_set, is_adding):
        """ is_adding (bool): adding (True) virtual helices to a selection
        or removing (False)
        """
        vhi_hash = self._virtual_helix_item_hash
        tw = self.treeWidget()
        model = tw.model()
        selection_model = tw.selectionModel()
        top_idx = tw.indexOfTopLevelItem(self)
        top_midx = model.index(top_idx, 0)
        vh_list = self._root_items['VHelixList']
        root_midx = model.index(self.indexOfChild(vh_list), 0, top_midx)
        tw.selection_filter_disabled = True
        if is_adding:
            flag = QItemSelectionModel.Select
            for id_num in vh_set:
                vhi = vhi_hash.get(id_num)
                # selecting a selected item will deselect it, so check
                idx = vh_list.indexOfChild(vhi)
                qmodel_idx = model.index(idx, 0, root_midx)
                if not vhi.isSelected() and not selection_model.isSelected(qmodel_idx):
                    # print("++++++slot Sselect outlinerview", vh_set)
                    selection_model.select(qmodel_idx, flag)
        else:
            flag = QItemSelectionModel.Deselect
            for id_num in vh_set:
                vhi = vhi_hash.get(id_num)
                # deselecting a deselected item will select it, so check
                idx = vh_list.indexOfChild(vhi)
                qmodel_idx = model.index(idx, 0, root_midx)
                if vhi.isSelected() and selection_model.isSelected(qmodel_idx):
                    # print("-----slot deselect outlinerview", vh_set)
                    selection_model.select(qmodel_idx, flag)
        tw.selection_filter_disabled = False
=======
                self.log('%s:  Changing %s to %s' % (vh_i, key, val))
#                if key in CNConsoleItem.PROPERTIES:
#                    vh_i.setValue(key, val)
    # end def

    def partVirtualHelicesSelectedSlot(self, sender, vh_set, is_adding):
        self.log('Selected %s' % str(vh_set) if is_adding else 'Deselected %s' % str(vh_set))
>>>>>>> 2.5.0:  Add console support for napartitem:cadnano/gui/views/consoleview/nucleicacidpartitem.py
    # end def

    def partActiveVirtualHelixChangedSlot(self, part, id_num):
        vhi = self._virtual_helix_item_hash.get(id_num)
#        self.setActiveVirtualHelixItem(vhi)
    # end def

    def partActiveChangedSlot(self, part, is_active):
<<<<<<< HEAD:cadnano/views/outlinerview/nucleicacidpartitem.py
        if part == self._cn_model:
            self.activate() if is_active else self.deactivate()
=======
        pass
        # if part == self._model_part:
        #     self.activate() if is_active else self.deactivate()
>>>>>>> 2.5.0:  Add console support for napartitem:cadnano/gui/views/consoleview/nucleicacidpartitem.py
    # end def

    def setActiveVirtualHelixItem(self, new_active_vhi):
        current_vhi = self.active_virtual_helix_item
        if new_active_vhi != current_vhi:
            if current_vhi is not None:
                current_vhi.deactivate()
            if new_active_vhi is not None:
                new_active_vhi.activate()
            self.active_virtual_helix_item = new_active_vhi
    # end def
# end class
