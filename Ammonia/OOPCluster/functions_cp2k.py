import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import datetime
from data_set_key import data_set


def get_value_from_key(cluster_id: int) -> tuple[int, int]:
    # TODO documentation
    """

    :type cluster_id: For example: 101 = 10 molecules of ammonia and
     cluster 1.
    """

    data = data_set.get(cluster_id)
    ammonia_number = data[0]
    number_of_cluster = data[1]
    return ammonia_number, number_of_cluster


def average_used_time(cluster_id: int):
    # TODO documentation
    """

    :param cluster_id: For example: 101 = 10 molecules of ammonia and
     cluster 1.
    """

    ammonia_number, number_of_cluster = get_value_from_key(cluster_id)
    filename = "./ammonia-{0}-{1}/small-clusters-1.csv". \
        format(ammonia_number, number_of_cluster)

    data = np.loadtxt(filename, skiprows=1, unpack=True, delimiter=";")
    used_time = data[6]
    average_time = round(np.average(used_time), 2)

    print(f"Average time per step is {average_time} s")


def graph_ener(cluster_id: int,
               data: str):
    # TODO dictionary
    # TODO documentation
    """
    Makes plot from ener files.
    :param cluster_id: For example: 101 = 10 molecules of ammonia and
     cluster 1.
    :param data: "Pot.[a.u.]" (Potential energy),
    "Kin.[a.u.]" (Kinetic energy),
    "Cons Qty[a.u.]" (Constant energy),
    "Temp[K]" (Temperature),
    "UsedTime[s]" (Used time per step)
    """

    ammonia_number, number_of_cluster = get_value_from_key(cluster_id)

    print("{0} Generated in:\n\t{1}"
          .format(data, datetime.datetime.now().strftime("%c")))
    filename = "./ammonia-{0}-{1}/small-clusters-1.csv". \
        format(ammonia_number, number_of_cluster)
    energy = np.loadtxt(filename, skiprows=1, unpack=True, delimiter=";")
    step, time, kin, temp, pot, cons, used_time = energy

    time_fs = "Time [fs]"
    n_step = "Number of step"
    data_dict = {"Kin.[a.u.]": kin,
                 "Temp[K]": temp,
                 "Pot.[a.u.]": pot,
                 "Cons Qty[a.u.]": cons,
                 "UsedTime[s]": used_time}

    if data == "Kin.[a.u.]":
        y_data = data_dict.get(data)
        plt.figure(figsize=[7.5, 3.5])
        plt.plot(time, y_data, color='seagreen')
        plt.xlabel(time_fs, fontsize=13)
        plt.ylabel("Cons Qty[a.u.]", fontsize=13)
        plt.title("Kinetic energy", fontweight="bold", fontsize=15)
        plt.yticks(fontsize=12)
        plt.xticks(fontsize=12, rotation=45)
        plt.grid()
        plt.plot()

    elif data == "Temp[K]":
        y_data = data_dict.get(data)
        plt.figure(figsize=[7.5, 3.5])
        plt.plot(time, y_data, color='red')
        plt.xlabel(time_fs, fontsize=13)
        plt.ylabel("Temperature [K]", fontsize=13)
        plt.title("Temperature", fontweight="bold", fontsize=15)
        plt.yticks(fontsize=12)
        plt.xticks(fontsize=12, rotation=45)
        plt.grid()
        plt.plot()

    elif data == "Pot.[a.u.]":
        y_data = data_dict.get(data)
        plt.figure(figsize=[7.5, 3.5])
        plt.plot(time, y_data, color='orangered')
        plt.xlabel(time_fs, fontsize=13)
        plt.ylabel("Pot.[a.u.]", fontsize=13)
        plt.title("Potential energy", fontweight="bold", fontsize=16)
        plt.yticks(fontsize=12)
        plt.xticks(fontsize=12, rotation=45)
        plt.grid()
        plt.plot()

    elif data == "Cons Qty[a.u.]":
        y_data = data_dict.get(data)
        plt.figure(figsize=[7.5, 3.5])
        plt.plot(time, y_data, color='forestgreen')
        plt.xlabel(time_fs, fontsize=13)
        plt.ylabel("Cons Qty[a.u.]", fontsize=13)
        plt.title("Constant energy", fontweight="bold", fontsize=16)
        plt.yticks(fontsize=12)
        plt.xticks(fontsize=12, rotation=45)
        plt.grid()
        plt.plot()

    elif data == "UsedTime[s]":
        y_data = data_dict.get(data)
        plt.figure(figsize=[7.5, 3.5])
        plt.plot(step, y_data, color='indigo')
        plt.xlabel(n_step, fontsize=13)
        plt.ylabel("Used time [s]", fontsize=13)
        plt.title("Used time for each step", fontweight="bold", fontsize=15)
        plt.yticks(fontsize=12)
        plt.xticks(fontsize=12, rotation=45)
        plt.grid()
        plt.plot()

    else:
        print("Wrong typed data arguments!")


