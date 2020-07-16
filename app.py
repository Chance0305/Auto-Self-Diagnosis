import time, sys, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout()
        self.lblScl = QLabel('학교', self)
        self.leScl = QLineEdit('양영디지털고등학교', self)
        self.lblName = QLabel('이름', self)
        self.leName = QLineEdit(self)
        self.lblBirth = QLabel('생년월일', self)
        self.leBirth = QLineEdit(self)
        self.submitBtn = QPushButton('자가 진단', self)

        self.initUI()

    def initUI(self):
        self.vbox.addWidget(self.lblScl)
        self.vbox.addWidget(self.leScl)
        self.vbox.addWidget(self.lblName)
        self.vbox.addWidget(self.leName)
        self.vbox.addWidget(self.lblBirth)
        self.vbox.addWidget(self.leBirth)
        self.vbox.addWidget(self.submitBtn)
        self.setLayout(self.vbox)

        self.submitBtn.pressed.connect(self.diagnosis)

        self.setWindowTitle('Application')
        self.setGeometry(200, 200, 200, 100)
        self.center()
        self.show()

    # 프로그램을 화면 중앙으로 배치
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def diagnosis(self):
        scl = self.leScl.text()
        name = self.leName.text()
        birth = self.leBirth.text()

        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('--disable-gpu')
        # options.add_argument('lang=ko_KR')
        browser = webdriver.Chrome(chrome_options=options)

        try:
            browser.get("https://eduro.goe.go.kr/stv_cvd_co00_002.do")
            browser.find_element_by_css_selector("#schulNm").send_keys(scl)
            browser.find_element_by_css_selector("#btnSrchSchul").click()
            browser.find_element_by_css_selector("#pName").send_keys(name)
            browser.find_element_by_css_selector("#frnoRidno").send_keys(birth)
            time.sleep(1)
            browser.find_element_by_css_selector("#btnConfirm").click()
            time.sleep(1)

            browser.find_element_by_css_selector("#rspns011").click()
            browser.find_element_by_css_selector("#rspns02").click()
            browser.find_element_by_css_selector("#rspns070").click()
            browser.find_element_by_css_selector("#rspns080").click()
            browser.find_element_by_css_selector("#rspns090").click()
            time.sleep(1)
            browser.find_element_by_css_selector("#btnConfirm").click()
            time.sleep(2)

            for i in reversed(range(self.vbox.count())): 
                self.vbox.itemAt(i).widget().deleteLater()

            self.lblEnd = QLabel("자가진단 완료!", self)
            self.vbox.addWidget(self.lblEnd)
        except Exception as e:
            print(e)
        finally:
            browser.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())