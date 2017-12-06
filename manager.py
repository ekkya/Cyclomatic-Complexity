import os
import time
import sqlite3
import git

from rq import Connection, Queue

from CC import get_complexity

def main():
    #Get a directory present in a git repo (cloned into local machine)
    directory = "/home/ekkya/Cyclomatic-Complexity/cpython/"

    # Kick off the tasks asynchronously
    async_results = {}
    connection = sqlite3.connect('results.db')
    print "Database Opened"
    #connection.execute('''CREATE TABLE RESULTS
      #                                       (FileName TEXT PRIMARY KEY     NOT NULL,
       #                                       CC            REAL,
        #                                     TimeTaken      REAL    NOT NULL);''')
    print "Table created successfully"
    q = Queue()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                q1 = str(os.path.join(directory, file))
                async_results[file] = q.enqueue(get_complexity, q1)

    start_time = time.time()
    done = False
    while not done:
        os.system('clear')
        print('Asynchronously: (now = %.2f)' % (time.time() - start_time,))
        done = True
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    q1 = str(os.path.join(directory, file))
                    result = async_results[file].return_value
            if result is None:
                done = False
                result = '(calculating)'
                #print('CC(%s) = %s' % (filename, result))
            total_time = time.time() - start_time
            if result == '(calculating)':
                print "Continue"
                    #connection.execute("DELETE from RESULTS where FileName = '(calculating)';")
                    #connection.commit()
            else:
                cursor = connection.execute("INSERT OR IGNORE INTO RESULTS VALUES (?, ?, ?)",
                                                (file, result, total_time))
                connection.commit()
    print('Done')


if __name__ == '__main__':
    # Tell RQ what Redis connection to use
    with Connection():
        main()

