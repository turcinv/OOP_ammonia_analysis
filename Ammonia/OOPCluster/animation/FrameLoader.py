from multiprocessing import Manager, Pool


def frame_loader(frame, read_pickle):
    """
    Loads data from pickle file
    :param frame: number of frame
    :param read_pickle: function to read pickle file
    :return: dictionary with pickle data
    """

    # multitask processing
    with Manager() as manager:
        dictionary = manager.dict()
        args = [(i, dictionary) for i in frame]
        with Pool(4) as p:
            p.map(read_pickle, args)
        return dict(dictionary)
