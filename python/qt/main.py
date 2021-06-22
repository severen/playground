import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from __feature__ import snake_case, true_property


if __name__ == "__main__":
    QGuiApplication.application_display_name = "Example"
    QGuiApplication.organization_name = "severen"

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load("main.qml")

    if not engine.root_objects():
        sys.exit(1)

    app.exec()
