from datetime import datetime
import matplotlib as plt
'''At minimum you should end up with:

* a Patient class with:
  * instance attributes for gender, DOB, race, etc.
  * a [property](https://docs.python.org/3/library/functions.html#property) called `age`
  * working comparison operators ">" and "<" using `__lt__()` and `__gt__()` that compare the age of the Patient to that of other Patients _and_ floats
    i.e. `Patient() > Patient()` and `Patient() > 57.0`
* an Observation class with:
  * instance attributes for value, units, etc.
  '''

def load_patients(patients_file):
	with open(patients_file) as patient_table:
		return [line.replace('\n','').split('\t') for line in patient_table][1:]

def load_labs(labs_file):
	with open(labs_file) as labs_table:
		return [line.replace('\n','').split('\t') for line in labs_table][1:]

class Patient():

    global patients, labs
    patients = load_patients('/Users/yiyangzhang/Desktop/Biostat821/ehr_analysis/PatientCorePopulatedTable.txt')
    labs = load_labs('/Users/yiyangzhang/Desktop/Biostat821/ehr_analysis/LabsCorePopulatedTable.txt')

    def __init__(self, patientID):
        for row in patients:
            if row[0] == patientID:
                self.id = row[0]
                self.gender = row[1]
                self.dob = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')
                self.race = row[3]
                self.marital = row[4]
                self.language = row[5]
                self.poverty = row[6]
   
    @property
    def age(self):
        return round((datetime.now() - self.dob).days / 365, 1)
    
    def __lt__(self, other):
        if isinstance(other, float):
            return self.age < other
        if isinstance(other, Patient):
            return self.age < other.age

    def __gt__(self, other):
        if isinstance(other, float):
            return self.age > other
        if isinstance(other, Patient):
            return self.age > other.age

    def plot(self, labname, filename):
        lab_datetime = []
        lab_value = []
        for row in labs:
            if self.id == row[0] and labname == row[2]:
               lab_value.append(row[3])
               lab_datetime.append(datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S.%f'))
            lab_unit = row[4]
        plt.plot(lab_datetime, lab_value)
        plt.xlabel('Lab datetime')
        plt.ylabel(f'Lab value / {lab_unit}')
        plt.title(f'{self.id}// {labname}')
        plt.savefig(filename)

class Observation():
    global labs
    labs = load_labs('/Users/yiyangzhang/Desktop/Biostat821/ehr_analysis/LabsCorePopulatedTable.txt')
    def __init__(self, patientID, labname, labdatetime):
        for row in labs:
            if patientID == row[0] and labname == row[2] and labdatetime == datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S.%f'):
                self.id = row[0]
                self.labname = row[2]
                self.labvalue = row[3]
                self.labunit = row[4]
                self.labdatetime = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S.%f')

if __name__ == '__main__':
	print(Patient('DB22A4D9-7E4D-485C-916A-9CD1386507FB') > 57.0)
	Patient('DB22A4D9-7E4D-485C-916A-9CD1386507FB').plot("URINALYSIS: PH", "ph_over_time.png")
