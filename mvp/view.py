from PyQt6.QtWidgets import QDialog, QFileDialog
from PyQt6.QtCore import pyqtSignal
from typing import Dict

from ui.mainwindow_ui import Ui_Dialog

class View(QDialog, Ui_Dialog):
    input_data_collected = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(View, self).__init__(parent)
        self.setupUi(self)
        self.generateButton.clicked.connect(self.on_generate_clicked)
        self.folderButton.clicked.connect(self.open_folder_dialog)

    # Øystein Hvor kommer K1 i folderpathen fra?
    def on_generate_clicked(self) -> None:
        data_dict: Dict[str, str] = {
            'iniFolderPath': self.iniFolderPath.toPlainText(), # Øystein K1 folderpathen fra bruker eller lese config?
     
            'Emberhosts/MyPowercore': self.emberhostsMyPowercore.text() + " 9000",
     
            'dbAlias/SystuaSnapsLocal_Server': self.dbAliasLocalServer.text(),
            'dbAlias/SystuaSnapsLocal_Database': self.dbAliasLocalDatabase.text(),
            'dbAlias/SystuaSnapsMA_Server': self.dbAliasMAServer.text(),
            'dbAlias/SystuaSnapsMA_Database': self.dbAliasMADatabase.text(),

            'VSMStudio_Hosts/VSM': self.VSMStudio_HostsVSM.text() + ' 8000', # Is : missing heres in the word document?

            'VSMStudio_Panels/Labels': self.prependAndAppendVSMDetails(self.VSMStudio_PanelsLabels.text()),
            'VSMStudio_Panels/OnAir': self.prependAndAppendVSMDetails(self.VSMStudio_PanelsOnAir.text()),
            'VSMStudio_Panels/Router': self.prependAndAppendVSMDetails(self.VSMStudio_PanelsRouter.text()),
            'VSMStudio_Panels/Prod': self.prependAndAppendVSMDetails(self.VSMStudio_PanelsProd.text()),
            'VSMStudio_Panels/Tekniker': self.prependAndAppendVSMDetails(self.VSMStudio_PanelsTekniker.text()),
            'VSMStudio_Panels/KLabels': self.prependAndAppendVSMDetails(self.VSMStudio_PanelsKLabels.text()),

            'NRKSettings/VSM': 'VSM' if self.NRKSettings_VSM.isChecked() else 'Not_VSM',
            'NRKSettings/type': self.NRKSettings_type.currentText(),
            'NRKSettings/studios': self.NRKSettings_studios.currentText(),
            'NRKSettings/AntTel': self.NRKSettings_antTel.currentText(),
            'NRKSettings/TB': 'TB:VSM' if self.NRKSettings_TB.isChecked() else 'TB:Not_VSM',
            'NRKSettings/String-7': self.NRKSettings_String_7.text(), # Øystein
            'NRKSettings/String-8': self.NRKSettings_String_8.text(), # Øystein
            'NRKSettings/String-9': self.NRKSettings_String_9.text(), # Øystein
            'NRKSettings/String-10': self.NRKSettings_String_10.text(), # Øystein
            'NRKSettings/TurboPlayerDNS': self.setTurboPlayerDnsByType(),
            'NRKSettings/AutocamDNS': self.NRKSettings_AutocamDNS.text() + ':8000',
            'NRKSettings/Overskrift_3': self.NRKSettings_Overskrift_3.text(), # Øystein
            'NRKSettings/Overskrift_4': self.NRKSettings_Overskrift_4.text(), # Øystein
            'NRKSettings/Overskrift_5': self.NRKSettings_Overskrift_5.text(), # Øystein
            'NRKSettings/HD1_html': self.NRKSettings_HD1.text(),
            'NRKSettings/HD2_html': self.NRKSettings_HD2.text(),
            'NRKSettings/HD3_html': self.NRKSettings_HD3.text(),
            'NRKSettings/Tel': 'Tel:Enable' if self.NRKSettings_Tel.isChecked() else 'Tel:Disable',
            'NRKSettings/RM': 'RM:Enable' if self.NRKSettings_RM.isChecked() else 'RM:Disable',
            'NRKSettings/PF': 'PF:Enable' if self.NRKSettings_PF.isChecked() else 'PF:Disable',
            'NRKSettings/MM': 'MM:Enable' if self.NRKSettings_MM.isChecked() else 'MM:Disable',
            'NRKSettings/HPVol': 'HPVol:Enable' if self.NRKSettings_HPVol.isChecked() else 'HPVol:Disable',
        }
        self.input_data_collected.emit(data_dict)

    def setTurboPlayerDnsByType(self):
        value = self.NRKSettings_TurboPlayerIP.text() + ':8090/turbo/html/index.html#/index/'

        # if type = selvkjor then add 2 at the end of TurboPlayerDNS
        # if type = Produsent then add 7 at the end of TurboPlayerDNS
        # if type = Ute then add 3 at the end of TurboPlayerDNS
        # Is it to add 9 to the end if Tekniker?
        if (self.NRKSettings_type.currentText() == 'selvkjor'):
            value += '2'
        if (self.NRKSettings_type.currentText() == 'Produsent'):
            value += '7'
        if (self.NRKSettings_type.currentText() == 'Ute'):
            value += '3'
        return value + '/'
    
    def prependAndAppendVSMDetails(self, panel):
        return 'VSM ' + panel + ' 200'
    
    def open_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.iniFolderPath.setText(folder_path)
