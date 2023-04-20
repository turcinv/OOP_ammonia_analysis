from functions_cp2k import get_value_from_key
from grid_xyz import generate_xyz_input

number_of_ammonia = [2, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8, 8]

for _, id in enumerate([21, 22, 34, 41, 42, 44, 51, 54, 62, 71, 81, 82, 83]):
    ammonia_number, number_of_cluster = get_value_from_key(id)

    generate_xyz_input(30, "./ammonia-{0}-{1}/ammonia-{0}-{1}.xyz".format(ammonia_number, number_of_cluster),
                       "./ammonia-{0}-{1}/small-cluster.xyz".format(ammonia_number, number_of_cluster),
                       number_of_ammonia[_])
    print("./ammonia-{0}-{1}/ammonia-{0}-{1}.xyz".format(ammonia_number, number_of_cluster))
