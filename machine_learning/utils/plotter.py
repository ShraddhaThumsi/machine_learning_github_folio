import matplotlib.pyplot as plt
import numpy as np
def plot_variance(X_train,y_train,X_test,y_test,regression_model):
    ## setting plot style
    plt.style.use('fivethirtyeight')


    ## plotting residual errors in training data
    plt.scatter(regression_model.predict(X_train), regression_model.predict(X_train) - y_train,
                color="green", s=10, label='Train data')

    ## plotting residual errors in test data
    plt.scatter(regression_model.predict(X_test), regression_model.predict(X_test) - y_test,
                color="blue", s=10, label='Test data')

    ## plotting line for zero residual error
    # plt.hlines(y=reg.score(X_train, y_train),xmin=0,xmax=3500,linewidth=2,color='b',label='closeness score of train data')
    plt.hlines(y=regression_model.score(X_test, y_test), xmin=0, xmax=3500, linewidth=2, color='r',
               label='closeness score of test data')

    ## plotting legend
    plt.legend(loc='lower right')

    ## plot title
    plt.title("Closeness to true total cereal production in lakh tonnes from 1950-2021")

    ## method call for showing the plot
    plt.show()


def plot_regression_line(x, y, b_0,b_1,crop='',is_singlevariate=True):
    # plotting the actual points as scatter plot


    if is_singlevariate:
        plt.scatter(x, y, color="m",
                marker="o", s=12)
    else:
        list_of_sums_of_indiv_x = []
        for item in list(x):
            su = sum(item)
            list_of_sums_of_indiv_x.append(su)

        reformatted_x = np.array(list_of_sums_of_indiv_x).astype(np.float)
        plt.scatter(reformatted_x,y,color='m',marker='o',s=12)

    # predicted response vector
    if is_singlevariate:
        y_pred = b_0 + x*b_1
        # plotting the regression line

    else:
        y_pred = b_0 + np.matmul(x,b_1)

    plt.plot(x, y_pred, color="g")



    # putting labels
    if is_singlevariate:
        crop_for_analysis = crop
    else:
        crop_for_analysis = 'Rice,Wheat,Cereal'
    plt.xlabel(f'Production of {crop_for_analysis}')
    plt.ylabel(f'Total production of cereal crops')
    plt.title(f'Total cereal production given {crop_for_analysis} in lakh tonne from 1950-2021')
    # function to show plot
    plt.show()


def plot_loss_function(numof_iters,loss_list):
    plt.scatter(numof_iters,loss_list, color='m', marker='o', s=12)
    plt.xlabel(f'Number of iterations')
    plt.ylabel(f'Cost funcion (aka log loss)')
    plt.title(f'Curve of loss function over all iterations')
    plt.show()
