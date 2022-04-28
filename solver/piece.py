import matplotlib.pyplot as plt
import numpy as np

class Piece():
    def __init__(self, piece):
        self.piece = piece
        self.all_pieces = []

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.voxels(self.piece, edgecolors='black')

        ax.axes.set_xlim3d(0, 3)
        ax.axes.set_ylim3d(0, 3)
        ax.axes.set_zlim3d(0, 3)
        ax.set_box_aspect(aspect = (1,1,1))

        plt.show()

    # These rotations are twisty puzzle rotation notation
    def y(piece):
        return

    def x(piece):
        return

    def x_prime(piece):
        return
