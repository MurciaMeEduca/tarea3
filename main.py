class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Contacto(Persona):
    def __init__(self, nombre, apellido, telefono, direccion):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.direccion = direccion

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

def formato_html(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<html><body>{result}</body></html>"
    return wrapper

Agenda.listar_contactos = formato_html(Agenda.listar_contactos)

if __name__ == '__main__':
    mi_agenda = Agenda()
    mi_agenda.alta_contacto(Contacto('Juan', 'Pérez', '123456789', 'Calle Falsa 123'))
    mi_agenda.alta_contacto(Contacto('Ana', 'López', '987654321', 'Avenida Siempreviva 742'))
    print(mi_agenda.listar_contactos())

