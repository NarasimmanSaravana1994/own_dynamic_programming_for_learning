import os
import time
from multiprocessing import Pool

class Matrix_Maniplation:
    def __init__(self, no_split: int, value_to_find: int, values: list):
        self.no_split = no_split
        self.value_to_find = value_to_find
        self.values = values

    def split(self, no_split_juck) -> list:
        is_first_loop_done = False
        last_index_no = 0
        final_matrix = []
        for value in range(0, self.no_split+1):
            if not is_first_loop_done:
                splitted_matrix = self.values[0:no_split_juck]
                if splitted_matrix != []:
                    final_matrix.append(splitted_matrix)
                    is_first_loop_done = True
                    last_index_no = no_split_juck
                else:
                    break
            else:
                splitted_matrix = self.values[last_index_no:last_index_no+no_split_juck]
                if splitted_matrix != []:
                    final_matrix.append(splitted_matrix)
                    last_index_no = last_index_no+no_split_juck
                else:
                    break

        return final_matrix

    def is_value_exist(self, splitted_matrixes):
        if self.value_to_find in splitted_matrixes:
            print("Yes")

    def call(self):
        total_split = round(len(self.values)/self.no_split)
        splitted_matrixes = self.split(total_split)
        pool = Pool(processes=len(splitted_matrixes))
        pool.map(self.is_value_exist, splitted_matrixes)
        pool.close()
        return

def search_value(value_to_find: int, source_values: list) -> bool:
    cpu_count = os.cpu_count()
    manipulated_matrix = Matrix_Maniplation(
        cpu_count, value_to_find, source_values)
    return manipulated_matrix.call()


if __name__ == '__main__':
    start_time = time.time()
    is_value_exist = search_value(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                  15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33])
    print("--- %s Total execution seconds taken ---" %
          round((time.time() - start_time), 2))
