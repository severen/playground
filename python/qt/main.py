import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

if __name__ == "__main__":
    QGuiApplication.setApplicationDisplayName("Test")
    QGuiApplication.setOrganizationName("severen")
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load("main.qml")

    if not engine.rootObjects():
        sys.exit(1)

    app.exec_()
