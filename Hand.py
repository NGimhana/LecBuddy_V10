import cv2
import win32gui
import time

def windowEnumerationHandler(hwnd, top_windows):    
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def windowOpenPP():
    if __name__ == "__main__":
        results = []
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if "powerpoint" in i[1].lower():
                print (i)
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                break


def windowOpenNotepad():
    if __name__ == "__main__":
        results = []
        top_windows = []
        win32gui.EnumWindows(windowEnumerationHandler, top_windows)
        for i in top_windows:
            if "notepad" in i[1].lower():
                print (i)
                win32gui.ShowWindow(i[0],5)
                win32gui.SetForegroundWindow(i[0])
                break



def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

cam = cv2.VideoCapture(0)

winName = "Movement Indicator"
cv2.namedWindow(winName, 200)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

i=0
while True:    
  cv2.imshow(winName, diffImg(t_minus,t,t_plus))
  ret,thresh = cv2.threshold(diffImg(t_minus, t, t_plus),0,255,cv2.THRESH_OTSU)
  
  if(ret<=14 and i!=1):
      i=i+1
      print (ret)
      image_2=cam.read()[1]
      cv2.imwrite("Img"+str(i)+".jpg",image_2)
      print("Don't Write")
      
      windowOpenPP();
  else:
      i=0
      print ("Writing")     
      windowOpenNotepad();        

        
    
  # Read next image
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

  key = cv2.waitKey(10)
  if key == 27:
    cv2.destroyWindow(winName)
    break
    
print ("Goodbye")
