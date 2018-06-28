import os, sys

def ape_to_flac(ape, flac):
    os.system("ffmpeg -i {} {}".format(ape, flac))

def gbk_to_utf8(cue):
    cue_bak = cue + ".bak"
    os.rename(cue, cue_bak)
    os.system("iconv -f gbk -t utf8 {} > {}".format(cue_bak, cue))

def split(flac, cue, output, format="flac"):
    if not os.path.isdir(output):
        os.makedirs(output)
    if format == "mp3":
        os.system("shntool split -t \"%n.%p.%t\" -f {} -o \"cust ext=mp3 lame -b 320 - %f\" -d {} {}".format(cue, output, flac))
    else:
        os.system("shntool split -t \"%n.%p.%t\" -f {} -o flac  -d {} {}".format(cue, output, flac))

if __name__=="__main__":
    if len(sys.argv) < 3:
        print "python split.py <in_dir> <out_dir>"
        sys.exit()
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    cuefiles = [os.path.join(in_dir, f) for f in os.listdir(in_dir) if os.path.isfile(os.path.join(in_dir, f)) and f.endswith(".cue")]
    for cue in cuefiles:
        ape = cue.replace(".cue", ".ape")
        flac = cue.replace(".cue", ".flac")
        output = os.path.join(out_dir, os.path.basename(cue).replace(".cue", ""))
        ape_to_flac(ape, flac)
        gbk_to_utf8(cue)
        split(flac, cue, output)
