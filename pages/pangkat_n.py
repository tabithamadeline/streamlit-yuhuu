import streamlit as st
import numpy as np

def matrix_exponentiation(matrix, power):
    try:
        result = np.linalg.matrix_power(matrix, power)
        return result
    except np.linalg.LinAlgError:
        return None

def main():
    st.title("Matrix Exponentiation Calculator")
    st.write("Enter a square matrix and the power to calculate its exponentiation:")

    matrix_size = st.number_input("Matrix Size", min_value=2, value=2, step=1)
    power = st.number_input("Pangkat", min_value=0, value=2, step=1)

    matrix = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            value = st.number_input(f"Element [{i+1}, {j+1}]", value=0.0)
            row.append(value)
        matrix.append(row)

    matrix = np.array(matrix)

    if st.button("Calculate Exponentiation"):
        exponentiation_result = matrix_exponentiation(matrix, power)
        if exponentiation_result is not None:
            st.write("Exponentiation Result:")
            st.write(exponentiation_result)
        else:
            st.write("The matrix is not square.")

if __name__ == "__main__":
    main()
