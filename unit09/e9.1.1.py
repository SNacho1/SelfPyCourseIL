def are_files_equal(file1, file2):
    f1 = open(file1, "r")
    f1_content = f1.read()
    f1.close()

    f2 = open(file2, "r")
    f2_content = f2.read()
    f2.close()

    if f1_content == f2_content:
        return True
    else:
        return False

    
print(are_files_equal("unit09/myFile1.txt", "unit09/myFile2.txt"))
