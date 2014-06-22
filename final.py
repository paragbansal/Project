''' This code takes the image input either from harddisk or webcam and prints the triangulated image using the process delaunay triagulation'''
from tkFileDialog import askopenfile 
from Tkinter import *
import cv
import cv2
import Image
import os
from PIL import ImageTk
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

root =Tk()
#Assigning title of the window
root.wm_title("Delaunay Triangulation")
#Size of the window
root.geometry("1000x900")
#Description about a button by writing text above it
label1=Label(root,text="Browse Image from your Directories",fg='blue',font=25)


#Function for triagulating the image obtained by browsing from harddisk
def getImagename():
	name=askopenfilename()
	
	root.destroy()
	a=[]
	img=cv2.imread(name,0)
	img = cv2.medianBlur(img,5) 
	th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
    	        cv2.THRESH_BINARY,3,1)
	
	for i in range (0,th2.shape[0]) :
    	    for j in range(0,th2.shape[1]):
        	        if th2[i,j]==0 :
            	        	a.append((j,-i))
	points=np.asarray(a)
	
	for i in a :
    	    del i
	tri = Delaunay(points)
	plt.triplot(points[:,0], points[:,1], tri.simplices.copy(),linewidth=0.5,color='b')
	
	#plt.plot(points[:,0], points[:,1], 'o')
	plt.xticks([]), plt.yticks([])
	plt.show()

#Button for browsing image
submit1 = Button(root,height=2,width=8,text="Browse",command=getImagename,font=25)
label1.pack()
submit1.pack(side =TOP)
label2=Label(root,text="Take a image from Web CAM",fg='blue',font=25)



#function for triangulating the image captured through webCAM
def webcam():
  if __name__=='__main__':
    capture=cv.CaptureFromCAM(0)
    cv.NamedWindow('image')
    
    while  True:
      frame=cv.QueryFrame(capture)
      cv.ShowImage('image',frame)
      k=cv.WaitKey(10)
      if k%256==27:
        break

    cv.DestroyWindow('image')

  img=np.asarray(frame[:,:])
  img=img[:,:,0]
  im = Image.fromarray(img)

  a=[]
  img = cv2.medianBlur(img,5) 
  th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
              cv2.THRESH_BINARY,3,1)
  for i in range (0,th2.shape[0]) :
          for j in range(0,th2.shape[1]):
                  if th2[i,j]==0 :
                        a.append((j,-i))
  points=np.asarray(a)
  for i in a :
          del i
  tri = Delaunay(points)
  plt.triplot(points[:,0], points[:,1], tri.simplices.copy(),linewidth=0.5,color='b')
  #plt.plot(points[:,0], points[:,1], 'o')
  plt.xticks([]), plt.yticks([])
  plt.show()


#Button for capturing image through webcam
submit2=Button(root,height=2,width=8,text="Get image",command=webcam,font=25)
label2.pack()
submit2.pack(side=TOP)
label3=Label(root,text="Original Image-Triangulated Image",font=100)
label3.pack()
#code for adding image in the GUI
add1=ImageTk.PhotoImage(Image.open("face.jpg"),palette=0)
panel=Label(root,image=add1)
panel.pack(side=LEFT,fill="both",expand="yes")
add2=ImageTk.PhotoImage(Image.open("facet.jpg"),palette=0)
panel=Label(root,image=add2)
panel.pack(side=RIGHT,fill="both",expand="yes")
root.mainloop()
