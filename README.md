# GestionBitacora

Este repositorio contiene la implementación y pruebas para el sistema de gestión de bitácora. La aplicación permite a los supervisores de obra registrar, consultar y gestionar la bitácora diaria de una construcción, garantizando la trazabilidad de las actividades realizadas en la obra.



## Funcionalidad 1: Registrar una actividad

Permite a los supervisores registrar una actividad en un día y una hora específica.


### Caso de Prueba #1: Caso Normal - Registro de Actividad

| ID Actividad |    Fecha/Hora    | Supervisor |        Descripcion       | Condiciones Climaticas |      Anexos      |
|--------------|------------------|------------|--------------------------|------------------------|------------------|
|    232245    | 08/03/2025 15:36 | Supervisor | Inicio de Nuevo Proyecto |   Nublado y Lluvioso   | InfoProyecto.pdf | 

|                  Supervisor                  |
|   Nombre   |       Correo       | Contraseña | 
|------------|--------------------|------------| 
| Juan Perez | juanp225@gmail.com | JuanPz4875 |


### Caso de Prueba #2: Caso Normal - Registro de Actividad con Fecha y Hora

| ID Actividad |    Fecha/Hora    | Supervisor |        Descripcion       | Condiciones Climaticas |           Anexos          |
|--------------|------------------|------------|--------------------------|------------------------|---------------------------|
|    498521    | 16/11/2024 22:45 | Supervisor |   Revision de Proyecto   |         Soleado        | ProyectoReorganizado.docx | 

|                    Supervisor                   |
|    Nombre    |       Correo        | Contraseña | 
|--------------|---------------------|------------| 
| Lucas Correa | lucasc998@gmail.com | LucasC2024 |

### Caso de Prueba #3: Caso Normal - Registro de Actividad con un Anexo Incluido

| ID Actividad |    Fecha/Hora    | Supervisor |            Descripcion            | Condiciones Climaticas |        Anexos       |
|--------------|------------------|------------|-----------------------------------|------------------------|---------------------|
|    984216    | 01/08/2025 08:27 | Supervisor | Evidencias y Avances Metro Bogota |        Neblina         | EvidenciasMetro.pdf | 

|                       Supervisor                     |
|      Nombre     |        Correo         | Contraseña | 
|-----------------|-----------------------|------------| 
| Maria Hernandez | maria_hdz87@gmail.com | MariaH3056 |


### Caso de Prueba #4: Caso Extremo - Registro de Actividad en el limite del dia

| ID Actividad |    Fecha/Hora    | Supervisor |                Descripcion                | Condiciones Climaticas  |             Anexos            |
|--------------|------------------|------------|-------------------------------------------|-------------------------|-------------------------------|
|    284719    | 03/11/2025 19:40 | Supervisor | Detalles técnicos y normativas del diseño |        Tormenta         | Especificaciones_Tecnicas.pdf | 

|                    Supervisor                   |
|    Nombre    |       Correo        | Contraseña | 
|--------------|---------------------|------------| 
| Mateo Herrera | mateoh993@gmail.com | MateoH7621 |


### Caso de Prueba #5: Caso Extremo - Registro de Actividad con multiples anexos

| ID Actividad |    Fecha/Hora    | Supervisor |                    Descripcion                    | Condiciones Climaticas |           Anexos           |
|--------------|------------------|------------|---------------------------------------------------|------------------------|----------------------------|
|    630582    | 18/06/2024 14:20 | Supervisor | Diapositivas con información general del proyecto |        Soleado         | Presentacion_Proyecto.pptx | 

|                    Supervisor                          |
|      Nombre      |        Correo         | Contraseña  | 
|------------------|-----------------------|-------------| 
| Camila Rodriguez | camila.rodr@gmail.com | CamilaR4823 |


### Caso de Prueba #6: Caso Extremo - Registro de Actividad con descripcion larga

