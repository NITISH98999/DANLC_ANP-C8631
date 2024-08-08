#6. wap to calculate the salary slip
# Calculate bonus of employee to 25 % of salary by shift operators.
u=float(input("Enter Basic salary of basic salary : "))
da=0.02*u
ta=u*0.03
hra=u*0.10
pf=u*0.15
totalsalary=(u+da+ta+hra+pf)
netsalary=int(totalsalary-pf)
bonus=netsalary>>2
print(f"DA : {da}")
print(f"TA : {ta}")
print(f"HRA : {hra}")
print(f"PF : {pf}")
print(f"Total Salary : {totalsalary}")
print(f"Net salary : {netsalary}")
print(f"Bonus : {bonus}")