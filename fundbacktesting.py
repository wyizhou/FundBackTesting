from math import floor
from FundBT import FundBT
from fundsParam import fundsList


fundBT = FundBT(fundsList= fundsList, loseStatusAssignFundCode= "163407",eachAdditionalCaptital= 5000, rebalanceRate=0.05,inititalCaptital= 10000, startDate="2018-01-01", endDate = "2023-12-01")
fundBT.checkFundData()
fundBT.simulationsCalc()
fundBT.outData()

