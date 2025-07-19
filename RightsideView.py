# Indexing List
"""
Left Child: 2i + 1
Right child: 2i + 2

Index starts at 0.
[0,1,2]
0 is root, no parent index.
1,2 have parent index 0
1 is left, 2 is right [Index]
"""


def rightSideView(tree_list):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    rightSideList = []
    leftSideList = []
    parentIndex = None
    areYouOnRight = False
    doesLeftExist = True
    doesRightExist = True
    x = 0
    index = 0

    for branch in range(len(tree_list)):
        i = tree_list[branch]
        if index == 0 and parentIndex == None:
            rightSideList.append(i)
            parentIndex = 0

        elif index == 0:
            if areYouOnRight == False:
                if i != None: leftSideList.append(i)
                else:
                    doesLeftExist = False
                areYouOnRight = True
            else:
                if i != None: rightSideList.append(i)
                else:
                    doesRightExist = False
                areYouOnRight = False
                index += 1
        else:
            if areYouOnRight == False:
                if branch+1 == (len(tree_list)-1):
                    #if i!= None: leftSideList.append(i)
                    x += 1
                    if x == 2:
                        areYouOnRight = True
                else:
                    if i!= None and doesLeftExist==True: leftSideList.append(i)
                    x += 1
                    if x == 2:
                        areYouOnRight = True

          
            else:
                if i!= None and doesRightExist == True: rightSideList.append(i)
                x -= 1
                if x == 0:
                    areYouOnRight = False

    print(tree_list)
    print(leftSideList, rightSideList)
    if len(rightSideList)-1 != len(leftSideList):
        difference =(len(rightSideList)-1) - len(leftSideList)
        rightSideList.extend(leftSideList[difference:])

    return rightSideList
                
                

#print(rightSideView([1,2,3,4,None,None,None,5]))
#print(rightSideView([1,2,3,5,6])) # 1 3 6
#print(rightSideView([1,2,3,4,None,None,None,5])) # 1 3 5 4
print(rightSideView([6,1,None,None,3,2,5,None,None,4])) # 6 1 3 5 4