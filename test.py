import git
import os.path
from radon.visitors import ComplexityVisitor
import radon.complexity
import subprocess
import lizard
#from git import Repo
import git

repo = git.Repo()
git_url = "https://github.com/ekkya/CS7NS1-Individual-task.git"
repo_dir = "/home/ekkya/Documents/test"
repo.clone_from(git_url, repo_dir)
print "1"
commits_touching_path = list(repo.iter_commits(paths=repo_dir))
print commits_touching_path
