from sklearn import tree

def results(wight,surface):

	features=([ [35,1], [47,1], [90,0], [48,1], [90,0], [35,1], [96,0], [43,1], [110,0], [95,0] ])
	label=[1,1,2,1,2,1,2,1,2,1,]

	clf=tree.DecisionTreeClassifier()
	clf=clf.fit(features,label)

	result=clf.predict([[wight,surface]])
	print("_"*100)
	if result==1:
		print("ball may be Tennis Ball")
	elif result == 2 :
		print("ball may be Cricket Ball") 
	print("_"*100)
def main():
	print("Fist Application")
	wight=input("Enter Wight  ")
	surface=input("Enter Surface Rough or Smooth  ")

	if surface.lower()=="rough":
		surface=1
	elif surface.lower()=="smooth":
		surface=0
	else :
		print("Wrong Input")

	results(wight,surface)	

if __name__=="__main__":
	main()













# 	output-:

# 	zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/ML/Application/1
# $ python ball.py
# Fist Application
# Enter Wight  90
# Enter Surface Rough or Smooth  smooth
# ____________________________________________________________________________________________________
# ball may be Cricket Ball
# ____________________________________________________________________________________________________

# zine@DESKTOP-BU1PSC0 MINGW64 ~/Desktop/python/ML/Application/1
# $ python ball.py
# Fist Application
# Enter Wight  40
# Enter Surface Rough or Smooth  rough
# ____________________________________________________________________________________________________
# ball may be Tennis Ball
# ____________________________________________________________________________________________________

