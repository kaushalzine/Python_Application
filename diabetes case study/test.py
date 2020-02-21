import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def dibabetes():
	data=pd.read_csv("diabetes.csv")
	print(data)
	print("columns.name.")
	print(data.columns)

	print("label Data")
	label=data.Outcome
	# print(label)

	print("Target data")
	
	target=data.iloc[:,:-1]
	

	train_data,test_data,train_label,test_label=train_test_split(target,label,test_size=10)

	algo=KNeighborsClassifier()

	algo.fit(train_data,train_label)

	test_datassss=data.iloc[766:768].values
	ted=[[1,93,70,31,0,30.4,0.315,23],[1,93,70,31,0,30.4,0.315,23],[5,	121	,72,	23	,112,	26.2	,0.245,	30]]
	test_labell=[0,0,0]
	print("test data row num 1" )
	print(test_datassss)
	
	print("test dATA-")
	print(test_data)

	predict=algo.predict(ted)

	#predict=algo.predict(test_data)



	
	print(predict)
	accuracy=accuracy_score(test_labell,predict)
	return accuracy

def main():

	print("*"*50)
	print("Application Of diabetes")
	print("*"*50)

	accuracy=dibabetes()
	print(accuracy*100)

if __name__=='__main__':
	main();