#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]

#Age: Young = 1, Prepresbyopic = 2, Presbyopic = 3
#SP: myope = 1, hypermetrope = 2
#AST: yes = 1, no = 2
#TPR: Normal = 1, Reduced = 2

for object in db:
   print(object)
   row = []
   col=0
   for value in object:
         if col== 0:
            if value == 'Young':
               row.append(1)
            elif value == 'Prepresbyopic':
               row.append(2)
            else:
               row.append(3)
         elif col == 1:
            if value == 'Myope':
               row.append(1)
            else:
               row.append(2)
         elif col == 2:
            if value == 'Yes':
              row.append(1)
            else:
              row.append(2)
         elif col == 3: 
            if value == 'Normal':
                row.append(1)
            else:
                row.append(2)
         col=col+1
   X.append(row)
   print(row)

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here

for object in db:
  val = object[-1]
  if val == 'Yes':
    Y.append(1)
  else:
    Y.append(2)
  print(Y)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()