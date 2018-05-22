#-------------------------------------------------
#
# Project created by QtCreator 2018-05-16T15:37:02
#
#-------------------------------------------------

QT       += core

QT       -= gui

TARGET = openni
CONFIG   += console
CONFIG   -= app_bundle

TEMPLATE = app


SOURCES += main.cpp

OPENNI_INC = $$quote(/home/victor/software/OpenNI-Linux-x64-2.3/Include/)
OPENNI_LIB = $$quote(/home/victor/software/OpenNI-Linux-x64-2.3/Redist/)

OPENCV_INC = /home/victor/software/opencv-3.1.0\include/
OPENCV_LIB = /home/victor/software/opencv-3.1.0/build/lib/

INCLUDEPATH += $$OPENCV_INC\opencv   \
            $$OPENCV_INC\opencv2 \
            $$OPENCV_INC    \
            $$OPENNI_INC

LIBS += $$OPENCV_LIB\libopencv*.so \
        $$OPENNI_LIB\libOpenNI2.so