| ID Actividad |    Fecha/Hora    | Supervisor |                   Descripcion                   | Condiciones Climaticas |       Anexos       |
|--------------|------------------|------------|-------------------------------------------------|------------------------|--------------------|
|    157943    | 25/12/2023 08:55 | Supervisor | Imagen digital del diseño exterior del proyecto |        Soleado         | Render_Fachada.png | 

|                        Supervisor                          |
|        Nombre       |         Correo          | Contraseña | 
|---------------------|-------------------------|------------| 
| Alejandro Fernandez | alejandrofz23@gmail.com | AlexF9052  |


### Caso de Prueba #7: Caso de Error - Registro de Actividad sin descripcion

| ID Actividad |    Fecha/Hora    | Supervisor | Descripcion | Condiciones Climaticas |         Anexos        |
|--------------|------------------|------------|-------------|------------------------|-----------------------|
|    902356    | 07/07/2025 22:30 | Supervisor |    None     |       No Aplica        | Presupuesto_Obra.xlsx | 

|                    Supervisor                   |
|    Nombre    |       Correo        | Contraseña | 
|--------------|---------------------|------------| 
| Lucas Correa | santi_rz99@gmail.com | SantiR6638 |


### Caso de Prueba #8: Caso de Error - Registro de Actividad con Fecha y Hora Invalida

| ID Actividad |      Fecha/Hora       | Supervisor |                      Descripcion                     | Condiciones Climaticas |           Anexos         |
|--------------|-----------------------|------------|------------------------------------------------------|------------------------|--------------------------|
|    418275    | 30 de Octubre de 2025 | Supervisor | La cubierta del edificio ha sido instalada con éxito |        LLuvioso        | Planos_Estructurales.pdf | 

|                        Supervisor                       |
|     Nombre      |          Correo          | Contraseña | 
|-----------------|--------------------------|------------| 
| Valentina Gomez | valentina.gm12@gmail.com | ValenG3721 |


### Caso de Prueba #9: Caso de Error - Registro de Actividad sin Anexos

| ID Actividad |    Fecha/Hora    | Supervisor |                                 Descripcion                                | Condiciones Climaticas | Anexos |
|--------------|------------------|------------|----------------------------------------------------------------------------|------------------------|--------|
|    765901    | 14/02/2023 16:45 | Supervisor | Las paredes del proyecto han sido construidas y están listas para acabados |        Nublado         |  None  | 

|                    Supervisor                          |
|    Nombre        |       Correo          | Contraseña  | 
|------------------|-----------------------|-------------| 
| Camila Rodriguez | camila.rodr@gmail.com | CamilaR4823 |




## Funcionalidad 2: Consultar actividades

Permite consultar actividades en un rango de fechas determinado.

### Caso de Prueba #1: Caso Normal - Consulta de actividades en un rango válido.

| Fecha Incio |  Fecha Fin | Supervisor | 
|-------------|------------|------------| 
| 01/06/2024  | 10/06/2024 | Juan Perez |

|   Resultado  |  
|--------------|
| 3 Actividades|




### Caso de Prueba #2: Caso Normal - Consulta de actividades con fecha específica.

| Fecha Consulta | Supervisor | 
|----------------|------------| 
|   01/06/2024   | Juan Perez |


### Caso de Prueba #3: Caso Normal - Consulta de actividades con múltiples filtros.

### Caso de Prueba #4: Caso Extremo - Consulta de actividades en un rango de fechas de varios años.

### Caso de Prueba #5: Caso Extremo - Consulta con múltiples filtros aplicados.

### Caso de Prueba #6: Caso Extremo - 

### Caso de Prueba #7: Caso de Error - Consulta sin definir fechas.

### Caso de Prueba #8: Caso de Error - Consulta con fecha de inicio mayor que la fecha de fin.

### Caso de Prueba #9: Caso de Error - Intento de consulta sin autenticación.



## Funcionalidad 3: Generar reporte de la bitácora

