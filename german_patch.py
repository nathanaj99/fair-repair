import pandas as pd
import numpy as np
import itertools
import argparse
import os.path
import random
import time

import eutil
import patch

########################################################
# Constrants for German dataset
########################################################

# Select categorical attributes
cols = [
    'CheckingAccountStatus',
    #'Duration',
    'CreditHistory',
    'Purpose',
    #'CreditAmount',
    'Savings',
    'EmploymentSince',
    #'InstallmentRate',
    'Sex',
    'OtherDebtors',
    #'ResidenceSince',
    'Property',
    #'Age',
    'OtherInstallmentPlans',
    'Housing',
    #'CreditsAtBank',
    'Job',
    #'NumDependents',
    'Telephone',
    'ForeignWorker',
    #'Class'
]

# Get all attributes, continuous and discrete.
Duration = 'Duration'
CreditAmount = 'CreditAmount'
InstallmentRate = 'InstallmentRate'
ResidenceSince = 'ResidenceSince'
Age = 'Age'
CreditsAtBank = 'CreditsAtBank'
NumDependents = 'NumDependents'
CheckingAccountStatus = ['CheckingAccountStatus_A11', 'CheckingAccountStatus_A12', 'CheckingAccountStatus_A13', 'CheckingAccountStatus_A14']
CreditHistory = ['CreditHistory_A30', 'CreditHistory_A31', 'CreditHistory_A32', 'CreditHistory_A33', 'CreditHistory_A34']
Purpose = ['Purpose_A40', 'Purpose_A41', 'Purpose_A42', 'Purpose_A43', 'Purpose_A44', 'Purpose_A45', 'Purpose_A46', 'Purpose_A48', 'Purpose_A49', 'Purpose_A410']
Savings = ['Savings_A61', 'Savings_A62', 'Savings_A63', 'Savings_A64', 'Savings_A65']
EmploymentSince = ['EmploymentSince_A71', 'EmploymentSince_A72', 'EmploymentSince_A73', 'EmploymentSince_A74', 'EmploymentSince_A75']
Sex = ['Sex_A91', 'Sex_A92', 'Sex_A93', 'Sex_A94']
OtherDebtors = ['OtherDebtors_A101', 'OtherDebtors_A102', 'OtherDebtors_A103']
Property = ['Property_A121', 'Property_A122', 'Property_A123', 'Property_A124']
OtherInstallmentPlans = ['OtherInstallmentPlans_A141', 'OtherInstallmentPlans_A142', 'OtherInstallmentPlans_A143']
Housing = ['Housing_A151', 'Housing_A152', 'Housing_A153']
Job = ['Job_A171', 'Job_A172', 'Job_A173', 'Job_A174']
Telephone = ['Telephone_A191', 'Telephone_A192']
ForeignWorker = ['ForeignWorker_A201', 'ForeignWorker_A202']

classes = (1,2)

# Gather all attributes into a map
attr_map = {
    'Duration': Duration ,
    'CreditAmount': CreditAmount ,
    'InstallmentRate': InstallmentRate ,
    'ResidenceSince': ResidenceSince ,
    'Age': Age ,
    'CreditsAtBank': CreditsAtBank ,
    'NumDependents': NumDependents ,
    'CheckingAccountStatus' : CheckingAccountStatus,
    'CreditHistory' : CreditHistory,
    'Purpose' : Purpose,
    'Savings' : Savings,
    'EmploymentSince' : EmploymentSince,
    'Sex' : Sex,
    'OtherDebtors' : OtherDebtors,
    'Property' : Property,
    'OtherInstallmentPlans' : OtherInstallmentPlans,
    'Housing' : Housing,
    'Job' : Job,
    'Telephone' : Telephone,
    'ForeignWorker' : ForeignWorker,
}

# Some pre-defined refinement heuristics
refineHeuristics = [(Property, True), (Purpose, True), (Job, True),
                    (CreditHistory, True), (CheckingAccountStatus, True),
                    (Savings, True), (OtherInstallmentPlans, True),
                    (Age, False), (Duration, False), (CreditAmount, False),
                    (Age, False), (Duration, False), (CreditAmount, False),
                    (Age, False), (Duration, False), (CreditAmount, False)
                    ]
########################################################

def parse_args():
    parser = eutil.create_base_parser(
        description='Patch German dataset.',
        sensitive_attrs_default = "['Sex']",
        dataset_default = 'german.data')
    args = parser.parse_args()
    evalu = eutil.EvalUtil(args)
    random.seed(args.random_seed)
    return evalu


if __name__ == '__main__':
    evalu = parse_args()
    patch.patch(evalu, cols, refineHeuristics, attr_map,classes)
    # reformed_tree_string = patch.patch(evalu, cols, refineHeuristics, attr_map,classes)
    # reformed_classifier = convert_string_classifier(reformed_tree_string)
    # # test data: X_test, Y_test
    # Y_test_predictions = reformed_classifier(X_test)
    # # we can compute Y_test and Y_pred accuracy and the passing rates
    evalu.save_vals()
