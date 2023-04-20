import datetime
import matplotlib.pyplot as plt
from data_set_key import data_set
import numpy as np


class AmmoniaCluster(object):

    def __init__(self,
                 cluster_id="0",
                 number_of_ammonia="0",
                 folder="None",
                 xyz_file=None):

        self.cluster_id = cluster_id
        self.number_of_ammonia = number_of_ammonia
        self.folder = folder
        self.xyz_file = xyz_file

    # TODO: make subclasses, for example Test_01, ...??????
    # TODO: Make methods
    def get_value_from_key(self):
        # TODO documentation
        data = data_set.get(self.cluster_id)
        ammonia_number = data[0]
        number_of_cluster = data[1]
        return ammonia_number, number_of_cluster

    def make_bash(self):
        return "This method makes SH input of {0.cluster_id}".\
            format(self)

    def generate_rdf(self):
        ammonia_number, number_of_cluster = self.get_value_from_key()
        # TODO filename
        filename = "ammonia-02-1/RDF_data_multitasking.csv"
        # format(ammonia_number, number_of_cluster)

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
        return "This method control LOG file of {0.cluster_id}".\
            format(self)

    def ener_to_csv(self):
        return "This method makes CSV file from ENER file of {0.cluster_id}".\
            format(self)

    def average_used_time(self):
        ammonia_number, number_of_cluster = self.get_value_from_key()
        # TODO filename
        filename = "./small-clusters-1.csv"
        # format(ammonia_number, number_of_cluster)

        data = np.loadtxt(filename, skiprows=1, unpack=True, delimiter=";")
        used_time = data[6]
        average_time = round(np.average(used_time), 2)

        print(f"Average time per step is {average_time} s")

    def graph_ener(self):
        return "This method makes interactive plot of {0.cluster_id}". \
            format(self)

    def four_plots_in_one(self):
        # average_used_time(cluster_id)
        ammonia_number, number_of_cluster = self.get_value_from_key()
        print("Generated in:\n\t{0}"
              .format(datetime.datetime.now().strftime("%c")))
        # TODO filename
        filename = "./small-clusters-1.csv"
        # format(ammonia_number, number_of_cluster)
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

    # TODO: Parameters for this method
    def cp2k_input(self):
        return "This method makes INP file of {0.cluster_id}". \
            format(self)

    # TODO: Parameters for this method
    def make_grid(self):
        return "This method makes XYZ file with ghost atoms of {0.cluster_id}". \
            format(self)

    def get_properties(self):
        return "Properties computing ammonia {self.cluster_id} from TXT file"

    def __str__(self):
        return "ID of cluster: {0.cluster_id}, Number of ammonia: {0.number_of_ammonia}, Folder: {0.folder}".\
            format(self)
