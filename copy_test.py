import os
import shutil
import ast



with open('/home/GRAMES.POLYMTL.CA/robana/duke/temp/rohan/data_training_human_sc_csf/scripts/5.txt') as f:
    data = f.read()
    res = ast.literal_eval(data)
    data_into_list = data.split(",")


    for i in range(len(res)):
        if res[i].find("sub") != -1:
            print(res[i])
            os.system("cp /home/GRAMES.POLYMTL.CA/robana/duke/temp/rohan/data_training_human_sc_csf/preprocessed_data_corrected/" + res[i] + "/func/" + res[i] + "_task-rest_bold.nii.gz /home/GRAMES.POLYMTL.CA/robana/duke/temp/rohan/data_training_human_sc_csf/test_5/")