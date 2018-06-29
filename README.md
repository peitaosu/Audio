Audio
=====

Audio tools.

## APE to FLAC

### Requirements
* ffmpeg (format conversion: ape -> flac)
* iconv (cue codepage conversion: gbk -> utf-8)
* shntool (flac split)

### Usage
```
python split <in_dir> <out_dir>
```

### Input & Output
In input directory, there should be many couple of .ape & .cue files with same name. `split.py` will search input directory, get all .ape & .cue files then convert & split them with single files and save to output directory.
