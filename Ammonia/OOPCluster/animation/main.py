from multiprocessing import Pool
import numpy as np
import mayavi.mlab as mlab
import argparse
from CubeToPickle import cube_to_pickle
from Update import update
from ReadPickle import read_pickle
from MakeVideo import make_video
from FrameLoader import frame_loader

parser = argparse.ArgumentParser()
parser.add_argument("--number_of_molecules", default=40, type=int, help="Number of molecules in system.")
parser.add_argument("--number_of_cubes", default=207, type=int, help="Amount of cube files.")
parser.add_argument("--pickling", default=False, type=bool, help="Pickling of cube files.")
parser.add_argument("--animate", default=True, type=bool, help="Show animation.")
parser.add_argument("--save_images", default=False, type=bool, help="Saving images of cube files.")
parser.add_argument("--make_video", default=False, type=bool, help="Make video from saved files?")


def main(args):
    frame = list(np.arange(0, args.number_of_cubes * 10, 10))
    ############################################################################
    # Cube to pickle
    if args.pickling:
        with Pool(4) as p:
            p.map(cube_to_pickle, frame)

    ############################################################################
    # Animation
    if args.animate:
        cubes = frame_loader(frame, read_pickle)
        animate = update(dictionary=cubes,
                         number_of_molecules=args.number_of_molecules,
                         frames=args.number_of_cubes,
                         save_frames=args.save_images)
        mlab.show()
    ############################################################################
    # Mke video
    if args.make_video:
        make_video("figures", fps=20, name="test.mp4")


if __name__ == '__main__':
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
