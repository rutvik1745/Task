import statistics

#list of positive integer number
datasets = [5,2,7,4,2,6,8]
x = statistics.mean(datasets)

#Printing the mean
print("mean is : ",x)

datasets1 = [4,-5,6,6,9,4,5,-2]
#Printing median of the
#random data-set
print("Mediam of data-set : %s"%(statistics.median(datasets1)))

#declaring a simple data-set consisting of real valued possitive integer
datasets2 = [2,4,7,7,2,2,3,6,6,8]

print("Calculated Mode %s"%(statistics.mode(datasets2)))


datasets3 = [7,8,9,10,11]
# Prints standard deviation   
a = statistics.stdev(datasets3)
print(a)

# simple list of a set of integers   
set1 = [4, 6, 2, 5, 7, 7]     
# Note: low median will always be a member of the data-set.     
# Print low median of the data-set   
print("Low median of data-set is % s "   
        % (statistics.median_low(set1)))  


# list of set of the integers   
dataset = [2, 1, 7, 6, 1, 9]     
print("High median of data-set is %s "   
        % (statistics.median_high(dataset)))  


import sys
print(sys.modules)

print(sys.version)


print(sys.path)