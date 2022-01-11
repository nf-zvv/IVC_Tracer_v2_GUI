import sys
import serial
import csv
import os
import serial.tools.list_ports as port_list
from datetime import datetime

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog, QListWidgetItem

from MainWindowForm import Ui_MainWindow
from UartSettingsDialogForm import Ui_UartSettingsDialog

parities = [serial.PARITY_NONE, serial.PARITY_ODD, serial.PARITY_EVEN, serial.PARITY_MARK, serial.PARITY_SPACE]
stopbits = [serial.STOPBITS_ONE, serial.STOPBITS_ONE_POINT_FIVE, serial.STOPBITS_TWO]
bytesize = [serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS]

folder_name = './archive'


class UartSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(UartSettingsDialog, self).__init__(parent)
        self.ui = Ui_UartSettingsDialog()
        self.ui.setupUi(self)
        self.port_data = {}
        self.update_ports_list()
        self.ui.updatePortsList.clicked.connect(self.update_ports_list)
        self.ui.port.currentIndexChanged.connect(self.update_tooltip)

    def update_tooltip(self, s):
        if int(s) >= 0:
            ports = list(port_list.comports())
            if len(ports) - 1 >= int(s):
                description = ports[int(s)].description
                self.ui.port.setToolTip("<html><head/><body><p>" + description + "</p></body></html>")
            else:
                self.ui.port.setToolTip("")
        else:
            self.ui.port.setToolTip("")

    def update_ports_list(self):
        self.ui.port.clear()
        ports = list(port_list.comports())
        for port in ports:
            self.ui.port.addItem(port.device)
        # Set tool tip with description of COM port
        if len(ports):
            description = ports[0].description
            self.ui.port.setToolTip("<html><head/><body><p>" + description + "</p></body></html>")

    def accept(self) -> None:
        self.port_data = {'port': self.ui.port.currentText(),
                          'baudrate': int(self.ui.baudrate.currentText()),
                          'dataBits': self.ui.dataBits.currentIndex(),
                          'parity': self.ui.parity.currentIndex(),
                          'stopBits': self.ui.stopBits.currentIndex(),
                          'flowControl': self.ui.flowControl.currentIndex()}
        QDialog.accept(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.quadrant_1_x = []
        self.quadrant_1_y = []
        self.quadrant_2_x = []
        self.quadrant_2_y = []
        self.quadrant_3_x = []
        self.quadrant_3_y = []
        self.quadrant_4_x = []
        self.quadrant_4_y = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.port_settings)
        self.ui.pushButton_2.clicked.connect(self.connect_serial)
        self.ui.action_uart_settings.triggered.connect(self.port_settings)
        self.ui.action_connect.triggered.connect(self.connect_serial)
        self.ui.execButton.clicked.connect(self.plot_data)
        self.ui.action_open.triggered.connect(self.open_data)
        self.ui.saveGraphButton.clicked.connect(self.save_data_to_csv)
        self.ui.saveGraphButton.setEnabled(False)

        self.update_file_list()
        self.ui.listOfFiles.currentItemChanged.connect(self.change_file)

    serialPort = serial.Serial()

    # Default values
    com_port = None
    baudrate = 19200
    dataBits = 3  # serial.EIGHTBITS
    parity = 0  # serial.PARITY_NONE
    stopBits = 0  # serial.STOPBITS_ONE
    xonxoff = False
    rtscts = False
    serialOpen = False

    def port_settings(self, s):
        uart_settings_dialog = UartSettingsDialog(self)
        uart_settings_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        if uart_settings_dialog.exec():
            print(uart_settings_dialog.port_data)
            self.com_port = uart_settings_dialog.port_data['port']
            self.baudrate = uart_settings_dialog.port_data['baudrate']
            self.dataBits = uart_settings_dialog.port_data['dataBits']
            self.parity = uart_settings_dialog.port_data['parity']
            self.stopBits = uart_settings_dialog.port_data['stopBits']
            if uart_settings_dialog.port_data['flowControl'] == 0:
                self.xonxoff = False
                self.rtscts = False
            elif uart_settings_dialog.port_data['flowControl'] == 1:
                self.xonxoff = True
                self.rtscts = False
            elif uart_settings_dialog.port_data['flowControl'] == 2:
                self.xonxoff = False
                self.rtscts = True
        else:
            print('Cancel')

    def connect_serial(self):
        _translate = QtCore.QCoreApplication.translate
        if not self.serialPort.is_open:
            if self.com_port:
                self.serialPort.port = self.com_port
                self.serialPort.baudrate = self.baudrate
                self.serialPort.bytesize = bytesize[self.dataBits]
                self.serialPort.parity = parities[self.parity]
                self.serialPort.stopbits = stopbits[self.stopBits]
                self.serialPort.xonxoff = self.xonxoff
                self.serialPort.rtscts = self.rtscts
                self.serialPort.timeout = 2
                # Opening serial port
                self.serialPort.open()
                if self.serialPort.is_open:
                    print(self.serialPort.name)
                    self.ui.pushButton_2.setText(_translate("MainWindow", "Отключиться"))
                else:
                    print('Fail open COM port')
            else:
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Не указан порт для подключения")
                msg.setInformativeText("Подключите USB-UART преобразователь, затем зайдите в настройки и выберите необходимый порт.")
                msg.setWindowTitle("Ошибка")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
        else:
            self.serialPort.close()
            self.ui.pushButton_2.setText(_translate("MainWindow", "Подключиться"))

    # Заготовка функции для чтения данных из COM порта
    def get_data(self):
        try:
            data_in = self.serialPort.read()
        except serial.SerialException as e:
            # There is no new data from serial port
            return None
        except TypeError as e:
            # Disconnect of USB->UART occured
            self.serialPort.close()
            return None
        else:
            # Some data was received
            return data_in

    def div1000(self, point):
        i = int(point[0]) / 1000
        u = int(point[1]) / 1000
        return u, i

    def open_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Открыть файл данных", "",
                                                  "CSV Files (*.csv);;All Files (*)", options=options)
        self.quadrant_1_x.clear()
        self.quadrant_1_y.clear()
        self.quadrant_2_x.clear()
        self.quadrant_2_y.clear()
        self.quadrant_3_x.clear()
        self.quadrant_3_y.clear()
        self.quadrant_4_x.clear()
        self.quadrant_4_y.clear()
        if fileName:
            print(fileName)
            with open(fileName, 'r', newline='', encoding='utf-8') as File:
                data = csv.reader(File, delimiter=';')
                # Переводим милливольты и миллиамперы в вольты и амперы
                result = list(map(self.div1000, data))
                # Сортировка по столбцу с напряжением
                result = sorted(result, key=lambda row: row[0])
                # Разбиваем данные по квадратнам
                # и формируем по два отдельных списка с координатами x и y
                for u, i in result:
                    if u >= 0 and i >= 0:
                        self.quadrant_1_x.append(u)
                        self.quadrant_1_y.append(i)
                    elif u <= 0 and i >= 0:
                        self.quadrant_2_x.append(u)
                        self.quadrant_2_y.append(i)
                    elif u <= 0 and i <= 0:
                        self.quadrant_3_x.append(u)
                        self.quadrant_3_y.append(i)
                    elif u >= 0 and i <= 0:
                        self.quadrant_4_x.append(u)
                        self.quadrant_4_y.append(i)

    def save_data_to_csv(self):
        now = datetime.now()
        filename = now.strftime('%Y%m%d%H%M%S.csv')
        now_time = now.strftime('%H:%M:%S')
        now_date = now.strftime('%d.%m.%Y')

        data = [['NAME', self.ui.dutName.text()],
                ['DATE', now_date],
                ['TIME', now_time],
                ['ILLUMINATION', self.ui.illumination.text()],
                ['TEMPERATURE', self.ui.temperature.text()],
                ['COMMENT', self.ui.comment.toPlainText()],
                ['FORVARD_IVC_DAC_START', self.ui.FrvdBrBegin.value()],
                ['FORVARD_IVC_DAC_END', self.ui.FrvdBrEnd.value()],
                ['FORVARD_IVC_DAC_STEP', self.ui.FrvdBrStep.value()],
                ['REVERSE_IVC_DAC_START', self.ui.RevBrBegin.value()],
                ['REVERSE_IVC_DAC_END', self.ui.RevBrEnd.value()],
                ['REVERSE_IVC_DAC_STEP', self.ui.RevBrStep.value()],
                ['VAH_DELAY', 20],
                ['U', 'I']]

        data += list(map(list, zip(self.quadrant_1_x, self.quadrant_1_y)))
        data += list(map(list, zip(self.quadrant_2_x, self.quadrant_2_y)))
        data += list(map(list, zip(self.quadrant_3_x, self.quadrant_3_y)))
        data += list(map(list, zip(self.quadrant_4_x, self.quadrant_4_y)))

        File = open(os.path.join(folder_name, filename), 'w', newline='', encoding='utf-8')
        with File:
            writer = csv.writer(File, delimiter=';')
            writer.writerows(data)

        self.ui.saveGraphButton.setEnabled(False)

        self.ui.listOfFiles.currentItemChanged.disconnect()
        self.ui.listOfFiles.clear()
        self.update_file_list()
        # Вешааем сигнал изменения текущего пункта списка
        self.ui.listOfFiles.currentItemChanged.connect(self.change_file)

    def plot_data(self):
        self.ui.plotWidget.canvas.ax1.clear()
        self.ui.plotWidget.canvas.ax2.clear()
        self.ui.plotWidget.canvas.ax3.clear()
        self.ui.plotWidget.canvas.ax4.clear()

        self.ui.plotWidget.canvas.ax1.plot(self.quadrant_2_x, self.quadrant_2_y, 'tab:blue', marker='o', linestyle='')    # II  quadrant
        self.ui.plotWidget.canvas.ax2.plot(self.quadrant_1_x, self.quadrant_1_y, 'tab:blue', marker='o', linestyle='')  # I   quadrant
        self.ui.plotWidget.canvas.ax3.plot(self.quadrant_3_x, self.quadrant_3_y, 'tab:blue', marker='o', linestyle='')   # III quadrant
        self.ui.plotWidget.canvas.ax4.plot(self.quadrant_4_x, self.quadrant_4_y, 'tab:blue', marker='o', linestyle='')     # IV  quadrant

        self.ui.plotWidget.canvas.ax1.grid(True)
        self.ui.plotWidget.canvas.ax2.grid(True)
        self.ui.plotWidget.canvas.ax3.grid(True)
        self.ui.plotWidget.canvas.ax4.grid(True)

        # Установка нулевых предеов по осям
        self.ui.plotWidget.canvas.ax1.set_xlim(xmin=None, xmax=0)
        self.ui.plotWidget.canvas.ax1.set_ylim(ymin=0, ymax=None)
        self.ui.plotWidget.canvas.ax2.set_xlim(xmin=0, xmax=None)
        self.ui.plotWidget.canvas.ax2.set_ylim(ymin=0, ymax=None)
        self.ui.plotWidget.canvas.ax3.set_xlim(xmin=None, xmax=0)
        self.ui.plotWidget.canvas.ax3.set_ylim(ymin=None, ymax=0)
        self.ui.plotWidget.canvas.ax4.set_xlim(xmin=0, xmax=None)
        self.ui.plotWidget.canvas.ax4.set_ylim(ymin=None, ymax=0)

        self.ui.plotWidget.canvas.draw()

        self.ui.saveGraphButton.setEnabled(True)

    def update_file_list(self):
        # Получаем список файлов
        files = os.listdir(folder_name)
        # Самые свежие файлы сверху
        files.sort(reverse=True)
        # Добавляем файлы в список
        for f in files:
            name = f.split('.')[0]
            item = QListWidgetItem(name)
            self.ui.listOfFiles.addItem(item)

    def change_file(self, item):
        with open(os.path.join(folder_name, item.text() + '.csv'), 'r', newline='', encoding='utf-8') as File:
            data = list(csv.reader(File, delimiter=';'))
            self.ui.dutNameValue.setText(data[0][1])
            self.ui.dateValue.setText(data[1][1])
            self.ui.timeValue.setText(data[2][1])
            self.ui.illuminationValue.setText(data[3][1])
            self.ui.temperatureValue.setText(data[4][1])
            self.ui.comment_2.clear()
            self.ui.comment_2.insertPlainText(data[5][1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

