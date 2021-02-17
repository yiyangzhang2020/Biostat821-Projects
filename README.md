# Biostat821-Projects

A Python module that provides some simple analytical capabilities on some (synthetic) EHR data.
Example data are provided as:
* A table of patients with demographic data: `PatientCorePopulatedTable.txt`
* A table of laboratory results: `LabsCorePopulatedTable.txt`

End user guide:
* setup/installation instructions, including information about the expected input file formats

Input data files should be in the format of txt files. 

* API description: 

System will ask user to enter a index age for the num_older_than function, input that is not a integar will result in a raise of TypeError. 

System will ask user to enter a index value for the sick_patients function, input that is not a float will result in a raise of TypeError. 

System will ask user to enter a lab name and a comparison symbol(< or >) for the sick_patients function, unvalid input will result in a raise of ValueError. 


* Examples
```python
>> patients = load_patients("PatientCorePopulatedTable.txt")
>> num_older_than(patients, 51.2)
52
>> labs = labs_patients("PatientCorePopulatedTable.txt")
>> sick_patients(labs, 'METABOLIC: ALBUMIN', '>', 5.8)
'1A8791E3-A61C-455A-8DEE-763EB90C9B2C', '1', 'METABOLIC: ALBUMIN', '5.9', 'pg', '1992-06-30 03:50:11.777'
```

*Testing instructions

test_ehr_analysis.py is a suite of tests using the 'pytest' framework for all four functions in ehr_analysis.py.

Testing functions include testing length of output and sample output, and values of output and sample output.

All 4 tests should pass, any change of sample output should result in a failed test. 
