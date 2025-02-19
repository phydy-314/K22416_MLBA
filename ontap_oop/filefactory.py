import json
import os

class FileFactory:
    # path: path to serialize array of product
    # arrData: array of Product
    def writeData(self, path, arrData):
        jsonString = json.dumps([item.__dict__ for item in arrData], default=str)
        with open(path, "w") as jsonFile:
            jsonFile.write(jsonString)

    # path: path to deserialize array of Product
    # ClassName: Product
    def readData(self, path, ClassName):
        if not os.path.isfile(path):
            return []
        with open(path, "r") as file:
            # Reading from file
            arrData = json.loads(file.read(), object_hook=lambda d: ClassName(**d))
        return arrData