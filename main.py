#Chương trình nhận diện cử chỉ bàn tay hiển thị chữ cái
import cv2 #import thư viện opencv
import mediapipe as mp #import thư viện mediapipe

# Cấu hình và khái báo đối tượng
mp_drawing_util = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles
mp_hand = mp.solutions.hands
hands = mp_hand.Hands(
    model_complexity = 0,
    min_detection_confidence = 0.5, #Giá trị mặc định
    min_tracking_confidence = 0.5   #Giá trị mặc định
)                       

# Mở máy ảnh
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    # Đọc hình ảnh thành công
    if not success:
        break
    # Chuyển thành ảnh màu
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    alphabet = ''
    # Vẽ tọa độ khung xương bàn tay
    if result.multi_hand_landmarks:
        myHand = []
        for idx, hand in enumerate(result.multi_hand_landmarks):
            mp_drawing_util.draw_landmarks(img, hand, mp_hand.HAND_CONNECTIONS, mp_drawing_style.get_default_hand_landmarks_style(), mp_drawing_style.get_default_hand_connections_style())
            for id, lm in enumerate(hand.landmark):
                # Lấy các tọa độ
                h, w, _ = img.shape
                myHand.append([int(lm.x * w), int(lm.y * h)]) #x = 0, y = 1
            # Từ các tọa độ => chữ cái muốn hiển thị
            # Nhận diện chữ A
            if myHand[4][0] > myHand[1][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1] and myHand[1][1] > myHand[8][1] > myHand[2][1] and myHand[1][1] > myHand[12][1] > myHand[2][1] and myHand[1][1] > myHand[16][1] > myHand[2][1] and myHand[1][1] > myHand[20][1] > myHand[2][1]:
                alphabet = 'A'
            # Nhận diện chữ B
            elif myHand[4][0] < myHand[2][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] < myHand[13][1] and myHand[20][1] < myHand[17][1]:
                alphabet = 'B'
            # Nhận diện chữ C
            elif myHand[4][0] > myHand[5][0] and myHand[8][0] > myHand[5][0] and myHand[12][0] > myHand[9][0] and myHand[16][0] > myHand[13][0] and myHand[20][1] > myHand[18][1] and myHand[0][1] > myHand[4][1] and myHand[4][1] > myHand[8][1] and myHand[4][0] > myHand[8][0]:
                alphabet = 'C'
            # Nhận diện chữ D
            elif myHand[4][0] > myHand[12][0] and myHand[8][0] > myHand[5][0] and myHand[12][0] > myHand[9][0] and myHand[16][0] > myHand[13][0] and myHand[20][1] < myHand[18][1]:
                alphabet = 'D'
            # Nhận diện chữ E
            elif myHand[4][0] < myHand[11][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1]:
                alphabet = 'E'
            # Nhận diện chữ F
            elif myHand[4][0] > myHand[2][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] < myHand[13][1] and myHand[20][1] < myHand[17][1]:
                alphabet = 'F'
            # Nhận diện chữ G
            elif myHand[8][0] < myHand[4][0] and myHand[10][1] < myHand[11][1] < myHand[14][1] < myHand[18][1] < myHand[19][1] and myHand[4][0] > myHand[10][0]:
                alphabet = 'G'
            # Nhận diện chữ H
            elif myHand[12][0] < myHand[8][0] and myHand[12][1] > myHand[8][1] and myHand[14][0] < myHand [18][0] and myHand[14][1] < myHand[18][1]:
                alphabet = 'H'
            # Nhận diện chữ I
            elif myHand[4][0] < myHand[10][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] < myHand[17][1] and myHand[4][0] < myHand[6][0]:
                alphabet = 'I'
            # Nhận diện chữ J
            elif myHand[20][0] < myHand[17][0] and myHand[20][1] < myHand[17][1] and myHand[14][0] < myHand[13][0] < myHand[16][0] and myHand[14][1] < myHand[13][1] < myHand[16][1] and myHand[10][0] < myHand[4][0] < myHand[6][0] and myHand[6][1] < myHand[10][1] < myHand[4][1] and myHand[20][0] < myHand[14][0] < myHand[10][0] < myHand[4][0] < myHand[6][0]:
                alphabet = 'J'
            # Nhận diện chữ K
            elif myHand[4][0] > myHand[2][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1]: 
                alphabet = 'K'
            # Nhận diện chữ L
            elif myHand[4][0] > myHand[2][0] and myHand[4][0] > myHand[12][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1]: 
                alphabet = 'L'
            # Nhận diện chữ M
            elif myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1] and myHand[0][1] > myHand[14][1] and myHand[0][1] > myHand[10][1] and myHand[14][0] < myHand[0][0] < myHand[10][0] and myHand[16][1] > myHand[0][1] and myHand[16][1] > myHand[12][1]:
                alphabet = 'M'
            # Nhận diện chữ N
            elif myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1] and myHand[0][1] > myHand[14][1] and myHand[0][1] > myHand[10][1] and myHand[14][0] < myHand[0][0] < myHand[10][0] and myHand[16][1] < myHand[0][1] and myHand[16][1] < myHand[12][1]:
                alphabet = 'N'
            # Nhận diện chữ O
            elif myHand[4][0] > myHand[5][0] and myHand[8][0] > myHand[5][0] and myHand[12][0] > myHand[9][0] and myHand[16][0] > myHand[13][0] and myHand[20][1] > myHand[18][1] and myHand[0][1] > myHand[4][1] and myHand[4][0] > myHand[8][0] and myHand[4][1] < myHand[8][1] and myHand[4][0] > myHand[1][0] and myHand[4][0] > myHand[8][0]:
                alphabet = 'O'
            # Nhận diện chữ P
            elif myHand[4][0] > myHand[11][0] and myHand[8][0] < myHand[6][0] and myHand[12][0] < myHand[9][0] and myHand[16][0] < myHand[13][0] and myHand[20][0] < myHand[17][0]:
                alphabet = 'P'
            # Nhận diện chữ Q
            elif myHand[4][1] > myHand[1][1] and myHand[8][1] > myHand[5][1] and myHand[8][0] < myHand[5][0] and myHand[8][0] < myHand[12][0] and myHand[8][0] < myHand[16][0] and myHand[8][0] < myHand[20][0]:
                alphabet = 'Q'
            # Nhận diện chữ R
            elif myHand[4][0] < myHand[2][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1] and myHand[4][1] < myHand[15][1] and myHand[8][0] < myHand[12][0]:
                alphabet = 'R'
            # Nhận diện chữ S
            elif myHand[4][0] > myHand[11][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1] and myHand[0][1] > myHand[1][1] and myHand[5][1] > myHand[6][1] and myHand[10][1] < myHand[4][1] < myHand[11][1]:
                alphabet = 'S'
            # Nhận diện chữ T
            elif myHand[4][1] < myHand[7][1] and myHand[8][0] > myHand[7][0] > myHand[6][0] > myHand[5][0] and myHand[12][0] > myHand[11][0] > myHand[10][0] > myHand[9][0]:
                alphabet = 'T'         
            # Nhận diện chữ V
            elif myHand[4][0] < myHand[2][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1] and myHand[16][1] > myHand[4][1] > myHand[15][1]:
                alphabet = 'V'
            # Nhận diện chữ U
            elif myHand[4][0] < myHand[2][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] > myHand[17][1] and myHand[4][1] < myHand[15][1] and myHand[8][0] > myHand[12][0]:
                alphabet = 'U'
            # Nhận diện chữ W
            elif myHand[4][0] < myHand[2][0] and myHand[8][1] < myHand[5][1] and myHand[12][1] < myHand[9][1] and myHand[16][1] < myHand[13][1] and myHand[20][1] > myHand[17][1]: 
                alphabet = 'W'
            # Nhận diện chữ X
            elif myHand[4][0] < myHand[8][0] and myHand[4][1] > myHand[8][1] and myHand[5][0] < myHand[8][0] and myHand[9][0] < myHand[12][0]:
                alphabet = 'X'
            # Nhận diện chữ Y
            elif myHand[4][0] > myHand[10][0] and myHand[8][1] > myHand[5][1] and myHand[12][1] > myHand[9][1] and myHand[16][1] > myHand[13][1] and myHand[20][1] < myHand[17][1] and myHand[4][0] > myHand[5][0]:
                alphabet = 'Y'
            # Nhận diễn chữ Z
            elif myHand[8][1] < myHand[4][1] and myHand[8][0] < myHand [4][0] and myHand[10][1] < myHand[4][1] < myHand[15][1]:
                alphabet = 'Z'
            # Các trường hợp cử chỉ sai
            else:
                alphabet = 'Khong xac dinh'

    # Hiển thị chữ đã nhận dạng ra màn hình
    cv2.putText(img, str(alphabet), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2, cv2.LINE_AA)
    # Hiển thị hình ảnh bàn tay
    cv2.imshow("Nhan dang bang chu cai tu cu chi tay", img)
    # Gán 1 key để thoát khỏi chương trình
    key = cv2.waitKey(1)
    # Key Esc close program
    if key == 27: 
        break
# Đóng máy ảnh
cap.release()
