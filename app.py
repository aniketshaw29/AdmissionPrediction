import pickle

model = pickle.load(open('admission_prediction.pickle','rb'))  #rb = read binary


#Gre, Toefl, Cgpa
print("chances is ",model.predict([[330, 120, 5, 4.5, 5.0, 9.56, 1]])*100)