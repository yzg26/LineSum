import math
import cv2
import matplotlib
import matplotlib.pyplot as plt



def LineSum(image,p0, p1):
    #po = [x0,y0] 
    #p1 = [x1, y1]
    
    
    img = cv2.imread(image,0) # reads image '1.png' as grayscale
    plt.imshow(img, cmap='gray')
    #print(img.shape[1::-1])
    #print(img.shape[1])
    #print(img.shape[0])
    
    if p0[0]>img.shape[0] or p1[0]>img.shape[0] or p0[1]>img.shape[1] or p1[1]>img.shape[1]:
         print("Coordinates are not bigger than image size")
    
   
    else:

        
        pixels = []
        dx = p1[0]-p0[0]
        dy = p1[1]-p0[1]
        flag = abs(dy) > abs(dx)
        if flag:
            p0[0] ,p0[1] = p0[1],p0[0] 
            p1[0],p1[1] = p1[1],p1[0]
            dy,dx = dx,dy 
            
        if p0[0] > p1[0]:
            p0[0] ,p1[0] = p1[0],p0[0] 
            p0[0] ,p1[1] = p1[1],p0[0] 
            
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]
        slope = dy / dx 
        
        x_end = round(p0[0])
        y_end = p0[1] + (slope * (x_end - p0[0]))
        xcoor0 = x_end
        ycoor0 = round(y_end)
        
        if flag:
             pixels.extend([(ycoor0, xcoor0), (ycoor0 + 1, xcoor0)])
             
        else:
             pixels.extend([(xcoor0, ycoor0), (xcoor0, ycoor0 + 1)])
        
        interpolated_y = y_end + slope
        
        
        x_end = round(p1[0])
        y_end = p1[1] + (slope * (x_end - p1[0]))
        xcoor1 = x_end
        ycoor1 = round(y_end)
        
        for x in range(xcoor0 + 1, xcoor1):
            if flag:
                pixels.extend([(math.floor(interpolated_y), x), (math.floor(interpolated_y) + 1, x)])
            else:
                pixels.extend([(x, math.floor(interpolated_y)), (x, math.floor(interpolated_y) + 1)])
            
            interpolated_y += slope
        
        
        if flag:
            pixels.extend([(ycoor1, xcoor1), (ycoor1 + 1, xcoor1)])
        else:
            pixels.extend([(xcoor1, ycoor1), (xcoor1, ycoor1 + 1)])
        
        for i in range(0,len(pixels)):
            
            matplotlib.pyplot.plot(pixels[i][0],pixels[i][1], marker=".", markersize=5)
        
        #A = len(pixels)
        
        count = 0
        for i in range(len(pixels)):
            
            if img[pixels[i][0]][pixels[i][1]] == 255:
                count +=1
                
        
        
        return count

        

    
    
    

