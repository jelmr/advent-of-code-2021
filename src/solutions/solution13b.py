import matplotlib.pyplot as plt
import numpy as np

from solutions.solution13 import Solution13


class Solution13B(Solution13):

    def solve(self, input_text):
        points, folds = self.parse_input(input_text)

        for fold in folds:
            self.fold(points, *fold)

        img = np.zeros(points.max(0) + 1)
        np.add.at(img, tuple(zip(*np.unique(points, axis=0))), 255)
        img = np.flip(img, axis=1)
        img = np.rot90(img)

        return self.ocr_identify_characters(img)

    @staticmethod
    def ocr_identify_characters(img):
        plt.imshow(img)
        plt.show(block=False)
        return input("Please enter the shown letters: ").upper()
