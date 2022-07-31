from scipy.stats import norm
import numpy as np
import scipy.stats as stats
from scipy.stats import binom
import scipy.stats as st
import statistics as s


'''
1.) The weights of steers in a herd are distributed normally.
The variance is 40,000 and the mean steer weight is 1300 lbs.
Find the probability that the weight of a randomly selected steer is greater than 979 lbs.
(Round your answer to 4 decimal places)
'''

mean = 1300.00
variance = 40000.00
std = variance**0.5


pdf = norm.sf(979, loc = mean , scale = std)
pdf_round_1 = round(pdf, 4)
print('1.) ', pdf_round_1)


'''
2.) SVGA monitors manufactured by TSI Electronics have life spans that have a normal distribution
with a variance of 1,960,000 and a mean life span of 11,000 hours.
If a SVGA monitor is selected at random, find the probability that
the life span of the monitor will be more than 8340 hours.(Round your answer to 4 decimal places)
'''

mean = 11000 
variance = 1960000 
std = variance**0.5


pdf_2 = norm.sf(8340, loc = mean , scale = std)
pdf_round_2 = round(pdf_2, 4)
print('2.) ', pdf_round_2)

'''
3.) Suppose the mean income of firms in the industry for a year is 80 million dollars with a standard deviation
of 3 million dollars.  If incomes for the industry are distributed normally, what is the probability that a
randomly selected firm will earn between 83 and 85 million dollars? (Round your answer to 4 decimal places)
'''

mean = 80
std = 3


pdf_3 = norm.cdf(85, loc = mean , scale = std) - norm.cdf(83, loc = mean , scale = std)
pdf_round_3 = round(pdf_3, 4)
print('3.) ',pdf_round_3)

'''
4.) Suppose GRE Verbal scores are normally distributed with a mean of 456 and a standard deviation of 123.
A university plans to offer tutoring jobs to students whose scores are in the top 14%.
What is the minimum score required for the job offer?  Round your answer to the nearest whole number,
if necessary.
'''
mean = 456
std = 123
q = 1 - 0.14


value_4 = norm.ppf(q, loc = mean , scale = std)
value_round_4 = round(value_4)
print('4.) ', value_round_4)

'''
5.) The lengths of nails produced in a factory are normally distributed with a mean of 6.13 centimeters and
a standard deviation of 0.06 centimeters. Find the two lengths that separate the top 7% and the bottom 7%.
These lengths could serve as limits used to identify which nails should be rejected.  Round your answer to
the nearest hundredth, if necessary.
'''

mean = 6.13
std = 0.06
q_1 = 1 - 0.07
q_2 = 0.07


value_one_5 = norm.ppf(q_1, loc = mean , scale = std)
value_two_5 = norm.ppf(q_2, loc = mean , scale = std)

value_round_one_5 = round(value_one_5, 2)
value_round_two_5 = round(value_two_5, 2)

print('5.) Top: ',value_round_one_5, 'Bottom: ',value_round_two_5)



'''
6.) An English professor assigns letter grades on a test according to the following scheme.
A:  Top 13% of scores
B:  Scores below the top 13% and above the bottom 55%
C:  Scores below the top 45% and above the bottom 20%
D:  Scores below the top 80% and above the bottom 9%
F:  Bottom 9% of scores
Scores on the test are normally distributed with a mean of 78.8 and a standard deviation of 9.8.
Find the numerical limits for a C grade.  Round your answers to the nearest whole number, if necessary.
'''

mean = 78.8
std = 9.8
q_1 = 0.45
q_2 = 0.20


value_one_6 = norm.ppf(q_1, loc = mean , scale = std)
value_two_6 = norm.ppf(q_2, loc = mean , scale = std)

value_round_one_6 = round(value_one_6)
value_round_two_6 = round(value_two_6)

print('6.) Below 45%: ', value_round_one_6, 'Above 20%: ',value_round_two_6 )

'''
7.) Suppose ACT Composite scores are normally distributed with a mean of 21.2 and a standard deviation of 5.4.
A university plans to admit students whose scores are in the top 45%.What is the minimum score required for
admission?  Round your answer to the nearest tenth, if necessary.
'''

mean = 21.2
std = 5.4
q = 1 - 0.45


value_7 = norm.ppf(q, loc = mean , scale = std)
value_round_7 = round(value_7, 1)
print('7.) ', value_round_7)

'''
8.) Consider the probability that less than 11 out of 151 students will not graduate on time.
Assume the probability that a given student will not graduate on time is 9%.
Approximate the probability using the normal distribution. (Round your answer to 4 decimal places.)
'''

value_8 = binom.pmf(k=10, n=151, p=0.09)
value_round_8 = round(value_8, 4)
print('8.) ',value_round_8)

#test = binom.cdf(k=10, n=151, p=0.09)
#print(test)


