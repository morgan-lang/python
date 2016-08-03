import pickle
print("pickling lists")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Brand X", "Brand Y", "Brand Z"]

f = open("pickles1.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nUnpickling lists...")
g = open("pickles1.dat", "rb")
rvariety = pickle.load(g)
rshape = pickle.load(g)
rbrand = pickle.load(g)

print(rvariety)
print(rshape)
print(rbrand)
g.close()
input("enter to exit")