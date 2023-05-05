import numpy as np

# Call np.array to create a NumPy array with your own hand-picked values. For example,
# the following call to np.array creates an 8-element array
one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(one_dimensional_array)

# You can also use np.array to create a two-dimensional array. To create a two-dimensional
# array specify an extra layer of square brackets. For example, the following call creates a 3x2 array:
two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)

# You can populate an array with a sequence of numbers:
sequence_of_integers = np.arange(5, 12)
print(sequence_of_integers)

# NumPy provides various functions to populate arrays with random numbers across certain ranges.
# For example, np.random.randint generates random integers between a low and high value.
# The following call populates a 6-element array with random integers between 50 and 100.
random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
print(random_integers_between_50_and_100)

# To create random floating-point values between 0.0 and 1.0, call np.random.random. For example:
random_floats_between_0_and_1 = np.random.random([6])
print(random_floats_between_0_and_1)

# If you want to add or subtract two arrays, linear algebra requires that the two operands have
# the same dimensions. Furthermore, if you want to multiply two arrays, linear algebra imposes
# strict rules on the dimensional compatibility of operands. Fortunately, NumPy uses a trick
# called broadcasting to virtually expand the smaller operand to dimensions compatible for
# linear algebra. For example, the following operation uses broadcasting to add 2.0 to the
# value of every item in the array created in the previous code cell:
random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print(random_floats_between_2_and_3)

# The following operation also relies on broadcasting to multiply each cell in an array by 3:
random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print(random_integers_between_150_and_300)

# Task 1: Create a Linear Dataset
# Your goal is to create a simple dataset consisting of a single feature and a label as follows:
#   Assign a sequence of integers from 6 to 20 (inclusive) to a NumPy array named feature.
#   Assign 15 values to a NumPy array named label such that:
feature = np.arange(6, 21)
print(feature)
label = 3*feature+4
print(label)

# Task 2: Add Some Noise to the Dataset
# To make your dataset a little more realistic, insert a little random noise into each
# element of the label array you already created. To be more precise, modify each value
# assigned to label by adding a different random floating-point value between -2 and +2.
# Don't rely on broadcasting. Instead, create a noise array having the same dimension as label.
noise = (np.random.random([15]) * 4) - 2
print(noise)
label = label + noise
print(label)
