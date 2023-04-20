import pandas as pd
import math


def generate_xyz_input(box_size: float,
                       fp_frame: str,
                       fp_output: str,
                       number_of_ammonia=0,
                       grid_spacing=2,
                       orb=False) -> None:
    # TODO: Try and except
    """
    This function generates coordinates of ghost atoms.
    Default spacing is 2 Angstrom for a box of defined size in Angstrom.

    :param fp_output: Name of output file.
    :param fp_frame: Name of input file.
    :param grid_spacing: Assumed grid space in Angstrom.
    :param orb: Default is False , for making orb must be changed
    to True.
    :param box_size: Size of box to generate grid.
    :param number_of_ammonia: Number of ammonia molecules
    :return: XYZ coordinates of ghost atoms and centered input atoms.
    """

    # Support functions

    def rows_in_range(range_1, df_n, file_1):
        for rows_1 in range(range_1):
            atom_1 = df_n.loc[rows_1, "atom"]
            row_x = df_n.loc[rows_1, 0]
            row_y = df_n.loc[rows_1, 1]
            row_z = df_n.loc[rows_1, 2]
            file_1.write(" {0!s:4}  {1:13.5f} {2:15.5f} {3:15.5f} \n"
                         .format(atom_1, row_x, row_y, row_z))

    def total(total_ghost_atoms_1, atom_num_1):
        print("\nTotal number of ghost atoms {}.\n"
              .format(total_ghost_atoms_1))
        print("Total number of atoms: {}\n"
              .format(total_ghost_atoms_1 + atom_num_1))

    def writing_and_saving(
            total_ghost_atoms_1,
            atom_num_1,
            df_3_1,
            df_3_g_1,
            file_1):
        file_1.write(str(total_ghost_atoms_1 + atom_num_1))
        file_1.write("\n \n")
        rows_in_range(atom_num_1, df_3_1, file_1)
        rows_in_range(total_ghost_atoms_1, df_3_g_1, file_1)

    # Centering atoms
    pd.set_option("display.max_rows", None,
                  "display.max_columns", None)
    atom_num = number_of_ammonia * 4
    shift = box_size / 2

    file = open(fp_output, 'a+')
    df = pd.read_csv(fp_frame, skiprows=2,
                     names=["atom", 0, 1, 2],
                     header=None,
                     skipinitialspace=True,
                     sep=' ')

    coord_moved = []
    for rows in range(atom_num):
        row = [df.loc[rows, 0] + shift,
               df.loc[rows, 1] + shift,
               df.loc[rows, 2] + shift]
        coord_moved.append(row)

    # Making grid by ghost atoms
    radius = box_size / 2
    center = [radius, radius, radius]
    x_ghost_coordinates, y_ghost_coordinates = [], []
    z_ghost_coordinates = []
    box = round(box_size, 5)
    print('Box size = {} A.\n'.format(box))
    number_of_ghost_atoms = math.ceil(box_size / grid_spacing)
    print("Number of ghost atoms in a row is {}."
          .format(number_of_ghost_atoms))
    dx = round((box_size / number_of_ghost_atoms), 5)
    print('Grid spacing = {} A.'.format(dx))

    if orb:
        for x in range(number_of_ghost_atoms):
            for y in range(number_of_ghost_atoms):
                for z in range(number_of_ghost_atoms):
                    size_x = dx * z + dx / 2
                    size_y = dx * y + dx / 2
                    size_z = dx * x + dx / 2
                    x_ghost_coordinates.append(size_x)
                    y_ghost_coordinates.append(size_y)
                    z_ghost_coordinates.append(size_z)

        atoms = len(x_ghost_coordinates)
        orb_of_ghost_atoms = []
        ghost_atoms = []

        for i in range(atoms):
            x_2 = (x_ghost_coordinates[i] - center[0]) ** 2
            y_2 = (y_ghost_coordinates[i] - center[0]) ** 2
            z_2 = (z_ghost_coordinates[i] - center[0]) ** 2
            final = (x_2 + y_2 + z_2) ** (1 / 2)
            if final <= radius:
                orb_of_ghost_atoms.append(i)
                row = [x_ghost_coordinates[i],
                       y_ghost_coordinates[i],
                       z_ghost_coordinates[i]]
                ghost_atoms.append(row)

            else:
                pass

        df_2 = pd.DataFrame(data=coord_moved, columns=[0, 1, 2])
        df_2_g = pd.DataFrame(data=ghost_atoms, columns=[0, 1, 2])

        total_ghost_atoms = len(orb_of_ghost_atoms)
        ghost_name = []
        for i in range(total_ghost_atoms):
            ghost_name.append("G")

        atom = pd.DataFrame(data=df["atom"])
        # TODO
        at = {"atom": ghost_name}
        ghost_atom = pd.DataFrame(data=at)
        df_3 = atom.join(df_2, how='left')
        df_3_g = ghost_atom.join(df_2_g, how='left')

        # writing and saving .xyz file
        writing_and_saving(total_ghost_atoms, atom_num, df_3, df_3_g, file)
        total(total_ghost_atoms, atom_num)

    else:
        size_x, size_y, size_z = [], [], []
        total_ghost_atoms = number_of_ghost_atoms ** 3
        # writing and saving .xyz file
        for x in range(number_of_ghost_atoms):
            for y in range(number_of_ghost_atoms):
                for z in range(number_of_ghost_atoms):
                    s_x = dx * x + dx / 2
                    s_y = dx * y + dx / 2
                    s_z = dx * z + dx / 2
                    size_x.append(s_x)
                    size_y.append(s_y)
                    size_z.append(s_z)

        for i in range(len(size_x)):
            row = [size_x[i], size_y[i], size_z[i]]
            coord_moved.append(row)

        ghost_atoms = []
        for i in range(len(size_x)):
            row = [size_x[i], size_y[i], size_z[i]]
            ghost_atoms.append(row)

        df_2 = pd.DataFrame(data=coord_moved, columns=[0, 1, 2])
        df_2_g = pd.DataFrame(data=ghost_atoms, columns=[0, 1, 2])
        ghost_name = []
        for i in range(total_ghost_atoms):
            ghost_name.append("G")

        atom = pd.DataFrame(data=df["atom"])
        # TODO
        at = {"atom": ghost_name}
        ghost_atom = pd.DataFrame(data=at)
        df_3 = atom.join(df_2, how='left')
        df_3_g = ghost_atom.join(df_2_g, how='left')

        # writing and saving .xyz file
        writing_and_saving(total_ghost_atoms, atom_num, df_3, df_3_g, file)
        total(total_ghost_atoms, atom_num)

        file.close()
