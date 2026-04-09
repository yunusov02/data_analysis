import numpy as np

def demonstrate_tiling():
    # Create a simple 1D array
    arr = np.array([10, 20])
    print(f"Original: {arr}")

    # 1. Tiling: Repeats the whole pattern as a block
    tiled = np.tile(arr, 3)
    print(f"\nnp.tile(arr, 3):")
    print(tiled)  # Output: [10 20 10 20 10 20]

    # 2. Repeating: Repeats individual elements
    repeated = np.repeat(arr, 3)
    print(f"\nnp.repeat(arr, 3):")
    print(repeated)  # Output: [10 10 10 20 20 20]

    # 3. 2D Tiling: Creating a matrix from a vector
    # Reps=(3, 2) means repeat 3 times on axis 0, 2 times on axis 1
    matrix_tiled = np.tile(arr, (3, 2))
    print(f"\nnp.tile(arr, (3, 2)) result shape: {matrix_tiled.shape}")
    print(matrix_tiled)
    # Resulting shape (3, 4) because (1, 2) array tiled (3, 2) times

if __name__ == "__main__":
    demonstrate_tiling()