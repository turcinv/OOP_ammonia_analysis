import pickle
from VMDLite import read_cube_file


def cube_to_pickle(frame):
    """
    Save data from cube file to pickle binary file
    :param frame: number of frame
    :return: pickle file
    """

    # loading cube file
    origin, step_size, data, atoms = read_cube_file(f"./cube_files/small-clusters-SPIN_DENSITY-1_{frame}_small.cube")
    info = {"origin": origin,
            "step_size": step_size,
            "data": data,
            "atoms": atoms,
            }

    # saving data to pickle file
    with open(f'./cube_files_pickle/ammonia-{frame}.pickle', 'wb') as file:
        pickle.dump(info, file, -1)
