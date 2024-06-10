1




# Custom version
# mohist / catserver   Install forge   first
# purpur               Install fabric  first
# snapshot             Install vanilla first

# Ngrok region
# Code           Place
#-----------     ---------------------------
# ap	          Asia/Pacific (Singapore)
# au		  Australia (Sydney)
# eu		  Europe (Frankfurt)
# in		  India (Mumbai)
# jp		  Japan (Tokyo)
# sa		  South America (São Paulo)
# us		  United States (Ohio)
# us-cal-1	  United States (California)















import requests, os, base64

# Decodificar y escribir el archivo .gitignore
if not os.path.exists("./.gitignore"):
    print("Creating .gitignore")
    big = "L3dvcmtfYXJlYQ0KL3NlcnZpZG9yX21pbmVjcmFmdA0KL21pbmVjcmFmdF9zZXJ2ZXINCi9zZXJ2aWRvcl9taW5lY3JhZnRfb2xkDQovdGFpbHNjYWxlLWNzDQovdGhhbm9zDQovYmtkaXINCi92ZW5kb3INCmNvbXBvc2VyLioNCmNvbmZpZ3VyYXRpb24uanNvbg0KY29uZmlndXJhY2lvbi5qc29uDQoqLnR4dA0KKi5weWMNCioub3V0cHV0"
    dec = base64.standard_b64decode(big).decode()
    with open(".gitignore", 'w') as giti:
        giti.write(dec)

# Función para descargar la última versión de un archivo
def download_latest_release(download_path='.'):
    print("Downloading the latest release")
    mirror = "https://elyxdev.github.io/latest"
    pet = requests.get(mirror)
    if pet.status_code == 200:
        data = pet.json()
        url = data.get('url')
        version = url.split("/")[-1]
        pathto = os.path.join(download_path, version)
        with open(pathto, 'wb') as archivo:
            archivo.write(requests.get(url).content)
        return version
    else:
        print("Failed to download the latest release")
        return None

# Descargar y ejecutar el archivo descargado
flnm = download_latest_release()
if flnm:
    print(f"Downloaded file: {flnm}")
    if flnm.split(".")[-1] == "pyc":
        print(f"Executing {flnm} with python3")
        os.system(f"python3 {flnm}")
    else:
        print(f"Making {flnm} executable and running it")
        os.system(f"chmod +x {flnm} && ./{flnm}")

    # Verificar si el archivo run.bat existe
    if os.path.exists("run.bat"):
        print("Found run.bat, executing it")
        os.system("run.bat")
    else:
        print("run.bat not found")
else:
    print("No file downloaded")
