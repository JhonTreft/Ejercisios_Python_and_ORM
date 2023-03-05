#1. Crear un modelo para una tabla de usuarios con los campos id, nombre, correo electrónico y contraseña. Crear un método para buscar usuarios por correo electrónico.


from django.contrib.auth.models import User

from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def find_by_email(cls, email):
        try:
            return cls.objects.get(email=email)
        except cls.DoesNotExist:
            return None




#2. Crear un modelo para una tabla de productos con los campos id, nombre, descripción y precio. Crear un método para buscar productos por nombre.



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    @classmethod
    def find_by_name(cls, name):
        return cls.objects.filter(name__icontains=name)


#3. Crear un modelo para una tabla de órdenes con los campos id, fecha de creación, fecha de envío, estado y usuario. Crear un método para buscar órdenes por usuario.

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    shipped_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered')
    ))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

    @classmethod
    def find_by_user(cls, user):
        return cls.objects.filter(user=user)



#4. Crear un modelo para una tabla de comentarios con los campos id, texto, fecha de creación y producto. Crear un método para buscar comentarios por producto.


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment #{self.id} - Product: {self.product.name}"

    @classmethod
    def find_by_product(cls, product):
        return cls.objects.filter(product=product)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


#5. Crear un modelo para una tabla de categorías con los campos id y nombre. Crear un método para buscar productos por categoría.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def find_products(self):
        return Product.objects.filter(category=self)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name__icontains


#6. Crea una base de datos con una tabla de usuarios y una tabla de publicaciones. Cada publicación pertenece a un usuario, y cada usuario puede tener varias publicaciones. Usa un ORM para crear las tablas y definir las relaciones entre ellas.


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title


#7. Crea un modelo de una tienda en línea con ORM. El modelo debe incluir productos, clientes y pedidos. Los productos tienen un nombre, una descripción y un precio. Los clientes tienen un nombre, una dirección y una lista de pedidos. Los pedidos contienen una lista de productos y la información de envío. Define las relaciones entre los modelos y crea las tablas en la base de datos.



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='OrderItem')
    shipping_address = models.CharField(max_length=255)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


#8. Crea un modelo de una biblioteca con ORM. El modelo debe incluir libros, autores y préstamos. Los libros tienen un título, una descripción y un autor. Los autores tienen un nombre y una lista de libros escritos. Los préstamos contienen la información del libro prestado, el usuario que lo ha tomado y la fecha de devolución. Define las relaciones entre los modelos y crea las tablas en la base de datos.




class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.book} - {self.borrower.username}"


#9. Crea un modelo de una aplicación de redes sociales con ORM. El modelo debe incluir usuarios, publicaciones y comentarios. Cada publicación pertenece a un usuario, y cada usuario puede tener varias publicaciones. Cada publicación puede tener varios comentarios, y cada comentario pertenece a una publicación y a un usuario. Define las relaciones entre los modelos y crea las tablas en la base de datos.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.post}: {self.content}"


#10. Crea un modelo de una aplicación de música con ORM. El modelo debe incluir canciones, álbumes y artistas. Cada canción pertenece a un álbum, y cada álbum pertenece a un artista. Los artistas tienen un nombre y una lista de álbumes y canciones. Define las relaciones entre los modelos y crea las tablas en la base de datos.


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.title

