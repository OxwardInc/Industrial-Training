# A brogram to compute a new salary if the salary is increased by 15%

salary = input("Enter your salary: ")

sal = float(salary)

nip = (sal / 100)

upd_sal = sal + (nip * 15)

print("The new salary is ", upd_sal)
