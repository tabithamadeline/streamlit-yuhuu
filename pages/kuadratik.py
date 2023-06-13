import streamlit as st
import numpy as np

def calculate_quadratic(matrix):
    result = np.square(matrix)
    return result

# Main Streamlit app
def main():
    st.title("Quadratic Matrix Calculator")

    # Input matrix dimension
    rows = st.number_input("Enter the number of rows:", min_value=1, value=2, step=1)
    cols = st.number_input("Enter the number of columns:", min_value=1, value=2, step=1)

    # Input matrix values
    st.header("Enter Matrix")
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            matrix[i, j] = st.number_input(f"A[{i+1}, {j+1}]:", value=0.0, step=0.1)

    # Perform quadratic calculation
    quadratic_result = calculate_quadratic(matrix)

    # Display results
    st.header("Results")
    st.subheader("Quadratic Result")
    st.write(quadratic_result)

if __name__ == "__main__":
    main()
