from PIL import Image
import os
import getopt
import sys

usage = '''
Usage:
 
    app_gen_icon.py <source png file> <output icon dir> [-p prefix]
       - source png file should be greater thant 180*180
       - output icon dir: The dir you need to save the output icons
    optional:
       -p  specified the output icon prefix, eg 'app-icon'
'''
 
_IPAD_PRO_2X = (167, 167)
_IPAD_1X     = (76, 76)
_IPAD_2X     = (152, 152)
_IPHONE_2X   = (120, 120)
_IPHONE_3X   = (180, 180)

_PREFIX = 'app-icon'

def gen_ipad_pro(img_path, out_dir, prefix=_PREFIX):
    img = Image.open(img_path)
    img.thumbnail(_IPAD_PRO_2X, Image.ANTIALIAS) 
    img.save(os.path.join(out_dir, '{}-ipad-pro@2X.png'.format(prefix)), format='png')

def gen_ipad_1x(img_path, out_dir, prefix=_PREFIX):
    img = Image.open(img_path)
    img.thumbnail(_IPAD_1X, Image.ANTIALIAS) 
    img.save(os.path.join(out_dir, '{}-ipad@1X.png'.format(prefix)), format='png')

def gen_ipad_2x(img_path, out_dir, prefix=_PREFIX):
    img = Image.open(img_path)
    img.thumbnail(_IPAD_2X, Image.ANTIALIAS) 
    img.save(os.path.join(out_dir, '{}-ipad@2X.png'.format(prefix)), format='png')

def gen_iphone_2x(img_path, out_dir, prefix=_PREFIX):
    img = Image.open(img_path)
    img.thumbnail(_IPHONE_2X, Image.ANTIALIAS) 
    img.save(os.path.join(out_dir, '{}-iphone@2X.png'.format(prefix)), format='png')

def gen_iphone_3x(img_path, out_dir, prefix=_PREFIX):
    img = Image.open(img_path)
    img.thumbnail(_IPHONE_3X, Image.ANTIALIAS) 
    img.save(os.path.join(out_dir, '{}-iphone@3X.png'.format(prefix)), format='png')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(usage)
        sys.exit(-1)
    
    opt, d = getopt.getopt(sys.argv[3:], 'p:')
    options = dict(opt)
    prefix = options.get('-p', _PREFIX)

    print('Generating ipad 1x...')
    gen_ipad_1x(sys.argv[1], sys.argv[2], prefix)
    print('Generating ipad 2x...')
    gen_ipad_2x(sys.argv[1], sys.argv[2], prefix)
    print('Generating iphone 2x...')
    gen_iphone_2x(sys.argv[1], sys.argv[2], prefix)
    print('Generating iphone 3x...')
    gen_iphone_3x(sys.argv[1], sys.argv[2], prefix)
    print('Generating ipad 2x...')
    gen_ipad_pro(sys.argv[1], sys.argv[2], prefix)
    print('App icons all generated.')
