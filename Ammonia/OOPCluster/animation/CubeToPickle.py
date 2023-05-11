import pickle
from VMDLite import read_cube_file


def cube_to_pickle(frame):
    origin, step_size, data, atoms = read_cube_file(f"./cube_files/small-clusters-SPIN_DENSITY-1_{frame}_small.cube")
    info = {"origin": origin,
            "step_size": step_size,
            "data": data,
            "atoms": atoms,
            }

    with open(f'./cube_files_pickle/ammonia-{frame}.pickle', 'wb') as file:
        pickle.dump(info, file, -1)
