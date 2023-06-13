import streamlit as st
import numpy as np

def matrix_addition(matrix1, matrix2):
    try:
        result = matrix1 + matrix2
        return result
    except ValueError:
        return None

def main():
    st.title("Matrix Addition Calculator")
    st.write("Enter two matrices to perform addition:")

    matrix1_rows = st.number_input("Matrix 1 Rows", min_value=1, value=2, step=1)
    matrix1_cols = st.number_input("Matrix 1 Columns", min_value=1, value=2, step=1)

    matrix2_rows = st.number_input("Matrix 2 Rows", min_value=1, value=2, step=1)
    matrix2_cols = st.number_input("Matrix 2 Columns", min_value=1, value=2, step=1)

    matrix1 = []
    for i in range(matrix1_rows):
        row = []
        for j in range(matrix1_cols):
            value = st.number_input(f"Matrix 1 [{i+1}, {j+1}]", value=0.0)
            row.append(value)
        matrix1.append(row)

    matrix2 = []
    for i in range(matrix2_rows):
        row = []
        for j in range(matrix2_cols):
            value = st.number_input(f"Matrix 2 [{i+1}, {j+1}]", value=0.0)
            row.append(value)
        matrix2.append(row)

    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    if st.button("Calculate Addition"):
        if matrix1.shape == matrix2.shape:
            addition_result = matrix_addition(matrix1, matrix2)
            if addition_result is not None:
                st.write("Addition Result:")
                st.write(addition_result)
            else:
                st.write("Matrices should have the same dimensions for addition.")
        else:
            st.write("Matrices should have the same dimensions for addition.")

if __name__ == "__main__":
    main()
