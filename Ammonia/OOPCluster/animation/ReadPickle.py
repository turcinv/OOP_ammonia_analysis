import pickle
import numpy as np


def read_pickle(args):
    frame, d = args
    with open(f"./cube_files_pickle/ammonia-{frame}.pickle", "rb") as file:
        cube = pickle.load(file)
    origin = cube.get("origin")
    step_size = cube.get("step_size")
    data = cube.get("data")
    atoms = cube.get("atoms")

    x, y, z = np.mgrid[0:data.shape[0], 0:data.shape[0], 0:data.shape[0]] * step_size[0]

    d[frame] = {"origin": origin,
                "step_size": step_size,
                "data": data,
                "atoms": atoms,
                "x": x,
                "y": y,
                "z": z}
