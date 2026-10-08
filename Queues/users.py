from datetime import datetime


usuarios = []


def pedir_dato(mensaje):
	dato = input(mensaje).strip()
	while not dato:
		print("Este dato es obligatorio.")
		dato = input(mensaje).strip()
	return dato


def registrar_usuario():
	identificacion = pedir_dato("Identificacion: ")
	while any(usuario["identificacion"] == identificacion for usuario in usuarios):
		print("Esa identificacion ya esta registrada.")
		identificacion = pedir_dato("Identificacion: ")

	usuario = {
		"identificacion": identificacion,
		"primer_nombre": pedir_dato("Primer nombre: "),
		"primer_apellido": pedir_dato("Primer apellido: "),
		"telefono": pedir_dato("Telefono: "),
		"correo_electronico": pedir_dato("Correo electronico: "),
		"genero": pedir_dato("Genero: "),
		"fecha_creacion": datetime.now().isoformat(timespec="seconds"),
		"status": "activo",
	}
	usuarios.append(usuario)
	return usuario


def cambiar_status(identificacion, status):
	if status not in ("activo", "inactivo"):
		raise ValueError("El status debe ser 'activo' o 'inactivo'.")

	for usuario in usuarios:
		if usuario["identificacion"] == identificacion:
			usuario["status"] = status
			return True
	return False


def mostrar_usuarios():
	if not usuarios:
		print("No hay usuarios registrados.")
		return

	for usuario in usuarios:
		print(" | ".join(str(valor) for valor in usuario.values()))


def main():
	while True:
		print("\n--- Registro de usuarios ---")
		print("1. Registrar usuario")
		print("2. Activar usuario")
		print("3. Desactivar usuario")
		print("4. Mostrar usuarios")
		print("5. Salir")
		opcion = input("Selecciona una opcion: ").strip()

		if opcion == "1":
			usuario = registrar_usuario()
			print(f"Usuario {usuario['identificacion']} registrado.")
		elif opcion in ("2", "3"):
			identificacion = pedir_dato("Identificacion del usuario: ")
			status = "activo" if opcion == "2" else "inactivo"
			if cambiar_status(identificacion, status):
				print(f"Usuario {identificacion} ahora esta {status}.")
			else:
				print("No se encontro esa identificacion.")
		elif opcion == "4":
			mostrar_usuarios()
		elif opcion == "5":
			break
		else:
			print("Opcion no valida.")


if __name__ == "__main__":
	main()
