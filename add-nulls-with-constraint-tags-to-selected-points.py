import c4d

def main():
    doc.StartUndo()
    obj = doc.GetActiveObject()
    sel = obj.GetPointS()
    count = obj.GetPointCount()
    null = c4d.BaseObject(c4d.Onull)
    null.SetName("Points")
    doc.InsertObject(null)

    for i in range(count):
        if(sel.IsSelected(i)):
            #print("id "+str(i)+" "+"pos "+str(obj.GetPoint(i)))
            point = c4d.BaseObject(c4d.Onull)
            point.SetName("p_"+str(i))
            point[c4d.NULLOBJECT_DISPLAY]=2
            objpos = obj.GetMg().off
            pointpos = obj.GetPoint(i)
            fposx = pointpos[0]+objpos[0]
            fposy = pointpos[1]+objpos[1]
            fposz = pointpos[2]+objpos[2]
            point.SetAbsPos(c4d.Vector(fposx, fposy, fposz))
            point.InsertTag(c4d.BaseTag(1019364))
            tag = point.GetFirstTag()
            tag[c4d.ID_CA_CONSTRAINT_TAG_CLAMP]=1
            tag[50004,1]=3
            tag[50004,4]=3
            tag[50001]=obj
            tag[50004,7]=1
            point.InsertUnder(null)
            doc.AddUndo(c4d.UNDOTYPE_NEW, null)
    c4d.EventAdd()
    doc.EndUndo()

if __name__=='__main__':
    main()