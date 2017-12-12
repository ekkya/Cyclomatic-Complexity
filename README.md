# Cyclomatic-Complexity

To construct a REST service system, focussed on the efficient computation of code complexity for a given repository, 
utilising a set of nodes as appropriate to minimise execution time from submission to result return.

Completed using Python.

Method

Manager
  Prepares the files cloned from a git repository. Receives code for each commit. Calculating on a commit by commit basis.
  Places them into a Queue, where the worker can access the files.
  Waits for the results from the worker and stores them into a Database (File name, Cyclomatic Complexity, Time)
  Plots the results using Matplotlib.

Worker
  Uses Cyclomatic Complexity library (Lizard) to calculate the Average Cyclomatic Complexity for each commit present in the Queue.
  When the worker finishes, they ask for more work until the queue is empty.
  
Result
  As the number of workers increases, the time taken decreases. It comes to a certain point where increasing the number of workers
  doesn't increase the efficiency of the system.
  
  Please see Results.png for Graph
  
  
  
  

