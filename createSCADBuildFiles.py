import os
import subprocess

def init():
    scad_file_paths = []
    sizes = [1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 4, 6, 6.25, 7]
    buttType = ['MasterBase', 'SculptingBase', 'StemCavity']
    current_dir = os.getcwd()
    for size in sizes:
        s = str(size).replace('.', '-')
        child_dir = '{}\{}u'.format(current_dir, s)

        if not os.path.isdir(child_dir):
            os.makedirs(child_dir)

        for butt in buttType:
            folder = child_dir
            filename = "{}\ZButt_{}U_{}.scad".format(folder, s, butt)
            scad_file_paths.append(filename)
            file = open(filename, 'w+')
            create_scad(file, butt, size)
            file.close()
    make_stl(scad_file_paths)

def create_scad(file, butt, size):
    file.write("include < <--Z-butt.openscad path here--> >\n")
    if butt == 'MasterBase':
        file.write('mx_master_base({});'.format(size))
    elif butt == 'SculptingBase':
        file.write('mx_sculpt_base({});'.format(size))
    else:
        file.write('rotate ([180, 0, 0]) mx_stem_cavity({});'.format(size))

def make_stl(file_paths):
    for path in file_paths:
        stl_path = path.replace('.scad', '') + ".stl"
        command = '"<--openscad folder path here-->"' + '\openscad -o {} {}'.format(stl_path, path)
        subprocess.Popen(command, shell=True);

init()
