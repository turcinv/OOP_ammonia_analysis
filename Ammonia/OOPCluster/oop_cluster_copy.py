import datetime
import matplotlib.pyplot as plt
from data_set_key import data_set
import numpy as np
# plotly pro interaktivni
# mayavi pro vizualizaci molekul (cube files)


class AmmoniaCluster(object):

    def __init__(self,
                 cluster_id="0",
                 folder="None",
                 xyz_file=None):
        
        self.cluster_id = cluster_id
        self.folder = folder
        self.xyz_file = xyz_file
    
    def __str__(self):
        number_of_ammonia, _, _, = self.get_value_from_key()
        return "ID of cluster: {0.cluster_id}, Number of ammonia: {1}, Folder: {0.folder}". \
            format(self, number_of_ammonia)

    # TODO: Parameters for this method
    def get_properties(self):
        return "Properties computing of {0.cluster_id} system from TXT file or DB".format(self)

    # TODO: make subclasses, for example Test_01, ...??????
    # TODO: Make methods
    def get_value_from_key(self):
        # TODO documentation
        data = data_set.get(self.cluster_id)
        ammonia_number = data[0]
        number_of_ammonia = int(ammonia_number)
        number_of_cluster = data[1]
        return number_of_ammonia, ammonia_number, number_of_cluster

    # "./inp_data/CP2K_NEW_REST.txt"
    def make_bash(self):
        # TODO documentation
        return "This method makes SH input for {0.cluster_id}". \
            format(self)

    def plot_rdf(self):
        # TODO documentation
        _, ammonia_number, number_of_cluster = self.get_value_from_key()
        # TODO filename
        # filename = "./ammonia-{0}-{1}/RDF_data_multitasking.csv".\
        # ?????
        filename = "./ammonia-{0}-{1}/RDF_data_multitasking.csv".\
            format(ammonia_number, number_of_cluster)

        rNN, g_rNN, rNH, g_rNH, rHH, g_rHH = np.loadtxt(filename,
                                                        skiprows=1,
                                                        delimiter=';',
                                                        unpack=True)

        plt.figure(figsize=(15, 7))
        plt.plot(rNN, g_rNN, color='indigo', lw=3, label='N-N')
        plt.plot(rHH, g_rHH, color='gold', lw=3, label='H-H')
        plt.plot(rNH, g_rNH, color='crimson', lw=3, label='N-H')
        plt.legend()
        plt.grid()
        plt.xlabel('distance [nm]', fontsize=13)
        plt.ylabel('g(r)', fontsize=13)
        plt.xlim([0, 1])
        plt.xticks(np.arange(0, 1, 0.05), rotation=45, fontsize=12)
        plt.yticks(fontsize=12)
        plt.title("Radial distribution function of ammonia", fontweight="bold", fontsize=15)
        plt.show()

    def control_logs(self):
        # TODO documentation
        return "This method control LOG file of {0.cluster_id}". \
            format(self)

    def ener_to_csv(self):
        # TODO documentation
        _, ammonia_number, number_of_cluster = self.get_value_from_key()

        filename = "./ammonia-{0}-{1}/small-clusters-1.ener". \
            format(ammonia_number, number_of_cluster)
        output = "./ammonia-{0}-{1}/small-clusters-1.csv". \
            format(ammonia_number, number_of_cluster)

        inputs = np.loadtxt(filename, skiprows=1, unpack=True)

        step, time_fs, kin, temp, pot, cons, used_time = inputs

        with open(output, "w", encoding="utf-8") as output:
            print("Step Nr.", "Time[fs]", "Kin.[a.u.]", "Temp[K]", "Pot.[a.u.]",
                  "Cons Qty[a.u.]", "UsedTime[s]", sep=";", file=output)
            for i in range(len(inputs[0])):
                print(step[i], time_fs[i], kin[i],
                      temp[i], pot[i], cons[i], used_time[i],
                      sep=";", file=output)

    def average_used_time(self):
        # TODO documentation
        _, ammonia_number, number_of_cluster = self.get_value_from_key()
        # TODO filename
        filename = "./ammonia-{0}-{1}/small-clusters-1.csv".\
            format(ammonia_number, number_of_cluster)

        data = np.loadtxt(filename, skiprows=1, unpack=True, delimiter=";")
        used_time = data[6]
        average_time = round(np.average(used_time), 2)

        print(f"Average time per step is {average_time} s")

    def graph_ener(self):
        # TODO documentation
        return "This method makes interactive plot for {0.cluster_id}". \
            format(self)

    def four_plots_in_one(self):
        # TODO documentation
        # average_used_time(cluster_id)
        _, ammonia_number, number_of_cluster = self.get_value_from_key()
        print("Generated in:\n\t{0}"
              .format(datetime.datetime.now().strftime("%c")))
        # TODO filename
        filename = "./ammonia-{0}-{1}/small-clusters-1.csv".\
            format(ammonia_number, number_of_cluster)
        energy = np.loadtxt(filename, skiprows=1, unpack=True, delimiter=";")
        step, time, kin, temp, pot, cons, used_time = energy

        plt.figure(figsize=(25, 12.5))

        plt.subplot(221)
        plt.plot(time, kin, linewidth=1, color='darkorchid')
        plt.title("Kinetic energy", fontweight="bold", fontsize=16)
        plt.xlabel("Time [fs]", fontsize=14)
        plt.ylabel("Kin.[a.u.]", fontsize=14)
        plt.minorticks_on()
        plt.grid(True)

        plt.subplot(222)
        plt.plot(time, pot, linewidth=1, color='orangered')
        plt.title("Potential energy", fontweight="bold", fontsize=16)
        plt.xlabel("Time [fs]", fontsize=14)
        plt.ylabel("Pot.[a.u.]", fontsize=14)
        plt.minorticks_on()
        plt.grid(True)

        plt.subplot(223)
        plt.plot(time, temp, linewidth=1, color='red')
        plt.title("Temperature", fontweight="bold", fontsize=16)
        plt.xlabel("Time [fs]", fontsize=14)
        plt.ylabel("Temperature [K]", fontsize=14)
        plt.minorticks_on()
        plt.grid(True)

        plt.subplot(224)
        plt.plot(time, cons, linewidth=1, color='springgreen')
        plt.title("Constant energy", fontweight="bold", fontsize=16)
        plt.xlabel("Time [fs]", fontsize=14)
        plt.ylabel("Cons Qty[a.u.]", fontsize=14)
        plt.minorticks_on()
        plt.grid(True)
        plt.show()

    # TODO: OOP parameters for this method - not static
    @staticmethod
    def cp2k_input(project_name: str,
                   box_size: str,
                   input_name: str,
                   temperature: float,
                   cubes_list: int,
                   total_atoms: int,
                   charge: int,
                   multiplicity: int,
                   walltime: int,
                   periodic='NONE',
                   restart_input=True):
        """
        Makes input for CP2K computing.

        :param walltime: Time for computing.
        :param total_atoms: Total amount of atoms.
        :param restart_input: Default is True.
        True means that the function generates a restart input.
        :type multiplicity: Multiplicity of system.
        :type charge: Total charge of system.
        :type periodic: Default is NONE. That means non-periodic conditions.
        :type cubes_list: Number of orbital/orbitals for generating CUBES files.
        :type temperature: Temperature in K.
        :type input_name: Name of generated input file.
        :type box_size: Size of cube box in Angstrom with two decimal places.
        :type project_name: Name of input project.
        """

        box = '{0} {0} {0}' \
            .format(box_size)
        fixed_atoms = '{0}..{1}' \
            .format(cubes_list, (total_atoms + 1))

        # Making input *************************************************************
        # 1; 10
        # GLOBAL *******************************************************************
        with open('./inp_data/GLOBAL.txt', 'r', encoding='utf-8') as GLOBAL:
            lines = GLOBAL.readlines()

        lines[1] = '  PROJECT {}\n' \
            .format(project_name)
        lines[10] = '  WALLTIME {}\n' \
            .format(walltime)

        with open(input_name, 'w') as input_file:
            for line in lines:
                print(line, file=input_file, end='')
            print('\n', file=input_file)
        # **************************************************************************
        # 1;
        # EXT_RESTART **************************************************************
        with open('./inp_data/EXT_RESTART.txt', 'r', encoding='utf-8') as EXT_RESTART:
            lines = EXT_RESTART.readlines()
            if restart_input:
                lines[0] = '&EXT_RESTART\n'
                lines[1] = '  EXTERNAL_FILE {}-1.restart\n' \
                    .format(project_name)
                lines[2] = '&END EXT_RESTART\n'
            else:
                lines[1] = '#  EXTERNAL_FILE {}-1.restart\n' \
                    .format(project_name)

        with open(input_name, 'a') as input_file:
            for line in lines:
                print(line, file=input_file, end='')
            print('\n', file=input_file)
        # **************************************************************************
        # 2; 3; 8; 112; 149; 156; 157;
        # FORCE_EVAL ***************************************************************
        with open('./inp_data/FORCE_EVAL.txt', 'r', encoding='utf-8') as FORCE_EVAL:
            lines = FORCE_EVAL.readlines()
            lines[2] = '    CHARGE {}\n' \
                .format(charge)
            lines[3] = '    MULTIPLICITY {}\n' \
                .format(multiplicity)
            lines[112] = '                CUBES_LIST {}\n' \
                .format(cubes_list)
            lines[149] = '      COORD_FILE_NAME ./{}.xyz\n' \
                .format(project_name)
            lines[156] = '      ABC [angstrom] {}\n' \
                .format(box)
            lines[157] = '      PERIODIC {}\n' \
                .format(periodic)

            if restart_input:
                lines[8] = '    WFN_RESTART_FILE_NAME {}-RESTART.wfn\n' \
                    .format(project_name)

            else:
                lines[8] = '#    WFN_RESTART_FILE_NAME {}-RESTART.wfn\n' \
                    .format(project_name)

            with open(input_name, 'a') as input_file:
                for line in lines:
                    print(line, file=input_file, end='')
                print('', file=input_file, end='')
        # **************************************************************************
        # 5; 19;
        # MOTION *******************************************************************
        with open('./inp_data/MOTION.txt', 'r', encoding='utf-8') as MOTION:
            lines = MOTION.readlines()
            lines[5] = '    TEMPERATURE {}\n' \
                .format(temperature)
            lines[19] = '        LIST {}\n' \
                .format(fixed_atoms)

        with open(input_name, 'a') as input_file:
            for line in lines:
                print(line, file=input_file, end='')
            print('', file=input_file)
        # **************************************************************************

    # TODO: Parameters for this method
    def make_grid(self):
        # TODO documentation
        return "This method makes XYZ file with ghost atoms for {0.cluster_id}". \
            format(self)

    # TODO: Parameters for this method
    def slice_traj(self):
        # TODO documentation
        return "Slicing {0.cluster_id}".format(self)

    # TODO: Parameters for this method
    def show_cube(self):
        # TODO documentation
        return "This showing cube file for {0.cluster_id}".format(self)

    
