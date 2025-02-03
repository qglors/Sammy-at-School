import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


import cv2
import mediapipe as mp
import numpy as np

myCam = cv2.VideoCapture(0)

mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils

objectron = mp_objectron.Objectron(static_image_mode=False,max_num_objects=5,
                                   min_detection_confidence=0.2,
                                   min_tracking_confidence=0.2,
                                   model_name='Shoe')



# while True:
#     _,image=myCam.read()

#     results = FDetect.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#     if results.detections:
#         for detection in results.detections:
#             mp_drawing.draw_detection(image, detection)
#     cv2.imshow("My WebCam", image)
#     cv2.moveWindow("My WebCam", 0,0)

#     if cv2.waitKey(1) == ord("q"):
#         break

# myCam.release()

while True:
    _,image=myCam.read()

    image.flags.writeable = False
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = objectron.process(image)

    image.flags.writeable = True
    if results.detected_objects:
        for detected_object in results.detected_objects:
            
            mp_drawing.draw_landmarks(image, 
                                      detected_object.landmarks_2d, 
                                      mp_objectron.BOX_CONNECTIONS)
          
            mp_drawing.draw_axis(image, 
                                 detected_object.rotation,
                                 detected_object.translation)

    cv2.imshow('MediaPipe Objectron', cv2.flip(image, 1))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

myCam.release()







# while myCam.isOpened():
#     success, image = myCam.read()

#     image.flags.writeable = False
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = objectron.process(image)

#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     if results.detected_objects:
#         for detected_object in results.detected_objects:
            
#             mp_drawing.draw_landmarks(image, 
#                                       detected_object.landmarks_2d, 
#                                       mp_objectron.BOX_CONNECTIONS)
          
#             mp_drawing.draw_axis(image, 
#                                  detected_object.rotation,
#                                  detected_object.translation)

#     cv2.imshow('MediaPipe Objectron', cv2.flip(image, 1))
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
# myCam.release()
# cv2.destroyAllWindows()