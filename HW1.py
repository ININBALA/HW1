# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '106061232.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

target_data = list(filter(lambda item: item['PRES'] != '-99', data))
target_data = list(filter(lambda item: item['PRES'] != '-999', target_data))

# Retrive ten data points from the beginning.

#target_data = target_data[995:999]


#=======================================


# Part. 4

#=======================================

# Print result
sum = 0
flag = 0
for item in target_data:
   if item['station_id']=='C0A880':
      sum = sum + float(item['PRES'])
      flag = flag + 1
if flag == 0:
   s = "[['C0A880', 'none'],"
   print(s, end=' ' )
else:
   s = "[['C0A880', '{0}'],".format(sum/flag)
   print(s, end=' ' )

sum = 0
flag = 0
for item in target_data:
   if item['station_id']=='C0F9A0':
      sum = sum + float(item['PRES'])
      flag = flag + 1
if flag == 0:
   s = "[C0F9A0', 'none'],"
   print(s, end=' ' )
else:
   s = "['C0F9A0', '{0}'],".format(sum/flag)
   print(s, end=' ' )

sum = 0
flag = 0
for item in target_data:
   if item['station_id']=='C0G640':
      sum = sum + float(item['PRES'])
      flag = flag + 1
if flag == 0:
   s = "['C0G640', 'none'],"
   print(s, end=' ' )
else:
   s = "['C0G640', '{0}'],".format(sum/flag)
   print(s, end=' ' )

sum = 0
flag = 0
for item in target_data:
   if item['station_id']=='C0R190':
      sum = sum + float(item['PRES'])
      flag = flag + 1
if flag == 0:
   s = "['C0R190', 'none'],"
   print(s, end=' ' )
else:
   s = "['C0R190', '{0}'],".format(sum/flag)
   print(s, end=' ' )

sum = 0
flag = 0
for item in target_data:
   if item['station_id']=='C0X260':
      sum = sum + float(item['PRES'])
      flag = flag + 1
if flag == 0:
   s = "['C0X260', 'none']],"
   print(s, end=' ' )
else:
   s = "['C0X260', '{0}']]".format(sum/flag)
   print(s)


#print(target_data[:10])

#========================================