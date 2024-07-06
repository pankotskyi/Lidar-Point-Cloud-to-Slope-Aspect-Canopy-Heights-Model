#Importing modules, checking out spatial extension

import arcpy

from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")



#Creating a layer

in_las = arcpy.GetParameterAsText(0)

lyrr = arcpy.CreateUniqueName("Layer")

arcpy.management.MakeLasDatasetLayer(in_las, lyrr, class_code=[2], return_values=["Last Return"])



#Conversion las dataset to raster, creating digital elevation model

out_dem = arcpy.GetParameterAsText(1)

c_size = arcpy.GetParameterAsText(2)

arcpy.conversion.LasDatasetToRaster(lyrr, out_dem, "ELEVATION","BINNING AVERAGE LINEAR", "FLOAT", "CELLSIZE", c_size)



#Creating digital surface model

out_dsm = arcpy.GetParameterAsText(3)

arcpy.conversion.LasDatasetToRaster(in_las, out_dsm, "ELEVATION","BINNING AVERAGE LINEAR", "FLOAT", "CELLSIZE", c_size)



#Creating canopy heights model using raster calculations

dem = arcpy.Raster(out_dem)

dsm = arcpy.Raster(out_dsm)

chm = dsm - dem

out_chm = arcpy.GetParameterAsText(4)

chm.save(out_chm)



#Creating a slope

slp = Slope(out_dem, "DEGREE")

out_slope = arcpy.GetParameterAsText(5)

slp.save(out_slope)



#Creating an aspect

asp = Aspect(out_dem)

out_asp = arcpy.GetParameterAsText(6)

asp.save(out_asp)

arcpy.CheckInExtension("Spatial")