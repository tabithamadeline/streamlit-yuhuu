import streamlit as st
import numpy as np

def convert_to_quadratic_equation(matrix):
    rows, cols = matrix.shape
    equations = []
    for i in range(rows):
        equation = ""
        for j in range(cols):
            coefficient = matrix[i, j]
            term = f"{coefficient}x{j+1}^2"
            equation += term + " + "
        equation = equation.rstrip(" + ")
        equations.append(equation)
    return equations

# Main Streamlit app
def main():
    st.title("Matrix to Quadratic Equation Converter")

    # Input matrix dimension
    rows = st.number_input("Enter the number of rows:", min_value=1, value=2, step=1)
    cols = st.number_input("Enter the number of columns:", min_value=1, value=2, step=1)

    # Input matrix values
    st.header("Enter Matrix")
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            matrix[i, j] = st.number_input(f"A[{i+1}, {j+1}]:", value=0.0, step=0.1)

    # Convert matrix to quadratic equations
    equations = convert_to_quadratic_equation(matrix)

    # Display results
    st.header("Results")
    st.subheader("Quadratic Equations")
    for idx, equation in enumerate(equations):
        st.write(f"Equation {idx+1}: {equation}")

if __name__ == "__main__":
    main()
