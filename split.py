import os, sys

def ape_to_flac(ape, flac):
    os.system("ffmpeg -i {} {}".format(ape, flac))

def gbk_to_utf8(cue):
    cue_tmp = cue + ".tmp"
    os.rename(cue, cue_tmp)
    os.system("iconv -f gbk -t utf8 {} > {}".format(cue_tmp, cue))
    os.remove(cue_tmp)

def split(flac, cue, output, format="flac"):
    if format == "mp3":
        os.system("shntool split -t \"%n.%p.%t\" -f {} -o \"cust ext=mp3 lame -b 320 - %f\" {} -d {}".format(cue, flac, output))
    else:
        os.system("shntool split -t \"%n.%p.%t\" -f {} -o flac {} -d {}".format(cue, flac, output))

if __name__=="__main__":
    ape = sys.argv[1]
    cue = sys.argv[2]
    flac = sys.argv[3]
    output = sys.argv[4]
    ape_to_flac(ape, flac)
    gbk_to_utf8(cue)
    split(flac, cue, output)
