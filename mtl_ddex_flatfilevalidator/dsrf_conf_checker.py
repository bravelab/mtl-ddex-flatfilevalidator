#!/usr/bin/env python3
import os
import sys
import subprocess

def main():
    print("\ndsrf-conf.py -- tool to check conformance of a DSRF file.")
    print("(c) 2016 Digital Data Exchange, LLC, utilising Google's dsrf library\n")

    # Set variables (filelist being the alphabetical list of input files)
    validator = "dsrf"
    parser = os.path.join(validator, "run_dsrf.py")
    conformance = os.path.join(validator, "conformance/conformance_processor.py")
    log = "/tmp/example.log"
    log2 = "/tmp/example2.log"
    usage = "Please use the script as follows:\n\tdsrfconf.py FILE [FILE*]\nProgram aborted"
    filelist = sorted(sys.argv[1:])
    filecount = len(filelist)
    profile = ""

    # Check if at least one file has been given and that all files exist
    if filecount < 1:
        sys.exit(f"No file to process. {usage}")
    
    for file in filelist:
        if not os.path.isfile(file):
            sys.exit(f"File '{file}' does not exist. {usage}")

    # Open the first file and obtain the profile
    with open(filelist[0], 'r') as file:
        for line in file:
            line = line.lstrip()  # remove leading spaces
            if line.startswith("HEAD"):
                fields = line.split("\t")
                profile = fields[2]
                break

    # End validation if there is no profile
    if not profile:
        print(f"No profile given in {filelist[0]}\nConformance cannot be tested")
        with open(f"{filelist[0]}.log", 'w') as logfile:
            logfile.write(f"No profile given in {filelist[0]}\nConformance cannot be tested\n")
        sys.exit()

    print(f"Checking input file(s) against the {profile} profile:\n\n")
    profile = profile.replace(" ", "")  # Remove all spaces from the profile name

    # Run the system commands
    with open(log2, 'w') as log2file:
        subprocess.run(["python", parser] + filelist, stdout=subprocess.PIPE, check=True)
        subprocess.run(["python", conformance], stdin=subprocess.PIPE, stdout=log2file, check=True)
    
    # Concatenate logs and clean up
    with open(f"{filelist[0]}.log", 'w') as final_log, open(log, 'r') as log1, open(log2, 'r') as log2file:
        final_log.write(log1.read())
        final_log.write(log2file.read())

    os.remove(log)
    os.remove(log2)
    print(f"\n\nAll done. Results are in {filelist[0]}.log\n")

if __name__ == "__main__":
    main()