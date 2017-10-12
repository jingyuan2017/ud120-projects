#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    print '-------------------------------------------';

    #print predictions;

    print ages;

    print len(ages)
    #print net_worths;


    resultX = [];

    print type(resultX)

    for i in range(0 , len(ages)):
        print ages[i];
        abss = abs(predictions[i] - net_worths[i]);
        print abss;

        tmp = (abss , (ages[i] , net_worths[i] , abss));

        resultX.append(tmp);

    print resultX;


    print '-------------------------------------------';

    resultX.sort(key=lambda x:x[0]);

    print resultX;

    resultX = resultX[:81];

    for i in range(0 , len(resultX)):
        cleaned_data.append(resultX[i][1]);
    #print resultX.sort(lambda x,y:cmp(x[0],y[0]));
    
    return cleaned_data

