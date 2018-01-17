# Name:        Batch Processing
# Purpose:
"""Create field to shp or fc, then Copy/Update feature class/shp to a different source/fgdb
"""

# Author:      Laura
#-------------------------------------------------------------------------------
#Importing modules
import arcpy

arcpy.env.workspace = r"C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb"
lyrUpdate_table = r"C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb\Layer_Update"
arcpy.overwriteOutput = True
field_names = ['BatchID', 'SourcePath', 'SourceName', 'TargetPath', 'TargetName', 'Method']
batch_Num = raw_input ("Please enter Batch ID: ")

#Define the copy features function
def copy_features(input_table, out_feature_class):
    print (input_table)
    print (out_feature_class)
    try:
        if arcpy.Exists(out_feature_class):
            arcpy.Delete_management(out_feature_class)

#Methods for updating, e.g. Copy Features, Feature class conversion
        arcpy.CopyFeatures_management (input_table, out_feature_class)
        print "Copy Features Complete!"
    except Exception as err:
        print err.message
        print "Error occurred while copying feature(s)"


#(Specify Query) Check table and access rows with BatchID as 1:
cursor = arcpy.da.SearchCursor(lyrUpdate_table, field_names, "\"BatchID\" = "+ str(batch_Num))

with arcpy.da.SearchCursor(lyrUpdate_table, field_names) as cursor:

    for row in cursor:
        #a = row.getValue("Batch_ID")
        #Access the data using indices, e.g BatchID's index is 0.
##        a = row [0]
        print row
        batch_id, source_path, source_name, target_path, target_name, method= row
        print ("C is "+ target_path)

        #Access data using tuple logic

        copy_features(source_path + '\\' + source_name, target_name)


#If Batch_ID == 1, execute copy features function

# Call the Copy features function

"""
- Add print statements, to show the steps, methods...
- try copying ny adding records to the table
"""
