import streamlit as st
import numpy as np

def calculate_eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Main Streamlit app
def main():
    st.title("Eigenvalue and Eigenvector Calculator")

    # Input matrix dimension
    size = st.number_input("Enter the size of the square matrix:", min_value=2, value=2, step=1)

    # Input matrix values
    st.header("Enter Matrix")
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i, j] = st.number_input(f"A[{i+1}, {j+1}]:", value=0.0, step=0.1)

    # Perform eigenvalue and eigenvector calculation
    eigenvalues, eigenvectors = calculate_eigen(matrix)

    # Display results
    st.header("Results")
    st.subheader("Eigenvalues")
    st.write(eigenvalues)

    st.subheader("Eigenvectors")
    st.write(eigenvectors)

if __name__ == "__main__":
    main()
