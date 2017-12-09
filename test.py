import os.path
import git
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

repo = git.Repo()
git_url = "https://github.com/geekcomputers/Python.git"
repo_dir = "/home/ekkya/Cyclomatic-Complexity/test"
repo.clone_from(git_url, repo_dir)
print "1"
commits_touching_path = list(repo.iter_commits('master'))
print commits_touching_path
print len(commits_touching_path)
print range(len(commits_touching_path))
for root, dirs, files in os.walk(repo_dir):
    for file in files:
        for i in range(len(commits_touching_path)):
            commits = commits_touching_path[i]
            if file.endswith(".py"):
                try:
                    file_contents = repo.git.show('{}:{}'.format(commits.hexsha, file))
                    #print file_contents
                    f1 = open('test_' + str(i) + '.txt', 'a')
                    f1.write(file_contents)
                except git.exc.GitCommandError:
                    continue
f1.close()