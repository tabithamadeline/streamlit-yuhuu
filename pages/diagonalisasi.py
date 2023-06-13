import streamlit as st
import numpy as np

def diagonalize_matrix(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    diagonal_matrix = np.diag(eigenvalues)
    inverse_eigenvectors = np.linalg.inv(eigenvectors)
    diagonalized_matrix = np.dot(np.dot(eigenvectors, diagonal_matrix), inverse_eigenvectors)
    return diagonalized_matrix

# Main Streamlit app
def main():
    st.title("Matrix Diagonalization")

    # Input matrix dimension
    size = st.number_input("Enter the size of the square matrix:", min_value=2, value=2, step=1)

    # Input matrix values
    st.header("Enter Matrix")
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i, j] = st.number_input(f"A[{i+1}, {j+1}]:", value=0.0, step=0.1)

    # Perform matrix diagonalization
    diagonalized_matrix = diagonalize_matrix(matrix)

    # Display results
    st.header("Results")
    st.subheader("Diagonalized Matrix")
    st.write(diagonalized_matrix)

if __name__ == "__main__":
    main()
