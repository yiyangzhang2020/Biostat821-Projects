from datetime import datetime
''' Import datetime library for later use in the num_older_than function 
    to convert the date format into datetime 
'''
def load_patients(patients_file):
       ''' 
	   A function that reads in original patients data and turn it into a new data table
	   @param patients_file: representing original input data of patients
	   @return: a new organized dataframe for later use
	   ''' 
    with open(patients_file) as patient_table:
		return [line.replace('\n','').split('\t') for line in patient_table]
def load_labs(labs_file):
    	''' 
	   A function that reads in original labs data and turn it into a new data table
	   @param labs_file: representing original input data of labs
	   @return: a new organized dataframe for later use
	   ''' 
	with open(labs_file) as labs_table:
		return [line.replace('\n','').split('\t') for line in labs_table]

def num_older_than(patient,age):
    	''' 
	   A function that reads in patients data and an index age
	   to see how many patients in the dataframe are older than the index age
	   @param patient: representing data of patients
	   @param age: representing the index age
	   @return: the number of patients older than the index age from the dataframe
	   ''' 
	birth_date = [row[2] for row in patient][1:]
	birth_date = [datetime.strptime(row, '%Y-%m-%d %H:%M:%S.%f') for row in birth_date]
	end_date = datetime.now()
	diff = [round((end_date - row).days / 365, 1) for row in birth_date]
	return len([row for row in diff if row > age])

def sick_patients(labs, lab_name, gt_lt, value):
    	''' 
	   A function that reads in labs data, a to-check index, a symbol for comparison and the corresponding value
	   to compare whether the index to-check is greater or less than an input value
	   @param labs: representing data of labs
	   @param lab_name: representing the index that needs to be checked 
	   @param gt_lt: representing the comparison method
	   @param value: representing the comparative value
	   @return: a list of patient IDs that satisfy the inclusion criteria
	   ''' 
	stat = lambda lab_value, ref_value: (gt_lt == '>' and lab_value > ref_value) or (gt_lt == '<' and lab_value < ref_value)
	sick_list = [row[0] for row in labs[1:] if row[2] == lab_name and stat(float(row[3]), value)]
	sick_list = list(set(sick_list))
	return sick_list

'''
if __name__ == '__main__':
'''
patients = load_patients('/Users/yiyangzhang/Desktop/Biostat821/ehr_analysis/PatientCorePopulatedTable.txt')
labs = load_labs('/Users/yiyangzhang/Desktop/Biostat821/ehr_analysis/LabsCorePopulatedTable.txt')


try: 
	index_age=int(input("Enter a index age: "))
    print(num_older_than(patients, index_age))
except: 
	raise TypeError("Please input an integar")


try: 
	index_value=float(input("Enter a index value"))
except: 
	raise TypeError("Please enter a float as the index value")

try:
	what_lab=input("Enter the lab name")
	compare=input("Enter > or < ")
	print(sick_patients(labs, what_lab, compare, index_value))
except: 
	raise ValueError("Follow instructions please")


print(sick_patients(labs, what_lab, compare, index_value))


print(len(sick_patients(labs, 'METABOLIC: ALBUMIN', '>', 5.9)))
print(labs[3])
print(len(patients))
print(len(labs))
