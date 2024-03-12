import numpy as np  
import pickle
test=np.load(fr'C:\Users\imanu\Desktop\coding projects\SAIL\Repeat\GraphSol\data\preprocess\esol\features\node_features\aaeX.npy')
#Repeat\GraphSol\data\preprocess\1amc\1amc_test.pickle
#C:\Users\imanu\Desktop\coding projects\SAIL\Repeat\GraphSol\data\preprocess\esol\esol_test.pickle
# Read the first pickle file

with open(r'C:\Users\imanu\Desktop\coding projects\SAIL\Repeat\GraphSol\data\preprocess\1amc\1amc_test.pickle', 'rb') as file1:
    data1 = pickle.load(file1)

# Read the second pickle file
with open(r'C:\Users\imanu\Desktop\coding projects\SAIL\Repeat\GraphSol\data\preprocess\esol\esol_test.pickle', 'rb') as file2:
    data2 = pickle.load(file2)

# Compare the size of the pickle files
size1 = len(pickle.dumps(data1))
size2 = len(pickle.dumps(data2))

# Compare the length of the pickle files
length1 = len(data1)
length2 = len(data2)

# Compare the shape of the pickle files


# Print the results
print(f"Size of first pickle file: {size1} bytes")
print(f"Size of second pickle file: {size2} bytes")
print(f"Length of first pickle file: {length1}")
print(f"Length of second pickle file: {length2}")
#also the type of the data
#print(data1)
#print(data2)