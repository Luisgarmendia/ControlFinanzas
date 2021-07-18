#  Clases

## Proyecto contol de gastos 


![Imagen](https://www.horizontum.mx/wp-content/uploads/2018/12/control-de-gastos-empresa.jpg)

### Tablas
1. clientes
   1. idCliente
   2. Nombre
   3. Apellido
2. FuenteDinero
   1. IdFuente
   2. IdCliente
   3. Fecha_regirtro 
   4. fuente
   5. Saldo
3. Ingresos
   1. idFuente
   2. Fecha
   3. Monto
4. Gastos
   1. idFuente
   2. IdTipo
   3. Fecha
   4. Monto
5. TipoGastos
   1. IdTipo
   2. Tipo


<br>
<br>
<br>

## Propuesta de Proyesto 

PRESUPUESTO PERSONAL
- Tipos de gasto (mantenimineto)
- Fuentes de dinero (mantenimiento)
- Registro del gasto (tipo, fuente, la fecha, monto)
    - Actualizacion del saldo
-Registo de ingreso (fuente, fecha, monto)
    - Actualizacion del saldo
-Visualiazcion del saldo actual en todo momento
    - Apliacion de colores adecuados segun el salgo
Reporte de gastos e ingresos mensuales y anual
    - Detallado en forma tabular
    - En grafica de pastel
-Despliegue de entradas y salidas del mes actual
    -Opcion para ver meses **anteriores**