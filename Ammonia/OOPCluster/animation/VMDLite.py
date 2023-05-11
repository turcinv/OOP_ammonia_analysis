import numpy as np


def read_cube_file(filename):
    with open(filename, 'r') as f:
        f.readline()
        f.readline()

        num_atoms, origin_x, origin_y, origin_z = f.readline().lstrip(" ").split("    ")
        num_atoms = int(num_atoms)
        grid_x, step_x, _, _ = f.readline().lstrip(" ").split("    ")
        grid_y, _, step_y, _ = f.readline().lstrip(" ").split("    ")
        grid_z, _, _, step_z = f.readline().lstrip(" ").split("    ")

        origin = np.array([float(origin_x), float(origin_y), float(origin_z)], dtype=float)
        grid_size = np.array([float(grid_x), float(grid_y), float(grid_z)], dtype=int)
        step_size = np.array([float(step_x), float(step_y), float(step_z)], dtype=float)

        atoms = []
        for i in range(num_atoms):
            line = f.readline().lstrip(" ").rstrip("\n").split("   ")
            atoms.append((line[0], float(line[2].lstrip(" ")), float(line[3].lstrip(" ")),
                          float(line[4].lstrip(" "))))

        data = []
        for line in f:
            data += [float(x.lstrip(" ")) for x in line.lstrip(" ").rstrip("\n").rstrip(" ").split()]

        data = np.array(data).reshape(grid_size)
        return origin, step_size, data, atoms