'''
9.)The mean lifetime of a tire is 48 months with a standard deviation of 7.  If 147 tires are sampled,
what is the probability that the mean of the sample would be greater than 48.83 months? (Round your answer to 4 decimal places)
'''
#z-score = (X_1 - X_2)*(n)**0.5/std

n =147
m_1 = 48
m_2 = 48.83
std = 7

z_score = ((m_2-m_1)*(n)**0.5)/std

value_9  = st.norm.cdf(z_score)
value_round_9 = round(value_9 , 4)
print('9.) ',value_round_9)


'''
10.)The quality control manager at a computer manufacturing company believes that the mean life of a computer is 91 months, with
a standard deviation of 10.  If he is correct, what is the probability that the mean of a sample of 68 computers would be greater
than 93.54 months? (Round your answer to 4 decimal places)
'''

n = 68
m_1 = 91
m_2 = 93.54
std = 10

z_score = ((m_2-m_1)*(n)**0.5)/std

value_10  = st.norm.cdf(z_score)
value_round_10 = round(value_10 , 4)
print('10.) ', value_round_10)


'''
11.)A director of reservations believes that 7% of the ticketed passengers are no-shows.  If the director is right, what is the probability
that the proportion of no-shows in a sample of 540 ticketed passengers would differ from the population proportion by less than 3%?
(Round your answer to 4 decimal places)
'''
n = 540
p = 0.07
q = 1-0.07
se = (p*q /n)**0.5 #standard_error
#print(se)


a = norm.cdf(0.10, p , se)
b = norm.cdf(0.04, p , se)
 

#print(a)
#print(b)


value_11 = a-b
value_round_11 = round(value_11 , 4)
print('11. )',value_round_11)

'''
12.)A bottle maker believes that 23% of his bottles are defective.  If the bottle maker is accurate, what is the probability that
the proportion of defective bottles in a sample of 602 bottles would differ from the population proportion by greater than 4%?
(Round your answer to 4 decimal places)
'''

n = 602
p = 0.23
q = 1-p
se = (p*q /n)**0.5 #standard_error
#print(se)


a = norm.cdf(0.27, p , se)
b = norm.cdf(0.19, p , se)
 

#print(a)
#print(b)


value_12 = a-b
value_round_12 = round(value_12 , 4)
print('12.) ',value_round_12)

'''
13.)A research company desires to know the mean consumption of beef per week among males over age 48.  Suppose a sample of size
208 is drawn with x ̅  = 3.9.  Assume ® = 0.8 .  Construct the 80% confidence interval for the mean number of lb. of beef per
week among males over 48. (Round your answers to 1 decimal place) 
'''

n = 208
mean = 3.9
std = 0.8
p= 0.8

se = std / (n)**0.5
t = st.t.ppf((1 - p)/ 2, n -1)  #t-distributed

lower_bound = mean + t * se

upper_bound = mean - t * se


value_round_13_lower = round(lower_bound , 1)
value_round_13_upper = round(upper_bound , 1)
print('13.) Lower Bound: ', value_round_13_lower, 'Upper Bound: ',value_round_13_upper )


'''
14.)An economist wants to estimate the mean per capita income (in thousands of dollars) in a major city in California.
Suppose a sample of size 7472 is drawn with x ̅  = 16.6.  Assume ® = 11 .  Construct the 98% confidence interval for
the mean per capita income. (Round your answers to 1 decimal place) 
'''

n = 7472
mean = 16.6
std = 11
p = 0.98

se = std / (n)**0.5
t = st.t.ppf((1 - p)/ 2, n -1)

lower_bound = mean + t * se

upper_bound = mean - t * se


value_round_14_lower = round(lower_bound , 1)
value_round_14_upper = round(upper_bound , 1)
print('14.) Lower Bound:' ,value_round_14_lower, 'Upper Bound: ',value_round_14_upper)


'''
15.)Find the value of t such that 0.05 of the area under the curve is to the left of t.  Assume the degrees of freedom equals 26.

Step 1. Choose the picture which best describes the problem. #Could not add picture 

Step 2. Write your answer below. 

'''

t =abs(st.t.ppf(0.05, 26))

print('15.) ',t)


'''
16.)The following measurements ( in picocuries per liter ) were recorded by a set of helium gas detectors installed in a laboratory facility:  
	                                             383.6, 347.1, 371.9, 347.6, 325.8, 337
Using these measurements, construct a 90% confidence interval for the mean level of helium gas present in the facility.
Assume the population is normally distributed.

Step 1. Calculate the sample mean for the given sample data. (Round answer to 2 decimal places) 


Step 2. Calculate the sample standard deviation for the given sample data. (Round answer to 2 decimal places) 


Step 3. Find the critical value that should be used in constructing the confidence interval. (Round answer to 3 decimal places) 


Step 4. Construct the 90% confidence interval. (Round answer to 2 decimal places)

'''

print('16.) ')
values = [383.6, 347.1, 371.9, 347.6, 325.8, 337]
mean = s.mean(values)
value_round_16_mean = round(mean , 2)
print('Step 1: ', value_round_16_mean)


