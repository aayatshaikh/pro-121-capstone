import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            #accessing the landmarks by their position
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

             #Code goes here   
            import cv2

# Fingertips array
fingertips = [(x1, y1), (x2, y2), (x3, y3), ...]

# Screen dimensions
screen_width = 1920
screen_height = 1080

# Loop through fingertips
for fingertip in fingertips:
    # Get x and y positions of the fingertip and scale them
    x = fingertip[0] * screen_width
    y = fingertip[1] * screen_height
    
    # Draw blue colored circle around the fingertip
    cv2.circle(image, (x, y), 10, (255, 0, 0), -1)
    
    # Check if finger is folded or not
    finger_fold_status = []
    if x < other_x_position_of_landmark:
        # Create green color circle at the fingertip
        cv2.circle(image, (x, y), 10, (0, 255, 0), -1)
        finger_fold_status.append(True)
    else:
        finger_fold_status.append(False)

# Check if all fingers are folded
if all(finger_fold_status):
    # Check if thumb is raised up or down
    if fingertip_y < previous_fingertip_y:
        # Print like statement and show "LIKE" text in green color
        print("Thumb raised up!")
        cv2.putText(image, "LIKE", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        # Print dislike statement and show "DISLIKE" text in red color
        print("Thumb raised down!")
        cv2.putText(image, "DISLIKE", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)



        mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("hand tracking", img)
    cv2.waitKey(1)