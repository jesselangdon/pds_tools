# -*- coding: utf-8 -*-
# Toolbox Name:     PDSTools.pyt
# Description:      PDS Tools is a Python toolbox written for ArcGIS Desktop, which includes custom tools that can perform
#                   basic data management tasks with ESRI geodatabases and MXD files.
# Dependencies:     arcpy, ArcGIS Desktop 10.x, Python 2.7
# Author:           Jesse Langdon
# Org:              Snohomish County Planning and Development Services (PDS)
# Date Created:     8/24/2022
# Date Modified:    11/14/2022


# Import modules
import os
import csv
import sys

import arcpy


# Declare Python Toolbox class
class Toolbox(object):
    def __init__(self):
        """PDS Tools init method"""
        self.label = "PDS Tools"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [MXDInventoryTool, GDBInventoryTool, ReplicaInventoryTool, GetDomainsTool, CleanGeodatabaseTool]


class MXDInventoryTool(object):
    def __init__(self):
        """MXD Inventory."""
        self.label = "MXD Inventory"
        self.description = "The MXD Inventory Tool will find all MXDs in a user-specified folder (top level) and " \
                           "return a CSV file with details on each layer found in each MXD."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input folder",
            name="input_workspace",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")

        param1 = arcpy.Parameter(
            displayName="Output CSV file",
            name="output_csv",
            datatype="DEFile",
            parameterType="Required",
            direction="Output"
        )
        param1.filter.list = ['txt', 'csv']

        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed. This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        mxd_inventory(parameters[0].valueAsText, parameters[1].valueAsText)
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return


class GDBInventoryTool(object):
    def __init__(self):
        """GDB Inventory class"""
        self.label = "GDB Inventory"
        self.description = "The GDB Inventory Tool searches through a user-specified enterprise geodatabase and " \
                           "returns a CSV file with details on each layer found in the geodatabase."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input SDE connection",
            name="input_sde_conn",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")
        param0.filter.list = ['Remote Database']

        param1 = arcpy.Parameter(
            displayName="Output CSV file",
            name="output_csv",
            datatype="DEFile",
            parameterType="Required",
            direction="Output")
        param1.filter.list = ['txt', 'csv']

        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed. This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        gdb_inventory(parameters[0].valueAsText, parameters[1].valueAsText)
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return


class ReplicaInventoryTool(object):
    def __init__(self):
        """Replica Inventory class"""
        self.label = "Replica Inventory"
        self.description = "The Replica Inventory Tool searches through a user-specified enterprise geodatabase and " \
                           "returns a CSV file with details on each sync replica object found in the geodatabase."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input SDE connection",
            name="input_sde_conn",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")
        param0.filter.list = ['Remote Database']

        param1 = arcpy.Parameter(
            displayName="Output CSV file",
            name="output_csv",
            datatype="DEFile",
            parameterType="Required",
            direction="Output")
        param1.filter.list = ['txt', 'csv']

        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed. This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        replica_inventory(parameters[0].valueAsText, parameters[1].valueAsText)
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return


class CleanGeodatabaseTool(object):
    def __init__(self):
        """Replica Inventory class"""
        self.label = "Clean Geodatabase"
        self.description = "The Clean Geodatabase Tool removes datasets, feature classes, rasters, and table objects" \
                           "from a user-supplied geodatabase."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input geodatabase",
            name="input_workspace",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")
        param0.filter.list = ['Remote Database', 'Local Database']

        param1 = arcpy.Parameter(
            displayName="Output log file",
            name="log_file",
            datatype="DEFile",
            parameterType="Required",
            direction="Output")
        param1.filter.list = ['txt']

        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed. This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        clean_gdb(input_workspace=parameters[0].valueAsText, log_file=parameters[1].valueAsText)
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return


class GetDomainsTool(object):
    def __init__(self):
        """Inventory domains class"""
        self.label = "Get Domains"
        self.description = "The Get Domains tool produces a CSV file listing feature classes, field " \
                           "names, and domains associated with those fields in a geodatabase."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="Input geodatabase",
            name="input_workspace",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input")
        param0.filter.list = ['Remote Database', 'Local Database']

        param1 = arcpy.Parameter(
            displayName="Output CSV file",
            name="output_csv",
            datatype="DEFile",
            parameterType="Required",
            direction="Output")
        param1.filter.list = ['csv', 'txt']

        params = [param0, param1]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed. This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        get_domains(input_workspace=parameters[0].valueAsText, output_csv=parameters[1].valueAsText)
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return


