import numpy as np

# Get user input
j = int(input("Enter any number (0-9): "))
# Step function

step_function = lambda x: 1 if x >= 0 else 0




# Corrected training data
training_data = [
    {'input': [1, 1, 0, 0, 0, 0], 'label': 1},
    {'input': [1, 1, 0, 0, 0, 1], 'label': 0},
    {'input': [1, 1, 0, 0, 1, 0], 'label': 1},
    {'input': [1, 1, 0, 1, 1, 1], 'label': 0},
    {'input': [1, 1, 0, 1, 0, 0], 'label': 1},
    {'input': [1, 1, 0, 1, 0, 1], 'label': 0},
    {'input': [1, 1, 0, 1, 1, 0], 'label': 1},
    {'input': [1, 1, 0, 1, 1, 1], 'label': 0},
    {'input': [1, 1, 1, 0, 0, 0], 'label': 1},
    {'input': [1, 1, 1, 0, 0, 1], 'label': 0},
]

# Initialize weights (6 inputs)
weights = np.zeros(6)

# Training (Perceptron learning rule)
for data in training_data:
    x = np.array(data['input'])
    label = data['label']
    output = step_function(np.dot(x, weights))
    error = label - output
    weights += error * x

# Test input
input = np.array([int(bit) for bit in list('{0:06b}'.format(j))])

# Prediction
predicted = step_function(np.dot(input, weights))

output = "even" if predicted == 1 else "odd"

print(j, "is", output)
