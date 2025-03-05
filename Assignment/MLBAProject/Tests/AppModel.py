from Assignment.MLBAProject.Connectors.Connector import Connector
from Assignment.MLBAProject.Models.PurchaseMLModel import PurchaseMLModel

connector=Connector(server="localhost",port=3360,database="newschema",username="root",password="123456")
connector.connect()
pm=PurchaseMLModel(connector)
pm.execPurchaseHistory()

dfTransform=pm.processTransform()
print(dfTransform.head())
pm.buildCorrelationMatrix(dfTransform)