def four_plots_in_one(cluster_id: int):
    # TODO dictionary
    """
    :param cluster_id: For example: 101 = 10 molecules of ammonia and
     cluster 1.

    """

    average_used_time(cluster_id)
    ammonia_number, number_of_cluster = get_value_from_key(cluster_id)
    print("Generated in:\n\t{0}"
          .format(datetime.datetime.now().strftime("%c")))
    filename = "./ammonia-{0}-{1}/small-clusters-1.csv". \
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


def interactive_plot(cluster_id: int):
    # TODO documentation
    """

    :param cluster_id: For example: 101 = 10 molecules of ammonia and
     cluster 1.
    """

    ammonia_number, number_of_cluster = get_value_from_key(cluster_id)

    print("Generated in:\n\t{0}"
          .format(datetime.datetime.now().strftime("%c")))
    filename = "./ammonia-{0}-{1}/small-clusters-1.csv". \
        format(ammonia_number, number_of_cluster)
    energy = np.loadtxt(filename, skiprows=1, unpack=True, delimiter=";")
    step, time, kin, temp, pot, cons, used_time = energy

    x = step
    y = used_time

    fig = px.line(x=x, y=y, labels={'x': 'Steps', 'y': 'Time [s]'},
                  title="Time per step", template="plotly_white")
    fig.layout.xaxis.gridcolor = "black"
    fig.layout.yaxis.gridcolor = "black"
    fig.layout.width = 850
    fig.layout.height = 450
    fig.show()


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
    with open('GLOBAL.txt', 'r', encoding='utf-8') as GLOBAL:
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
    with open('EXT_RESTART.txt', 'r', encoding='utf-8') as EXT_RESTART:
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
    with open('FORCE_EVAL.txt', 'r', encoding='utf-8') as FORCE_EVAL:
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
    with open('MOTION.txt', 'r', encoding='utf-8') as MOTION:
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


def make_bash(job_name: str,
              new_sh: str,
              finish=datetime.date.today().strftime("%d/%m/%Y")):
    """
    Makes submit files for jobs.
    :param finish: Time to finish restarts (for example "07/05/2022"),
    default is date now.
    :param new_sh: Name os output SH file.
    :type job_name: Name of job.
    """

    with open('CP2K_NEW_REST.txt', 'r', encoding='utf-8') as cp2k:
        lines = cp2k.readlines()

    lines[4] = '#SBATCH --job-name="{0}"\n' \
        .format(job_name)
    lines[38] = 'finish="{0}"\n' \
        .format(finish)
    lines[41] = 'if [ "$dt" != "$finish" ]; then\n'
    lines[42] = '   sbatch -p cpu,scpu,bfill cp2k_new_rest.sh\n'
    lines[43] = 'fi\n'

    with open(new_sh, "w", encoding='utf-8') as cp2k_new:
        for line in lines:
            cp2k_new.write(line)


def control_jobs(cluster_id: int,
                 output: str):
    """
    Checks jobs to see if they have finished correctly.
    :param cluster_id: For example: 101 = 10 molecules of ammonia and
     cluster 1.
    :type output: Name of output file.
    """

    ammonia_number, number_of_cluster = get_value_from_key(cluster_id)

    filename = "../ammonia-{0}-{1}/cluster_hybrid.log". \
        format(ammonia_number, number_of_cluster)
    file = "CP2K_error_test.txt"
    done = "CP2K_done_test.txt"

    with open(filename, 'r', encoding='utf-8') as logfile:
        lines_1 = logfile.readlines()

    with open(done, 'r', encoding='utf-8') as done:
        lines_2 = done.readlines()

    with open(file, 'r', encoding='utf-8') as error:
        lines_3 = error.readlines()

    with open(output, "a", encoding='utf-8') as output:
        date = datetime.datetime.now()
        print(date.strftime("%c"), file=output)
        a = set(lines_2[2]).issubset(set(lines_1[-4]))
        if a:
            print("{0}-{1}: CP2K done".
                  format(ammonia_number, number_of_cluster), file=output)

        else:
            b = set(lines_3[0:9]).issubset(set(lines_1[-26:-16]))
            # TODO vytahnout posledni radky a zjistit, jestli tam je error
            if b:
                print("{0}-{1}: Cholesky decompose failed".
                      format(ammonia_number, number_of_cluster), file=output)
            else:
                print("{0}-{1}: New Error".
                      format(ammonia_number, number_of_cluster), file=output)


def ener_to_csv(cluster_id: int):
    """
    Converts ENER files to CSV files.
    :param cluster_id: For example: 101 = 10 molecules of ammonia and
    cluster 1.
    """

    ammonia_number, number_of_cluster = get_value_from_key(cluster_id)

    filename = "../ammonia-{0}-{1}/small-clusters.pdb-1.ener". \
        format(ammonia_number, number_of_cluster)
    output = "../ammonia-{0}-{1}/small-clusters-1.csv". \
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


def rdf(cluster_id: int):
    """

    :param cluster_id:
    :return:
    """

    ammonia_number, number_of_cluster = get_value_from_key(cluster_id)
    filename = "./ammonia-{0}-{1}/RDF_data_multitasking.csv".\
        format(ammonia_number, number_of_cluster)

    rNN, g_rNN, rNH, g_rNH, rHH, g_rHH = np.loadtxt(filename, skiprows=1, delimiter=';', unpack=True)

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


