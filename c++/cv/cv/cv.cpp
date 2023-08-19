#include <iostream>
#include <opencv2/ml.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/core/mat.hpp>
#include <iostream>
#include <vector>
#include <string>

using namespace cv;
using namespace std;

void get_conturs_feagurs(Mat& bw_image, Mat& color_image, int obl_low, int obl_high)
{
    vector<vector<Point>> contours; // тут храним контуры
    vector <Vec4i> hierarchy; // vec4i означает, что есть 4 int переменные typedef vec <int, 4> vec4i в векторе;
    findContours(bw_image, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

    vector<vector<Point>> contourOblast(contours.size());
    vector<Rect> b_rect(contours.size());

    // убираем дефект контура
    for (int i = 0; i < contours.size(); ++i) {
        int oblast = contourArea(contours[i]);

        if (oblast > obl_low && oblast < obl_high) {
            float perimetr = arcLength(contours[i], true);
            approxPolyDP(contours[i], contourOblast[i], 0.025 * perimetr, true);

            b_rect[i] = boundingRect(contourOblast[i]);

            int number_of_corners = (int)contourOblast[i].size();

            if (number_of_corners >= 4 && number_of_corners <= 5)
            {
                putText(color_image, "box", Point(b_rect[i].x, b_rect[i].y - 5), FONT_HERSHEY_PLAIN, 1, Scalar(0, 0, 255), 1);
                drawContours(color_image, contourOblast, i, Scalar(255, 0, 255), 2);
                rectangle(color_image, b_rect[i].tl(), b_rect[i].br(), Scalar(0, 0, 255), 2);
            }
        }
    }
}


void detection(Mat image, Mat correct_image, int up, int low, int obl_l, int obl_h, int blur, int divergent, int dil, string name)
{
    Mat copy_image, blur_image, canny_image, dilate_image, bilatera_image, bynary;

    copy_image = image;
    int Dilate = dil + 1;
    int Low = low;
    int Up = up;
    int Oblast_L = obl_l;
    int Oblast_H = obl_h;
    int Blur = blur * 2 + 1;
    int Divergent = divergent;

    threshold(correct_image, bynary, Low, Up, THRESH_BINARY);
    GaussianBlur(bynary, blur_image, Size(Blur, Blur), divergent, 1);
    Canny(blur_image, canny_image, Low, Up, 3, true);
    Mat p_dilate = getStructuringElement(MORPH_RECT, Size(Dilate, Dilate));
    dilate(canny_image, dilate_image, p_dilate);
    get_conturs_feagurs(dilate_image, copy_image, Oblast_L, Oblast_H);
    string window_name = name;
    imshow(name, copy_image);
    waitKey(30);

}

void correct_image(Mat image, string name, int up, int low, int obl_l, int obl_h, int blur, int divergent, int dil)
{
    resize(image, image, Size(300, 300), INTER_LINEAR);
    Mat gray_image, blur_image, canny_image, dilate_image, bilatera_image, m_image, bynary, mask_hsv, hsvImage;

    int channels = image.channels();
    int meanH, meanS, meanV, hValues = 0, sValues = 0, vValues = 0;
    // Переводим изображение 
    cvtColor(image, gray_image, COLOR_BGR2GRAY);
    cvtColor(image, hsvImage, COLOR_BGR2HSV);

    if (3 == channels)
    {
        int rowNumber = hsvImage.rows; // Количество строк
        int colNumber = hsvImage.cols; // Количество столбцов

        Point pointVal;
        for (int i = 0; i < rowNumber; i++) // цикл строки, при необходимости можно заменить на rowNumber
        {
            for (int j = 0; j < colNumber; j++) // цикл столбца, та же причина
            {
                pointVal.x = j;
                pointVal.y = i;

                hValues += hsvImage.at <Vec3b>(Point(pointVal))[0]; // значение серого H канала
                sValues += hsvImage.at <Vec3b>(Point(pointVal))[1]; // значение серого канала S
                vValues += hsvImage.at <Vec3b>(Point(pointVal))[2]; // значение серого V-канала
                //cout << intensity << " " ;
            }
            cout << endl;
        }

        meanH = hValues / (rowNumber * colNumber); // Среднее значение H изображения области
        meanS = sValues / (rowNumber * colNumber); // Среднее значение S изображения области
        meanV = vValues / (rowNumber * colNumber); // Среднее значение V изображения области
    }

    inRange(hsvImage, Scalar(meanH - 10, meanS, meanV), Scalar(meanH + 10, 255, 255), mask_hsv);
    bitwise_and(image, image, hsvImage, mask_hsv);
    Mat copy_image = image.clone();
    
    detection(copy_image, hsvImage, up, low, obl_l, obl_h, blur, divergent, dil, name);
    detection(copy_image, gray_image, up, low, obl_l, obl_h, blur, divergent, dil, name);
    waitKey(0);
}


int main()
{
    // Указываем путь к файлу 
    Mat image1 = imread("j1.jpg");
    Mat image2 = imread("j2.jpg");
    Mat image3 = imread("j3.jpg");
    Mat image4 = imread("j4.jpg");

    correct_image(image1, "image1", 216, 132, 44, 323, 2, 0, 0);
    correct_image(image2, "image2", 203, 195, 242, 469, 9, 3, 1);
    correct_image(image3, "image3", 53, 4, 76, 131, 1, 4, 0);
    correct_image(image4, "image4", 255, 116, 428, 1000, 1, 4, 0);

    return 0;
}
