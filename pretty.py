# This is pretty table a good way to write your code blocks msgs 
# https://pypi.org/project/PrettyTable/
# I mainly used it for describing what case does and putitng the results
# in a table format.


from prettytable import PrettyTable

#=========Here is the start of case block ==========#

x = PrettyTable()
x.field_names=["TC: Verify XYZ "]
msg=r'''
    TestCase will do : 
    1- This case will start doing  XYZ to bla bla 
    2- then will start bla bla on this 
    3- then will verify bla bla  on that 
    4- we can expect the following error after that
    Error msg
    '''
x.add_row([msg])
print x
del x

#=========Here is the start of case block ==========#


#now let's say we have multiple case in this case: 
all_test_passed=True 
test_result=[]

#now for each  cases we can append results based  on the expected paramters
# Like  
if True: #this true will be based on our test 
     test_result.append( 'ICMP_SRC_TO_DST : FAILED')
     all_test_passed=False


if True: #this true will be based on our test 
     test_result.append( 'TCP_FLOW  : FAILED')
     all_test_passed=False
#now at the end of  test let's say we have  a list of all 1-4 steps : 


x = PrettyTable()

for result in test_result:
    x.field_names=["Case Name", "Status"]
    x.add_row([result.split(':')[0],result.split(':')[1]])
print x
del x,




#On running the above code Output will be something like this
#
#[dujoshi@DUJOSHI-M-K1YF:~/CODE/TEMP_CODE] $ python pretty.py
#+-----------------------------------------------------+
#|                   TC: Verify XYZ                    |
#+-----------------------------------------------------+
#|                                                     |
#|                   TestCase will do :                |
#|      1- This case will start doing  XYZ to bla bla  |
#|           2- then will start bla bla on this        |
#|          3- then will verify bla bla  on that       |
#|     4- we can expect the following error after that |
#|                        Error msg                    |
#|                                                     |
#+-----------------------------------------------------+
#
#+------------------+---------+
#|    Case Name     |  Status |
#+------------------+---------+
#| ICMP_SRC_TO_DST  |  FAILED |
#|    TCP_FLOW      |  FAILED |
#+------------------+---------+
