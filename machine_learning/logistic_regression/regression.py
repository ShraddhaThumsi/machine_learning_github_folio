import numpy as np
class LogisticRegression:
    def initialize(self,X):
        weights = np.zeros((X.shape[1]+1,1))
        X = np.c_[np.ones(X.shape[0],1),X]
        return weights,X
    def sigmoid(self,z):
        sig = 1/(1+(np.e ** -z))
        return sig

    def cost(self,X,y,theta):
        z = np.dot(X,theta)
        cost0 = np.dot(y.T,np.log(self.sigmoid(z)))
        cost1 = np.dot((1-y).T,np.log(1-self.sigmoid(z)))
        cost = -((cost0 + cost1))/len(y)
        return cost

    def fit(self,X,y,alpha=0.001,iter=100):
        params,X = self.initialize(X)
        cost_list = np.zeros(iter,)
        for i in range(iter):
            params = params - alpha * np.dot(X.T,self.sigmoid(np.dot(X,params))-np.reshape(y,(len(y),1)))
            cost_list[i] = self.cost(X,y,params)
        self.params = params
        return cost_list

    def predict(self,X,weights):
        z = np.dot(self.initialize(X)[1],weights)
        l = []
        for i in self.sigmoid(z):
            if i > 0.5:
                l.append(1)
            else:
                l.append(0)