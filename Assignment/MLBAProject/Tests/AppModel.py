from Assignment.MLBAProject.Connectors.Connector import Connector
from Assignment.MLBAProject.Models.PurchaseMLModel import PurchaseMLModel

connector=Connector(server="localhost",port=8000,database="newschema",username="root",password="Phydy@1311")
connector.connect()
pm=PurchaseMLModel(connector)
pm.execPurchaseHistory()

dfTransform=pm.processTransform()
print(dfTransform.head())
pm.buildCorrelationMatrix(dfTransform)