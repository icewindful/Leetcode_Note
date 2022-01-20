
pytest = False
avoid01 = True
avoid02 = False
avoid03 = False


if pytest :
    import sys
    from PyQt5 import QtWidgets
    from Ui_test01 import  Ui_MainWindow

if avoid01:
    class MainWindow(QtWidgets.QMainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent=parent)
            ui = Ui_MainWindow()
            ui.setupUi(self)

    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        w = MainWindow()
        w.show()
        sys.exit(app.exec_())

if avoid02:
    class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent=parent)
            self.setupUi(self)

    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        w = MainWindow()
        w.show()
        sys.exit(app.exec_())

if avoid03:
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        ex = Ui_MainWindow()
        w = QtWidgets.QMainWindow()
        ex.setupUi(w)
        w.show()
        sys.exit(app.exec_())


