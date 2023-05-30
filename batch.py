import os
import argparse
import run

fcwd = lambda x: os.path.join(os.getcwd(), x)
INPFACES = "inputface"
INPVIDS = "inputvid"
OUTDIR = "output"
OUTFMT = "output{}.mp4"

parser = argparse.ArgumentParser()
arser.add_argument('-f', '--face', help='use this face', dest='source', default = "input_face")
parser.add_argument('-t', '--target', help='replace this face', dest='target', default = "input_vid")
parser.add_argument('-o', '--output', help='save outputs to this folder', dest='output', default = "output")
parser.add_argument('-m', '--output', help='output format', dest='outfile', default = "output{}.mp4")
parser.add_argument('--keep-fps', help='maintain original fps', dest='keep_fps', action='store_true', default=False)
parser.add_argument('--gpu', help='use gpu', dest='gpu', action='store_true', default=False)
parser.add_argument('--keep-frames', help='keep frames directory', dest='keep_frames', action='store_true', default=False)

args = dict()
for name, value in vars(parser.parse_args()).items():
    args[name] = value

if __name__ == "__main__":
    cnt = 0
    for flface in os.listdir(args["source"]):
        for flvid in os.listdir(args["target"]):
            if flface.endswith(".png") and flvid.endswith(".mp4"):
                ptface = os.path.join(args["source"],flface)
                # ptface = fcwd(ptface)
                ptvid = os.path.join(args["target"],flvid)
                # ptvid = fcwd(ptvid)
                outpt = os.path.join(args["output"],args["outfile"].format(cnt))
                # outpt = fcwd(outpt)
                args["source_img"] = ptface
                args ["target_path"] = ptvid
                args["output_file"] = outpt
                run.start_batch(args)