Genera un informe en PDF sobre actividades en un rango de fechas.

### Caso de Prueba #1: Caso Normal - Generación de reporte con datos completos.

### Caso de Prueba #2: Caso Normal - Generación de reporte sin actividades en el rango de fechas.

### Caso de Prueba #3: Caso Normal - Generación de reporte con anexos.

### Caso de Prueba #4: Caso Extremo - Generación de un reporte con miles de actividades.

### Caso de Prueba #5: Caso Extremo - Generación de reporte en el formato más grande permitido.

### Caso de Prueba #6: Caso Extremo - Generación de reporte con filtros avanzados.

### Caso de Prueba #7: Caso de Error - Intento de generar un reporte sin definir fechas.

### Caso de Prueba #8: Caso de Error - Intento de generar un reporte con fechas inválidas.

### Caso de Prueba #9: Caso de Error - Intento de generar un reporte sin autenticación.



## Funcionalidad 4: Crear cuenta

Permite a los supervisores registrarse en el sistema.

### Caso de Prueba #1: Caso Normal - Registro exitoso con datos válidos.

### Caso de Prueba #2: Caso Normal - Registro con correo válido y contraseña fuerte.

### Caso de Prueba #3: Caso Normal - Registro con nombre y apellido válidos.

### Caso de Prueba #4: Caso Extremo - Registro con la contraseña más larga permitida.

### Caso de Prueba #5: Caso Extremo - Registro con caracteres especiales en el nombre.

### Caso de Prueba #6: Caso Extremo - Registro con un email en el límite de longitud permitida.

### Caso de Prueba #7: Caso de Error - Registro sin correo electrónico.

### Caso de Prueba #8: Caso de Error - Registro con una contraseña muy corta.

### Caso de Prueba #9: Caso de Error - Registro con un email ya registrado.



## Funcionalidad 5: Iniciar sesión

Facilita el acceso de los supervisores al sistema.

### Caso de Prueba #1: Caso Normal - Inicio de sesión exitoso.

### Caso de Prueba #2: Caso Normal - Inicio de sesión con recordar sesión activado.

### Caso de Prueba #3: Caso Normal - Inicio de sesión con múltiples intentos.

### Caso de Prueba #4: Caso Extremo - Inicio de sesión con una contraseña en el límite de longitud.

### Caso de Prueba #5: Caso Extremo - Inicio de sesión con una contraseña que contiene solo letras minúsculas.

### Caso de Prueba #6: Caso Extremo - Inicio de sesión con una contraseña que contiene solo números.

### Caso de Prueba #7: Caso de Error - Inicio de sesión con contraseña incorrecta.

### Caso de Prueba #8: Caso de Error - Inicio de sesión con email no registrado.

### Caso de Prueba #9: Caso de Error - Inicio de sesión con un email en formato inválido.



## Funcionalidad 6: Cambiar contraseña

Permite a los supervisores modificar su contraseña.

### Caso de Prueba #1: Caso Normal - Cambio de contraseña exitoso con credenciales correctas.

### Caso de Prueba #2: Caso Normal - Cambio de contraseña con una clave fuerte.

### Caso de Prueba #3: Caso Normal - Caso Normal - Cambio de contraseña seguido de un inicio de sesión exitoso con la nueva clave.

### Caso de Prueba #4: Caso Extremo - Cambio de contraseña con la más larga permitida.

### Caso de Prueba #5: Caso Extremo - Cambio de contraseña utilizando exclusivamente caracteres especiales.

### Caso de Prueba #6: Caso Extremo - Cambio de contraseña con caracteres especiales y números.

### Caso de Prueba #7: Caso de Error - Intento de cambio de contraseña con la clave anterior incorrecta.

### Caso de Prueba #8: Caso de Error - Intento de cambio de contraseña con claves no coincidentes.

### Caso de Prueba #9: Caso de Error - Intento de cambio de contraseña sin estar autenticado.

