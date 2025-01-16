from ultralytics import YOLO, settings

import torch

print("PyTorch versão:", torch.__version__)
print("CUDA disponível:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Nome da GPU:", torch.cuda.get_device_name(0))
    print("Número de GPUs disponíveis:", torch.cuda.device_count())
else:
    print("Nenhuma GPU detectada pelo PyTorch.")

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

settings["datasets_dir"] = "./carTimer-2"
# Train the model
results = model.train(data="./carTimer-2/data.yaml", epochs=100, imgsz=640)