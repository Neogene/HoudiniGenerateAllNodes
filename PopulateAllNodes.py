#!/usr/bin/python
#TILE: HOUDINI POPULATES
#AUTHOR: eng. ANDREA LEGANZA
#HOUDINI VERSION: TESTED ON HOUDINI 16.0 AND 16.5
#SCRIPT VERSION: 1.0
#DESCRIPTION:
#1. create a geometry node
#2. right click on it -> Type Propertis -> scripts
#3. Load the script after downloading or select the OnUpdated voice from the dropdown menu and paste the code (remember to select PYTHON as language on the right area dropdown menu)

import hou
def populateWithAllNodes():

    categories = hou.nodeTypeCategories()
    
    i = 0
    
    parent = hou.node("/obj/geo1")
    
    #if len(parent.allItems())>0:
    #parent.deleteItems(parent.allItems()) #removes all children

    #print "Children deleted..."
    
    for category in categories.values():
        node_types = category.nodeTypes()
        #print "NODE TYPES:"+node_types
        for node_type in node_types.keys():
            #print "Creating: "+node_type 
            
            if node_type=="v_constant":
                continue
                
            try:
                node = parent.createNode(node_type)
                i=i+1
                
            except hou.OperationFailed:
                print "error creating:"+node_type

    #print ("PARENT:"+parent.name())
    hou.ui.displayMessage(str(i) + " nodes created.")

populateWithAllNodes()