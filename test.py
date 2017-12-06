import git
import os.path
from radon.visitors import ComplexityVisitor
import radon.complexity
import subprocess
import lizard
#from git import Repo
import git

repo = git.Repo()
#git_url = "https://github.com/ekkya/CS7NS1-Individual-task.git"
repo_dir = "/home/ekkya/Cyclomatic-Complexity/"
#repo.clone_from(git_url, repo_dir)
print "1"

for root, dirs, files in os.walk(repo_dir):
        for file in files:
            if file.endswith(".py"):
                commits_touching_path = list(repo.iter_commits(paths=file))
                print file + str(commits_touching_path)
                result = lizard.analyze_file(file)
                print result
                cc = result.average_cyclomatic_complexity
                print cc
