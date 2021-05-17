class transversalSection:

    def __init__(self, yVector, zVector):
        self.yVector = yVector
        self.zVector = zVector

    '''yLimits = [self.max(yVector), min(self_.yVector)]
    zLimits = [max(self.zVector), min(self.zVector)]'''

    def getSectionArea(self):
        area = [0.5*(self.yVector[i] + self.yVector[i+1]) * (-self.zVector[i] + self.zVector[i+1]) for i in range(0, len(self.yVector) - 1)]
        return round(sum(area), 4)

    def getYCentroid(self):
        yCentroid = [-1/6 * (self.zVector[i] - self.zVector[i+1]) * (self.yVector[i+1]**2 + self.yVector[i]**2 + self.yVector[i] * self.yVector[i+1]) for i in range(0, len(self.yVector) - 1)]
        return round((sum(yCentroid)/self.getSectionArea()), 4)

    def getYInertia(self):
        inertiaY = [(1/12 * (self.yVector[i] * self.zVector[i+1] - self.yVector[i+1] * self.zVector[i])*(self.zVector[i]**2 + self.zVector[i] * self.zVector[i+1] + self.zVector[i+1]**2)) for i in range(0, len(self.yVector) - 1)]
        return round((sum(inertiaY) - self.getSectionArea()*self.getZCentroid()**2), 4)

    def getZCentroid(self):
        zCentroid = [1/6 * (self.yVector[i] - self.yVector[i+1]) * (self.zVector[i+1]**2 + self.zVector[i]**2 + self.zVector[i]*self.zVector[i+1]) for i in range(0, len(self.zVector) - 1)]
        return round((sum(zCentroid) / self.getSectionArea()), 4)

    def getZInertia(self):
        inertiaZ = [1/12 * (self.yVector[i] * self.zVector[i+1] - self.yVector[i+1]*self.zVector[i]) * (self.yVector[i]**2 + self.yVector[i] * self.yVector[i+1] + self.yVector[i+1]**2) for i in range(0, len(self.yVector) - 1)]
        return round((sum(inertiaZ) - self.getSectionArea()*self.getYCentroid()**2), 4)

    def getProductMomentOfArea(self):
        productMoment = [1/24*(self.yVector[i] * self.zVector[i+1] - self.yVector[i+1] * self.zVector[i]) * (self.yVector[i] * self.zVector[i+1] + 2 * self.yVector[i] * self.zVector[i] + 2 * self.yVector[i+1] * self.zVector[i+1] + self.yVector[i+1] * self.zVector[i]) for i in range(0, len(self.yVector) - 1)]
        return round((sum(productMoment) - self.getSectionArea()*self.getZCentroid() * self.getYCentroid()), 4)

    def returnAllParameters(self):
        print('\nÁrea = ' + str(self.getSectionArea()) + '\n')
        print('Centroide: yc = ' + str(self.getYCentroid()) + ', zc = ' + str(self.getZCentroid()) + '\n')
        print('Inércia: Iy = ' + str(self.getYInertia()) + ', Iz = ' + str(self.getZInertia()) + '\n')
        print('Produto de inércia = ' + str(self.getProductMomentOfArea()))

# Teste
section = transversalSection(
    yVector=[0, 10, 10, 25, 25, 0, 0],
    zVector=[0, 0, 15, 15, 20, 20, 0]
)
section.returnAllParameters()
