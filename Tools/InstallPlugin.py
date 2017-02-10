import os, shutil

if __name__ == "__main__":
    
    AnyLibrary_Home = os.getenv('AnyLibrary_Home')
    Python_Home = os.getenv('Python_Home')

    if AnyLibrary_Home is None:
        print 'AnyLibrary_Home has no such path!'
        exit()
    
    if Python_Home is None:
        print 'Python_Home has no such path!'
        exit()

    PackageDir = AnyLibrary_Home + r'\..\Package'
    platformsDir = AnyLibrary_Home + r'\platforms'

    try:
        shutil.copytree(PackageDir, Python_Home+r'\Package')
        shutil.copytree(platformsDir, Python_Home+r'\platforms')
    except:
        shutil.rmtree(Python_Home+r'\Package')
        shutil.rmtree(Python_Home+r'\platforms')
        print 'happend except, please try again!'
        exit()
    print 'Install finished!'


