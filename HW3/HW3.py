def fLoadDataMatrix(filename):
    with open(filename, 'r') as file:
        features = []
        samples = []
        matrix = []
        classes = []
        lines = file.readlines()
        for i, line in enumerate(lines):
            line_data = line.strip().split(',')
            if i == 0:
                features.extend(line_data[1:-1]) 
            else:
                samples.append(line_data[0])
                matrix.append(line_data[1:-1])
                classes.append(line_data[-1])
                
    return samples, classes, features, matrix

filename = 'HW3.csv'
samples, classes, features, matrix = fLoadDataMatrix(filename)
print(f"Samples: {samples}\n")
print(f"Classes: {classes}\n")
print(f"Features: {features}\n")
print(f"Matrix: {matrix}\n")
