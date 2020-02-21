import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def dibabetes():
	data=pd.read_csv("diabetes.csv")
	#print(data)
	print("columns.name.")
	print(data.columns)

	print("label Data")
	label=data.Outcome
	# print(label)

	print("Target data")
	#target=data.iloc[3]  #row data display
	target=data.iloc[:,:-1]
	#print(target.columns)

	train_data,test_data,train_label,test_label=train_test_split(target,label,test_size=10)

	algo=KNeighborsClassifier()

	algo.fit(train_data,train_label)

	print("Test_data",test_data)
	predict=algo.predict(test_data)

	# test_data_new=([[1,93,70,31,0,30.4,0.315,23]])
	# ans=algo.predict(test_data_new)
	# print("Predicted op=",ans)
	print(predict)
	accuracy=accuracy_score(test_label,predict)
	return accuracy

def main():

	print("*"*50)
	print("Application Of diabetes")
	print("*"*50)

	accuracy=dibabetes()
	print(accuracy*100)

if __name__=='__main__':
	main();