from sqlalchemy import DateTime,ForeignKey
from datetime import datetime
from app import db

usuarios_fondos = db.Table('usuarios_fondos',
				db.Column('usuario_email',db.String(100),ForeignKey('usuario.email'),primary_key=True),
				db.Column('fondo_id',db.Integer,ForeignKey('fondo.id'),primary_key=True)
)
class Usuario(db.Model):
  email = db.Column(db.String(120),primary_key=True,index=True,unique=True)
  password = db.Column(db.String(128)) # Variado, depende el hash
  nombre = db.Column(db.String(60),index=True)
  apellido = db.Column(db.String(60),index=True)

  permisos = db.relationship('Permiso', backref='usuario') #relacion de uno a muchos //listo
  fondos = db.relationship('Fondo',secondary=usuarios_fondos, lazy='subquery',backref=db.backref('usuarios',lazy=True)) # relacion de muchos a muchos //listo
  to_dos = db.relationship('To_do',backref='usuario')
  def __repr__(self):
    return '<User {} {}>'.format(self.nombre,self.correo)

class Permiso(db.Model):
	servicio = db.Column(db.String(20), primary_key=True)
	usuario_correo = db.Column(db.String(120),ForeignKey('usuario.email'),primary_key=True,nullable=False) 
	token = db.Column(db.String(120))
	permiso = db.Column(db.String(200))
	fecha_inicio = db.Column(db.DateTime, default=datetime.utcnow) 
	#fecha_fin = db.Column(db.String(60)=str(int(fecha_inicio)+100),index=True)

class Fondo(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
    link = db.Column(db.String(200))
    categoria = db.Column(db.String(20))

class To_do(db.Model):
	id = db.Column(db.Integer, primary_key=True,autoincrement=True,nullable=False)
	usuario_to_do = db.Column(db.String(60),ForeignKey('usuario.email'),nullable=False) 

	actividades = db.relationship('Actividad',backref='to_do') # relacion de uno a muchos //listo
class Actividad(db.Model):
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	to_do_id = db.Column(db.Integer,ForeignKey('to_do.id'),primary_key=True,nullable=False)
	estado = db.Column(db.String(1))
	actividad = db.Column(db.String(100))
