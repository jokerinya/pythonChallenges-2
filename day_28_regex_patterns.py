"""
Output Format

Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a new line.

Sample Input

6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
Sample Output

julia
julia
riya
samantha
tanya

"""

N = int(input())
my_list = []
    
for N_itr in range(N):
    firstNameEmailID = input().split()
    firstName = firstNameEmailID[0]
    emailID = firstNameEmailID[1]
    if emailID.endswith("@gmail.com"):
        my_list.append(firstName)
    
if len(my_list):
    for i in sorted(my_list):
        print(i)