def mxd_inventory(input_workspace, output_csv):
    """This function performs the processing for the MXD Inventory tool.
    :param input_workspace: directory with MXDs to be searched. Subdirectories are not searched.
    :param output_csv: name of the output CSV file with found layer information as rows.
    """
    # Initiate variables
    mxd_list = []
    layer_list = []

    # get list of all MXDs in user-specified filepath
    arcpy.AddMessage("Found the following MXD files in {}:".format(input_workspace))
    for file in os.listdir(input_workspace):
        if file.endswith(".mxd"):
            mxd_path = os.path.join(input_workspace, file)
            arcpy.AddMessage("    ...{}".format(file))
            mxd_list.append(mxd_path)

    # open each MXD and find layers
    for m in mxd_list:
        arcpy.AddMessage("Finding layers in {}...".format(m))
        mxd = arcpy.mapping.MapDocument(m)
        for df in arcpy.mapping.ListDataFrames(mxd, "*"):
            lyrs = arcpy.mapping.ListLayers(mxd, "", df)
            for lyr in lyrs:
                if lyr.supports("dataSource"):
                    if lyr.isBroken:
                        status = "broken"
                    else:
                        status = "working"
                    mxd_shortname = m.split("\\")[-1]
                    layer_list_row = [m, mxd_shortname, lyr.name, lyr.datasetName, status]
                    layer_list.append(layer_list_row)
                    arcpy.AddMessage("    ...{}".format(lyr.name))

    # write to a CSV file
    csv_header = ["mxd_fullpath", "mxd_shortname", "layer_name", "data_source", "layer_status"]
    csv_writer(output_csv, csv_header, layer_list)
    arcpy.AddMessage('{} was successfully processed'.format(input_workspace.split('.')[-1]))
    return


def gdb_inventory(input_workspace, output_csv):
    """This function performs the processing for the GDB Inventory tool.
    :param input_workspace: SDE connection to the enterprise geodatabase to be examined.
    :param output_csv: name of the output CSV file with dataset information as rows.
    """
    # Initiate variables
    dataset_list = []

    # top down walk through each geodatabase
    arcpy.env.workspace = input_workspace
    for dirpath, workspaces, filepaths in arcpy.da.Walk(
            input_workspace,
            topdown=True,
            followlinks=True,
            datatype="FeatureClass"):
        for filepath in filepaths:
            try:
                arcpy.AddMessage('Processing {0}...'.format(filepath))
                desc = arcpy.Describe(filepath)
                if desc.featureType != "Annotation":
                    dataset_list.append([dirpath, filepath, arcpy.GetCount_management(filepath)[0], "feature class"])
            except Exception as e:
                arcpy.AddWarning('There was an issue processing {0}'.format(filepath))
                arcpy.AddWarning(e)
        dataset_list += [[dirpath, workspace, "NA", "feature dataset"] for workspace in workspaces]

    csv_header = ['workspace', 'feature_class', 'feature_count', 'dataset_type']
    csv_writer(output_csv, csv_header, dataset_list)
    arcpy.AddMessage('{} was successfully processed'.format(input_workspace.split('.')[-1]))
    return


def replica_inventory(input_workspace, output_csv):
    """This function performs the processing for the Replica Inventory tool.
    :param input_workspace: SDE connection to the enterprise geodatabase to be examined.
    :param output_csv: name of the output CSV file with dataset information as rows.
    """
    # initiate variables
    csv_header = ["Name", "Owner", "Role", "Type", "IsParent", "IsSender", "LastReceiveDate", "LastSendDate"]
    list_replica = []

    # Call the ListReplicas method
    replicas = arcpy.da.ListReplicas(input_workspace)

    for r in replicas:
        # get receive/send dates if is parent/sender (respectively)
        if r.isParent == True:
            lastReceiveDate = 'N/A'
        else:
            lastReceiveDate = r.lastReceive
        if r.isSender == False:
            lastSendDate = 'N/A'
        else:
            lastSendDate = r.lastSend
        # append the replica properties to replica list
        r_row = [r.name, r.owner, r.role, r.type, r.isParent, r.isSender, lastReceiveDate, lastSendDate]
        list_replica.append(r_row)

    csv_writer(output_csv, csv_header, list_replica)
    arcpy.AddMessage('{} was successfully processed'.format(input_workspace.split('.')[-1]))
    return


