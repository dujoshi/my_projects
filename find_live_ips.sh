One line Utility for getting the Alive IPs in a network. 

for ip in $(seq 129 158); do ping -c 1 10.197.131.$ip > /dev/null; [ $? -eq 0 ] && echo "10.197.131.$ip UP" || : ; done


Output: 

[dujoshi@DUJOSHI-M-K1YF:~/Downloads] $
echo "10.197.131.$ip UP" || : ; done $ for ip in $(seq 129 158); do ping -c 1 10.197.131.$ip > /dev/null; [ $? -eq 0 ] &&
10.197.131.129 UP
10.197.131.130 UP
10.197.131.131 UP
10.197.131.132 UP
10.197.131.134 UP
10.197.131.135 UP
10.197.131.136 UP
10.197.131.137 UP
10.197.131.138 UP
10.197.131.139 UP
