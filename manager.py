import os.path
import time
import sqlite3
import git
import sys

from rq import Connection, Queue

from CC import get_complexity

reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    repo = git.Repo()
    git_url = "https://github.com/geekcomputers/Python.git"
    repo_dir = "/home/ekkya/Cyclomatic-Complexity/test"
    directory = "/home/ekkya/Cyclomatic-Complexity/results/"
    #repo.clone_from(git_url, repo_dir)
    #print "1"
    repo = git.Repo(repo_dir)
    # Kick off the tasks asynchronously
    async_results = {}
    connection = sqlite3.connect('results_4w.db')
    print "Database Opened"
    connection.execute('''CREATE TABLE RESULTS
                                             (FileName TEXT PRIMARY KEY     NOT NULL,
                                              CC            REAL,
                                             TimeTaken      REAL    NOT NULL);''')
    print "Table created successfully"
    q = Queue()
    #commits_touching_path = list(repo.iter_commits('master'))
    #for root, dirs, files in os.walk(repo_dir):
     #   for file in files:
      #      for i in range(len(commits_touching_path)):
       #         commits = commits_touching_path[i]
        #        if file.endswith(".py"):
         #           try:
          #              file_contents = repo.git.show('{}:{}'.format(commits.hexsha, file))
           #             # print file_contents
            #            f1 = open(directory + 'test_' + str(i) + '.py', 'a')
             #           f1.write(file_contents)
              #      except git.exc.GitCommandError:
               #         continue
    #f1.close()
    for root, dirs, files in os.walk(directory):
        for file in files:
            q1 = str(os.path.join(directory, file))
            async_results[file] = q.enqueue(get_complexity, q1)  ##CHANGE TO PATH OF F1
            start_time = time.time()

    #start_time = time.time()
    done = False
    while not done:
        os.system('clear')
        print('Asynchronously: (now = %.2f)' % (time.time() - start_time,))
        done = True
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    result = async_results[file].return_value
                    #print result
                    if result is None:
                        done = False
                        result = '(calculating)'
                        #print('CC(%s) = %s' % (filename, result))
                    #total_time = time.time() - start_time
                    if result != '(calculating)':
                        total_time = time.time() - start_time
                        cursor = connection.execute("INSERT OR REPLACE INTO RESULTS VALUES (?, ?, ?)",
                                                    (file, result, total_time))
                        connection.commit()
                    else:
                        print "Continue"
    print('Done')


if __name__ == '__main__':
    # Tell RQ what Redis connection to use
    with Connection():
        main()

