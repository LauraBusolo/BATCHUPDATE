# Name:        Batch Processing
# Purpose:
"""Create field to shp or fc, then Copy/Update feature class/shp to a different source/fgdb
"""

# Author:      Laura
#-------------------------------------------------------------------------------
#Importing modules
import arcpy

print ("Setting up workspace...\n")
arcpy.env.workspace = r"C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb"
arcpy.overwriteOutput = True
#Setting up global variables
lyrUpdate_table = r"C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb\Layer_Update"
field_names = ['BatchID', 'SourcePath', 'SourceName', 'TargetPath', 'TargetName', 'Method']
batch_Num = raw_input ("Please enter Batch ID: ")

#Define the copy features function
def copy_features(input_table, out_feature_class):
##    print (input_table)
##    print (out_feature_class)
    print ("Checking if feature(s) exist in the database...\n")
    try:
        if arcpy.Exists(out_feature_class):
            arcpy.Delete_management(out_feature_class)

#Methods for updating, e.g. Copy Features, Feature class conversion
        print ("Copying features...\n")
        arcpy.CopyFeatures_management (input_table, out_feature_class)
        print ("Copy Features Complete!\n")
    except Exception as err:
        print err.message
        print ("Error occurred while copying feature(s)\n")


#(Specify Query) Check table and access rows with the input Batch ID as 1:
cursor = arcpy.da.SearchCursor(lyrUpdate_table, field_names, "\"BatchID\" = "+ str(batch_Num))

print ("Checking the table rows using the Search cursor...\n")
with arcpy.da.SearchCursor(lyrUpdate_table, field_names) as cursor:

    for row in cursor:
        #a = row.getValue("Batch_ID")
        #Access the data using indices, e.g BatchID's index is 0.
##        a = row [0]
##        print row
        #Setting up the row/field name variables...
        batch_id, source_path, source_name, target_path, target_name, method= row
        print ("C is the "+ target_path)

        #Access data using tuple logic
        print ("Executing the copy features function...\n")
        copy_features(source_path + '\\' + source_name, target_name)
        print ("Successfully copied features_o_ _o_ _o_")


#If Batch_ID == 1, execute copy features function

# Call the Copy features function

"""
- Add print statements, to show the steps, methods...
- try adding more records to the table.
"""
