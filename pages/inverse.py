import streamlit as st
import numpy as np

def matrix_inverse(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return None

def main():
    st.title("Matrix Inverse Calculator")
    st.write("Enter a square matrix to calculate its inverse:")

    matrix_size = st.number_input("Matrix Size", min_value=2, value=2, step=1)

    matrix = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            value = st.number_input(f"Element [{i+1}, {j+1}]", value=0.0)
            row.append(value)
        matrix.append(row)

    matrix = np.array(matrix)

    if st.button("Calculate Inverse"):
        inverse_matrix = matrix_inverse(matrix)
        if inverse_matrix is not None:
            st.write("Inverse Matrix:")
            st.write(inverse_matrix)
        else:
            st.write("The matrix is singular and does not have an inverse.")

if __name__ == "__main__":
    main()
