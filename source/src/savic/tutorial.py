import savic
import os

def tutorial_path():
    
    return os.path.dirname(savic.__file__) + '/tutorial/SAVIC_Examples.h5'
    
def readme_path():
    
    return os.path.dirname(savic.__file__) + '/tutorial/SAVIC_readme.pdf'
    
def test_path():
    
    return os.path.dirname(savic.__file__) + '/tutorial/SAVIC_testing.ipynb'

def article_path():
    
    return [os.path.dirname(savic.__file__) + '/tutorial/Article_I_Statistical_Trends.pdf', os.path.dirname(savic.__file__) + '/tutorial/Article_II_Classification_and_Multidimensional_Mapping.pdf']
    

def docs_path():
    
    return 'https://savic.readthedocs.io/en/latest/'


