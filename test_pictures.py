import os

import pictures as p
import pytest


def test_image_open():
    assert p.image_open('img.jpg')
    
@pytest.mark.xfail
def test_image_open_1():
    assert p.image_open('img.txt'), 'Assert None'

@pytest.mark.xfail
def test_image_open_2():
    assert p.image_open('x'), 'Assert None'
    
# def test_image_to_str():
    # img_name = 'img2.jpg'
    # img = p.image_open(img_name)
    # assert p.image_to_str(img) in 'PIL.JpegImagePlugin.JpegImageFile'   


def test_write_file():
    assert p.write_file('fname.txt', 'text'), 'Assert None'    

@pytest.mark.xfail
def test_write_file_1():
    assert p.write_file('fname', text), "Name 'text' is not defined"

@pytest.mark.xfail
def test_write_file_2():
    name = 'name'
    assert p.write_file(name, 'text'), 'Assert None'
        
def test_getSize(): 
    st = os.stat('file.txt') 
    assert st.st_size > 0

if __name__ == '__main__':
    pytest.main()
    
    
# import os

# dirpath = '/mnt/f/code.books/articles/python'
# filepath = '/mnt/f/code.books/articles/python/code/file_dir.py'

# os.path.isfile(dirpath) # False
# os.path.isdir(dirpath) # True
# os.path.isfile(filepath) # True
# os.path.isdir(filepath) # False

# emptyfile = '/mnt/f/code.books/articles/python/emptyfile'
# nonemptyfile = '/mnt/f/code.books/articles/python/onebytefile'

# result = os.stat(nonemptyfile)
# result.st_size # 1

# result = os.stat(emptyfile)
# result.st_size # 0
# from pathlib import Path

# dirpath = '/mnt/f/code.books/articles/python'
# filepath = '/mnt/f/code.books/articles/python/code/file_dir.py'

# Path(dirpath).is_file() # False
# Path(dirpath).is_dir() # True
# Path(filepath).is_file() # True
# Path(dirpath).is_file() # False
# emptyfile = '/mnt/f/code.books/articles/python/emptyfile'
# nonemptyfile = '/mnt/f/code.books/articles/python/onebytefile'

# print('File stats: ' + Path(emptyfile).stat())

# print('File size: ' + Path(emptyfile).stat().st_size + ' byte(s)')

# print('File stats: ' + Path(nonemptyfile).stat())

# print('File size: ' + Path(nonemptyfile).stat().st_size + ' byte(s)')

# # type nul > emptyfile