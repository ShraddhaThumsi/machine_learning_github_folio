import matplotlib.pyplot as plt
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
