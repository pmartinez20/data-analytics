import random 
import math 
import statistics 

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

#Experimenting with a subset of integers 1-100:
#Sum of 75 sample values from 1 to 100: ____

sample_sum = sum(vals_sample)
print(sample_sum)
#3797
#Average of 75 sample values: ____

sample_avg = statistics.mean(vals_sample)
print(sample_avg)
#50.62
#Median of 75 sample values: ____

sample_median = statistics.median(vals_sample)
print(sample_median)
#52

#Experimenting with a superset of 200 values, integers 1-100:
#Average of 200 values: ____
choices_avg = statistics.mean(vals_choices)
print(choice_avg)
#Median of 200 values: ____
choices_median = statistics.median(vals_choices)
print(choices_median)
#Mode of 200 values: ____
choices_mode = statistics.mode(vals_choices)
print(choices_mode)
#Standard deviation of 200 values: ____
choices_stdev = statistics.stdev(vals_choices)
print(choices_stdev)
#Variance of 200 values: ____
choices_variance = statistics.variance(vals_choices)
print(choices_variance)
#Modeling a random circle:
#Radius = __, area = ____ (rounded up to the nearest integer)
#Radius = __, area = ____ (rounded down to the nearest integer)
#a) Your final print statement should include the printed headers each beginning with
#an underscore and the line breaks between sections in your output. For the line
#breaks, use print('\n')
#b) Your calculated answers should fill in the blanks above.
