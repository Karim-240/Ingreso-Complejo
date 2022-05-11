from django.db import models

# Create your models here.

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'app/static/app/QRS')

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    produto = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()

    def __str__(self):
        return self.nombre

class UserComplex(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    QR = models.CharField(max_length=50)
    status = models.CharField(max_length=15)
    tipoUsuario = models.CharField(max_length=50, blank=True)
    token = models.CharField(max_length=50, blank=True)
    fechaCreacion = models.DateField()
    

    def __str__(self):
        return self.correo
    
    