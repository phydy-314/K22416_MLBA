from HousingPricePrediction.Coding_pyqt6.HousingPricePredictionMainWindow import Ui_MainWindow
import pickle
import os
from HousingPricePrediction.use_trainedmodel.Myprediction import trainedmodel


class HousingPricePredictionMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
        self.add_model_list()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonPredict.clicked.connect(self.process_predict_housepricing)
    def add_model_list(self):
        trainedmodellink="../Trainedmodel"
        for file_name in os.listdir(trainedmodellink):
            if os.path.isfile(os.path.join(trainedmodellink,file_name)) and file_name.endswith(".zip"):
                self.comboBoxTrainedmodel.addItem(file_name)

    def process_predict_housepricing(self):
        AreaIncome=float(self.lineEditAreaIncome.text())
        AreaHouseAge=float(self.lineEditAreaHouseAge.text())
        AreaNumberofRooms=float(self.lineEditAreaNumberofRooms.text())
        AreaNumberofBedrooms=float(self.lineEditAreaNumberofBedrooms.text())
        AreaPopulation=float(self.lineEditAreaPopulation.text())

        modelname="../Trainedmodel/housingmodel.zip"
        if self.comboBoxTrainedmodel.currentIndex()!=-1:
            modelname=f"../Trainedmodel/{self.comboBoxTrainedmodel.currentText()}"
        with open(modelname,'rb') as file:
            trainedmodel=pickle.load(file)

        prediction=trainedmodel.predict(
            [[AreaIncome,AreaHouseAge,AreaNumberofRooms,AreaNumberofBedrooms,AreaPopulation]])
        print("kết quả =",prediction)
        self.lineEditPredictedHousePrice.setText(f'{prediction[0]}')