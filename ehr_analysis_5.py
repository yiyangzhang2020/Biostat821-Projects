from datetime import datetime
from flask import Flask, jsonify, request
from urllib.request import urlopen

def load_patients(url):
    patients = [str(line)[2:-1].replace('\\r\\n', '').split('\\t') for line in urlopen(url)][1:]
    patient_id = [patient[0] for patient in patients]
    info = ['gender', 'DOB', 'race', 'marital_status', 'language', 'population_percentage_below_poverty']
    patient_info = [patient[1:] for patient in patients]
    patient_info_dic = [dict(zip(info, item)) for item in patient_info]
    for info in patient_info_dic:
        info['DOB'] = datetime.strptime(info['DOB'], '%Y-%m-%d %H:%M:%S.%f')
    patient_dic = dict(zip(patient_id, patient_info_dic))
    return patient_dic


def load_labs(url):
    labs = [str(line)[2:-1].replace('\\r\\n', '').split('\\t') for line in urlopen('http://biostat821.colab.duke.edu/labs.txt')][1:]
    patient_id = [lab[0] for lab in labs]
    info = ['admission_id', 'name', 'value', 'units', 'datetime']
    lab_info = [lab[1:] for lab in labs]
    lab_info_dic = [dict(zip(info, item)) for item in lab_info]
    for info in lab_info_dic:
        info['datetime'] = datetime.strptime(info['datetime'], '%Y-%m-%d %H:%M:%S.%f')
    lab_dic = dict()
    for patient, lab in zip(patient_id, lab_info_dic):
        lab_dic.setdefault(patient, []).append(lab)
    return lab_dic

ehr = Flask(__name__)

@ehr.route('/patients', methods=['POST'])
def patients():
    url = list(request.form.to_dict().keys())[0][9:-2]
    global patient_dic
    patient_dic = load_patients(url)
    return '==success=='

@ehr.route('/labs', methods=['POST'])
def labs():
    url = list(request.form.to_dict().keys())[0][9:-2]
    global lab_dic
    lab_dic = load_labs(url)
    return '==success=='

@ehr.route('/patients/<patient_id>', methods=['GET'])
def patient(patient_id):
    return jsonify(patient_dic[patient_id])

@ehr.route('/patients/<patient_id>/labs', methods=['GET'])
def lab(patient_id):
    return jsonify(lab_dic[patient_id])

@ehr.route('/num_older_than', methods=['GET'])
def num_older_than():
    ref_age = request.args['age']
    num = 0
    for patient_info_dic in patient_dic.values():
        if round((datetime.now() - patient_info_dic['DOB']).days / 365, 1)>float(ref_age):
            num += 1
    return jsonify(num)

@ehr.route('/sick_patients', methods=['GET'])
def sick_patients():
    sick_patients = []
    lab_name = request.args['lab_name']
    operator = request.args['operator']
    lab_value = request.args['lab_value']
    for patient, labs in lab_dic.items():
        for lab in labs:
            if lab['name']==lab_name and eval(lab['value']+operator+lab_value):
                sick_patients.append(patient)
    return jsonify(sick_patients)

if __name__=='__main__':
    ehr.run(debug=True)