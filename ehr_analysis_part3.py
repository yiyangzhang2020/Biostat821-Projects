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

class Patients():
    #define data entry
    def __init__(self,entry):
        self.id = entry[0]
        self.gender = entry[1]
        self.birth_date = datetime.strptime(entry[2], '%Y-%m-%d %H:%M:%S.%f')
        self.race = entry[3]
        self.MS = entry[4]
        self.language = entry[5]
        self.population_underproverty = entry[6]

    #instance attributes
    def __int__(self,id,gender,birth_date, race,MS,language,population_underproverty):
        self.id=id
        self.gender=gender
        self.birth_date=birth_date
        self.race=race
        self.MS=MS
        self.language=language
        self.population_underproverty=population_underproverty

    #read in converted data from original file
    def readlab(self, labs_file):
        with open(labs_file) as labs_table:
            labfile = [line.replace('\n', '').split('\t') for line in labs_table]
        sickness = [row for row in labfile if row[0] == self.id]
        self.sickness = sickness

    def getsick(self):
        return self.sickness

    def getid(self):
        return self.id

    def getage(self):
        num = round((datetime.now() - self.birth_date).days / 365, 1)
        return num

    def getgender(self):
        return self.gender

    def getrace(self):
        return self.race

    def __lt__(self, other):
        if type(other) == int or type(other) == float:
            return self.age < other
        else:
            return self.age < other.age

    def __gt__(self, other):
        if type(other) == int or type(other) == float:
            return self.age > other
        else:
            return self.age > other.age

    def plot(self, sick):
        values = [row[3] for row in self.sickness if row[2] == sick]
        # yr = [row[5][:4] for row in self.sickness if row[2]==sick]
        plt.plot(values)
        plt.title(self.id + '\n' + sick)
        plt.show()

    ID = property(getid)
    age = property(getage)
