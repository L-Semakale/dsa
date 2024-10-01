class SparseMatrix:
    def __init__(self, matrix_file_path):
        self.num_rows = 0
        self.num_cols = 0
        self.elements = {}  # Dictionary to store non-zero elements (row, col): value
        self.load_matrix(matrix_file_path)
    
    def load_matrix(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            self.num_rows = int(lines[0].split('=')[1])
            self.num_cols = int(lines[1].split('=')[1])
            
            for line in lines[2:]:
                line = line.strip()
                if line:  # Ignore empty lines
                    row, col, value = map(int, line.strip('()').split(','))
                    self.elements[(row, col)] = value
    
    def display_matrix(self):
        print(f"Matrix Dimensions: {self.num_rows}x{self.num_cols}")
        for (row, col), value in self.elements.items():
            print(f"Element at ({row}, {col}): {value}")


# Example usage:
if __name__ == "__main__":
    matrix = SparseMatrix("../sample_inputs/easy_sample_03_3.txt")
    matrix.display_matrix()

