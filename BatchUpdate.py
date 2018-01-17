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


def copy_features(input_table, out_feature_class):
    try:
        if arcpy.Exists(out_feature_class):
            arcpy.Delete_management(out_feature_class)

##        arcpy.FeatureClassToGeodatabase_conversion (input_table, Output_Geodatabase)
#Methods for updating, e.g. Copy Features, Feature class conversion
        arcpy.CopyFeatures_management (input_table, out_feature_class)
        print "Copy Features Complete!"
    except Exception as err:
        print err.message
        print "Error occurred while copying feature(s)"

#Setting up workspace
##arcpy.env.workspace = r"C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb"
arcpy.env.workspace = raw_input("Please enter the path of your workspace")
##input_table = r"C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Test Data\CitiesTestShp\Cities2015.shp"
input_table = raw_input("Please enter the path of your input shapefile")
arcpy.overwriteOutput = True

#Setting variables
field_name = "BatchID"
copy_features()

#####Adding New Field
##try:
##    arcpy.AddField_management (input_table, field_name, field_type, field_length)
##    print field_name + " field was added successfully!"
##
##except Exception as e:
##    print e.message
##    print "Error occurred while adding field"


in_features = input_table
out_feature_class = "CitiesFC"
Output_Geodatabase = arcpy.env.workspace
##outWorkspace = "C:\Users\msgis-student\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb"
##arcpy.CopyFeatures_management(in_features, out_feature_class)
#Copying features to destination db


