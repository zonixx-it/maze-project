import random
import pytest

from src.maze_solver.core.models import Maze, Cell

MAXROWS: int = 100
MAXCOLS: int = 100


class TestMaze:
    def setup_method(self):
        self.__mazeRows: int = random.randint(1, MAXROWS)
        self.__mazeCols: int = random.randint(1, MAXCOLS)

        # Проверяет успешное создание лабиринта
        try:
            self.__maze = Maze(self.__mazeRows, self.__mazeCols)
        except Exception as e:
            pytest.fail(f"Объект Maze не смог создаться: {e}")

    def test_type(self):
        """Проверяет то, что лабиринт - это объект класса Maze"""
        assert isinstance(
            self.__maze, Maze
        ), f"Тип создаваемого лабиринта не Maze, а {type(self.__maze)}"

    def test_cells_type(self):
        """Проверяет то, что лабиринт состоит из объектов класса Cell"""
        testCell: Cell = self.__maze.get_cell(
            random.randint(0, self.__mazeRows - 1),
            random.randint(0, self.__mazeCols - 1),
        )
        assert isinstance(
            testCell, Cell
        ), f"Тип клеток лабиринта не Cell, а {type(testCell)}"

    def test_data_privacy(self):
        """
        Проверяет то, что параметр data в лабиринте
        недоступен для чтения напрямую
        """
        assert not hasattr(
            self.__maze, "__data"
        ), "Нарушение инкапсуляции: параметр __data не "
        "должен быть доступен извне класса"
        assert not hasattr(
            self.__maze, "_Maze.__data"
        ), "Нарушение инкапсуляции: параметр __data не "
        "должен быть доступен извне класса"

    def test_rows_count_privacy(self):
        """
        Проверяет то, что параметр rowsCount в лабиринте
        недоступен для чтения напрямую
        """
        assert not hasattr(
            self.__maze, "__rowsCount"
        ), "Нарушение инкапсуляции: параметр __rowsCount не "
        "должен быть доступен извне класса"
        assert not hasattr(
            self.__maze, "_Maze.__rowsCount"
        ), "Нарушение инкапсуляции: параметр __rowsCount не "
        "должен быть доступен извне класса"

    def test_rows_count_function(self):
        """
        Проверяет то, что функция-геттер выводит
        корректное число строк в лабиринте
        """
        assert (
            self.__maze.get_rows_count() == self.__mazeRows
        ), f"Функция get_rows_count() выводит не {self.__mazeRows} "
        "строк, а {self.__maze.get_rows_count()}"

    def test_cols_count_privacy(self):
        """
        Проверяет то, что параметр colsCount в лабиринте
        недоступен для чтения напрямую
        """
        assert not hasattr(
            self.__maze, "__colsCount"
        ), "Нарушение инкапсуляции: параметр __colsCount не "
        "должен быть доступен извне класса"
        assert not hasattr(
            self.__maze, "_Maze.__colsCount"
        ), "Нарушение инкапсуляции: параметр __colsCount не "
        "должен быть доступен извне класса"

    def test_cols_count_function(self):
        """
        Проверяет то, что функция-геттер выводит
        корректное число столбцов в лабиринте
        """
        assert (
            self.__maze.get_cols_count() == self.__mazeCols
        ), f"Функция get_rows_count() выводит не {self.__mazeCols} "
        "столбцов, а {self.__maze.get_cols_count()}"


def test_cell_creation():
    cell: Cell = Cell()
    assert isinstance(cell, Cell)
