import glob
import shutil
import os
from pathlib import Path
from distutils.dir_util import copy_tree

visscript_dir = "/home/cc/vue-image-diff/dist"
rootdir = "/home/cc/phd/testdir/outputs"
outdir = "/home/cc/phd/vis"

img_basenames = open('paths.txt','r').readlines()

os.makedirs(outdir,exist_ok=True)

models = glob.glob("%s/*" % rootdir)
# imgs = glob.glob("%s/*" % models[0])

all_imgfile_dict = {}

for img in img_basenames:

    files = glob.glob('%s/**/%s' % (rootdir,img.strip()),recursive=True)

    single_imgfile_dict = {}

    for file in files:
        model = os.path.basename(Path(file).parent.parent.parent.as_posix())
        single_imgfile_dict[model] = file

    all_imgfile_dict[img.strip()] = single_imgfile_dict

# print(all_imgfile_dict)

def get_dict(idx,filepath,name):
    return '''
    {
        "id": "%d",
        "name": "%s",
        "params": {"dimension": "512x512"},
        "url": "%s",
        "ext": "png"
    }''' % (idx,name,filepath)

# swap
swapfrom = 'swinir_rcab'


# main loop

index = open('%s/index.html' % outdir,'w')
index.write('''
            <html>
            <head>
                <!-- CSS only -->
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            </head>
            <body>
            <h2>
                VSR-SIM Reconstruction Output Comparison
            </h2>
            <table class="table">

            ''')

for k,v in all_imgfile_dict.items():

    if len(v) == 0: continue

    os.makedirs('%s/%s' % (outdir,k),exist_ok=True)
    copy_tree(visscript_dir,'%s/%s' % (outdir,k))

    imgjson = open('%s/%s/img.json' % (outdir,k),'w')
    imgjson.write('[\n')

    print(k,v)
    count = 0

    for k_,v_ in v.items():
        if count > 0: imgjson.write(',')
        modelname = k_
        if not modelname == swapfrom:
            newname = '%s-%s' % (k_,os.path.basename(v_))
            shutil.copy(v_,'%s/%s/%s' % (outdir,k,newname))
            imgjson.write(get_dict(count,newname,modelname))
        else:
            substituted_name = v_.replace('/out/','/wf/').replace('_out','_wf')
            newname = '%s-%s' % ('wf',os.path.basename(substituted_name))
            shutil.copy(substituted_name,'%s/%s/%s' % (outdir,k,newname))
            imgjson.write(get_dict(count,newname,'wf'))

        count += 1

    imgjson.write('\n]')
    imgjson.close()

    index.write('''
                <tr><td class="align-middle text-center">
                <a target="_blank" href="%s"> %s </a>
                </td><td>
                <img width=256 src="%s/%s"/>
                </td></tr>
                ''' % (k,k,k,newname))


index.write('''
            </table></body></html>''')

index.close()
