import string
import maya.cmds as cmds

######FUNCTIONS######
    
def dobleArrow():
    double_arrow_grp = cmds.group(em=True,n='double_arrow_offset')
    firstArrow = makeArrow()
    secondArrow = makeArrow()
    cmds.setAttr(secondArrow + '.sx',-1)
    cmds.setAttr(secondArrow + '.sz',-1)
    double_arrow_curv = cmds.attachCurve(firstArrow,secondArrow,rpo=False,n='double_arrow_ctrl')
    cmds.delete(firstArrow,secondArrow)
    cmds.CenterPivot()
    cmds.parent(double_arrow_curv,double_arrow_grp)
    
    
def square_curve():
    square_curv_grp = cmds.group(em=True,n='square_offset')
    square_curv = cmds.curve(d=1, n='square_ctrl', p=[(1,0,1),(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1)])
    cmds.parent(square_curv,square_curv_grp)
    
def QuadCurve():
    quad_arrow_grp = cmds.group(em=True,n='quad_arrow_offset')
    firstArrow = makeArrow()
    secondArrow = makeArrow()
    thirdArrow = makeArrow()
    fourthdArrow = makeArrow()
    cmds.setAttr(firstArrow + '.tx',1)
    cmds.setAttr(secondArrow + '.tx',-1)
    cmds.setAttr(secondArrow + '.sx',-1)
    cmds.setAttr(secondArrow + '.sz',-1)
    cmds.setAttr(thirdArrow + '.ry',90)
    cmds.setAttr(thirdArrow + '.tz',-1)
    cmds.setAttr(fourthdArrow + '.ry',-90)
    cmds.setAttr(fourthdArrow + '.tz',1)
    quad_arrow_curv = cmds.attachCurve(firstArrow,secondArrow,thirdArrow,fourthdArrow,rpo=False,n='quad_arrow_ctrl')
    cmds.delete(firstArrow,secondArrow,thirdArrow,fourthdArrow)
    cmds.CenterPivot()
    cmds.parent(quad_arrow_curv,quad_arrow_grp)
    
def QuadCurvedArrow():
    quad_curved_arrow_grp = cmds.group(em=True,n='quad_curved_arrow_offset')
    firstArrow = makeArrow()
    secondArrow = makeArrow()
    thirdArrow = makeArrow()
    fourthdArrow = makeArrow()
    archFirst = cmds.circle(r=1,sw=90, nr=(0,1,0))
    cmds.setAttr(archFirst[0] + '.tx',-1 )
    cmds.setAttr(archFirst[0] + '.tz',-1 )
    archSecond = cmds.circle(r=1,sw=90, nr=(0,1,0))
    cmds.setAttr(archSecond[0] + '.tx',1 )
    cmds.setAttr(archSecond[0] + '.tz',1 )
    cmds.setAttr(archSecond[0] + '.ry',180 )
    archThird = cmds.circle(r=1,sw=90, nr=(0,1,0))
    cmds.setAttr(archThird[0] + '.tx',1 )
    cmds.setAttr(archThird[0] + '.tz',-1 )
    cmds.setAttr(archThird[0] + '.ry',-90 )
    archFourth = cmds.circle(r=1,sw=90, nr=(0,1,0))
    cmds.setAttr(archFourth[0] + '.tx',-1 )
    cmds.setAttr(archFourth[0] + '.tz',1 )
    cmds.setAttr(archFourth[0] + '.ry',90 )
    cmds.setAttr(firstArrow + '.tx',2)
    cmds.setAttr(secondArrow + '.tx',-2)
    cmds.setAttr(secondArrow + '.sx',-1)
    cmds.setAttr(secondArrow + '.sz',-1)
    cmds.setAttr(thirdArrow + '.ry',90)
    cmds.setAttr(thirdArrow + '.tz',-2)
    cmds.setAttr(fourthdArrow + '.ry',-90)
    cmds.setAttr(fourthdArrow + '.tz',2)
    quad_curved_arrow = cmds.attachCurve(firstArrow,secondArrow,thirdArrow,fourthdArrow,archFirst[0],archSecond[0],archThird[0],archFourth[0],rpo=False,n='quad_curved_arrow_ctrl')
    cmds.delete(firstArrow,secondArrow,thirdArrow,fourthdArrow,archFirst[0],archSecond[0],archThird[0],archFourth[0])
    cmds.CenterPivot()
    cmds.parent(quad_curved_arrow,quad_curved_arrow_grp)
    
    
