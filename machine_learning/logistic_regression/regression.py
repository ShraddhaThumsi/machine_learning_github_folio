import numpy as np
class LogisticRegression:
    def initialize(self,X):
        weights = np.zeros((X.shape[1]+1,1))
        X = np.c_[np.ones((X.shape[0],1)),X]
        return weights,X
    def sigmoid(self,z):
        return 1/(1+(np.e ** -z))




    def fit(self,X,y,alpha=0.001,iter=200):
        weights,X = self.initialize(X)
        cost_list = np.zeros(iter,)

        def cost(theta):
            z = np.dot(X, theta)
            cost0 = np.dot(y.T, np.log(self.sigmoid(z)))
            cost1 = np.dot((1 - y).T, np.log(1 - self.sigmoid(z)))
            cost = -((cost0 + cost1)) / len(y)
            return cost
        for i in range(iter):
            weights = weights - alpha * np.dot(X.T,self.sigmoid(np.dot(X,weights))-np.reshape(y,(len(y),1)))
            cost_list[i] = cost(weights)
        self.weights = weights
        return iter,cost_list

    def predict(self,X):
        z = np.dot(self.initialize(X)[1],self.weights)
        l = []
        for i in self.sigmoid(z):
            if i > 0.5:
                l.append(1)
            else:
                l.append(0)
        return l

def F1_score(y,y_hat):
    tp,tn,fp,fn=0,0,0,0
    for i in range(len(y)):
        if y[i]==1 and y_hat[i]==1:
            tp += 1
        if y[i]==0 and y_hat[i]==0:
            tn+=1
        if y[i]==0 and y_hat[i]==1:
            fp += 1
        if y[i] == 1 and y_hat[i] == 0:
            fn += 1
    precision = tp / (tp+fp)
    recall = tp / (tp + fn)
    f1_score = 2*precision*recall/(precision+recall)
    return f1_score