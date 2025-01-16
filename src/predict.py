from ultralytics import YOLO
import cv2

# Carregue o modelo treinado
model = YOLO("./models/carTimer2.pt")

# Abra o vídeo
video_path = "./static/videos/prefeitura_move_car.mp4"
cap = cv2.VideoCapture(video_path)

# Configure o vídeo de saída (opcional)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Faça a inferência
    results = model(frame)

    # Obtenha os quadros com as detecções desenhadas
    annotated_frame = results[0].plot()

    # Salve o quadro no vídeo de saída
    out.write(annotated_frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()