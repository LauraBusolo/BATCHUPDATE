#-------------------------------------------------------------------------------
# Name:        Batch Processing
# Purpose:
"""Create field to shp or fc, then Copy/Update feature class/shp to a different source/fgdb
"""

# Author:      Laura
#
# Created:     04/01/2018
#-------------------------------------------------------------------------------

#Importing modules
import arcpy

#Setting up workspace
##arcpy.env.workspace = r"C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb"
arcpy.env.workspace = raw_input("Please enter the path of your workspace")
##input_table = r"C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Test Data\CitiesTestShp\Cities2015.shp"
input_table = raw_input("Please enter the path of your input shapefile")
arcpy.overwriteOutput = True

#Setting variables
field_name = "BatchID"
field_type = "TEXT"
##field_precision = 10
##field_scale = 0
field_length = 10
field_is_nullable = "NON_NULLABLE "
field_is_required = "REQUIRED"

#Adding New Field
try:
    arcpy.AddField_management (input_table, field_name, field_type, field_length)
    print field_name + " field was added successfully!"

except Exception as e:
    print e.message
    print "Error occurred while adding field"


##in_features = input_table
out_feature_class = "CitiesFC"
Output_Geodatabase = arcpy.env.workspace
##outWorkspace = "C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb"
##arcpy.CopyFeatures_management(in_features, out_feature_class)
#Copying features to destination db
if input_table in Output_Geodatabase:
    arcpy.overwriteOutput = True

else:
    try:
##        arcpy.FeatureClassToGeodatabase_conversion (input_table, Output_Geodatabase)
        arcpy.CopyFeatures_management (input_table, out_feature_class)
        print "Copy Features Complete!"
    except Exception as err:
        print err.message
        print "Error occurred while copying feature(s)"
