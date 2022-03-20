from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import cv2
from model import Model
    
class FaceMaskDetection(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("UI\MainWindow.ui")
        self.ui.show()
        
        model = Model()
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = video_cap.read()
            if not ret:
                break
            
            frame_result, result_pred = model.with_Or_Without_Mask(frame)
            if result_pred == "Face detected ✅":
                flag = True
            elif result_pred == "Face not detected ❌":
                flag = False
            
            self.ui.result_label.setText(result_pred)
            
            if flag:
                frame_rgb = cv2.cvtColor(frame_result, cv2.COLOR_BGR2RGB)
                frame_rgb = cv2.resize(frame_rgb, (600, 500))
                frame_rgb = QImage(frame_rgb, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
                pixmap = QPixmap(frame_rgb)
            else:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_rgb = cv2.resize(frame_rgb, (600, 500))
                frame_rgb = QImage(frame_rgb, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
                pixmap = QPixmap(frame_rgb)
            
            self.ui.cam_label.setPixmap(pixmap)
            
            cv2.waitKey(1)
        
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QApplication([])
    main_window = FaceMaskDetection()
    app.exec()