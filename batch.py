import os
import argparse
import run

fcwd = lambda x: os.path.join(os.getcwd(), x)

# Might instead grab the one from run and add to it.
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--face', help='use this face', dest='source', default = "input_face")
parser.add_argument('-t', '--target', help='replace this face', dest='target', default = "input_vid")
parser.add_argument('-o', '--output', help='save outputs to this folder', dest='output', default = "output")
parser.add_argument('-m', '--output', help='output format', dest='outfile', default = "output{}.mp4")
parser.add_argument('--keep-fps', help='maintain original fps', dest='keep_fps', action='store_true', default=False)
parser.add_argument('--gpu', help='use gpu', dest='gpu', action='store_true', default=False)
parser.add_argument('--keep-frames', help='keep frames directory', dest='keep_frames', action='store_true', default=False)

args = dict()
for name, value in vars(parser.parse_args()).items():
    args[name] = value

ARGSEXC = ["input_face","input_vid","output"]
VALID_SOURCE = [".png", ".jpg", ".jpeg"]
VALID_TARGET = [".mp4"]
    
if __name__ == "__main__":
    cnt = 0
    drun = {k:v for k,v in args.items() if k not in ARGSEXC}
    drun["cli_mode"] = True
    for flface in os.listdir(args["source"]):
        for flvid in os.listdir(args["target"]):
            faceext = os.path.splitext(flface)
            vidext = os.path.splitext(flvid)
            if faceext in VALID_SOURCE and vidext in VALID_TARGET:
                cnt = cnt + 1
                ptface = os.path.join(args["source"],flface)
                # ptface = fcwd(ptface)
                ptvid = os.path.join(args["target"],flvid)
                # ptvid = fcwd(ptvid)
                outpt = os.path.join(args["output"],args["outfile"].format(cnt))
                # outpt = fcwd(outpt)
                drun["source_img"] = ptface
                drun["target_path"] = ptvid
                drun["output_file"] = outpt
                run.start(drun)
