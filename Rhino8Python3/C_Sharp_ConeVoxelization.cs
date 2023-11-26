// Grasshopper Script Instance
using System;
using System.Collections;
using System.Collections.Generic;
using System.Drawing;

using Rhino;
using Rhino.Geometry;

using Grasshopper;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Data;
using Grasshopper.Kernel.Types;

public class Script_Instance : GH_ScriptInstance
{
  /* 
    Members:
      RhinoDoc RhinoDocument
      GH_Document GrasshopperDocument
      IGH_Component Component
      int Iteration

    Methods (Virtual & overridable):
      Print(string text)
      Print(string format, params object[] args)
      Reflect(object obj)
      Reflect(object obj, string method_name)
  */
  
  private void RunScript(
	Brep S,
	double xS,
	double yS,
	double zS,
	out object A,
	out object B,
	out object C)
  {
    // Write your logic here
    // a = null;

    BoundingBox BBox = S.GetBoundingBox(true);

    double W = BBox.Diagonal.X;
    double L = BBox.Diagonal.Y;
    double H = BBox.Diagonal.Z;

    int UC = (int) System.Math.Ceiling(W / xS);
    int VC = (int) System.Math.Ceiling(L / yS);
    int WC = (int) System.Math.Ceiling(H / zS);
    A = WC;
    B = BBox;
    Plane bPlane = new Plane(BBox.Min, Vector3d.XAxis, Vector3d.YAxis);
    //int k = 0;

    double xShift = 0.5 * xS;
    double yShift = 0.5 * yS;
    double zShift = 0.5 * zS;
    List<Point3d> pointList = new List<Point3d>();
    List<double> distanceList = new List<double>();
    for(int i = 0; i < UC;i++){
      for(int j = 0; j < VC; j++){
        for(int k = 0; k < WC;k++){
          Point3d point = bPlane.PointAt(xShift + i * xS, yShift + j * yS, zShift + k * zS);
          pointList.Add(point);

          Point3d cPoint = S.ClosestPoint(point);
          double distance = cPoint.DistanceTo(point);
          if(!S.IsPointInside(point,0.1,true)){
            distance = -distance;
          }
          distanceList.Add(distance);


        }
      }
    }
    A = pointList;
    C = distanceList;
  }
}
