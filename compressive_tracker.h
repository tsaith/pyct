/************************************************************************
* File:	CompressiveTracker.h
* Brief: C++ demo for paper: Kaihua Zhang, Lei Zhang, Ming-Hsuan Yang,"Real-Time Compressive Tracking," ECCV 2012.
* Version: 1.0
* Author: Yang Xian
* Email: yang_xian521@163.com
* Date:	2012/08/03
* History:
* Revised by Kaihua Zhang on 14/8/2012
* Email: zhkhua@gmail.com
* Homepage: http://www4.comp.polyu.edu.hk/~cskhzhang/
************************************************************************/
#pragma once

#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <vector>

typedef unsigned char uint8;

using std::vector;
using namespace cv;
//---------------------------------------------------
class CompressiveTracker {
public:
  CompressiveTracker(void);
  ~CompressiveTracker(void);

private:
  int featureMinNumRect;
  int featureMaxNumRect;
  int featureNum;
  vector<vector<Rect> > features;
  vector<vector<float> > featuresWeight;
  int rOuterPositive;
  vector<Rect> samplePositiveBox;
  vector<Rect> sampleNegativeBox;
  int rSearchWindow;
  Mat imageIntegral;
  Mat samplePositiveFeatureValue;
  Mat sampleNegativeFeatureValue;
  vector<float> muPositive;
  vector<float> sigmaPositive;
  vector<float> muNegative;
  vector<float> sigmaNegative;
  float learnRate;
  vector<Rect> detectBox;
  Mat detectFeatureValue;
  RNG rng;

private:
  void HaarFeature(Rect& _objectBox, int _numFeature);
  void sampleRect(Mat& _image, Rect& _objectBox, float _rInner, float _rOuter, int _maxSampleNum, vector<Rect>& _sampleBox);
  void sampleRect(Mat& _image, Rect& _objectBox, float _srw, vector<Rect>& _sampleBox);
  void getFeatureValue(Mat& _imageIntegral, vector<Rect>& _sampleBox, Mat& _sampleFeatureValue);
  void classifierUpdate(Mat& _sampleFeatureValue, vector<float>& _mu, vector<float>& _sigma, float _learnRate);
  void ratioClassifier(vector<float>& _muPos, vector<float>& _sigmaPos, vector<float>& _muNeg, vector<float>& _sigmaNeg, Mat& _sampleFeatureValue, float& _ratioMax, int& _ratioMaxIndex);
public:
  void processFrame(Mat& _frame, Rect& _objectBox);
  void init(Mat& _frame, Rect& _objectBox);

  void init_wrap(vector<vector<uint8> > &_frame, vector<int> &_objectBox);
  void process_frame_wrap(vector<vector<uint8> > &_frame, vector<int> &_objectBox);
};

void c_get_feature_values_v1(
  vector<vector<double> > &feature_values,
  vector<vector<int> > boxes,
  vector<vector<vector<int> > > features,
  vector<vector<double> > weights,
  vector<vector<double> > integral_image);

void c_get_feature_values(
  vector<vector<double> > &feature_values,
  vector<Rect> boxes,
  vector<vector<Rect> > features,
  vector<vector<double> > weights,
  vector<vector<double> > integral_image);

void c_ratio_classifier(
  int &index_ratio_max, double &ratio_max,
  vector<double> mu_pos, vector<double> sigma_pos,
  vector<double> mu_neg, vector<double> sigma_neg,
  vector<vector<double> > feature_values);
