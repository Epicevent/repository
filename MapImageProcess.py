def diff(img1, img2):
    if img1.size[0] != img2.size[0] or img1.size[1] != img2.size[1]:
        return True
    im1 = img1.load()
    im2 = img2.load()
    return array2d_diff(im1,im2,img1.size[0],img1.size[1])

def diff_col(img1,img2,colIndex1,colIndex2):
    if img1.size[1] !=img2.size[1]:
        return True
    im1 = img1.load()
    im2 = img2.load()
    rows = img1.size[1]
    if colIndex1<0:
        colIndex1+=rows
    if colIndex2<0:
        colIndex2+=rows
    return array2d_coldiff(im1,im2,rows,colIndex1,colIndex2)

def diff_row(img1,img2,rowIndex1,rowIndex2):
    if img1.size[0] !=img2.size[0]:
        return True
    im1 = img1.load()
    im2 = img2.load()
    cols=img1.size[0]
    if rowIndex1<0:
        rowIndex1 += cols
    if rowIndex2<0:
        rowIndex2 += cols
    return array2d_coldiff(im1, im2, rowIndex1, rowIndex2,cols)

def array2d_diff(Arr1,Arr2,W,H):
    for i in range(0, W):
        for j in range(0, H):
            if (Arr1[i, j] != Arr2[i, j]):

                return True
    return False

def array2d_rowdiff(Arr1,Arr2,rowIndex1,rowIndex2,cols):
    for j in range(0, cols):
        if (Arr1[j,rowIndex1] != Arr2[ j,rowIndex2]):
            return True
    return False

def array2d_coldiff(Arr1, Arr2, rows, colIndex1,colIndex2):
    for i in range(0, rows):
        if (Arr1[colIndex1,i] != Arr2[colIndex2,i]):
            return True
    return False