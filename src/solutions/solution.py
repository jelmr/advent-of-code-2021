from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def solve(self, input_text):
        pass
