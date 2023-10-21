from typing import Tuple

import numpy as np

#left_motor  = const + gain *  np.sum( LEFT * preprocess(image) )
#right_motor = const + gain *  np.sum( RIGHT * preprocess(image) )


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")

    res[:,0:320] = 1
    #res.fill(1.0)
    ## these are random values
    #res[100:150, 100:150] = 1
    #res[300:, 200:] = 1
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")

    res[:,320:640] = -1
    #res.fill(1.0)
    # these are random values
    #res[100:150, 100:300] = -1
    # ---
    return res
