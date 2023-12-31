"""Grasshopper Script"""
a = "Hello Python 3 in Grasshopper!"
print(a)
import sys
print(sys.version)
print(sys.path)
print(sys.executable)

#https://discourse.mcneel.com/t/rhino-8-feature-scripteditor-cpython-csharp/128353/425

#https://discourse.mcneel.com/t/rhino-8-feature-scripteditor-cpython-csharp/128353/437?u=pirouz_nourian1
"""Testing pip install specific packages"""
# r: numpy
# r: matplotlib

import numpy as np
print(np.__version__)

print(np.zeros((3,3)))

a=np.zeros((3,3))

#documentation is available here: https://developer.rhino3d.com/api/rhinocommon/?version=8.x
import Rhino.Geometry as rg

#we will use GH only for making datatrees, if absolutely necessary, nothing else
import Grasshopper as gh
# get the grasshopper sdk by typing GrasshopperGetSDKDocumentation in your Rhino commandline

b=rg.Circle(x,10)
(m,n)=(3,4)
GDT=gh.DataTree[rg.Point3d]()
for i in range(m):
    GDT.EnsurePath(i)
    for j in range(n):
        point=rg.Point3d(i,j,0)
        GDT.Branch(i).Add(point)

c=GDT

from matplotlib import cm
# Get the 'viridis' colormap with 256 colors
viridis = cm.get_cmap('viridis', 256)

# Generate colors from the 'viridis' colormap
colors = viridis(np.linspace(0, 1, 256))
print(type(colors))

distArray=np.array(d)
a=distArray
a=rg.Point3d(3,4,5)