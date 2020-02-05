import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Window 2.12

ApplicationWindow {
  id: window
  visible: true
  title: "Hello!"

  MenuBar {
    Menu {
      title: qsTr("&File")

      MenuItem {
        text: qsTr("&Open")
      }
    }
  }

  Text {
    anchors.centerIn: parent
    text: "Hello world!"
  }
}
