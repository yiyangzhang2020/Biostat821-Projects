import ehr_analysis

def test_num_older_than():
    ''' 
	   A test function that checks whether the num_older_than function returns the correct number 
       We used a sample output from ehr_analysis
    ''' 
    assert ehr_analysis.num_older_than(ehr_analysis.patients, 50) == 77

def test_sick_patients():
    ''' 
	   A test function that checks whether the sick_patients function returns the correct list of patient IDs 
       We compared the length of the output list to the actual number of list in the labs dataframe
    ''' 
    assert len(ehr_analysis.sick_patients(ehr_analysis.labs, 'METABOLIC: ALBUMIN', '>', 5.9))==42

def test_load_patients():
    ''' 
	   A test function that checks whether the load_patients function reads in the dataset or not 
       We used a sample list from the original dataset to check if it was included in the sample output
       We alse compared the length of the sample output data to the actual number of datasets from the original dataframe
    ''' 
    assert ['64182B95-EB72-4E2B-BE77-8050B71498CE', 'Male', '1952-01-18 19:51:12.917', 'African American', 'Separated', 'English', '13.03'] in ehr_analysis.patients
    assert len(ehr_analysis.patients)==101

def test_load_labs():
    ''' 
	   A test function that checks whether the load_patients function reads in the dataset or not 
       We used a sample list from the original dataset to check if it was included in the sample output
       We alse compared the length of the sample output data to the actual number of datasets from the original dataframe
    ''' 
    assert ['1A8791E3-A61C-455A-8DEE-763EB90C9B2C', '1', 'CBC: MCH', '35.8', 'pg', '1992-06-30 03:50:11.777'] in ehr_analysis.labs
    assert len(ehr_analysis.labs)==111484

def test_age_calc():
    ''' 
	   A test function that checks whether it returns the age of a given patient
       We used a sample patient ID from the original dataset to check if it outputs the correct age of the person
    '''
    assert ehr_analysis.age_calc(ehr_analysis.patients,'FB2ABB23-C9D0-4D09-8464-49BF0B982F0F')==74
