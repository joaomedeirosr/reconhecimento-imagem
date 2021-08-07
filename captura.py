import cv2 as cv

camera = cv.VideoCapture(0)

while(True):
    conectado, imagem = camera.read()

    cv.imgshow("Face detectada",imagem)

    cv.waitKey(1)

    camera.realese()
    cv.destroyAllWindows()