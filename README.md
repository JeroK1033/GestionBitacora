# GestionBitacora

Este repositorio contiene la implementación y pruebas para el sistema de gestión de bitácora. La aplicación permite a los supervisores de obra registrar, consultar y gestionar la bitácora diaria de una construcción, garantizando la trazabilidad de las actividades realizadas en la obra.



## Funcionalidad 1: Registrar una actividad

Permite a los supervisores registrar una actividad en un día y una hora específica.

### Casos de Prueba

#### Caso de Prueba #1: Caso Normal - Registro de Actividad

| ID Actividad |    Fecha/Hora    | Supervisor |        Descripcion       | Condiciones Climaticas |      Anexos      |
|--------------|------------------|------------|--------------------------|------------------------|------------------|
|    232245    | 08/03/2025 15:36 | Supervisor | Inicio de Nuevo Proyecto |   Nublado y Lluvioso   | InfoProyecto.pdf | 

|                  Supervisor                  |
|   Nombre   |       Correo       | Contraseña | 
|------------|--------------------|------------| 
| Juan Perez | juanp225@gmail.com | JuanPz4875 |


#### Caso de Prueba #2: Caso Normal - Registro de Actividad con Fecha y Hora

| ID Actividad |    Fecha/Hora    | Supervisor |        Descripcion       | Condiciones Climaticas |           Anexos          |
|--------------|------------------|------------|--------------------------|------------------------|---------------------------|
|    498521    | 16/11/2024 22:45 | Supervisor |   Revision de Proyecto   |         Soleado        | ProyectoReorganizado.docx | 

|                    Supervisor                   |
|    Nombre    |       Correo        | Contraseña | 
|--------------|---------------------|------------| 
| Lucas Correa | lucasc998@gmail.com | LucasC2024 |

#### Caso de Prueba #3: Caso Normal - Registro de Actividad con un Anexo Incluido

| ID Actividad |    Fecha/Hora    | Supervisor |            Descripcion            | Condiciones Climaticas |        Anexos       |
|--------------|------------------|------------|-----------------------------------|------------------------|---------------------|
|    984216    | 01/08/2025 08:27 | Supervisor | Evidencias y Avances Metro Bogota |        Neblina         | EvidenciasMetro.pdf | 

|                       Supervisor                     |
|      Nombre     |        Correo         | Contraseña | 
|-----------------|-----------------------|------------| 
| Maria Hernandez | maria_hdz87@gmail.com | MariaH3056 |


#### Caso de Prueba #4: Caso Extremo - Registro de Actividad en el limite del dia

| ID Actividad |    Fecha/Hora    | Supervisor |                Descripcion                | Condiciones Climaticas  |             Anexos            |
|--------------|------------------|------------|-------------------------------------------|-------------------------|-------------------------------|
|    284719    | 03/11/2025 19:40 | Supervisor | Detalles técnicos y normativas del diseño |        Tormenta         | Especificaciones_Tecnicas.pdf | 

|                    Supervisor                   |
|    Nombre    |       Correo        | Contraseña | 
|--------------|---------------------|------------| 
| Mateo Herrera | mateoh993@gmail.com | MateoH7621 |


#### Caso de Prueba #5: Caso Extremo - Registro de Actividad con multiples anexos

| ID Actividad |    Fecha/Hora    | Supervisor |                    Descripcion                    | Condiciones Climaticas |           Anexos           |
|--------------|------------------|------------|---------------------------------------------------|------------------------|----------------------------|
|    630582    | 18/06/2024 14:20 | Supervisor | Diapositivas con información general del proyecto |        Soleado         | Presentacion_Proyecto.pptx | 

|                    Supervisor                          |
|      Nombre      |        Correo         | Contraseña  | 
|------------------|-----------------------|-------------| 
| Camila Rodriguez | camila.rodr@gmail.com | CamilaR4823 |


#### Caso de Prueba #6: Caso Extremo - Registro de Actividad con descripcion larga

| ID Actividad |    Fecha/Hora    | Supervisor |                   Descripcion                   | Condiciones Climaticas |       Anexos       |
|--------------|------------------|------------|-------------------------------------------------|------------------------|--------------------|
|    157943    | 25/12/2023 08:55 | Supervisor | Imagen digital del diseño exterior del proyecto |        Soleado         | Render_Fachada.png | 

|                        Supervisor                          |
|        Nombre       |         Correo          | Contraseña | 
|---------------------|-------------------------|------------| 
| Alejandro Fernandez | alejandrofz23@gmail.com | AlexF9052  |


#### Caso de Prueba #7: Caso de Error - Registro de Actividad sin descripcion

| ID Actividad |    Fecha/Hora    | Supervisor | Descripcion | Condiciones Climaticas |         Anexos        |
|--------------|------------------|------------|-------------|------------------------|-----------------------|
|    902356    | 07/07/2025 22:30 | Supervisor |    None     |       No Aplica        | Presupuesto_Obra.xlsx | 

|                    Supervisor                   |
|    Nombre    |       Correo        | Contraseña | 
|--------------|---------------------|------------| 
| Lucas Correa | santi_rz99@gmail.com | SantiR6638 |


#### Caso de Prueba #8: Caso de Error - Registro de Actividad con Fecha y Hora Invalida

| ID Actividad |      Fecha/Hora       | Supervisor |                      Descripcion                     | Condiciones Climaticas |           Anexos         |
|--------------|-----------------------|------------|------------------------------------------------------|------------------------|--------------------------|
|    418275    | 30 de Octubre de 2025 | Supervisor | La cubierta del edificio ha sido instalada con éxito |        LLuvioso        | Planos_Estructurales.pdf | 

|                        Supervisor                       |
|     Nombre      |          Correo          | Contraseña | 
|-----------------|--------------------------|------------| 
| Valentina Gomez | valentina.gm12@gmail.com | ValenG3721 |


#### Caso de Prueba #9: Caso de Error - Registro de Actividad sin Anexos

| ID Actividad |    Fecha/Hora    | Supervisor |                                 Descripcion                                | Condiciones Climaticas | Anexos |
|--------------|------------------|------------|----------------------------------------------------------------------------|------------------------|--------|
|    765901    | 14/02/2023 16:45 | Supervisor | Las paredes del proyecto han sido construidas y están listas para acabados |        Nublado         |  None  | 

|                    Supervisor                          |
|    Nombre        |       Correo          | Contraseña  | 
|------------------|-----------------------|-------------| 
| Camila Rodriguez | camila.rodr@gmail.com | CamilaR4823 |




## Funcionalidad 2: Consultar actividades

Permite consultar actividades en un rango de fechas determinado.

### Casos de Prueba



## Funcionalidad 3: Generar reporte de la bitácora

Genera un informe en PDF sobre actividades en un rango de fechas.
### Casos de Prueba

## Funcionalidad 4: Crear cuenta

Permite a los supervisores registrarse en el sistema.
### Casos de Prueba

## Funcionalidad 5: Iniciar sesión

Facilita el acceso de los supervisores al sistema.
### Casos de Prueba

## Funcionalidad 6: Cambiar contraseña

Permite a los supervisores modificar su contraseña.
### Casos de Prueba

