import os
def find_existing_strafe():
    output = os.popen('wmic process get description, processid').read()
    print(output)


find_existing_strafe()
