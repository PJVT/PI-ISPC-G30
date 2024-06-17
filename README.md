# PI-ISPC-G30 - SISTEMA DE GESTIÓN ESCOLAR SIMPLE (SGES)
Proyecto integrador ISPC 2024 - Grupo G30.

Maria Celeste Montivero,	
celemontivero2@gmail.com |
https://github.com/MaCelMon	
30.331.023

Pablo Javier Vaz Torres,	
p.j.vaztorres@gmail.com	|
https://github.com/PJVT	| 1a evidencia, 3a evidencia

Juan Villarreal,	
vin197172@gmail.com	|
https://github.com/Jmv315 | 1a evidencia, 2a evidencia

Lourdes Ferreyra Farias, 41756661,
lourdesferreyrafarias@gmail.com	|
https://github.com/Lourdes00

Yesica Pesqueira, 35573808
Yesica.Pesqueira@gmail.com |
https://github.com/yesicapesqueira20

Análisis y Descripción de la Propuesta de Proyecto:

**Texto final para evidencia 3 y Proyecto final**

A través de Sistema de Gestión Escolar Simple (SGES), un sitio web para escritorio, los usuarios de instituciones educativas podrán operar con más objetividad y dinamismo, en lo concerniente a registro de datos personales y académicos de docentes y estudiantes. En algunos menúes, los usuarios alumnos no tendrán permiso de edición (por ejemplo, en “Alumno_Asignatura”), mientras que, en otros, sí (por ejemplo, en “Localidad”, referido al docente, o “Alumno”). Lo mismo sucederá a los usuarios docentes, quienes no tendrán permiso de edición en algunos menúes (por ejemplo, “Alumno” o “Localidad”, referido al estudiante), pero en otros, sí (por ejemplo, en menú “Alumno_Asignatura”).

Para poder construir SGES, creamos el repositorio que están visualizando en este momento, en el cual hallaremos carpetas, responsables de reflejar el trabajo procesual y colaborativo.

En la carpeta “Aplicación”, encontraremos ocho (8) archivos, que detallamos seguidamente. De la segunda evidencia, data el archivo primigenio de este proyecto, “Pseudo codigo”. Archivos representantes de la tercera evidencia 3, son: “python_menú_Alumno_Asignatura”, “python_menú_Asignatura.py”, “python_menú_Localidad.py”, “python_menú_Persona.py”, “python_menú_Profesor.py” y “python_menú_alumno.py”. Respecto de la entrega final, el archivo representativo es “conexion_pythonmysql.py”, cuyo nombre anticipa el conectar Python con MySQL.

En la carpeta “Base de Datos”, hemos organizado archivos presentados en la segunda evidencia, en el recuperatorio de la segunda evidencia, en la tercera evidencia y en la entrega final. De la segunda evidencia, data el archivo “Diagrama-ER-NotacionChen.png”, el cual necesitó ajustes para el recuperatorio, que se vislumbraron en los siguientes archivos: “DiagramaER(Chen).svg”. En la evidencia 3, presentamos a SGES a través de “Institucion.sql”, la base de datos que dio origen al diagrama de Crow´s foot [Institucion(Crowsfoot).png], donde se detallan las claves primarias y foráneas. En lo pertinente a la entrega final, hallarán el PDF resumen y “de alto impacto” del repositorio, a través del archivo “Base de datos del proyecto, sus diagramas y SQL.pdf”, como también “institución creación de tablas y consultas.sql”, actividades solicitadas para la puesta en práctica de lo aprendido, para el proyecto final.

Cabe destacar también la carpeta SQL

Antes de concluir esta descripción, no queremos dejar de destacar que en el apartado WIKI, hallarán todo lo concerniente a legislación provincial, nacional e internacional que regula el trabajo de programadores y desarrolladores, a través de situaciones hipotéticas y sus posibles soluciones con leyes, convenios y acuerdos pertinentes.

**Recuperatorio de evidencia 2**

Se tratará de una app que podrán emplear tanto los docentes como los estudiantes, de instituciones educativas formales, sin interferir en los perfiles de uno y otro. Como es necesario en todo instituto de educación formal, tendrán campos donde procederán de forma pasiva o activa. Por ejemplo, los docentes tendrán actuación sostenida en las entidades "Profesor", "Asignatura" y "Alumno_Asignatura"; mientras que el estudiante tendrá actuación sostenida en las entidades "Alumno", "Persona" (alumno) y "Localidad" (alumno). El Docente actuará pasivamente sobre "Localidad" (alumno), "Alumno" (alumno) y "Persona" (alumno). Por su parte, el Estudiante actuará pasivamente sobre "Localidad" (profesor), "Profesor" (profesor), "Persona" (profesor) y "Alumno_Asignatura".

**Texto Evidencia 2**

Desarrollar una app básica y simple para una institución educativa, en donde cada alumno puede gestionar su cuenta académica (inscribirse a distintas materias y ver sus notas, evolución, interactuar con docentes y compañeros, etc). 