def CurvedArrow():
    curved_arrow_grp = cmds.group(em=True,n='curved_arrow_offset')
    firstArrow = makeArrow()
    secondArrow = makeArrow()
    largeArch = cmds.circle(nr=(0,1,0), r=4, sw=90)
    cmds.setAttr(largeArch[0] +'.tz', 3)
    smallArch = cmds.circle(nr=(0,1,0), r=2, sw=90)
    cmds.setAttr(smallArch[0] + '.tz', 3)
    cmds.setAttr(secondArrow +'.tz', 3)
    cmds.setAttr(secondArrow +'.tx', -3)
    cmds.setAttr(secondArrow +'.ry', -90)
    curved_arrow = myCurve = cmds.attachCurve(firstArrow, secondArrow, largeArch[0], smallArch[0], rpo=False, n='curved_arrow_ctrl')
    cmds.delete(firstArrow, secondArrow, largeArch[0], smallArch[0])
    cmds.xform('curved_arrow_ctrl', cp=False)
    cmds.move(1,0,-2, 'curved_arrow_ctrl', a=True)
    cmds.CenterPivot()
    cmds.makeIdentity(apply=True, t=True, r=True, s=True)
    cmds.parent(curved_arrow,curved_arrow_grp)
    
def BoxCurve():
    box_grp = cmds.group(em=True,n='box_offset')
    box_curv = cmds.curve(n='box_ctrl',d=1, p=[(1,-1,1), (-1,-1,1), (-1,-1,-1), (1,-1,-1),(1,-1,1),(1,1,1), (-1,1,1),(-1,-1,1),(-1,1,1), (-1,1,-1),(-1,-1,-1),(-1,1,-1), (1,1,-1),(1,-1,-1),(1,1,-1),(1,1,1)])
    cmds.parent(box_curv,box_grp)
    
def CircleCurve():
    circule_grp = cmds.group(em=True,n='circule_offset')
    circule_curv = cmds.circle(n='circule_ctrl', nr=(0,1,0))
    cmds.parent(circule_curv,circule_grp)
    
def make_arrow_curv():
    arrow_grp = cmds.group(em=True,n='arrow_offset')
    lenght = 2
    arrow_curv = cmds.curve(n= "arrow_ctrl", d=1, p=[(0,0,-1), (lenght,0,-1), (lenght,0,-2), (lenght + 2,0,0), (lenght,0,2), (lenght,0,1), (0,0,1)])
    cmds.parent(arrow_curv,arrow_grp)
    
    
def makeArrow():
    lenght = 2
    myarrow = cmds.curve(n= "arrow_ctrl", d=1, p=[(0,0,-1), (lenght,0,-1), (lenght,0,-2), (lenght + 2,0,0), (lenght,0,2), (lenght,0,1), (0,0,1)])
    return(myarrow)
    
def changeCurveColor(NewColor):
    selection = cmds.ls(sl=True)
    for myarrow in selection:
        shape = cmds.listRelatives (myarrow, s=True )
        shape = shape[0]
        cmds.setAttr(shape + '.overrideEnabled',1)
        if NewColor == 'red':
            cmds.setAttr(shape + '.overrideColor',13)
        if NewColor == 'blue':
            cmds.setAttr(shape + '.overrideColor',6)
        if NewColor == 'green':
            cmds.setAttr(shape + '.overrideColor',14)
        if NewColor == 'yellow':
            cmds.setAttr(shape + '.overrideColor',17)

######WINDOW######

def createWindow(WinName):
    if cmds.window(WinName, exists = True):
        cmds.deleteUI(WinName)
    cmds.window(WinName, sizeable=False, bgc=(0.2,0.2,0.2))
    cmds.columnLayout(adj=False,h=230,w=90)
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

        
    Tab1 = cmds.rowColumnLayout(numberOfColumns=2,rs=[1,5], cs=[1,5])

    cmds.rowLayout(adj=1,nc=4)
    cmds.button(l='Circle Curve',c='CircleCurve()')
    cmds.button(l='Square Curve', c='square_curve()')
    cmds.button(l='Box Curve', c='BoxCurve()')

    cmds.setParent('..')
    cmds.rowLayout(adj=1,nc=1)
    cmds.setParent('..')

    cmds.rowLayout(adj=1,nc=3)
    cmds.button(l='Arrow Curve', c='make_arrow_curv()')
    cmds.button(l='Curved Arrow', c='CurvedArrow()')
    cmds.button(l='Double Arrow', c='dobleArrow()')
    cmds.setParent('..')
    cmds.rowLayout(adj=1,nc=1)
    cmds.setParent('..')
    cmds.rowLayout(adj=1,nc=2)
    cmds.button(l='Quad Arrow', c='QuadCurve()')
    cmds.button(l='Quad Curved Arrow', c='QuadCurvedArrow()')
    cmds.setParent('..')
    cmds.rowLayout(adj=1,nc=1)
    cmds.setParent('..')
    cmds.rowLayout(adj=1,nc=5)
    cmds.text(l='Curve Colors:')
    cmds.button(l='Red', bgc=(1,0,0),c='changeCurveColor("red")')
    cmds.button(l='Blue', bgc=(0,0,1),c='changeCurveColor("blue")')
    
    cmds.button(l='Green', bgc=(0,1,0),c='changeCurveColor("green")')
    cmds.button(l='Yellow', bgc=(1,1,0),c='changeCurveColor("yellow")')
    cmds.setParent('..')
    cmds.setParent( '..' )
    
    cmds.tabLayout( tabs, edit=True, tabLabel=((Tab1, 'Curve Tool')))
    
    cmds.showWindow(WinName)


createWindow('AM_Tool')