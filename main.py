from datetime import datetime
import sqlite3

def load_patients(patients_file):
    with open(patients_file) as patient_table:
        return [line.replace('\n', '').split('\t') for line in patient_table][1:]


def load_labs(labs_file):
    with open(labs_file) as labs_table:
        return [line.replace('\n', '').split('\t') for line in labs_table][1:]


class Patient():
    global patients
    patients = load_patients('/Users/yiyangzhang/Desktop/Biostat821/ehr_analysis/PatientCorePopulatedTable.txt')

    def __init__(self, patientID):
        patientdb = sqlite3.connect('/Users/yiyangzhang/Desktop/Biostat821/ehr_analysis/patient.db')
        cursor = patientdb.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Patients(
            id TEXT PRIMARY KEY,
            gender TEXT NOT NULL,
            dob TIMESTAMP,
            race TEXT NOT NULL,
            marital_status TEXT NOT NULL,
            language TEXT NOT NULL,
            percentage_below_poverty NUMERIC
            )
        ''')
        for row in patients:
            cursor.execute(
                "INSERT OR REPLACE INTO Patients (id, gender, dob, race, marital_status, language, percentage_below_poverty) VALUES (?,?,?,?,?,?,?)", \
                (row[0], row[1], datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f'), row[3], row[4], row[5], row[6]))
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_id ON Patients (id)")
        cursor.execute("SELECT * FROM Patients INDEXED BY idx_id WHERE id=?", (patientID,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)


class Observation():
    global labs
    labs = load_labs('/Users/yiyangzhang/Desktop/Biostat821/ehr_analysis/LabsCorePopulatedTable.txt')

    def __init__(self, patientID):
        labdb = sqlite3.connect('/Users/yiyangzhang/Desktop/Biostat821/ehr_analysis/lab.db')
        cursor = labdb.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Labs(
            id TEXT NOT NULL,
            labname TEXT NOT NULL,
            labvalue NUMERIC,
            labunits TEXT NOT NULL,
            labdatetime TIMESTAMP
            )
        ''')
        for row in labs:
            cursor.execute(
                "INSERT OR REPLACE INTO Labs (id, labname, labvalue, labunits, labdatetime) VALUES (?,?,?,?,?)", \
                (row[0], row[2], row[3], row[4], datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S.%f')))
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_id ON Labs (id)")
        cursor.execute("SELECT * FROM Labs INDEXED BY idx_id WHERE id = ?", (patientID,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)


if __name__ == '__main__':
    Patient('6E70D84D-C75F-477C-BC37-9177C3698C66')
    Observation('6E70D84D-C75F-477C-BC37-9177C3698C66')


