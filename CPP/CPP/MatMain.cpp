#include<opencv2/opencv.hpp>  
#include<iostream>  
using namespace std;


int main() {
	cv::Mat img = cv::imread("D:/GithubRepository/opencv/samples/data/lena.jpg");

	//���Ͻ��ǣ�0,0��
	cv::Rect rect(180, 180, 200, 200);
	cv::Mat pImgRect = img.clone();		//clone()Ϊ���		copyto()ͬ��

	//��ͼ�ϻ����Σ�Scalar() �൱�ڸ�Vector BGR��
	cv::rectangle(pImgRect, rect, cv::Scalar(255, 0, 0), 2);

	cv::imshow("original mage with rectangle", pImgRect);
	cv::imshow("roi", img);

	//������� �� һ �Խ�
	cv::Mat zeroMatrix = cv::Mat::zeros(cv::Size(2, 3), CV_8UC1);			//8λ�޷��� 1��ͨ��
	cv::Mat oneMatrix = cv::Mat::ones(cv::Size(2, 3), CV_32F);			//δָC�� ���ǵ�ͨ��
	cv::Mat eyeMatrix = cv::Mat::eye(cv::Size(2, 3), CV_64F);

	cout << eyeMatrix << endl;

	/*
	cv::Mat imgNew = cv::Mat(pImgRect.rows, pImgRect.cols, CV_32F);
	//���ض�д
	for (int i = 0; i < imgNew.rows; ++i)
	{
		for (int j = 0; j < imgNew.cols; ++j)
		{
			imgNew.at<uchar>(i, j) = (i + j) % 255;
		}
	}
	cv::imshow("newImage", imgNew);
	*/

	//stl������ iterator��ʹ�� ����������������for �ٶȿ�
	//cv::MatIterator_<uchar> grayit, grayend;

	//for (grayit = pImgRect.begin<uchar>(), grayend = pImgRect.end<uchar>(); grayit != grayend; ++grayit)
	//{
	//	*grayit = rand() % 255;
	//}
	//cv::imshow("s", pImgRect);

	cv::Vec3f illu = cv::Vec3f(0.229f, 0.518f, 0.114f);
	//ͨ��ָ�뷽ʽ
	for (int i = 0; i < pImgRect.rows; ++i)
	{
		cv::Vec3b *p = pImgRect.ptr<cv::Vec3b>(i);		//ָ��һ��		ʹ�ò�ͬ�Ľṹ���Ľ����һ���� ���ǻ���template��ģ��

		//����һ��ָ�룬ָ�����������׵�ַ
		for (int j = 0; j < pImgRect.cols; ++j)
		{
			//p[i] = (i + j) % 255;
			//��һ�� �������ˡ�������
			cv::Vec3b pixelValue = p[j];
			p[j] = cv::Vec3b(pixelValue[1], 0, 0);

			//ת��������ͼ
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
	pImgRect.isContinuous();		//�Ƿ���������
	int refCount = *pImgRect.refcount;		//���mat����һ�����ݣ�����


	//���ض�д����4
	//*data ���stepʹ��
	/*uchar* data = pImgRect.data;
	pImgRect.step*/

	//400*400 ȫ��ͼ��
	cv::Mat canvas = cv::Mat(400, 400, CV_8U, cv::Scalar(0));

	for (int col = 0; col < 400; ++col)
	{
		for (int row = 195; row < 205; ++row)
		{
			//��[row,col]�����ص�ĵ�ַ
			//����ǲ�ɫͼ��
			//B: *(canvas.data + canvas.step[0] * row + canvas.step[1] * col)
			//G: *(canvas.data + canvas.step[0] * row + canvas.step[1] * col + canvas.elemSize1())
			//R: *(canvas.data + canvas.step[0] * row + canvas.step[1] * col + canvas.elemSize1() * 2)
			//ע������Ѱַ��ʽ ָ�룬�ٶȱȽϿ�
			*(canvas.data + canvas.step[0] * row + canvas.step[1] * col) = 255;
		}
	}


	cv::imshow("canvas", canvas);

	//Mat_ �࣬Mat_<uchar> m1 = (Mat_<uchar>&)M;  ָ����������
	//ʹ��ʱ M1(i,j) 

	//table ��ʽ ������ɫ�ռ䣬����ٶ�
	int divideWidth = 10;
	uchar table[256];

	//������ɫ�ռ䣬10��Ϊһ����λ	 256����ɫҲ�ͱ����250 /10 25����ɫ�ռ�
	for (int i = 0; i < 256; ++i)
	{
		table[i] = divideWidth * (i / divideWidth);
	}

	//ͼ����Ǿ��� [1 * 256]�ľ���Ҳ����һά���飩
	cv::Mat lookupTable(1, 256, CV_8U);
	uchar* p = lookupTable.data;
	for (int i = 0; i < 256; ++i)
		p[i] = table[i];

	
	//cv::LUT(inputImage,lookuptable,outImage) ����ԭͼ������ľ��ǰ�lookuptableӳ����ͼ�񣬣��е�����python���map()��

	//ͨ�� mat.isempty() �ж� imread()�Ƿ��ǿ�


	cv::waitKey();

	return 0;

}