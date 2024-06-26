from PyQt6 import QtWidgets, QtCore

class Ui_Dialog(object):
    def setupUi(self, Dialog: QtWidgets.QDialog):
        Dialog.setObjectName("Dialog")

        self.main_layout = QtWidgets.QHBoxLayout(Dialog)
        self.section1_layout = QtWidgets.QVBoxLayout()
        self.section2_layout = QtWidgets.QVBoxLayout()
        self.section3_layout = QtWidgets.QVBoxLayout()

        emberGroup = self.add_EmberHosts_Fields()
        self.section1_layout.addWidget(emberGroup)

        dbAliasGroup = self.add_DbAlias_Fields()
        self.section1_layout.addWidget(dbAliasGroup)

        VSMStudioHostsGroup = self.add_VSMStudio_HostsFields()
        self.section1_layout.addWidget(VSMStudioHostsGroup)

        VSMStudioPanelsGroup = self.add_VSMStudio_Panels_Fields()
        self.section1_layout.addWidget(VSMStudioPanelsGroup)

        NRKSettingsGroup = self.add_NRKSettings_Fields()
        self.section2_layout.addWidget(NRKSettingsGroup)
        
        formLayout = QtWidgets.QFormLayout()

        self.iniFolderPath = QtWidgets.QTextEdit()
        self.iniFolderPath.setReadOnly(True)
        
        iniFolderPathLabel = QtWidgets.QLabel("Folder path")
        formLayout.addRow(iniFolderPathLabel, self.iniFolderPath)
        groupBox = QtWidgets.QGroupBox("Tool config")
        groupBox.setLayout(formLayout)
        self.section3_layout.addWidget(groupBox)

        self.folderButton = QtWidgets.QPushButton("Select Folder")
        self.section3_layout.addWidget(self.folderButton)

        self.generateButton = QtWidgets.QPushButton("Generate")
        self.section3_layout.addWidget(self.generateButton)

        self.main_layout.addLayout(self.section1_layout)
        self.main_layout.addLayout(self.section2_layout)
        self.main_layout.addLayout(self.section3_layout)

        Dialog.setLayout(self.main_layout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("NRK Lawo ini generator")

    def add_EmberHosts_Fields(self):
        formLayout = QtWidgets.QFormLayout()

        self.emberhostsMyPowercore = QtWidgets.QLineEdit()
        powerCorelabel = QtWidgets.QLabel("My Powercore IP")
        powerCorelabel.setToolTip("Dette er Ip til maskina som står inne i studioet under bordet.")
        formLayout.addRow(powerCorelabel,self.emberhostsMyPowercore)
        
       # icon = QtGui.QIcon('path_to_icon.png')  # replace 'path_to_icon.png' with the path to your icon

        groupBox = QtWidgets.QGroupBox("Emberhosts.ini")
        groupBox.setLayout(formLayout)
        return groupBox
    
    def add_DbAlias_Fields(self):
        formLayout = QtWidgets.QFormLayout()

        self.dbAliasLocalServer = QtWidgets.QLineEdit()
        dbAliasLocalServerLabel = QtWidgets.QLabel("SystuaSnapsLocal Server")
        formLayout.addRow(dbAliasLocalServerLabel, self.dbAliasLocalServer)

        self.dbAliasLocalDatabase = QtWidgets.QLineEdit()
        dbAliasLocalDatabaseLabel = QtWidgets.QLabel("SystuaSnapsLocal Database")
        formLayout.addRow(dbAliasLocalDatabaseLabel, self.dbAliasLocalDatabase)

        self.dbAliasMAServer = QtWidgets.QLineEdit()
        dbAliasMAServerLabel = QtWidgets.QLabel("SystuaSnapsMA Server")
        formLayout.addRow(dbAliasMAServerLabel, self.dbAliasMAServer)

        self.dbAliasMADatabase = QtWidgets.QLineEdit()
        dbAliasMADatabaseLabel = QtWidgets.QLabel("SystuaSnapsMA Database")
        formLayout.addRow(dbAliasMADatabaseLabel, self.dbAliasMADatabase)

        groupBox = QtWidgets.QGroupBox("dbAlias.ini")
        groupBox.setLayout(formLayout)
        return groupBox
    
    def add_VSMStudio_HostsFields(self):
        formLayout = QtWidgets.QFormLayout()

        self.VSMStudio_HostsVSM = QtWidgets.QLineEdit()
        VSMStudio_HostsVSMlabel = QtWidgets.QLabel("VSM IP")
        formLayout.addRow(VSMStudio_HostsVSMlabel, self.VSMStudio_HostsVSM)

        groupBox = QtWidgets.QGroupBox("VSMStudio_Hosts.ini")
        groupBox.setLayout(formLayout)
        return groupBox
    
    def add_VSMStudio_Panels_Fields(self):
        formLayout = QtWidgets.QFormLayout()

        self.VSMStudio_PanelsLabels = QtWidgets.QLineEdit()
        VSMStudio_PanelsLabelslabel = QtWidgets.QLabel("Labels")
        formLayout.addRow(VSMStudio_PanelsLabelslabel, self.VSMStudio_PanelsLabels)

        self.VSMStudio_PanelsOnAir = QtWidgets.QLineEdit()
        VSMStudio_PanelsOnAirlabel = QtWidgets.QLabel("OnAir")
        formLayout.addRow(VSMStudio_PanelsOnAirlabel, self.VSMStudio_PanelsOnAir)

        self.VSMStudio_PanelsRouter = QtWidgets.QLineEdit()
        VSMStudio_PanelsRouterlabel = QtWidgets.QLabel("Router")
        formLayout.addRow(VSMStudio_PanelsRouterlabel, self.VSMStudio_PanelsRouter)

        self.VSMStudio_PanelsProd = QtWidgets.QLineEdit()
        VSMStudio_PanelsProdlabel = QtWidgets.QLabel("Prod")
        formLayout.addRow(VSMStudio_PanelsProdlabel, self.VSMStudio_PanelsProd)

        self.VSMStudio_PanelsTekniker = QtWidgets.QLineEdit()
        VSMStudio_PanelsTeknikerlabel = QtWidgets.QLabel("Tekniker")
        formLayout.addRow(VSMStudio_PanelsTeknikerlabel, self.VSMStudio_PanelsTekniker)

        self.VSMStudio_PanelsKLabels = QtWidgets.QLineEdit()
        VSMStudio_PanelsKLabelslabel = QtWidgets.QLabel("K.Labels")
        formLayout.addRow(VSMStudio_PanelsKLabelslabel, self.VSMStudio_PanelsKLabels)

        groupBox = QtWidgets.QGroupBox("VSMStudio_Panels.ini")
        groupBox.setLayout(formLayout)
        return groupBox
    
    def add_NRKSettings_Fields(self):
        formLayout = QtWidgets.QFormLayout()

        self.NRKSettings_VSM = QtWidgets.QCheckBox()
        NRKSettings_VSM_label = QtWidgets.QLabel("VSM")
        formLayout.addRow(NRKSettings_VSM_label, self.NRKSettings_VSM)
        
        self.NRKSettings_TB = QtWidgets.QCheckBox()
        NRKSettings_TB_label = QtWidgets.QLabel("TB")
        formLayout.addRow(NRKSettings_TB_label, self.NRKSettings_TB)

        self.NRKSettings_type = QtWidgets.QComboBox()
        self.NRKSettings_type.addItems(['Selkjor', 'Produsent', 'Ute', 'Tekniker'])
        NRKSettings_type_label = QtWidgets.QLabel("Type")
        formLayout.addRow(NRKSettings_type_label, self.NRKSettings_type)

        self.NRKSettings_studios = QtWidgets.QComboBox()
        self.NRKSettings_studios.addItems(['Kx', 'MK', 'TV'])
        NRKSettings_studios_label = QtWidgets.QLabel("Studio")
        formLayout.addRow(NRKSettings_studios_label, self.NRKSettings_studios)

        self.NRKSettings_antTel = QtWidgets.QComboBox()
        self.NRKSettings_antTel.addItems(['','1', '2', '3'])
        NRKSettings_antTel_label = QtWidgets.QLabel("Antel")
        formLayout.addRow(NRKSettings_antTel_label, self.NRKSettings_antTel)

        self.NRKSettings_TurboPlayerIP = QtWidgets.QLineEdit()
        NRKSettings_TurboPlayerIP_label = QtWidgets.QLabel("Turboplayer IP")
        formLayout.addRow(NRKSettings_TurboPlayerIP_label, self.NRKSettings_TurboPlayerIP)

        self.NRKSettings_String_7 = QtWidgets.QLineEdit()
        NRKSettings_String_7_label = QtWidgets.QLabel("String 7")
        formLayout.addRow(NRKSettings_String_7_label, self.NRKSettings_String_7)

        self.NRKSettings_String_8 = QtWidgets.QLineEdit()
        NRKSettings_String_8_label = QtWidgets.QLabel("String 8")
        formLayout.addRow(NRKSettings_String_8_label, self.NRKSettings_String_8)

        self.NRKSettings_String_9 = QtWidgets.QLineEdit()
        NRKSettings_String_9_label = QtWidgets.QLabel("String 9")
        formLayout.addRow(NRKSettings_String_9_label, self.NRKSettings_String_9)

        self.NRKSettings_String_10 = QtWidgets.QLineEdit()
        NRKSettings_String_10_label = QtWidgets.QLabel("String 10")
        formLayout.addRow(NRKSettings_String_10_label, self.NRKSettings_String_10)

        self.NRKSettings_AutocamDNS = QtWidgets.QLineEdit()
        NRKSettings_AutocamDNS_label = QtWidgets.QLabel("Autocam DNS")
        formLayout.addRow(NRKSettings_AutocamDNS_label, self.NRKSettings_AutocamDNS)

        self.NRKSettings_Overskrift_3 = QtWidgets.QLineEdit()
        NRKSettings_Overskrift_3_label = QtWidgets.QLabel("Overskrift_3")
        formLayout.addRow(NRKSettings_Overskrift_3_label, self.NRKSettings_Overskrift_3)

        self.NRKSettings_Overskrift_4 = QtWidgets.QLineEdit()
        NRKSettings_Overskrift_4_label = QtWidgets.QLabel("Overskrift_4")
        formLayout.addRow(NRKSettings_Overskrift_4_label, self.NRKSettings_Overskrift_4)

        self.NRKSettings_Overskrift_5 = QtWidgets.QLineEdit()
        NRKSettings_Overskrift_5_label = QtWidgets.QLabel("Overskrift_5")
        formLayout.addRow(NRKSettings_Overskrift_5_label, self.NRKSettings_Overskrift_5)

        self.NRKSettings_HD1 = QtWidgets.QLineEdit()
        NRKSettings_HD1_label = QtWidgets.QLabel("HD1_html")
        formLayout.addRow(NRKSettings_HD1_label, self.NRKSettings_HD1)

        self.NRKSettings_HD2 = QtWidgets.QLineEdit()
        NRKSettings_HD2_label = QtWidgets.QLabel("HD2_html")
        formLayout.addRow(NRKSettings_HD2_label, self.NRKSettings_HD2)

        self.NRKSettings_HD3 = QtWidgets.QLineEdit()
        NRKSettings_HD3_label = QtWidgets.QLabel("HD3_html")
        formLayout.addRow(NRKSettings_HD3_label, self.NRKSettings_HD3)

        self.NRKSettings_Tel = QtWidgets.QCheckBox()
        NRKSettings_Tel_label = QtWidgets.QLabel("Tel")
        formLayout.addRow(NRKSettings_Tel_label, self.NRKSettings_Tel)

        self.NRKSettings_RM = QtWidgets.QCheckBox()
        NRKSettings_RM_label = QtWidgets.QLabel("RM")
        formLayout.addRow(NRKSettings_RM_label, self.NRKSettings_RM)

        self.NRKSettings_PF = QtWidgets.QCheckBox()
        NRKSettings_PF_label = QtWidgets.QLabel("PF")
        formLayout.addRow(NRKSettings_PF_label, self.NRKSettings_PF)

        self.NRKSettings_MM = QtWidgets.QCheckBox()
        NRKSettings_MM_label = QtWidgets.QLabel("MM")
        formLayout.addRow(NRKSettings_MM_label, self.NRKSettings_MM)

        self.NRKSettings_HPVol = QtWidgets.QCheckBox()
        NRKSettings_HPVol_label = QtWidgets.QLabel("HPVol")
        formLayout.addRow(NRKSettings_HPVol_label, self.NRKSettings_HPVol)
        
        groupBox = QtWidgets.QGroupBox("NRKSettings.ini")
        groupBox.setLayout(formLayout)
        return groupBox
    