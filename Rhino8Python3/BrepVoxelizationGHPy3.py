"""Grasshopper Script"""
a = "Hello Python 3 in Grasshopper!"
print(a)
import Rhino.Geometry as rg
import math
print(type(solid))

RBBox=solid.GetBoundingBox(rg.Plane.WorldXY)#https://developer.rhino3d.com/api/rhinocommon/rhino.geometry.geometrybase/getboundingbox

print(RBBox.Min)
print(RBBox.Max)
(u,v,w)=(size.X,size.Y,size.Z)
diagonalR3=RBBox.Max-RBBox.Min
print(diagonalR3)
diagonalN3=(round(diagonalR3.X/size.X),round(diagonalR3.Y/size.Y),round(diagonalR3.Z/size.Z))
# here we make the minimimum corner in Z3
#creating a minimum corner voxel point in R3 so that the point (0,0,0) in R3 is mapped to (0,0,0) in Z3
minZ3=RBBox.Min
minZ3.X=round(minZ3.X/u)
minZ3.Y=round(minZ3.Y/v)
minZ3.Z=round(minZ3.Z/w)
minVoxel=rg.Point3d()
minVoxel.X=minZ3.X*u
minVoxel.Y=minZ3.Y*v
minVoxel.Z=minZ3.Z*w

(m,n,o)=diagonalN3

print(m,n,o)
print(type(m))
voxelPoints=[]
N3Voxels=[]
distances=[]
for i in range(m+1):
    for j in range(n+1):
        for k in range(o+1):
            voxelPoint=minVoxel+rg.Point3d(i*u,j*v,k*w)
            voxelPoints.append(voxelPoint)
            N3Voxels.append((i,j,k))
            cPoint=solid.ClosestPoint(voxelPoint)
            distance=voxelPoint.DistanceTo(cPoint)
            if not (solid.IsPointInside(voxelPoint,0.1,True)):
                 distance=-distance
            distances.append(distance)
a=voxelPoints
b=N3Voxels# inspect these voxels and get comfortable with their abstract meaning, note the reason to 'embed' the voxel points in R3 in the line above
d=distances