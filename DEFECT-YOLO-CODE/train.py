import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':

    model_name=r'ultralytics/cfg/models/v8/yolov8-Defect-YOLO.yaml'
    model = YOLO(model_name)
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data=r'data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=2,
                close_mosaic=10,
                workers=12,
                device='0',
                optimizer='SGD', # using SGD
                pretrained=False,
                # resume='', # last.pt path
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/train',
                name=model_name.split("/")[-1].split(".")[0],
                )