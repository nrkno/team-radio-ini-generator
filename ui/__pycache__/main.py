import configparser
import sys
from PyQt6.QtWidgets import QApplication
from mvp.model import Model
from mvp.view import View
from mvp.presenter import Presenter

def main():
    app = QApplication(sys.argv)

    config = configparser.ConfigParser()
    config['DEFAULT'] = {'ServerAliveInterval': '45',
                        'Compression': 'yes',
                        'CompressionLevel': '9'}
    config['forge.example'] = {}
    config['forge.example']['User'] = 'hg'
    config['topsecret.server.example'] = {}
    topsecret = config['topsecret.server.example']
    topsecret['Port'] = '50022'     # mutates the parser
    topsecret['ForwardX11'] = 'no'  # same here
    config['DEFAULT']['ForwardX11'] = 'yes'
    # with open('example.ini', 'w') as configfile:
    #    config.write(configfile)    



    model = Model()
    view = View()
    _ = Presenter(model, view)  # This implicitly ties model and view together
    
    view.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()