'''import pickle
data=['prince',24,'pune']

with open("data.pkl","wb") as prin:
    pickle.dump(data, prin)

with open("data.pkl", "rb") as prin:
    loaded_data = pickle.load(prin)

print("the loaded data is", loaded_data)'''
import pickle
#with open("data.pkl","rb") as prin:
#    loaded_data=pickle.load(prin)
#print("loaded_data")
'''student={
    "name":"prince",
    "age":24,
    "city":"kathmandu",
    "skills":["python","java"]
}
with open ("self.pkl","wb") as selffile:
    pickle.dump(student, selffile)

print("data serialized successfully ")'''
#dump & dumps
data=[1,2,3,4,5]
byte_data =pickle.dumps(data)
original=pickle. loads ( byte_data )
print("the byte data is", byte_data)
print("the original data is",original)
# example using load loads dump and dumps
import pickle as pk
student={
    "name":"Abhishek",
    "age":24,
    "city":"kathmandu",
    "skills":["python","java"]
}
#dumps()
byte_data=pk.dumps(student)
print("byte data is", byte_data )

#loads()
print("from bytes: ")
pk.loads(byte_data)

#dump()
with open("class.pkl","wb") as classfile:
    pk.dump(student, classfile)

#load()
with open("class.pkl","rb") as classfile:
    loaded_data=pk.load(classfile)
    print("the loaded data is", loaded_data)
