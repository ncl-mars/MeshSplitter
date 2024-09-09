# Mesh Splitter

A Blender add-on to implement few tools to split a mesh in order to be printable part by part

### Geometry Nodes Prototype

![overview, xray](readme-data/XRay.png)


Split Mesh Surface              |  Split Mesh Topology
:-------------------------:|:-------------------------:
![](readme-data/BodySplit.png)  |  ![](readme-data/BodySplit_wire.png)


Split Arm Piece             |  Piece Thickness
:-------------------------:|:-------------------------:
![](readme-data/ArmPiece.png) | ![](readme-data/Thickness.png) 

Modifier GUI             |  Node Tree
:-------------------------:|:-------------------------:
![](readme-data/Modifier.png) | ![](readme-data/NodeTree.png)


### Developpers

The geometry node tree is made to demonstrate the process considered to be implemented into a proper addon

To operate the boolean operations, particularly ressource intensive, some python wrappers + cuda modules (?) would probably be much faster.

### References

- luban : https://www.luban3d.com/
- Inigo Quilez : https://iquilezles.org/articles/