
DevOps = float(input("Enter marks for DevOps: "))
LA = float(input("Enter marks for LA: "))
DM = float(input("Enter marks for DM: "))
CN = float(input("Enter marks for CN: "))


pass_mark = 40


if DevOps >= pass_mark and LA >= pass_mark and DM >= pass_mark and CN >= pass_mark:
    print("\nResult: PASSED")
else:
    print("\nResult: FAILED (You scored below 40 in one or more subjects)")
