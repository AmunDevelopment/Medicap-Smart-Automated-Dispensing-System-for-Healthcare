from src.views.windows.pages.ui_AuthenticationPage import *
from src.models.database import Database
from PySide6.QtCore import *
from src.ai.camera import Camera
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtCore import QUrl
import os
class authenticationPage(QWidget):
    def __init__(self,mainWindow):
        QWidget.__init__(self)
        self.ui = Ui_authenticationPage()
        self.mainWindow = mainWindow
        self.mainWindow.ui.title_Label.setText('Welcome to ADC')
        self.authorizedSound_file = 'src\\views\\assets\\soundeffects\\authorized.mp3'
        self.unauthorizedSound_file = 'src\\views\\assets\\soundeffects\\unauthorized.mp3'
        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.cameraInit = Camera(self.ui.cameraCaptureLabel)
        self.cameraInit.face_recognition_active = True
        self.cameraInit.setup_camera()
    def check_action(self,enable_Buttons):
        if(self.cameraInit.similarity != None):
            if(self.cameraInit.similarity >= 0.5):
                self.cameraInit.close_camera()
                self.__Get__Staff(self.cameraInit.recognizied_face)
                self.__play_sound(self.authorizedSound_file)
                self.timer.stop()
                enable_Buttons()
            elif (self.cameraInit.similarity<0.5):
                self.__play_sound(self.unauthorizedSound_file)
                self.cameraInit.similarity = None
    def __Get__Staff(self,faceID):
        db = Database()
        target_faceID = os.path.join('src','data','known_faces',faceID)
        db.cursor.execute("SELECT name,id,role FROM Staff WHERE face_id=?",(target_faceID,))
        self.authorized_staff = db.cursor.fetchone()
        self.mainWindow.current_staff = self.authorized_staff
        self.mainWindow.ui.title_Label.setText(f'Welcome {self.authorized_staff[0]}')
    def __play_sound(self,sound):
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.mediaPlayer.setSource(QUrl.fromLocalFile(sound))
        self.audioOutput.setVolume(50)
        self.mediaPlayer.play()