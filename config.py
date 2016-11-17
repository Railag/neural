import random


class Config:
    k = 5
    Em = 0.001
    alpha = 0.05

    start_T = 1

    neurons_count = 10

    min_w = -0.5
    max_w = 0.5

    @staticmethod
    def get_random_w():
        w = random.uniform(Config.min_w, Config.max_w)

        return w
