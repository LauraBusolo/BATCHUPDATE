# Name:        Batch Processing
# Purpose:
"""Use an update table as a directory for source and target data. Then use a batch ID to Copy/Update feature class/shapefiles to a different source/fgdb
"""

# Author:      Laura
#-------------------------------------------------------------------------------
#Importing modules
import arcpy
import os
import datetime

print ("Setting up workspace...\n")
arcpy.env.workspace = r".\Batch Processing.gdb"
arcpy.overwriteOutput = True
#Setting up global variables
LYR_UPDATE_TABLE = r".\Batch Processing.gdb\Layer_Update"
FIELD_NAMES = ['BatchID', 'SourcePath', 'SourceName', 'TargetPath', 'TargetName', 'Method', 'LastUpdate']

#Define the copy features function
def copy_features(input_table, out_feature_class):
    print ("Checking if feature(s) exist in the database...\n")
    try:
        if arcpy.Exists(out_feature_class):
            arcpy.Delete_management(out_feature_class)

        # Methods for updating, e.g. Copy Features, Feature class conversion
        arcpy.CopyFeatures_management (input_table, out_feature_class)
        print ("Copying features...\n")
        print ("Copy Features Complete!\n")
    except Exception as err:
        print err.message
        print ("Error occurred while copying feature(s)\n")

#(Specify Query) Check table and access rows with the input Batch ID as 1,2...n:
def iterate_update_table(table_Lyr, flds, btch_num):
    process_success = False

    print ("Checking the table rows using the Search cursor...\n")
    with arcpy.da.UpdateCursor(table_Lyr, flds, "\"BatchID\" = "+ str(btch_num)) as cursor:

        for row in cursor:
            #Setting up the row/field name variables, e.g. batch_id is BatchID...
            batch_id, source_path, source_name, target_path, target_name, method, last_update= row
            print ("This, "+ target_path + (" is the target path"))

# #-----------------Testing the copy feature dataset code------------
#             #Copy Feature dataset- features
#             try:
#             #if batchid == 4----------#testing with batch ID 4 since it is a feature dataset
#                 if arcpy.Exists(source_name):
#                     arcpy.Delete_management(source_name)
#                 elif batch_id == int(btch_num):
#                     ds = arcpy.ListFeatureClasses('','', source_name)
#                     for fc in ds:
#                         print ('These features') + (fc) + (' are in the feature dataset!')
#                         arcpy.CopyFeatures_management(fc, os.path.join(target_path, os.path.splitext(fc)[0]))
#             except Exception as dt_err:
#                 print ("Sorry! did not copy features in dataset.")
#                 print (dt_err)

#             # if batch_id == 4:
#             if batch_id == int(btch_num):
#                 ds = arcpy.ListFeatureClasses('','', source_name)
#                 for i in ds:
#                     arcpy.CopyFeatures_management(
#                     #i, os.path.join(r"C:\Users\Laura\Documents\Quartic solutions\Batch Processing\Batch Processing.gdb", os.path.splitext(i)[0]))
#                     i, os.path.join(target_path, os.path.splitext(i)[0]))
# #-----------------------end of test-----------------


            #Access data using tuple logic
            if batch_id == int(btch_num):
                print ("Executing the copy features function...\n")
                copy_features(source_path + '\\' + source_name, target_name)
                print ("Successfully copied features_o_ _o_ _o_")
                process_success = True

                #Update the current date of the features copied
                row [6] = datetime.datetime.strftime(datetime.date.today(),"%Y-%m-%d")
                cursor.updateRow(row)

                print ("Success!")
            else:
                print ("The Batch ID you entered does not exist. Please try again.")
                process_success = False

    return process_success

# ------ APPLICATION MAIN ------

if __name__ == '__main__':
    count = 0
    #loop through the process 3 times to check whether the user's batch id input exists. Afterwhich, the script exists
    while True:
        count +=1

        batch_Num = raw_input ("Please enter a valid Batch ID: ")
        success = iterate_update_table(LYR_UPDATE_TABLE, FIELD_NAMES, batch_Num)

        if (success):
            break
        elif count == 3:
            break
        else:
            print("invalid entry")

    print("yay! completed!")