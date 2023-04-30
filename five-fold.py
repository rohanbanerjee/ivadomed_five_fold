import random

# Set the number of subjects
num_subjects = 96

# Set the size of the train, validation, and test sets
train_size = int(num_subjects * 0.6)
val_size = int(num_subjects * 0.3)
test_size = num_subjects - train_size - val_size

# Shuffle the list of subjects
subjects = list(range(num_subjects))
random.shuffle(subjects)

# Split the subjects into train, validation, and test sets
train_set = subjects[:train_size]
val_set = subjects[train_size:train_size + val_size]
test_set = subjects[train_size + val_size:]

# Print the sizes of the sets
print(f"Train set size: {len(train_set)}")
print(f"Validation set size: {len(val_set)}")
print(f"Test set size: {len(test_set)}")

# Perform 5-fold cross-validation on the train set
kfold = 5
fold_size = int(len(train_set) / kfold)

for fold in range(kfold):
    fold_start = fold * fold_size
    fold_end = (fold + 1) * fold_size

    # Get the indices of the validation set for this fold
    val_indices = train_set[fold_start:fold_end]

    # Get the indices of the training set for this fold
    train_indices = [i for i in train_set if i not in val_indices]

    # Print the sizes of the training and validation sets for this fold
    print(train_indices)
    print(val_indices)
    print(f"Fold {fold+1}: Train set size = {len(train_indices)}, Validation set size = {len(val_indices)}")
