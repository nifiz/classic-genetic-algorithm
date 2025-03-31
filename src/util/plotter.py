import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Plotter3D:
    def __init__(
            self,
            x_axis: list, 
            y_axis: list, 
            z_axis: list,
            x_axis_label: str = "",
            y_axis_label: str = "",
            z_axis_label: str = ""):
        self._fig = plt.figure()
        self._ax = self._fig.add_subplot(111, projection='3d')
        self._ax.set_xlabel(x_axis_label)
        self._ax.set_ylabel(y_axis_label)
        self._ax.set_zlabel(z_axis_label)
        self._x_axis = x_axis
        self._y_axis = y_axis
        self._z_axis = z_axis

    def build(self):
        self._ax.cla()
        self._ax.scatter(self._x_axis, self._y_axis, self._z_axis, c=self._z_axis, cmap='viridis')
        return self._fig
    
    def show(self):
        plt.show()
    
    def set_x_axis(self, x_axis):
        self._x_axis = x_axis
    
    def set_y_axis(self, y_axis):
        self._y_axis = y_axis

    def set_z_axis(self, z_axis):
        self._z_axis = z_axis

