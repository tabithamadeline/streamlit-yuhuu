import streamlit as st
import numpy as np

def matrix_determinant(matrix):
    try:
        det = np.linalg.det(matrix)
        return det
    except np.linalg.LinAlgError:
        return None

def main():
    st.title("Matrix Determinant Calculator")
    st.write("Enter a square matrix to calculate its determinant:")

    matrix_size = st.number_input("Matrix Size", min_value=2, value=2, step=1)

    matrix = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            value = st.number_input(f"Element [{i+1}, {j+1}]", value=0.0)
            row.append(value)
        matrix.append(row)

    matrix = np.array(matrix)

    if st.button("Calculate Determinant"):
        determinant = matrix_determinant(matrix)
        if determinant is not None:
            st.write("Determinant:")
            st.write(determinant)
        else:
            st.write("The matrix is not square or its determinant is undefined.")

if __name__ == "__main__":
    main()
