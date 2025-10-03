from src.maze_solver.core.models import Maze, Cell


def test_maze_creation():
    maze = Maze()
    assert maze == Maze


def test_cell_creation():
    cell = Cell()
    assert cell == Cell
