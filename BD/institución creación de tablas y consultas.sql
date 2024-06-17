#CAMBIOS EN LA TABLA LOCALIDAD#
insert into `mydb`.`localidad` (Codigo_Postal,Nombre) values (5010,"Cordoba")
insert into `mydb`.`localidad` (Codigo_Postal,Nombre) values (5013,"Villa allende")
insert into `mydb`.`localidad` (Codigo_Postal,Nombre) values (2000,"Rosario") 

#CAMBIOS EN LA TABLA ASIGNATURA
insert into `mydb`.`asignatura` (id_Asignatura,Nombre,"Carga horaria",Profesor_id_Profesor,Profesor_Persona_DNI) values (100,"Matematica",4,10,11111111
insert into `mydb`.`asignatura` (id_Asignatura,Nombre,"Carga horaria",Profesor_id_Profesor,Profesor_Persona_DNI) values (200,"Programacion",6,20,22222222)

# CAMBIOS EN LA TABLA PERSONA
INSERT INTO `mydb`.`persona` (DNI,Nombre,Apellido,Teléfono,"Localidad Código _Postal") values (11111111,"profe dos","profesor",3512222222,5013)
INSERT INTO `mydb`.`persona` (DNI,Nombre,Apellido,Teléfono,"Localidad Código _Postal") values (22222222,"profe uno",profesor,3511111111,5013)
INSERT INTO `mydb`.`persona` (DNI,Nombre,Apellido,Teléfono,"Localidad Código _Postal") values (30331023,"Celeste","alumnodos",3519876543,5013)
INSERT INTO `mydb`.`persona` (DNI,Nombre,Apellido,Teléfono,"Localidad Código _Postal") values (35573808,"Yesica Pesqueira",Pesqueira,3518669970,5010
)
INSERT INTO `mydb`.`persona` (DNI,Nombre,Apellido,Teléfono,"Localidad Código _Postal") values (41756661,Lourdes,alumnouno,3511234567,2000
)

#CAMBIOS EN LA TABLA ALUMNO
INSERT INTO `mydb`.`alumno` (nro_legajo,E-mail,Edad,Persona_DNI,Localidad_Código Postal) VALUES (135573808,yesica.pesqueira@gmail.com,33,35573808,5010)
INSERT INTO `mydb`.`alumno` (nro_legajo,E-mail,Edad,Persona_DNI,Localidad_Código Postal) VALUES (241756661,lourdesferreyrafarias@gmail.com,25,41756661,2000)
INSERT INTO `mydb`.`alumno` (nro_legajo,E-mail,Edad,Persona_DNI,Localidad_Código Postal) VALUES (330331023,celemontivero2@gmail.com,34,30331023,5013)

#CAMBIOS EN LA TABLA ALUMNO_ASIGNATURA#
INSERT INTO `mydb`.`alumno_asignatura` (`Alumno_nro_legajo`, `Alumno_Persona_DNI`, `Asignatura_id_Asignatura`, `Horario`, `Nota`) VALUES ('241756661', '41756661', '200', '9', '7');
INSERT INTO `mydb`.`alumno_asignatura` (`Alumno_nro_legajo`, `Alumno_Persona_DNI`, `Asignatura_id_Asignatura`, `Horario`, `Nota`) VALUES ('330331023', '30331023', '100', '10', '8');
UPDATE `mydb`.`alumno_asignatura` SET `Nota` = '6' WHERE (`Alumno_nro_legajo` = '135573808') and (`Alumno_Persona_DNI` = '35573808') and (`Asignatura_id_Asignatura` = '100');

#consultas usasndo where y between#
SELECT * FROM alumno where Edad between 30 and 35

#consulta usando where y limit# 
SELECT * FROM alumno where Edad > 23 LIMIT 25

#Consulta de más de una tabla con INNER JOIN
select alumno.nro_legajo from alumno 
inner join alumno_asignatura 
on alumno.nro_legajo = alumno_asignatura.Alumno_nro_legajo

#Consulta de más de una tabla con inner join y filtros#
select alumno.nro_legajo from alumno 
inner join alumno_asignatura 
on alumno.nro_legajo = alumno_asignatura.Alumno_nro_legajo
where alumno_asignatura.Nota > 7