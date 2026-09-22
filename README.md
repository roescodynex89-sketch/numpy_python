# NumPy

NumPy (**Numerical Python**) is an open-source Python library designed for **numerical computing, data science, scientific computing, and machine learning**.

It provides powerful **N-dimensional arrays (`ndarray`)** and a large collection of mathematical functions that make working with large datasets fast and efficient.

---

## 📌 What is NumPy?

NumPy is one of the most important libraries in the Python ecosystem.

In standard Python, we commonly use **lists** to store collections of data. However, Python lists can be slower and consume more memory when working with large numerical datasets.

NumPy solves this problem by providing the **`ndarray` (N-dimensional array)**, which is optimized for numerical operations.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```

Output:

```text
[10 20 30 40 50]
```

---

## 🚀 Why is NumPy Important?

NumPy is important because it provides:

* ⚡ Fast numerical operations
* 📦 Efficient data storage
* 🔢 Multi-dimensional arrays
* 🧮 Mathematical and statistical functions
* 🔄 Vectorized operations
* 📊 Support for data analysis
* 🤖 A foundation for Machine Learning
* 🐼 Integration with Pandas, Matplotlib, Scikit-learn, and other Python libraries

---

## 🆚 Python List vs NumPy Array

### Python List

```python
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers]

print(result)
```

### NumPy Array

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

result = numbers * 2

print(result)
```

Output:

```text
[ 2  4  6  8 10]
```

NumPy allows us to perform operations on an entire array without writing explicit loops.

---

# 📚 NumPy Topics

This repository contains my NumPy learning and practice.

## 1. NumPy Basics

* Installing NumPy
* Importing NumPy
* Creating NumPy arrays
* `np.array()`
* Checking array type
* Array attributes

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(type(arr))
print(arr)
```

---

## 2. Array Attributes

Important NumPy array attributes:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.ndim)   # Number of dimensions
print(arr.shape)  # Shape of array
print(arr.size)   # Total number of elements
print(arr.dtype)  # Data type
```

---

## 3. Creating Arrays

NumPy provides several functions for creating arrays.

```python
np.zeros((3, 3))
np.ones((2, 4))
np.full((2, 3), 7)
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
```

Example:

```python
zeros = np.zeros((3, 3))

print(zeros)
```

---

## 4. Indexing and Slicing

NumPy supports powerful indexing and slicing.

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[1:4])
```

For 2D arrays:

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix[0, 1])
print(matrix[:, 1])
```

---

## 5. Mathematical Operations

NumPy makes mathematical operations simple.

```python
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
```

---

## 6. Array Operations

NumPy supports element-wise operations.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Output:

```text
[5 7 9]
[-3 -3 -3]
[ 4 10 18]
[0.25 0.4  0.5 ]
```

---

## 7. Reshaping Arrays

Arrays can be converted into different shapes.

```python
arr = np.array([1, 2, 3, 4, 5, 6])

matrix = arr.reshape(2, 3)

print(matrix)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

---

## 8. Boolean Indexing

Boolean indexing allows us to filter data.

```python
arr = np.array([10, 20, 30, 40, 50])

result = arr[arr > 25]

print(result)
```

Output:

```text
[30 40 50]
```

---

## 9. Random Numbers

NumPy provides useful functions for generating random numbers.

```python
random_numbers = np.random.randint(1, 100, 5)

print(random_numbers)
```

---

## 10. Linear Algebra

NumPy also provides tools for linear algebra.

```python
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

result = np.dot(a, b)

print(result)
```

---

# 🛠️ Installation

Install NumPy using pip:

```bash
pip install numpy
```

Check the installed version:

```python
import numpy as np

print(np.__version__)
```

---

# 📁 Repository Structure

```text
numpy-learning/
│
├── basics/
├── arrays/
├── indexing-slicing/
├── mathematical-operations/
├── reshaping/
├── broadcasting/
├── random/
├── statistics/
├── linear-algebra/
└── README.md
```

---

# 🎯 Learning Goals

Through this repository, I am learning how to use NumPy for:

* Numerical computing
* Data manipulation
* Array operations
* Data analysis
* Statistical calculations
* Scientific computing
* Machine Learning preparation

---

# 🔗 NumPy Ecosystem

NumPy is commonly used together with:

* **Pandas** → Data analysis
* **Matplotlib** → Data visualization
* **Seaborn** → Statistical visualization
* **Scikit-learn** → Machine Learning
* **SciPy** → Scientific computing

---

## 📖 Official Documentation

[NumPy Documentation](https://numpy.org/doc/)

---

## 👨‍💻 Author

**Estiak Aktar Roes**

Learning Python, NumPy, Data Science, and Machine Learning step by step.

---

⭐ If you find this repository useful, consider giving it a star!
