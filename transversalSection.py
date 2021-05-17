class TransversalSection:

    def __init__(self, yVector, zVector):
        self.yVector = yVector
        self.zVector = zVector
        self.area = self.getSectionArea()
        self.yc = self.getYCentroid()
        self.zc = self.getZCentroid()
        self.iy = self.getYInertia()
        self.iz = self.getZInertia()
        self.iyz = self.getProductMomentOfArea()

    def getSectionArea(self):
        area = [0.5*(self.yVector[i] + self.yVector[i+1]) * (-self.zVector[i] + self.zVector[i+1]) for i in range(0, len(self.yVector) - 1)]
        return round(sum(area), 4)

    def getYCentroid(self):
        yCentroid = [-1/6 * (self.zVector[i] - self.zVector[i+1]) * (self.yVector[i+1]**2 + self.yVector[i]**2 + self.yVector[i] * self.yVector[i+1]) for i in range(0, len(self.yVector) - 1)]
        return round((sum(yCentroid)/self.area), 4)

    def getYInertia(self):
        inertiaY = [(1/12 * (self.yVector[i] * self.zVector[i+1] - self.yVector[i+1] * self.zVector[i])*(self.zVector[i]**2 + self.zVector[i] * self.zVector[i+1] + self.zVector[i+1]**2)) for i in range(0, len(self.yVector) - 1)]
        return round((sum(inertiaY) - self.area*self.getZCentroid()**2), 4)

    def getZCentroid(self):
        zCentroid = [1/6 * (self.yVector[i] - self.yVector[i+1]) * (self.zVector[i+1]**2 + self.zVector[i]**2 + self.zVector[i]*self.zVector[i+1]) for i in range(0, len(self.zVector) - 1)]
        return round((sum(zCentroid) / self.area), 4)

    def getZInertia(self):
        inertiaZ = [1/12 * (self.yVector[i] * self.zVector[i+1] - self.yVector[i+1]*self.zVector[i]) * (self.yVector[i]**2 + self.yVector[i] * self.yVector[i+1] + self.yVector[i+1]**2) for i in range(0, len(self.yVector) - 1)]
        return round((sum(inertiaZ) - self.area*self.getYCentroid()**2), 4)

    def getProductMomentOfArea(self):
        productMoment = [1/24*(self.yVector[i] * self.zVector[i+1] - self.yVector[i+1] * self.zVector[i]) * (self.yVector[i] * self.zVector[i+1] + 2 * self.yVector[i] * self.zVector[i] + 2 * self.yVector[i+1] * self.zVector[i+1] + self.yVector[i+1] * self.zVector[i]) for i in range(0, len(self.yVector) - 1)]
        return round((sum(productMoment) - self.area*self.getZCentroid() * self.getYCentroid()), 4)

    def returnAllParameters(self):
        print('\nÁrea = ' + str(self.area) + '\n')
        print('Centroide: yc = ' + str(self.yc) + ', zc = ' + str(self.zc) + '\n')
        print('Inércia: Iy = ' + str(self.iy) + ', Iz = ' + str(self.iz) + '\n')
        print('Produto de inércia = ' + str(self.iyz))

class Calculator:

    def __init__(self, TransversalSection, Nx, My, Mz):
        self.transversalSection = TransversalSection
        self.Nx = Nx
        self.My = My
        self.Mz = Mz
        self.yLimits = [max(self.transversalSection.yVector), min(self.transversalSection.yVector)]
        self.zLimits = [max(self.transversalSection.zVector), min(self.transversalSection.zVector)]

    


# Teste
section = TransversalSection(
    yVector=[0, 10, 10, 25, 25, 0, 0],
    zVector=[0, 0, 15, 15, 20, 20, 0]
)
section.returnAllParameters()
