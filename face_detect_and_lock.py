import cv2
from time import sleep
import ctypes
import subprocess

def save_cam() :
    webcam = cv2.VideoCapture(0)
    sleep(2)
    i = 0
    while i != 1 :
        try:
            check, frame = webcam.read()
            #sleep(2)
            #print(check) #prints true as long as the webcam is running
            #print(frame) #prints matrix values of each framecd 
            #cv2.imshow("Capturing", frame)
            #sleep(2)
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            print("Image saved!")
            i = i + 1
            webcam.release()
            cv2.destroyAllWindows()
        
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()

def face_record(img_path, xml_path) :
    faceCascade = cv2.CascadeClassifier(xml_path)
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
    )
    print ("Found {0} faces!".format(len(faces)))
    return len(faces)

def face_record_sure(img_path, xml_path_v2) :
    faceCascade = cv2.CascadeClassifier(xml_path_v2)
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
    )
    print ("Found {0} eyes!".format(len(faces)))
    return len(faces)

def face_record_sure_v2(img_path, xml_path_v3) :
    faceCascade = cv2.CascadeClassifier(xml_path_v3)
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
    )
    print ("Found {0} face!".format(len(faces)))
    return len(faces)

def profile(img_path, xml_path_profile):
    faceCascade = cv2.CascadeClassifier(xml_path_profile)
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
    )
    print ("Found {0} profile face!".format(len(faces)))
    return len(faces)

if __name__ == '__main__':
    while True :
        process_name='LogonUI.exe'
        callall='TASKLIST'
        outputall=subprocess.check_output(callall)
        outputstringall=str(outputall)
        save_cam()
        img_path = "saved_img.jpg"
        xml_path = "frontalface.xml"
        xml_path_v2 = "eye_glasses.xml"
        xml_path_v3 = "haarcascade_frontalface_default.xml"
        xml_path_profile = "profile.xml"
        if face_record(img_path, xml_path) == 0 and face_record_sure(img_path, xml_path_v2) == 0 and face_record_sure_v2(img_path, xml_path_v3) == 0 and profile(img_path, xml_path_profile) == 0:
            print("No Face Detect")
            ctypes.windll.user32.LockWorkStation()
        else :
            print("Face Detect")
        while process_name in outputstringall :
            outputall=subprocess.check_output(callall)
            outputstringall=str(outputall)
            print("Lock")
            sleep(5)