class AdministradorDBRouter:
    # Aplicaciones
    router_app_labels = {
        'auth', 'contenttypes', 'sessions', 'admin'
    }
    
    # Metodos
    
    # Leer datos
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            # El dato se toma de apps.py y de la clase meta de los models.py
            return 'default'
        return None
    
    # Escribir datos
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return 'default'
        return None
    
    # Permitir la relacion
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.router_app_labels or obj2._meta.app_label in self.router_app_labels:
            return True
        return None
    
    # Permitir la migracion
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == 'default'
        return None

class EmpleadosRouter:
    # Metodos
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'empleados':
            return 'empleados'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'empleados':
            return 'empleados'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'empleados' or obj2._meta.app_label == 'empleados':
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'empleados':
            return db == 'empleados'
        return None

class DepartamentosRouter:
    # Metodos
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'departamentos':
            return 'departamentos'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'departamentos':
            return 'departamentos'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'departamentos' or obj2._meta.app_label == 'departamentos':
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'departamentos':
            return db == 'departamentos'
        return None

class PuestosRouter:
    # Metodos
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'puestos':
            return 'puestos'
        return None
   
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'puestos':
            return 'puestos'
        return None
   
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'puestos' or obj2._meta.app_label == 'puestos':  # Corregido aquí
            return True
        return None
   
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'puestos':
            return db == 'puestos'
        return None