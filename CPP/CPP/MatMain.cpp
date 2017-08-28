#include<opencv2/opencv.hpp>  
#include<iostream>  
using namespace std;


int main() {
	cv::Mat img = cv::imread("D:/GithubRepository/opencv/samples/data/lena.jpg");

	//左上角是（0,0）
	cv::Rect rect(180, 180, 200, 200);
	cv::Mat pImgRect = img.clone();		//clone()为深拷贝		copyto()同理

	//在图上画矩形（Scalar() 相当于个Vector BGR）
	cv::rectangle(pImgRect, rect, cv::Scalar(255, 0, 0), 2);

	cv::imshow("original mage with rectangle", pImgRect);
	cv::imshow("roi", img);

	//特殊矩阵 零 一 对角
	cv::Mat zeroMatrix = cv::Mat::zeros(cv::Size(2, 3), CV_8UC1);			//8位无符号 1个通道
	cv::Mat oneMatrix = cv::Mat::ones(cv::Size(2, 3), CV_32F);			//未指C几 就是单通道
	cv::Mat eyeMatrix = cv::Mat::eye(cv::Size(2, 3), CV_64F);

	cout << eyeMatrix << endl;

	/*
	cv::Mat imgNew = cv::Mat(pImgRect.rows, pImgRect.cols, CV_32F);
	//像素读写
	for (int i = 0; i < imgNew.rows; ++i)
	{
		for (int j = 0; j < imgNew.cols; ++j)
		{
			imgNew.at<uchar>(i, j) = (i + j) % 255;
		}
	}
	cv::imshow("newImage", imgNew);
	*/

	//stl迭代器 iterator的使用 迭代器比上面两层for 速度快
	//cv::MatIterator_<uchar> grayit, grayend;

	//for (grayit = pImgRect.begin<uchar>(), grayend = pImgRect.end<uchar>(); grayit != grayend; ++grayit)
	//{
	//	*grayit = rand() % 255;
	//}
	//cv::imshow("s", pImgRect);

	cv::Vec3f illu = cv::Vec3f(0.229f, 0.518f, 0.114f);
	//通过指针方式
	for (int i = 0; i < pImgRect.rows; ++i)
	{
		cv::Vec3b *p = pImgRect.ptr<cv::Vec3b>(i);		//指向一行		使用不同的结构出的结果不一样。 都是基于template的模板

		//回忆一下指针，指针就是数组的首地址
		for (int j = 0; j < pImgRect.cols; ++j)
		{
			//p[i] = (i + j) % 255;
			//作一下 都变蓝了。哈哈哈
			cv::Vec3b pixelValue = p[j];
			p[j] = cv::Vec3b(pixelValue[1], 0, 0);

			//转换成亮度图
			//p[j] = pixelValue[0] * illu[0] + pixelValue[1] * illu[1] + pixelValue[2] * illu[2];

		}
	}

	cv::imshow("eeee", pImgRect);



	//for (int i = 0; i < pImgRect.rows; ++i)
	//{
	//	for (int j = 0; j < pImgRect.cols; ++j)
	//	{
	//		cv::Vec3b pixel;

	//		pixel = pImgRect.at<cv::Vec3b>(i, j);



	//		pImgRect			//mat.at
	//	}
	//}

	//flag
	pImgRect.isContinuous();		//是否是连续的
	int refCount = *pImgRect.refcount;		//多个mat共享一个数据，就是


	//像素读写方法4
	//*data 配合step使用
	/*uchar* data = pImgRect.data;
	pImgRect.step*/

	//400*400 全黑图像
	cv::Mat canvas = cv::Mat(400, 400, CV_8U, cv::Scalar(0));

	for (int col = 0; col < 400; ++col)
	{
		for (int row = 195; row < 205; ++row)
		{
			//第[row,col]个像素点的地址
			//如果是彩色图像
			//B: *(canvas.data + canvas.step[0] * row + canvas.step[1] * col)
			//G: *(canvas.data + canvas.step[0] * row + canvas.step[1] * col + canvas.elemSize1())
			//R: *(canvas.data + canvas.step[0] * row + canvas.step[1] * col + canvas.elemSize1() * 2)
			//注意这种寻址方式 指针，速度比较快
			*(canvas.data + canvas.step[0] * row + canvas.step[1] * col) = 255;
		}
	}


	cv::imshow("canvas", canvas);

	//Mat_ 类，Mat_<uchar> m1 = (Mat_<uchar>&)M;  指明数据类型
	//使用时 M1(i,j) 

	//table 方式 减低颜色空间，提高速度
	int divideWidth = 10;
	uchar table[256];

	//降低颜色空间，10个为一个单位	 256个颜色也就变成了250 /10 25个颜色空间
	for (int i = 0; i < 256; ++i)
	{
		table[i] = divideWidth * (i / divideWidth);
	}

	//图像就是矩阵 [1 * 256]的矩阵（也就是一维数组）
	cv::Mat lookupTable(1, 256, CV_8U);
	uchar* p = lookupTable.data;
	for (int i = 0; i < 256; ++i)
		p[i] = table[i];

	
	//cv::LUT(inputImage,lookuptable,outImage) 输入原图像，输出的就是按lookuptable映射后的图像，（有点类型python里的map()）

	//通过 mat.isempty() 判断 imread()是否是空


	cv::waitKey();

	return 0;

}