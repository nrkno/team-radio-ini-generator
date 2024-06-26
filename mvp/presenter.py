import os
from configparser import ConfigParser
from typing import Dict

from mvp.model import Model
from mvp.view import View

class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.view.input_data_collected.connect(self.handle_input_data)

    def handle_input_data(self, data_dict: Dict[str, str]) -> None:
        self.model.set_input_data(data_dict)
        self.write_data()
        
    def write_data(self) -> None:
        data = self.model.get_input_data()
        print(data)
        
        folder_path = data.get('iniFolderPath') or './'
        print(folder_path)

        dbAliasConfig = ConfigParser()
        dbAliasConfig.optionxform = str
        dbAliasConfig['SystuaSnapsLocal'] = {
            'Server': data.get('dbAlias/SystuaSnapsLocal_Server'),
            'Database': data.get('dbAlias/SystuaSnapsLocal_Database')
        }
        dbAliasConfig['SystuaSnapsMA'] = {
            'Server': data.get('dbAlias/SystuaSnapsMA_Server'),
            'Database': data.get('dbAlias/SystuaSnapsMA_Database')
        }

        self.write_ini_file(dbAliasConfig, 'dbAlias.ini', folder_path)

        VSMStudio_PanelsConfig = ConfigParser()
        VSMStudio_PanelsConfig.optionxform = str
        VSMStudio_PanelsConfig['General'] = {
            'Labels': data.get('VSMStudio_Panels/Labels'),
            'OnAir': data.get('VSMStudio_Panels/OnAir'),
            'Router': data.get('VSMStudio_Panels/Router'),
            'Prod': data.get('VSMStudio_Panels/Prod'),
            'Tekniker': data.get('VSMStudio_Panels/Tekniker'),
            'K.Labels': data.get('VSMStudio_Panels/KLabels')
        }

        self.write_ini_file(VSMStudio_PanelsConfig, 'VSMStudio_Panels.ini', folder_path)

        EmberhostsConfig = ConfigParser()
        EmberhostsConfig.optionxform = str
        EmberhostsConfig['General'] = {
            'MyPowercore': data.get('Emberhosts/MyPowercore'),
        }

        self.write_ini_file(EmberhostsConfig, 'Emberhosts.ini', folder_path)

        NRKSettingsConfig = ConfigParser()
        NRKSettingsConfig.optionxform = str
        details = {}
        for i in range(1, 33):
            details[f'gpio\\Boolean-{i}'] = 'False'

        for i in range(1, 21):
            details[f'gpio\\Integer-{i}'] = 0
        
        for i in range(1, 34):
            details[f'gpio\\Real-{i}'] = 0

        details[f'gpio\\String-1'] = 'NRKSettings_Default.ini'
        details[f'gpio\\String-2'] = 'Version 0.9'
        details[f'gpio\\String-3'] = data.get('NRKSettings/VSM')
        details[f'gpio\\String-4'] = data.get('NRKSettings/type')
        details[f'gpio\\String-5'] = data.get('NRKSettings/studios')
        details[f'gpio\\String-6'] = data.get('NRKSettings/TB')
        details[f'gpio\\String-7'] = data.get('NRKSettings/String-7')#'4W1' # Fetch from dict the correct value
        details[f'gpio\\String-8'] = data.get('NRKSettings/String-8')#'4W2' # Fetch from dict the correct value
        details[f'gpio\\String-9'] = data.get('NRKSettings/String-9') #'4W3' # Fetch from dict the correct value
        details[f'gpio\\String-10'] = data.get('NRKSettings/String-10') #'4W4' # Fetch from dict the correct value
        details[f'gpio\\String-11'] = 'Prod'
        details[f'gpio\\String-12'] = 'AntTel:' + data.get('NRKSettings/AntTel')
        details[f'gpio\\String-13'] = ''
        details[f'gpio\\String-14'] = ''
        details[f'gpio\\String-15'] = 'Turboplayer'
        details[f'gpio\\String-16'] = data.get('NRKSettings/TurboPlayerDNS')
        details[f'gpio\\String-17'] = 'Autocam'
        details[f'gpio\\String-18'] = data.get('NRKSettings/AutocamDNS')
        details[f'gpio\\String-19'] = 'Overskrift 3'
        details[f'gpio\\String-20'] = data.get('NRKSettings/Overskrift_3')
        details[f'gpio\\String-21'] = 'Overskrift 4'
        details[f'gpio\\String-22'] = data.get('NRKSettings/Overskrift_4')
        details[f'gpio\\String-23'] = 'Overskrift 5'
        details[f'gpio\\String-24'] = data.get('NRKSettings/Overskrift_5')
        details[f'gpio\\String-25'] = 'Chromium'
        details[f'gpio\\String-26'] = ''
        details[f'gpio\\String-27'] = 'HD1_html'
        details[f'gpio\\String-28'] = data.get('NRKSettings/HD1_html')
        details[f'gpio\\String-29'] = 'HD2_html'
        details[f'gpio\\String-30'] = data.get('NRKSettings/HD2_html')
        details[f'gpio\\String-31'] = 'HD3_html'
        details[f'gpio\\String-32'] = data.get('NRKSettings/HD3_html')
        details[f'gpio\\String-33'] = ''
        details[f'gpio\\String-34'] = data.get('NRKSettings/Tel')
        details[f'gpio\\String-35'] = data.get('NRKSettings/RM')
        details[f'gpio\\String-36'] = data.get('NRKSettings/PF')
        details[f'gpio\\String-38'] = data.get('NRKSettings/MM')
        details[f'gpio\\String-39'] = ''
        details[f'gpio\\String-40'] = data.get('NRKSettings/HPVol')

        for i in range(21, 33):
            details[f'gpio\\Integer-{i}'] = 0
        
        for i in range(34, 41):
            details[f'gpio\\Boolean-{i}'] = 'False'
        
        for i in range(34, 41):
            details[f'gpio\\Integer-{i}'] = 0

        for i in range(35, 41):
            details[f'gpio\\Real-{i}'] = 0

        NRKSettingsConfig['Project'] = details
        
        self.write_ini_file(NRKSettingsConfig, 'NRKSettings.ini', folder_path)

    def write_ini_file(self, config: ConfigParser, fileName: str , folder_path: str):
        with open(folder_path + '/' + fileName, 'w') as configfile:
            config.write(configfile)
