import cv2, time, pandas
from datetime import datetime

first_frame=None
#fill list with two empty items
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start", "End"])

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #making the gray image blurry to remove noise and increase accuracy
    gray=cv2.GaussianBlur(gray, (21,21),0) 

    if first_frame is None:
        #store the first frame in the first_frame variable
        first_frame=gray
        continue

    #delta_frame is the frame that holds the difference between frame 1 and teh current frame
    delta_frame =cv2.absdiff(first_frame,gray)
    
    #thresh value - if there is a difference of more than 30 between the first frame we assign those as white pixels
    #may need to test - having much more success with 100 thresh value
    thresh_frame=cv2.threshold(delta_frame, 100, 255, cv2.THRESH_BINARY)[1] #threshBinary only requires access to the second returned tuple

    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    #find all the contours of the image
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        #if contour has less than 1000 pixels
        if cv2.contourArea(contour) < 500:
            continue
        status=1
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0), 3)

    status_list.append(status)

    #to improve memory - only include last two status
    #comment to see all status
    status_list=status_list[-2:]

    #check the last item in the list and the item before the last item
    #if the last frame of the status_list (index of -1) equals 1 and the next to last frame = 0 append the date and time
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    #key=cv2.waitKey(1000)   # 1 second intevals
    key=cv2.waitKey(1)      # 1 millisecond intervals
    #print the variables to check results - info only - not needed for project
    #print(gray)
    #print(delta_frame)

    #this is to break the loop with a "q" key (for quit)
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

#print(status)
print(status_list)
print(times)

for i in range(0,len(times), 2):
    #append the first and  second objects into the first 2 columns
    #then i value is 3 so you are now appending 3 and 4 to the first 2 columns
    df=df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()