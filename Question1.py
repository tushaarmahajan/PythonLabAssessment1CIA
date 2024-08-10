#Defining the function
def reconstruct_path(ordered_part, jumbled_part):
    correct_order = ['Start', 'Clearing', 'River', 'Village', 'Cave']
    result = []

    for landmark in correct_order:
        if landmark in ordered_part:
            result.append(landmark)
        elif landmark in jumbled_part:
            result.append(landmark)
    
    return result

#Putting in the given lists
ordered_part = ['Start', 'River']
jumbled_part = ['Clearing', 'Village', 'Cave']

#Reconstructing the path
path = reconstruct_path(ordered_part, jumbled_part)
print("Correct path:", path)
