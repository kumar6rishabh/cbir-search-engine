A small but complete cbir search engine

The implementation of this search engine is based on the idea of histograms and color coherence vectors.

1> Histogram based approach.
     The histogram based approach is implemented using two python files, histogram.py and histogram_searcher.py.
         The first file, histogram.py, creates features based on the histograms of every image. But there is a certain way we are going to do it. Firstly, we are going to divide the image into 5 parts. The first part will be an ellipse in the centre of the image and others will be rectangle with 1/4 of the ellipse cut from it. For all the five parts, eliipse and subtracted rectangles, we will calculate the histogram using the cv.calcHist() function.
         Each histogram in broken into bins. These bins will become the feature vectors. 
        
         The second file, histogram_searcher.py, creates features for a query image in the same way as we made feature vectors for all the images in the database. For with every row in the csv file having the features vector for every image, we find the euclidean distance with the query image. Then the distances are sorted and the closest 10 images are taken as the most similar images and displayed.
         
2> Color Coherence Vector based approach.
     The Color Coherence Vector(ccv) is also implemented using two python files, ccv.py and ccv_searcher.py.
          The first file, ccv.py, just like histogram.py file creates feature vectors for every image in the database, but instead find the connected components for every image. The implementation of connected components is explained in detail in the video on my Youtube channel. 
          The second file, ccv_searcher.py creates feature vectors for the query image in the same way as we made feature vectors for all the images in the database.For with every row in the csv file having the features vector for every image, we find the euclidean distance with the query image. Then the distances are sorted and the closest 10 images are taken as the most similar images and displayed.
