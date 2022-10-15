#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Claire Elias (claire.elias@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#Create a variable point to the data file
file_name = 'data/raw/Sara.txt'

#Create a file object from the filename
file_object = open(file=file_name,mode='r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file object
file_object.close()

#Extract one data line into a variable
for lineString in line_list:

    #Check to see if the lineString is a data line
    if lineString[0] == '#' or lineString[0] == 'u':
        continue
    
    #Split lineString into a list of items
    lineData = lineString.split()
    
    #Assign variables to items in the lineData list
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #Print information to the user
    print(f'Record {record_id} indicates Sara was seet and {obs_lat}N, {obs_lon}W  on {obs_date}. ')

    # check to see if the lineString is a data line
    if lineString[0] == '#':

    # use the split command to parse the items in lineString into a list obj
    lineData = lineString.split()
    
    # Assign variables to specific items in the list
    record_id = lineData[0]    # ARGOS tracking record ID
    obs_date = lineData[2]    # Observation date
    obs_lc = lineData[4]          # Observation location class
    obs_lat = lineData[6]      # Observation latitude
    obs_lon = lineData[7]      # Observation longitude 

# Print information to the user
    print(f'Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}')
