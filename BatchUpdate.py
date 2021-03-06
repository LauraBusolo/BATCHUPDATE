# Name: Batch Processing
# Purpose:
"""
    Use an update table as a directory for source and target data.
    Then use a batch ID to Copy feature classes/shapefiles to a different source/fgdb
    Get the count of features in the source and target file, checking if the difference is >20%
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

#opening a dataset in target GDB
outt = r"C:\Users\Laura\Documents\Quartic solutions\Batch Processing\backupShps"
out_dataset_path = r".\Batch Processing.gdb"
out_nameFD = "newFD"
CoordSys = r"C:\Users\Laura\Documents\Quartic solutions\Batch Processing\Test Data\test1.gdb\SanTest\SDiegoCity_1"

#Define the copy features function
def copy_features(input_table, out_feature_class):
    print ("Checking if feature(s) exist in the database...\n")
    try:
        if arcpy.Exists(out_feature_class):
            arcpy.Delete_management(out_feature_class)

        # creating a new Feature dataset, "newFD", if it doesn't exist
        if not arcpy.Exists(out_nameFD):
            arcpy.CreateFeatureDataset_management(out_dataset_path, out_nameFD, CoordSys)

        # Methods for updating, e.g. Copy Features, Feature class conversion
        arcpy.CopyFeatures_management(input_table, out_feature_class)
        print ("Copying features...\n")
        print ("Copy Features Complete!\n")
    except Exception as err:
        print err.message
        print ("Error occurred while copying feature(s)\n")

#Define the count features function
def countRows(input_table, out_feature_class):
    print ("Counting the rows ...\n")
    print ("Source data: " + input_table + ", Copied/target data: " + out_feature_class)
    rows = arcpy.SearchCursor(input_table)
    row = rows.next()
    #input_table_result is the source data
    input_table_result = 0
    while row:
        input_table_result += 1
        row = rows.next()
    print ("There are " + str(input_table_result) + " features in the source data\n")
    rows2 = arcpy.SearchCursor(out_feature_class)
    row2 = rows2.next()
    #out_feature_class_result is the target data
    out_feature_class_result = 0
    while row2:
        out_feature_class_result += 1
        row2 = rows2.next()
    print ("There are " + str(out_feature_class_result) + " features in the Copied/target data\n")

    result_difference = int(input_table_result) - int(out_feature_class_result)
    result_ratio = (result_difference / out_feature_class_result) * 100
    if result_ratio < 20.00:

        print ("Not much changes")
    else:

        print ("The data has over 20% changes")

#(Specify Query) Check table and access rows with the input Batch ID as 1,2...n:
def iterate_update_table(table_Lyr, flds, btch_num):
    process_success = False

    #Check in the current working directory to see if the backupShps folder exists. If not, create it.
    dirr = os.getcwd()
    if not os.path.exists(dirr + '\\backupShps'):
        os.mkdir(dirr + '\\backupShps')

    print ("Checking the table rows using the Search cursor...\n")
    with arcpy.da.UpdateCursor(table_Lyr, flds, "\"BatchID\" = "+ str(btch_num)) as cursor:

        for row in cursor:
            #Setting up the row/field name variables, e.g. batch_id is BatchID...
            batch_id, source_path, source_name, target_path, target_name, method, last_update= row
            print ("This, "+ target_path + (" is the target path"))

            #Access data using tuple logic
            if batch_id == int(btch_num):

                print ("Computing the difference...\n")
                if arcpy.Exists(target_path + '\\' + target_name):
                    countRows(source_path + '\\' + source_name, target_path + '\\' + target_name)

                print ("Executing the copy features function...\n")
                copy_features(source_path + '\\' + source_name, target_name)
                #copy the copied data into a folder called backupShps, to be used later to compare data counts between the source and destination.
                copy_features(source_path + '\\' + source_name, outt + '\\' + target_name + ".shp")

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
        count += 1

        batch_Num = raw_input ("Please enter a valid Batch ID: ")
        success = iterate_update_table(LYR_UPDATE_TABLE, FIELD_NAMES, batch_Num)

        if success:
            break
        elif count == 3:
            break
        else:
            print("invalid entry")

    print("yay! completed!")