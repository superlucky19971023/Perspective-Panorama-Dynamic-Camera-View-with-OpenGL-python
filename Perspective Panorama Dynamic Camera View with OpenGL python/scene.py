from model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        n, s = 20, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        for i in range(7):
            add(Cube(app, pos=(18, i * s, -7 + i), tex_id=2))
            add(Cube(app, pos=(18, i * s, 5 - i), tex_id=2))


        self.moving_cube = MovingCube(app, pos=(2, 8 ,6), scale=(3, 3, 3), tex_id=1)
        add(self.moving_cube)

        # Adding a Sphere to the scene
        # self.sphere = Sphere(app, pos=(2,8,-12), scale=(3, 3, 3), tex_id=3)
        # add(self.sphere)

        # Adding a moving sphere
        self.moving_sphere = MovingSphere(app, pos=(2, 8, -12), scale=(3, 3, 3), tex_id=3)
        add(self.moving_sphere)

    def update(self):
        self.moving_cube.rot.xyz = self.app.time
        self.moving_sphere.rot.xyz = self.app.time  # Optionally update sphere's rotation
        for obj in self.objects:
            obj.update()
