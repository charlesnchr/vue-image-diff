import glob
import shutil
import os
from pathlib import Path
from distutils.dir_util import copy_tree
import sys

outdir = sys.argv[1]

# os.makedirs(outdir,exist_ok=True)

def get_dict(idx,filepath,name):
    return '''
    {
        "id": "%d",
        "name": "%s",
        "params": {"dimension": "512x512"},
        "url": "%s",
        "ext": "png"
    }''' % (idx,name,filepath)


# main loop
imgjson = open('%s/img.json' % (outdir),'w')
imgjson.write('[\n')

for iidx,img in enumerate(sys.argv[2:]):
    if iidx > 0: imgjson.write(',')
    newname = '%d-%s' % (iidx,os.path.basename(img))
    print(img, 'saving to %s/%s' % (outdir,newname))
    shutil.copy(img,'%s/%s' % (outdir,newname))
    imgjson.write(get_dict(iidx,newname,os.path.basename(img)))


imgjson.write('\n]')

