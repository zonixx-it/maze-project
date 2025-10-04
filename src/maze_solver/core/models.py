class Cell:
    pass


class Maze:
    def __init__(self, rowsCount: int, colsCount: int):
        self.__rowsCount: int = rowsCount
        self.__colsCount: int = colsCount
        self.__data: list[list[Cell]] = [
            [Cell() for _ in range(colsCount)] for _ in range(rowsCount)
        ]

    def get_rows_count(self) -> int:
        return self.__rowsCount

    def get_cols_count(self) -> int:
        return self.__colsCount

    def get_cell(self, rowIndex, colIndex) -> Cell:
        return self.__data[rowIndex][colIndex]