std = s.stdev(values)
value_round_16_std = round(std , 2)
print('Step 2: ',value_round_16_std)

n = 6
p = 0.9

t = st.t.ppf((1 - p)/ 2, n -1)
t_abs = abs(t)
value_round_16_t = round(t_abs , 3)
print('Step 3: ', value_round_16_t)

se = std / (n)**0.5

lower_bound = mean + t * se

upper_bound = mean - t * se


value_round_16_lower = round(lower_bound , 2)
value_round_16_upper = round(upper_bound , 2)
print('Step 4: Lower Bound: ' ,value_round_16_lower, 'Upper Bound: ', value_round_16_upper)


'''
17.)A random sample of 16 fields of spring wheat has a mean yield of 46.4 bushels per acre and standard deviation of 2.45 bushels per acre.
Determine the 80% confidence interval for the true mean yield.  Assume the population is normally distributed.

Step 1. Find the critical value that should be used in constructing the confidence interval. (Round answer to 3 decimal places) 


Step 2. Construct the 80% confidence interval. (Round answer to 1 decimal place)

'''

print('17.) ')
n = 16
mean = 46.4 
std = 2.45 
p = 0.8

se = std / (n)**0.5
t = st.t.ppf((1 - p)/ 2, n -1)
t_abs = abs(t)

value_round_17_t = round(t_abs, 3)
print('Step 1: ', value_round_17_t)


lower_bound = mean + t * se

upper_bound = mean - t * se


value_round_17_lower = round(lower_bound , 1)
value_round_17_upper = round(upper_bound , 1)
print('Step 2: Lower Bound: ',value_round_17_lower, 'Upper Bound: ', value_round_17_upper)

'''
18.)A toy manufacturer wants to know how many new toys children buy each year.  She thinks the mean is 8 toys per year.
Assume a previous study found the standard deviation to be 1.9.  How large of a sample would be required in order to estimate
the mean number of toys bought per child at the 99% confidence level with an error of at most 0.13 toys?
(Round your answer up to the next integer)
'''

mean = 8
std = 1.9
p = 0.99
se = 0.13

z = st.norm.ppf(1 - (1 - p)/2)

n = ((z*std)/se)**2
print('18.) ', round(n))

'''
19.)A research scientist wants to know how many times per hour a certain strand of bacteria reproduces.  He believes that the
mean is 12.6.  Assume the variance is known to be 3.61.  How large of a sample would be required in order to estimate the
mean number of reproductions per hour at the 95% confidence level with an error of at most 0.19 reproductions?
(Round your answer up to the next integer)
'''

mean = 12.6
variance = 3.61
std = variance**0.5
p = 0.95
se = 0.19

z = st.norm.ppf(1 - (1 - p)/2)

n = ((z*std)/se)**2
print('19.) ', round(n))

'''
20.)The state education commission wants to estimate the fraction of tenth grade students that have reading skills at or below
the eighth grade level.

Step 1. Suppose a sample of 2089 tenth graders is drawn. Of the students sampled, 1734 read above the eighth grade level.
Using the data, estimate the proportion of tenth graders reading at or below the eighth grade level.
(Write your answer as a fraction or a decimal number rounded to 3 decimal places)

Step 2. Suppose a sample of 2089 tenth graders is drawn.  Of the students sampled, 1734 read above the eighth grade level.
Using the data, construct the 98% confidence interval for the population proportion of tenth graders reading at or below the
eighth grade level. (Round your answers to 3 decimal places)

'''

print('20.) ')
n = 2089
n_above = 1734
n_below = n - n_above
p = n_below/n
r = round (p, 3)
print('Step 1: ', r)

z = st.norm.ppf(1 - (1 - 0.98)/2)

upper = z*(p*((1-p)/n))**0.5
print('Step 2: Lower Bound: ', round((p- upper),3) , 'Upper Bound: ', round((upper +p), 3))


'''
21.)An environmentalist wants to find out the fraction of oil tankers that have spills each month.

Step 1. Suppose a sample of 474 tankers is drawn.  Of these ships, 156 had spills.  Using the data, estimate the proportion
of oil tankers that had spills. (Write your answer as a fraction or a decimal number rounded to 3 decimal places)

Step 2. Suppose a sample of 474 tankers is drawn.  Of these ships, 156 had spills.  Using the data, construct the 95%
confidence interval for the population proportion of oil tankers that have spills each month. (Round your answers to 3
decimal places)

'''

print('21.) ')
n = 474
n_spill = 156
p = n_spill/n
r = round (p, 3)
print('Step 1: ', r)

z = st.norm.ppf(1 - (1 - 0.98)/2)

upper = z*(p*((1-p)/n))**0.5
#print(upper + p)

#print(p - upper)

print('Step 2: Lower Bound: ', round((p- upper),3) , 'Upper Bound: ', round((upper +p), 3))
