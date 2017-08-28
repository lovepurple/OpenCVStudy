#include<opencv2/opencv.hpp>  
#include<iostream>  

using namespace std;
using namespace cv;
/*
	��׽����ͷ
*/
int main()
{
	VideoCapture capture = VideoCapture(0);		//0���豸���
	//���ļ� VideoCapture cap("viedo.short.raw.avi")	//file name
	if (!capture.isOpened())
	{
		cerr << "Can not open a camera or file" << endl;
		return -1;
	}

	Mat edges;
	namedWindow("edges", 1);

	while (true)
	{
		Mat frame;
		capture.read(frame);

		if(frame.empty())
			break;
	
		//����֡��
		if(waitKey(30) >= 0)
			break;
	}

	//д
	Size s(320, 240);
	VideoWriter write = VideoWriter("myvideo.avi", CV_FOURCC('M', 'J', 'P', 'G'), 25, s);

	Mat frame(s, CV_8UC3);
	for (int i = 0; i < 100; ++i)
		write.write(frame);

	return 0;
}