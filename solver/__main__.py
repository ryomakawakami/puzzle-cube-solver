import numpy as np

from solver.piece import Piece

Piece(np.array([[[1, 1, 1], [1, 0, 0]]]))
Piece(np.array([[[1]]]))
Piece(np.array([
    [[1, 1, 1], [1, 0, 0]],
    [[1, 0, 0], [0, 0, 0]]
])).display()
