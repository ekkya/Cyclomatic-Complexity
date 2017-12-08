import git
import os.path
from radon.visitors import ComplexityVisitor
import radon.complexity
import subprocess
import lizard
#from git import Repo
import git
import tempfile
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
repo = git.Repo()
#git_url = "https://github.com/ekkya/CS7NS1-Individual-task.git"
repo_dir = "/home/ekkya/Cyclomatic-Complexity"
#repo.clone_from(git_url, repo_dir)
print "1"
commits_touching_path = list(repo.iter_commits(paths=repo_dir))
print commits_touching_path
for root, dirs, files in os.walk(repo_dir):
    for i in range(len(commits_touching_path)):
        commits = commits_touching_path[i]
        for file in files:
            if file.endswith(".py"):
                commits_touching_path = list(repo.iter_commits(paths=file))
                print file + str(commits_touching_path)
                #print len(commits_touching_path)
                file_contents = repo.git.show('{}:{}'.format(commits.hexsha, file))
                print file_contents
                f = open('test.txt', 'w')
                f.write(file_contents)
                #result = lizard.analyze_file(file)
                #print result
                #cc = result.average_cyclomatic_complexity
                #print cc
f.close()