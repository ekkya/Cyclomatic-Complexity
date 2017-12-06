import git
import os.path
from radon.visitors import ComplexityVisitor
import radon.complexity
import subprocess
import lizard

def get_complexity(f_name):
    #pth = "/home/ekkya/CS7NS1-Individual-task/Dummy"
    #f_name = "directory.py"
    #q = str(os.path.join(pth, f_name))
    #print q
    result = lizard.analyze_file(f_name)
        #print result
    cc = result.average_cyclomatic_complexity
    #print cc

    return cc

