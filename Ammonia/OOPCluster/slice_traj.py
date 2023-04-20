def slice_traj(trajectory, n_frames, dir_output):


    """
    slices and saves the given trajectory into given number of frames

    trajectory    already MDTraj object with all the topologies and bla bla bla
    (path, fp_traj,fp_pdb, traj = md.load(fp_traj, top=fp_pdb))
    fp_pdb        the topology file in .pdb format
    n_frames      number of frames you want to generate
    dir_output    directory, in which will be createdd x=n_frames directories with output files
    """


    traj = trajectory

    #     print('Initial trajectory: ', traj)
    n_frames_all = traj.n_frames
    #     print('Number of frames = ', n_frames_all)
    #     print('Number of frames wanted = ', n_frames)
    step = math.floor(n_frames_all/n_frames)
    #     print('Step = ', step)
    traj_sliced = traj[::step]    ###taking each x-th frame from trajectory
    #     print('Sliced trajectory: ', traj_sliced)
    for x in range(0, n_frames):
        one_frame = traj_sliced.slice(x)
        #         print(x + 1, one_frame)
        directory = str('Frame_' + str(x + 1))
        fp_output = str(dir_output + directory + '/conf.xyz')


        if Path(dir_output + directory).exists():
            if Path(fp_output).exists():
                os.remove(fp_output)
        else:
            os.mkdir(dir_output + directory)
        #         print(fp_output)
        one_frame.save_xyz(fp_output)