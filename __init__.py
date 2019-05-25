import dataSetCreator
import trainner
import recognizer
from trainner import trainer

ch = raw_input('Enter your choice \n1: New Person \n2:Recognize\n0:Quit\n')
print  ch
if ch=='1':
    dataSetCreator.create()
    trainner.trainer()
if ch=='2':
    recognizer.recognizer()
