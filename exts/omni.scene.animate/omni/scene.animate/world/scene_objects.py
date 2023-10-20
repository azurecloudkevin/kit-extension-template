import move_robot as mv

class SceneObject:
    def __init__(self, name, path, x, y, z, rx, ry, rz, plane):
        self.name = name
        self.path = path
        self.x = x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz
        self.plane = plane
    
    def turn(self, angle):
        turnvector = mv.degrees_to_vector(angle, self.plane)
        