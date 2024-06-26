import sys
from PyQt6.QtWidgets import QApplication
from mvp.model import Model
from mvp.view import View
from mvp.presenter import Presenter

def main():
    app = QApplication(sys.argv)

    model = Model()
    view = View()
    _ = Presenter(model, view)
    
    view.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
