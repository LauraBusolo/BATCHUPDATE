#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      msgis-student
#
# Created:     17/01/2018
# Copyright:   (c) msgis-student 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Importing modules
import arcpy

#Define the copy features function
def copy_features(input_table, out_feature_class):
    try:
        if arcpy.Exists(out_feature_class):
            arcpy.Delete_management(out_feature_class)

#Methods for updating, e.g. Copy Features, Feature class conversion
        arcpy.CopyFeatures_management (input_table, out_feature_class)
        print "Copy Features Complete!"
    except Exception as err:
        print err.message
        print "Error occurred while copying feature(s)"

#Setting up workspace
arcpy.env.workspace = r"C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb"
#arcpy.env.workspace = raw_input("Please enter the path of your workspace")
input_table = r"C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb\Layer_Update"
#input_table = raw_input("Please enter the path of your input table")
arcpy.overwriteOutput = True
field_names = ['BatchID', 'SourcePath', 'SourceName', 'TargetPath', 'TargetName', 'Method']
batch_Num = 'BatchID'
t_fieldList= arcpy.ListFields (input_table)

###Get field names from in_table
##for field in t_fieldList:
##    print field.name

##BatchID_Entry = raw_input('Please enter Batch ID: ')

###Creating the search cursor to read throw the rows in the table
##rows = arcpy.da.SearchCursor(in_table)
## Call SearchCursor.next() to read the first row
##row = rows.next()
##
##while row:
##    print row.BatchID
##    row = rows.next()

#(Specify Query) Check table and access rows with BatchID as 1:
cursor = arcpy.da.SearchCursor(input_table, field_names, "\"Batch_ID\" = 1")


with arcpy.da.SearchCursor(input_table, field_names) as cursor:

    for row in cursor:
        print "Access granted"



###Get Field names from table
##TableFields = arcpy.ListFields (in_table)
##for field in TableFields:
##    print field.name

#If Batch_ID == 1, execute copy features function

# Call the Copy features function

#copy_features()
