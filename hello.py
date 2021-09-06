def output_by_subject() :
     with open("C:\\Users\\joelr\\OneDrive\\Documents\\GitHub\\1901EE32_2021\\tut03\\regtable_old.csv", "r") as f:
        for line in f:
            file1 = line.split(',')
            
            del file1[4:8]
            del file1[2]
            if (file1[2] =="subno"):continue
            try : 
                with open(f"C:\\Users\\joelr\\OneDrive\\Documents\\GitHub\\1901EE32_2021\\tut03\\output_by_subject\\{file1[2]}.csv" ):
                    with open(f"C:\\Users\\joelr\\OneDrive\\Documents\\GitHub\\1901EE32_2021\\tut03\\output_by_subject\\{file1[2]}.csv", "a") as f11:
                        file1=",".join(file1)
                        f11.write(file1)

            except IOError:
                with open(f"C:\\Users\\joelr\\OneDrive\\Documents\\GitHub\\1901EE32_2021\\tut03\\output_by_subject\\{file1[2]}.csv", 'w') as f11:
                        f11.write("rollno,register_sem,subno,sub_type\n")
                        file1=",".join(file1)
                        f11.write(file1)
        return
def output_individual_roll():
    with open("C:\\Users\\joelr\\OneDrive\\Documents\\GitHub\\1901EE32_2021\\tut03\\regtable_old.csv", "r") as f:
        for line in f:
            file1 = line.split(',')
            
            del file1[4:8]
            del file1[2]
            if (file1[0] =="rollno"):continue
            try: 
                with open(f"C:\\Users\\joelr\\OneDrive\\Documents\\GitHub\\1901EE32_2021\\tut03\\output_individual_roll\\{file1[0]}.csv"):
                    with open(f"C:\\Users\\joelr\\OneDrive\\Documents\\GitHub\\1901EE32_2021\\tut03\\output_individual_roll\\{file1[0]}.csv", 'a') as f11:
                        file1=",".join(file1)
                        f11.write(file1)
            except IOError:
                with open(f"C:\\Users\\joelr\\OneDrive\\Documents\\GitHub\\1901EE32_2021\\tut03\\output_individual_roll\\{file1[0]}.csv", 'w') as f11:
                        f11.write("rollno,register_sem,subno,sub_type\n")
                        file1=",".join(file1)
                        f11.write(file1)
        return
output_by_subject()
output_individual_roll()