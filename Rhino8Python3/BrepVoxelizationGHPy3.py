"""Grasshopper Script"""
a = "Hello Python 3 in Grasshopper!"
print(a)
import Rhino.Geometry as rg
import math
import Grasshopper as gh
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
tol=10E-3
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
            distance=cPoint.DistanceTo(voxelPoint)
            if (solid.IsPointInside(voxelPoint, tol, True)):
                distance=-distance
            distances.append(distance)
a=voxelPoints
d=distances

def HeatColourANum(num):
    grad=gh.GUI.Gradient.GH_Gradient.Heat()
    grad.Linear=True
    return grad.ColourAt(num)

def boxelAVoxel(voxelPoint, voxelSize):
    '''
    v7_____________v6  
    |\             |\  
    | \            | \  
    |  \ _____________\  
    |   v4         |   v5  
    |   |          |   |  
    |   |          |   |  
    v3--|----------v2  |  
     \  |           \  |  
      \ |            \ |  
       \|             \|  
        v0_____________v1
    '''
    u=voxelSize.X/2
    v=voxelSize.Y/2
    w=voxelSize.Z/2
    v0=voxelPoint+rg.Vector3d(-u,-v,-w)
    v1=voxelPoint+rg.Vector3d(+u,-v,-w)
    v2=voxelPoint+rg.Vector3d(+u,+v,-w)
    v3=voxelPoint+rg.Vector3d(-u,+v,-w)
    v4=voxelPoint+rg.Vector3d(-u,-v,+w)
    v5=voxelPoint+rg.Vector3d(+u,-v,+w)
    v6=voxelPoint+rg.Vector3d(+u,+v,+w)
    v7=voxelPoint+rg.Vector3d(-u,+v,+w)
    vertices=[v0,v1,v2,v3,v4,v5,v6,v7]
    box=rg.Mesh.CreateFromBox(vertices,1,1,1)
    return box
def cboxelAVoxel(voxelPoint, voxelSize, colour):
    '''
    v7_____________v6  
    |\             |\  
    | \            | \  
    |  \ _____________\  
    |   v4         |   v5  
    |   |          |   |  
    |   |          |   |  
    v3--|----------v2  |  
     \  |           \  |  
      \ |            \ |  
       \|             \|  
        v0_____________v1
    '''
    u=voxelSize.X/2
    v=voxelSize.Y/2
    w=voxelSize.Z/2
    v0=voxelPoint+rg.Vector3d(-u,-v,-w)
    v1=voxelPoint+rg.Vector3d(+u,-v,-w)
    v2=voxelPoint+rg.Vector3d(+u,+v,-w)
    v3=voxelPoint+rg.Vector3d(-u,+v,-w)
    v4=voxelPoint+rg.Vector3d(-u,-v,+w)
    v5=voxelPoint+rg.Vector3d(+u,-v,+w)
    v6=voxelPoint+rg.Vector3d(+u,+v,+w)
    v7=voxelPoint+rg.Vector3d(-u,+v,+w)
    vertices=[v0,v1,v2,v3,v4,v5,v6,v7]
    box=rg.Mesh.CreateFromBox(vertices,1,1,1)
    box.VertexColors.CreateMonotoneMesh(colour)
    return box
def remapNumbers(nums):
    #remaps numbers into a range starting from the minimum and ending with the maximum of the list
    remappedNs=[]
    maxN=max(nums)
    minN=min(nums)
    for num in nums:
        remappedN=(num-minN)/(maxN-minN)
        remappedNs.append(remappedN)
    return remappedNs
remappedDists=remapNumbers(distances)
colours=[]
for remappedDist in remappedDists:
    colour=HeatColourANum(remappedDist)
    colours.append(colour)
r=remappedDists#
colouredBoxes=[]
for i in range(len(distances)):
    colouredBox=cboxelAVoxel(voxelPoints[i],size,HeatColourANum(remappedDists[i]))
    colouredBoxes.append(colouredBox)
c=colouredBoxes
