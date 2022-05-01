import matplotlib.pyplot as plt
import numpy as np

# These rotations are twisty puzzle rotation notation
def x(piece):
    return np.rot90(piece, axes=(2, 1))

def y(piece):
    return np.rot90(piece, axes=(1, 0))

def y_prime(piece):
    return np.rot90(piece, axes=(0, 1))

def display(piece):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(piece, edgecolors='black')

    ax.axes.set_xlim3d(0, 3)
    ax.axes.set_ylim3d(0, 3)
    ax.axes.set_zlim3d(0, 3)
    ax.set_box_aspect(aspect = (1,1,1))

    plt.show()

class Piece():
    def __init__(self, piece):
        self.piece = piece
        self.all_pieces = []

        # Get all 90 degree rotations
        for i in range(6):
            piece = x(piece)
            self.all_pieces.append(piece)
            for j in range(3):
                if i % 2 == 0:
                    piece = y(piece)
                else:
                    piece = y_prime(piece)
                self.all_pieces.append(piece)
        
        # Remove duplicates
        self.all_pieces = {piece.tostring(): piece for piece in self.all_pieces}
        print(len(self.all_pieces))
    
    def display(self):
        display(self.piece)