def clean_gdb(input_workspace, log_file):
    '''
    This function deletes all objects from a geodatabase, including feature datasets, feature classes, tables, and
    rasters.
    :param input_workspace: Filepath and name of the geodatabase to be cleaned.
    :param log_file: Filepath and name of the log file which annotates the objects found and deleted, and any errors.
    '''
    # Import modules
    import logging

    # Initiate variables
    arcpy.env.workspace = input_workspace
    arcpy.env.overwriteOutput = True

    # Set up log file
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename=log_file, level=logging.INFO)
    logging.info('arcpy.env.workspace = {}'.format(arcpy.env.workspace))

    # Compile list of objects in feature datasets
    fds = arcpy.ListDatasets(wild_card='*', feature_type="Feature")
    for fd in fds:
        fcs = arcpy.ListFeatureClasses(wild_card='*', feature_type='All', feature_dataset=fd)
        # Remove all feature classes from the dataset
        if fcs:  # run only if feature class list is not empty
            for fc in fcs:
                try:
                    arcpy.Delete_management(fc)
                    logging.info('Feature Dataset: {0} | Feature Class: {1} deleted successfully'.format(fd, fc))
                except arcpy.ExecuteError:
                    error_msg = arcpy.GetMessages(2)
                    logging.error('Feature Dataset: {0} | Feature Class: {1} {2}'.format(fd, fc, error_msg))
        # Remove the feature dataset
        arcpy.Delete_management(fd)

    # Compile list of all objects in geodatabase at root level
    fcs_gdb = arcpy.ListFeatureClasses(wild_card='*', feature_type='All')
    rasters = arcpy.ListRasters(wild_card='*', raster_type='All')
    tables = arcpy.ListTables(wild_card='*', table_type='All')

    # Remove all feature classes
    if fcs_gdb:  # run only if feature class list is not empty
        for fc in fcs_gdb:
            try:
                arcpy.Delete_management(fc)
                logging.info('Feature Class: {0} deleted successfully'.format(fc))
            except arcpy.ExecuteError:
                error_msg = arcpy.GetMessages(2)
                logging.error('Feature Class: {0} {1}'.format(fc, error_msg))
    # Remove all rasters
    if rasters:  # run only if raster list is not empty
        for raster in rasters:
            try:
                arcpy.Delete_management(raster)
                logging.info('Raster: {0} deleted successfully'.format(raster))
            except arcpy.ExecuteError:
                error_msg = arcpy.GetMessages(2)
                logging.error('Raster: {0} {1}'.format(raster, error_msg))
    # Remove all tables
    if tables:  # run only if table list is not empty
        for table in tables:
            try:
                arcpy.Delete_management(table)
                logging.info('Table: {0} deleted successfully...'.format(table))
            except arcpy.ExecuteError:
                error_msg = arcpy.GetMessages(2)
                logging.error('Table: {0} {1}'.format(table, error_msg))

    return


# Adapted from https://gis.stackexchange.com/a/413675
def get_domains(input_workspace, output_csv):
    '''

    :param input_workspace:
    :param output_csv:
    :return:
    '''
    # Set variables
    arcpy.env.workspace = input_workspace
    result_list = []

    domain_list = arcpy.da.ListDomains(input_workspace)
    arcpy.AddMessage('{0} domains found in {1}'.format(len(domain_list), input_workspace))
    fd_list = arcpy.ListDatasets(feature_type='Feature')

    for fd in fd_list:
        arcpy.AddMessage("Feature dataset: {}".format(fd))
        fc_list = arcpy.ListFeatureClasses(feature_dataset=fd)
        for fc in fc_list:
            arcpy.AddMessage("  Feature class: {}".format(fc))
            field_list = arcpy.ListFields(fc)
            for field in field_list:
                for domain in domain_list:
                    if field.domain == domain.name:
                        arcpy.AddMessage('    Processing {0} | {1} | {2}...'.format(fc, field.name, field.domain))
                        result_list.append([fd, fc, field.name, field.domain])
    header = ['feature_dataset', 'feature_class', 'field_name', 'domain_name']
    csv_writer(output_path=output_csv, header_list = header, row_list=result_list)
    return


def csv_writer(output_path, header_list, row_list):
    # write to a CSV file
    csv_header = header_list
    with open(output_path, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_header)
        for row in row_list:
            if row is not None:
                writer.writerow(row)
    arcpy.AddMessage("CSV output: {}".format(output_path))
    return


# # TEST
# input_filepath = r"\\snoco\gis\plng\GDB_connections\SCD_GDBA@SCD_GIS_PROD.SDE"
# # input_filepath = r"\\snoco\gis\plng\carto\__PDSGIS_GDBUpdate\SDE_connections\2022\PRO_Connection\SCD_GDBA@SCD_GIS_PROD_TEST.sde"
# output_csv = r"C:\Users\SCDJ2L\dev\PDSTools\test\PROD_2016_inventory.csv"
# gdb_inventory(input_filepath, output_csv)
