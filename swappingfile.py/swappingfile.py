def swappingFiles():
    fileA=input("Enter the name of the first file")
    fileB=input("Enter the name of the second file")
    with open(fileA,'r') as a:
       data_a = a.read()
    with open(fileB,'r') as b:
        data_b = b.read()
    with open(fileA,'w') as a:
        a.write (data_b)
    with open(fileB,'w') as b:
        b.write (data_a)
swappingFiles()