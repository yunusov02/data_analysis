import numpy as np

def demonstrate_transpose():
    # Create a simple 2D array (3 rows, 2 columns)
    original = np.array([[10, 20], [30, 40], [50, 60]])
    print(f"Original Shape: {original.shape}")
    print(original)

    # Transpose using .T (Returns a view, not a copy)
    transposed = original.T
    print(f"\nTransposed Shape: {transposed.shape}")
    print(transposed)

    # Demonstrate that it is a view: modifying 'transposed' affects 'original'
    transposed[0, 0] = 999
    print(f"\nModified Transposed[0,0] to 999")
    print(f"Original[0,0] is now: {original[0,0]}")

    # 1D Array behavior and the 'correction' for column vectors
    vec = np.array([1, 2, 3])
    print(f"\n1D Vector Shape: {vec.shape}")
    print(f"1D Vector Transposed Shape: {vec.T.shape} (No change!)")

    # Correcting 1D Transpose: Expand dimensions first
    col_vec = vec[:, np.newaxis]
    print(f"Corrected Column Vector Shape: {col_vec.shape}")
    print(col_vec)
    
    row_vec_again = col_vec.T
    print(f"Transposed back to Row Vector Shape: {row_vec_again.shape}")

if __name__ == "__main__":
    demonstrate_transpose()