#!/usr/bin/python
from threading import Thread
from math import pow
from time import clock, time, ctime
import argparse


class CalcPy (Thread):

  def __init__ (self, pStart, pFinish):
    Thread.__init__(self)
    #Declaring protected vars to range calc
    self.__vStart      = pStart
    self.__vFinish     = pFinish
    self.__vSum        = 0

  def run(self):
    for n in range(self.__vStart, self.__vFinish):
      self.__vSum += (pow(-1, n)) / (2 * n + 1)

  @property
  def Sum(self):
    return self.__vSum

def main():
  #Define the variables to get the args
  tThreads = 1
  tIterations = 1000000

  #Parsing the arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--threads", type=int,
                      help="change the number of threads (default is 1)")
  parser.add_argument("-i", "--iterations", type=int,
                      help="change the number of iterations (default is 1000000)")
  args = parser.parse_args()

  #Testing args
  if args.threads:
    tThreads = args.threads
  if args.iterations:
    tIterations = args.iterations

  print "Total of Threads", tThreads
  print "Total of iterations: ", tIterations

  """
  The program
  """
  #Creating the list
  Calcs = []
  vBlock = tIterations / tThreads
  vNextBlock = vBlock
  vPartial = 0


  vCounter = 0
  #Including the nThreads into Calc list
  for lCalcs in range (0, tThreads):
    vCounter +=1
    vThreadName = "Thread-"+str(vCounter)
    Calcs.append(CalcPy(vPartial, vNextBlock))
    vPartial = (vNextBlock + 1)
    vNextBlock += vBlock
    print "Thread ", vThreadName, " created..."

  vStartTime = clock()
  print "Process started at ", ctime(time())
  [lCalc.start() for lCalc in Calcs]

  [lCalc.join() for lCalc in Calcs]

  tSum = 0

  for lCalc in Calcs:
    tSum += lCalc.Sum

  vFinishTime = clock()
  print "Process finished at ", ctime(time())
  #Result
  print "Result: ", tSum * 4

  print "Time to process: ", vFinishTime - vStartTime

if __name__ == '__main__':
  main()
