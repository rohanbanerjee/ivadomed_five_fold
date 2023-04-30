import os
from numpy import savetxt
def find_missing_contents(dir1, dir2):
    """
    Finds the missing contents of dir1 compared to dir2.

    Parameters:
    dir1 (str): The path to the first directory -- one of the fold directory.
    dir2 (str): The path to the second directory -- original directory.

    Returns:
    A list of filenames that are in dir2 but not in dir1.
    """
    # Get the list of filenames in dir1 and dir2
    dir1_files = os.listdir(dir1)
    dir2_files = os.listdir(dir2)

    # Get the set of filenames in dir2 that are not in dir1
    missing_files = set(dir2_files) - set(dir1_files)
    print(len(set(dir2_files)))

    # Return the list of missing filenames
    print(list(missing_files))
    print(len(list(missing_files)))
    with open("5.txt", "w") as output:
        output.write(str(list(missing_files)))

find_missing_contents("/home/GRAMES.POLYMTL.CA/robana/duke/temp/rohan/data_training_human_sc_csf/data_train_val_5", "/home/GRAMES.POLYMTL.CA/robana/duke/temp/rohan/data_training_human_sc_csf/preprocessed_data_corrected")