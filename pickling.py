import pickle
data = {"name":"Apsa","Age":22,"place":"Alappuzha"}

pickle.dump(data,open("sample_pickling.dkl","wb"))
load = pickle.load(open("sample_pickling.dkl","rb"))
print(load)
