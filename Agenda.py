class Agenda:
    def __init__(self):
        self.contactos = []

    def alta_contacto(self, contacto):
        self.contactos.append(contacto)

    def baja_contacto(self, nombre, apellido):
        self.contactos = [c for c in self.contactos if not (c.nombre == nombre and c.apellido == apellido)]

    def modificar_contacto(self, nombre, apellido, telefono=None, direccion=None):
        for contacto in self.contactos:
            if contacto.nombre == nombre and contacto.apellido == apellido:
                contacto.telefono = telefono if telefono else contacto.telefono
                contacto.direccion = direccion if direccion else contacto.direccion
                return True
        return False

    def listar_contactos(self):
        return ''.join(f'<p>{contacto.nombre} {contacto.apellido} - Tel: {contacto.telefono}, Dir: {contacto.direccion}</p>' for contacto in self.contactos)
