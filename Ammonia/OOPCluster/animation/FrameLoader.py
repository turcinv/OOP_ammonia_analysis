from multiprocessing import Manager, Pool


def frame_loader(frame, read_pickle):
    with Manager() as manager:
        dictionary = manager.dict()
        args = [(i, dictionary) for i in frame]
        with Pool(4) as p:
            p.map(read_pickle, args)
        return dict(dictionary)
