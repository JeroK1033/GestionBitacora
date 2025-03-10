# GestionBitacora

Este repositorio contiene la implementación y pruebas para el sistema de gestión de bitácora. La aplicación permite a los supervisores de obra registrar, consultar y gestionar la bitácora diaria de una construcción, garantizando la trazabilidad de las actividades realizadas en la obra.



## Funcionalidad 1: Registrar una actividad

Permite a los supervisores registrar una actividad en un día y una hora específica.

### Casos de Prueba

Caso de Prueba #1: Caso Normal - Registro de Actividad

| ID Actividad |    Fecha/Hora    | Supervisor |        Descripcion       | Condiciones Climaticas |      Anexos      |
|--------------|------------------|------------|--------------------------|------------------------|------------------|
|    232245    | 08/03/2025 15:36 | Supervisor | Inicio de Nuevo Proyecto |   Nublado y Lluvioso   | InfoProyecto.pdf | 

|                  Supervisor                  |
|   Nombre   |       Correo       | Contraseña | 
|------------|--------------------|------------| 
| Juan Perez | juanp225@gmail.com | JuanPz4875 |


Caso de Prueba #2: Caso Normal - Registro de Actividad con Fecha y Hora

| ID Actividad |    Fecha/Hora    |  Supervisor  |        Descripcion       | Condiciones Climaticas |           Anexos          |
|--------------|------------------|--------------|--------------------------|------------------------|---------------------------|
|    498521    | 16/11/2024 22:45 | Lucas Correa |   Revision de Proyecto   |         Soleado        | ProyectoReorganizado.docx | 


Caso de Prueba #3: Caso Normal - Registro de Actividad con un Anexo Incluido

| ID Actividad |    Fecha/Hora    |   Supervisor    |            Descripcion            | Condiciones Climaticas |        Anexos       |
|--------------|------------------|-----------------|-----------------------------------|------------------------|---------------------|
|    984216    | 01/08/2025 08:27 | Maria Hernandez | Evidencias y Avances Metro Bogota |        Neblina         | EvidenciasMetro.pdf | 


Caso de Prueba #4: Caso Extremo - Registro de Actividad en el limite del dia

| ID Actividad |    Fecha/Hora    |   Supervisor    |                Descripcion                | Condiciones Climaticas  |             Anexos            |
|--------------|------------------|-----------------|-------------------------------------------|-------------------------|-------------------------------|
|    284719    | 03/11/2025 19:40 |  Mateo Herrera  | Detalles técnicos y normativas del diseño |        Tormenta         | Especificaciones_Tecnicas.pdf | 


Caso de Prueba #5: Caso Extremo - Registro de Actividad con multiples anexos

| ID Actividad |    Fecha/Hora    |    Supervisor    |                    Descripcion                    | Condiciones Climaticas |           Anexos           |
|--------------|------------------|------------------|---------------------------------------------------|------------------------|----------------------------|
|    630582    | 18/06/2024 14:20 | Camila Rodríguez | Diapositivas con información general del proyecto |        Soleado         | Presentacion_Proyecto.pptx | 


Caso de Prueba #6: Caso Extremo - Registro de Actividad con descripcion larga

| ID Actividad |    Fecha/Hora    |     Supervisor      |                   Descripcion                   | Condiciones Climaticas |       Anexos       |
|--------------|------------------|---------------------|-------------------------------------------------|------------------------|--------------------|
|    157943    | 25/12/2023 08:55 | Alejandro Fernández | Imagen digital del diseño exterior del proyecto |        Soleado         | Render_Fachada.png | 


Caso de Prueba #7: Caso de Error - Registro de Actividad sin descripcion

| ID Actividad |    Fecha/Hora    |    Supervisor    | Descripcion | Condiciones Climaticas |         Anexos        |
|--------------|------------------|------------------|-------------|------------------------|-----------------------|
|    902356    | 07/07/2025 22:30 | Santiago Ramírez |    None     |           NN           | Presupuesto_Obra.xlsx | 


Caso de Prueba #8: Caso de Error - Registro de Actividad con Fecha y Hora Invalida

| ID Actividad |      Fecha/Hora       |   Supervisor    |                      Descripcion                     | Condiciones Climaticas |           Anexos         |
|--------------|-----------------------|-----------------|------------------------------------------------------|------------------------|--------------------------|
|    418275    | 30 de Octubre de 2025 | Valentina Gómez | La cubierta del edificio ha sido instalada con éxito |        LLuvioso        | Planos_Estructurales.pdf | 


Caso de Prueba #9: Caso de Error - Registro de Actividad sin Anexos

| ID Actividad |    Fecha/Hora    |    Supervisor    |                                 Descripcion                                | Condiciones Climaticas | Anexos |
|--------------|------------------|------------------|----------------------------------------------------------------------------|------------------------|--------|
|    765901    | 14/02/2023 16:45 | Camila Rodríguez | Las paredes del proyecto han sido construidas y están listas para acabados |        Nublado         |  None  | 





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

