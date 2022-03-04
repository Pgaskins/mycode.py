#!/usr/bin/env python3


#Conditional If
message = 'You only get out what you put in !!! '


test_score = float(input("What is your test score ?"))

# if input value 
if test_score > 90 and test_score <= 100:
    message = message + 'great job you made an A+ '
elif test_score <90 and test_score >= 80:
    message = message + 'Good job you earned a B '
elif test_score <80 and test_score >=70:
    message = message + 'You can do better than a C, Keep working.'
elif test_score <70 and test_score >=60:
    message = message + ' D....Spend more time studying and lees time gamming.'
else:
    message = message + 'Parent conference is needed '
print(message)

