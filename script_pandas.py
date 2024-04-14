import random
import pandas as pd

class GeneradorDatos:
    @staticmethod
    def generar_departamentos(cantidad):
        departamentos = ["Tecnología", "Ventas", "Recursos Humanos", "Contabilidad", "Marketing"]
        departamentos_data = {
            "id": list(range(1, cantidad + 1)),
            "nombre": departamentos[:cantidad]
        }
        return pd.DataFrame(departamentos_data)

    @staticmethod
    def generar_puestos_trabajo(cantidad, departamentos_df):
        puestos_de_trabajo = ["Desarrollador", "Gerente de Ventas", "Reclutador", "Contador", "Especialista en Marketing"]
        puestos_data = {
            "id": list(range(1, cantidad + 1)),
            "nombre": puestos_de_trabajo[:cantidad],
            "departamento_id": [random.choice(departamentos_df["id"]) for _ in range(cantidad)]
        }
        return pd.DataFrame(puestos_data)

    @staticmethod
    def generar_empleados(cantidad, puestos_df):
        nombre_ficticios = ["Fabian Ramirez", "Vivian Perez", "Juana Rodriguez", "Mario Rueda", "Patricia Benitez", "Julian Perez", "Pablo Restrepo", "Maria Hincapie"]
        nombres_aleatorios = [random.choice(nombre_ficticios) for _ in range(cantidad)]
        habilidades = ["Python", "Ventas", "Entrevista", "Contabilidad", "Redes Sociales"]
        empleados_data = {
            "id": list(range(1, cantidad + 1)),
            "nombre": nombres_aleatorios,
            "puesto_id": [random.choice(puestos_df["id"]) for _ in range(cantidad)],
            "habilidades": [random.sample(habilidades, random.randint(1, len(habilidades))) for _ in range(cantidad)]
        }
        return pd.DataFrame(empleados_data)

    @staticmethod
    def exportar_csv(departamentos_df, puestos_df, empleados_df):
        departamentos_df.to_csv("departamentos.csv", index=False)
        puestos_df.to_csv("puestos_de_trabajo.csv", index=False)
        empleados_df.to_csv("empleados.csv", index=False)

if __name__ == "__main__":
    departamentos_df = GeneradorDatos.generar_departamentos(5)
    puestos_df = GeneradorDatos.generar_puestos_trabajo(5, departamentos_df)
    empleados_df = GeneradorDatos.generar_empleados(100, puestos_df)
    
    GeneradorDatos.exportar_csv(departamentos_df, puestos_df, empleados_df)