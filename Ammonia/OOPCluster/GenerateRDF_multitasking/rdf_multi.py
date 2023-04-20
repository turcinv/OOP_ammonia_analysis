from multiprocessing import Pool
from functions_cp2k import get_value_from_key
import mdtraj as md
import numpy as np
import datetime


def rdf(cluster_id: int):
    ammonia_number, number_of_cluster = get_value_from_key(cluster_id)
    fp_traj = './../ammonia-{0}-{1}/small-clusters.pdb-pos-1.xyz'.\
        format(ammonia_number, number_of_cluster)
    fp_topol = './../ammonia-{0}-{1}/small-clusters.pdb.pdb'.\
        format(ammonia_number, number_of_cluster)
    cube_size = 300
    angle = 90
    traj = md.load_xyz(fp_traj, top=md.load(fp_topol))
    topol = traj.topology
    traj.unitcell_lengths = np.ones((len(traj), 3))*cube_size
    traj.unitcell_angles = np.ones((len(traj), 3))*angle
    topol.unitcell_lengths = [cube_size, cube_size, cube_size]
    topol.unitcell_angles = [angle, angle, angle]
    Ns = topol.select('name N')
    Hs = topol.select('name H')

    pairs_NN = topol.select_pairs(Ns, Ns)
    rNN, g_rNN = md.compute_rdf(traj, pairs_NN, r_range=(0.0, 1), periodic=False)

    pairsHH = topol.select_pairs(Hs, Hs)
    pairs_HH = []
    for i in range(len(pairsHH)):
        if 0 < pairsHH[i][1] - pairsHH[i][0] < 4:
            pass

        else:
            x = pairsHH[i]
            pairs_HH.append(x)
    rHH, g_rHH = md.compute_rdf(traj, pairs_HH, r_range=(0.0, 1), periodic=False)

    pairsNH = topol.select_pairs(Ns, Hs)
    pairs_NH = []
    for i in range(len(pairsNH)):
        if 0 < pairsNH[i][1] - pairsNH[i][0] < 4:
            pass

        else:
            x = pairsNH[i]
            pairs_NH.append(x)
    rNH, g_rNH = md.compute_rdf(traj, pairs_NH, r_range=(0.0, 1), periodic=False)

    RDF_file = './../ammonia-{0}-{1}/RDF_data_multitasking.csv'.\
        format(ammonia_number, number_of_cluster)

    with open(RDF_file, "w") as RDF_write:
        print("rNN(r)",
              "g_rNN[nm]",
              "rNH(r)",
              "g_rNH[nm]",
              "rHH(r)",
              "g_rHH[nm]",
              file=RDF_write,
              sep=';', end=';\n')

        for index, step in enumerate(rNN):
            print(rNN[index],
                  g_rNN[index],
                  rNH[index],
                  g_rNH[index],
                  rHH[index],
                  g_rHH[index],
                  file=RDF_write,
                  sep=';', end='\n')


if __name__ == '__main__':
    # Pool = počet procesů zároveň
    start_time = datetime.datetime.now()
    with Pool(4) as p:
        p.map(rdf, [101, 102, 103,
                    121, 122, 123,
                    141, 142, 143,
                    161, 162, 163,
                    201, 202, 203,
                    241, 242, 243,
                    281, 282, 283,
                    321, 322, 323,
                    361, 362, 363,
                    401, 402, 403,
                    481, 482, 483])

    end_time = datetime.datetime.now()
    print("Start time: {}".format(start_time.strftime("%c")))
    print("End time: {}".format(end_time.strftime("%c")))

# 4 process
# Start time: Sat May 28 13:56:47 2022
# End time: Sat May 28 14:02:44 2022

# Start time: Sat May 28 15:04:08 2022
# End time: Sat May 28 15:12:10 2022

# Start time: Sat May 28 15:20:45 2022
# End time: Sat May 28 15:28:22 2022


# 6 process
# Start time: Sat May 28 15:13:46 2022
# End time: Sat May 28 15:20:08 2022
