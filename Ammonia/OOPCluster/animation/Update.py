import mayavi.mlab as mlab
import numpy as np


@mlab.animate
def update(dictionary, number_of_molecules, frames, save_frames):
    fig = mlab.figure(bgcolor=(1, 1, 1), size=(1000, 1000))
    for i in range(frames):
        f = mlab.clf()
        # origin = dictionary[i * 10].get("origin")
        # step_size = dictionary[i * 10].get("step_size")
        data = dictionary[i * 10].get("data")
        atoms = dictionary[i * 10].get("atoms")
        x = dictionary[i * 10].get("x")
        y = dictionary[i * 10].get("y")
        z = dictionary[i * 10].get("z")

        mlab.contour3d(x, y, z, data, contours=[0.0005, ], opacity=0.8, color=(0, 1, 0.75), transparent=True)
        mlab.contour3d(x, y, z, data, contours=[0.002, ], opacity=0.8, color=(0, 1, 0.50), transparent=True)
        mlab.contour3d(x, y, z, data, contours=[0.001, ], opacity=0.5, color=(153 / 255, 153 / 255, 0),
                       transparent=True)

        atoms = np.array(atoms[:number_of_molecules], dtype=float)
        N = np.array(atoms[::4], dtype=float)
        H1 = np.array(atoms[1::4], dtype=float)
        H2 = np.array(atoms[2::4], dtype=float)
        H3 = np.array(atoms[3::4], dtype=float)
        n_x, h1_x, h2_x, h3_x = N[:, 1], H1[:, 1], H2[:, 1], H3[:, 1]
        n_y, h1_y, h2_y, h3_y = N[:, 2], H1[:, 2], H2[:, 2], H3[:, 2]
        n_z, h1_z, h2_z, h3_z = N[:, 3], H1[:, 3], H2[:, 3], H3[:, 3]

        mlab.points3d(n_x, n_y, n_z, scale_factor=1.22, resolution=20, color=(0, 0, 1), scale_mode='none')
        mlab.points3d(h1_x, h1_y, h1_z, scale_factor=1, resolution=20, color=(1, 1, 1), scale_mode='none')
        mlab.points3d(h2_x, h2_y, h2_z, scale_factor=1, resolution=20, color=(1, 1, 1), scale_mode='none')
        mlab.points3d(h3_x, h3_y, h3_z, scale_factor=1, resolution=20, color=(1, 1, 1), scale_mode='none')

        for j in range(number_of_molecules // 4):
            N_H1_x, N_H1_y, N_H1_z = [N[j][1], H1[j][1]], [N[j][2], H1[j][2]], [N[j][3], H1[j][3]]
            N_H2_x, N_H2_y, N_H2_z = [N[j][1], H2[j][1]], [N[j][2], H2[j][2]], [N[j][3], H2[j][3]]
            N_H3_x, N_H3_y, N_H3_z = [N[j][1], H3[j][1]], [N[j][2], H3[j][2]], [N[j][3], H3[j][3]]

            mlab.plot3d(N_H1_x, N_H1_y, N_H1_z, tube_radius=0.2, color=(1, 1, 1))
            mlab.plot3d(N_H2_x, N_H2_y, N_H2_z, tube_radius=0.2, color=(1, 1, 1))
            mlab.plot3d(N_H3_x, N_H3_y, N_H3_z, tube_radius=0.2, color=(1, 1, 1))
        if save_frames:
            mlab.savefig(f"./figures/animate_{i}.png")
        yield
