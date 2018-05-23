#include <opencv2/core.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/videoio.hpp>//for camera
#include <opencv2/imgproc//imgproc.hpp>
#include <opencv2/ml/ml.hpp>
#include <time.h>
#include <ctime>
#include <iostream>
#include <string>
using namespace std;
using namespace cv;


int main(int argc, char ** argv)
{
	VideoCapture capture;
	capture.open("/home/victor/detectron/output/1.avi");
    Mat frame;
	if (!capture.isOpened())
	{
		cout << "Could not initialize capturing...\n" << endl;
		return -1;
	}
	int n = 1;
	while (true)
	{
		capture >> frame;
		imshow("Video_Capture", frame);
		if (frame.empty())
		{
			break;
		}
		waitKey(3);

	}
}
