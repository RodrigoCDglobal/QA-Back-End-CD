import subprocess
import argparse

class CustomHelpFormatter(argparse.HelpFormatter):
    def add_arguments(self, actions):
        actions = [action for action in actions if not action.option_strings]
        super().add_arguments(actions)

def obtener_ruta_ambiente(ambiente):
    ambiente_path_dict = {
        'prod': 'environment/prod_environment.json',
        'test': 'environment/test_environment',
        'lookup': 'environment/lookup_environment'
    }
    return ambiente_path_dict.get(ambiente, None)

def ejecutar_newman(coleccion_path, folder_name, environment_path=None, export_environment=True, report_path="report.html", iterations=1, delay_request=0, export_cookie_jar=None, import_cookie_jar=None, working_dir=None):
    newman_path = r"C:\Users\anton\AppData\Roaming\npm\newman.cmd"
    comando = [newman_path, "run", coleccion_path, "--verbose"]

    if folder_name:
        comando.extend(["--folder", folder_name])
    if environment_path:
        comando.extend(["-e", environment_path])
        if export_environment:
            comando.extend(["--export-environment", environment_path])
    comando.extend(["--reporters", "cli,htmlextra", "--reporter-htmlextra-export", report_path])
    if iterations > 1:
        comando.extend(["--iteration-count", str(iterations)])
    if delay_request > 0:
        comando.extend(["--delay-request", str(delay_request)])
    
    if working_dir:
        comando.extend(["--working-dir", working_dir])

    if export_cookie_jar:
        comando.extend(["--export-cookie-jar", export_cookie_jar])

    if import_cookie_jar:
        comando.extend(["--cookie-jar", import_cookie_jar])

    print("Comando ejecutado:", ' '.join(comando))  # Para depuración
    resultado = subprocess.run(comando, capture_output=True, text=True, encoding='utf-8', errors='ignore')

    print("Salida de Newman:")
    print(resultado.stdout)  # Imprimir toda la salida para depuración
    print("Errores (si existen):")
    print(resultado.stderr)  # Imprimir errores para depuración

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutar Newman con diferentes entornos e instancias.", formatter_class=CustomHelpFormatter)
    parser.add_argument("ambiente", choices=["lookup", "prod", "test"], help="El ambiente con el que se desea trabajar.")
    parser.add_argument("instancia", help="La instancia con la que se desea trabajar (e.g., i0000, i0001).")
    parser.add_argument("--iterations", type=int, default=1, help="Número de iteraciones para las pruebas de rendimiento.")
    parser.add_argument("--delay-request", type=int, default=0, help="Tiempo de espera entre cada solicitud en milisegundos.")
    args = parser.parse_args()
    ambiente_path = obtener_ruta_ambiente(args.ambiente)
    folder_name = f"Login a cuenta de coleccion {args.instancia}"

    login_coleccion_path = 'collection/login_collection.json'
    ejecutar_newman(login_coleccion_path, folder_name, ambiente_path, report_path="reportes/login_report.html", iterations=args.iterations, delay_request=args.delay_request, export_cookie_jar="login_cookies.json")

    carga_archivos_muestra_collection_path = 'collection/carga_archivos_muestra_collection.json'
    ejecutar_newman(carga_archivos_muestra_collection_path, None, ambiente_path, report_path="reportes/carga_archivos_muestra_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json", working_dir="files/")

    amx_activity_collection_path = 'collection/amx_activity_collection.json'
    ejecutar_newman(amx_activity_collection_path, None, ambiente_path, report_path="reportes/amx_activity_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json")

    amx_branding_avatar_collection_path = 'collection/amx_branding_avatar_collection.json'
    ejecutar_newman(amx_branding_avatar_collection_path, None, ambiente_path, report_path="reportes/amx_branding_avatar_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json", working_dir="files/")

    amx_family_plan_collection_path = 'collection/amx_family_plan_collection.json'
    ejecutar_newman(amx_family_plan_collection_path, None, ambiente_path, report_path="reportes/amx_family_plan_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json")

    amx_files_collection_path = 'collection/amx_files_collection.json'
    ejecutar_newman(amx_files_collection_path, None, ambiente_path, report_path="reportes/amx_files_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json")

    amx_filesharing_collection_path = 'collection/amx_filesharing_collection.json'
    ejecutar_newman(amx_filesharing_collection_path, None, ambiente_path, report_path="reportes/amx_filesharing_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json")

    amx_gallery_collection_path = 'collection/amx_gallery_collection.json'
    ejecutar_newman(amx_gallery_collection_path, None, ambiente_path, report_path="reportes/amx_gallery_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json")

    amx_metadata_integration_collection_path = 'collection/amx_metadata_integration_collection.json'
    ejecutar_newman(amx_metadata_integration_collection_path, None, ambiente_path, report_path="reportes/amx_metadata_integration_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json")

    amx_payment_collection_path = 'collection/amx_payment_collection.json'
    ejecutar_newman(amx_payment_collection_path, None, ambiente_path, report_path="reportes/amx_payment_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json")

    dav_amx_branding_trashbin_collection_path = 'collection/dav_amx_branding_trashbin_collection.json'
    ejecutar_newman(dav_amx_branding_trashbin_collection_path, None, ambiente_path, report_path="reportes/dav_amx_branding_trashbin_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json")

    amx_ping_middleware_collection_path = 'collection/amx_ping_middleware_collection.json'
    ejecutar_newman(amx_ping_middleware_collection_path, None, ambiente_path, report_path="reportes/amx_ping_middleware_report.html", iterations=args.iterations, delay_request=args.delay_request, import_cookie_jar="login_cookies.json")
