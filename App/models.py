from django.db import models

#Archivo Models utilizado para crear y migrar las clases a la que será la Base de Datos de MySQL
# Create your models here.

class acompanantes(models.Model):
    Id_Acomp =  models.AutoField(primary_key=True)
    Nombre_Acomp = models.CharField(max_length=50, null=False)

class areastrabajo(models.Model):
    Id_Area = models.AutoField(null=False, primary_key=True)
    NombreArea = models.CharField(max_length=35, null=False)

class edocivil(models.Model):
    Id_EdoCivil = models.AutoField(primary_key=True)
    Nombre_EdoCivil = models.CharField(max_length=25, null=False)

class metanticonceptivos(models.Model):
    Id_Metodo = models.AutoField(primary_key=True)
    NombreMetodo = models.CharField(max_length=25, null=False)

class tipoconsultas(models.Model):
  Id_TipoConsulta = models.AutoField(primary_key=True)
  Nombre_TipoConsulta = models.CharField(max_length=50, null=False)

class valoraciontanner(models.Model):
    Id_ValTanner = models.AutoField(primary_key=True)
    Img_ValTanner = models.ImageField(null=True, upload_to='images/EVtanner')
    NombreValTanner = models.CharField(max_length=50, null=False)
    DescripcionValTanner = models.TextField()

class pacientes(models.Model):
    Nombre_Pac = models.CharField(max_length=50, null=False)
    Apellidos_Pac = models.CharField(max_length=50, null=True)
    FechaNac = models.DateField(null=False)
    Peso = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    Talla= models.DecimalField(max_digits=3, decimal_places=2, null=False)
    CURP = models.CharField(max_length=18, primary_key=True)
    Telefono = models.CharField(max_length=10, null=False)
    Sexo = models.CharField(max_length=1,null=False)
    Id_EdoCivil = models.ForeignKey(edocivil, blank=True, null=True, on_delete=models.CASCADE)

class domicilios(models.Model):
    Id_Domicilio = models.AutoField(primary_key=True)
    CURP = models.ForeignKey(pacientes, blank=True, null=True, on_delete=models.CASCADE)
    Calle = models.CharField(max_length=100, null=False)
    NumInt = models.IntegerField(null=False, default=0)
    NumExt = models.IntegerField(null=False, default=0)
    Colonia = models.CharField(max_length=75, null=False)
    CP = models.IntegerField(null=False)
    Municipio = models.CharField(max_length=100, null=False)
    Estado = models.CharField(max_length=50, null=False)

class expedientes(models.Model):
    Id_Exped = models.AutoField(primary_key=True)
    CURP = models.ForeignKey(pacientes, blank=True, null=True, on_delete=models.CASCADE)

# class usuarios(models.Model):
#     Nombre = models.CharField(max_length=50, null=False)
#     Apellidos = models.CharField(max_length=50, null=False)
#     Id_Area = models.ForeignKey(areastrabajo, blank=True, null=True, on_delete=models.CASCADE)
#     Mail = models.CharField(primary_key=True, max_length=50)
#     Telefono = models.CharField(null=False, max_length=10)

class consultagral(models.Model):
    Id_Exped = models.ForeignKey(expedientes, blank=True, null=True, on_delete=models.CASCADE)
    FolioConsulta = models.AutoField(primary_key=True)
    CURP = models.ForeignKey(pacientes, blank=True, null=True, on_delete=models.CASCADE)
#    Mail = models.ForeignKey(usuarios, blank=True, null=True, on_delete=models.CASCADE)
    UserID = models.CharField(max_length=50, null=True)
    FechaConsulta = models.DateTimeField()
    Id_TipoConsulta = models.ForeignKey(tipoconsultas, blank=True, null=True, on_delete=models.CASCADE)
    Id_Acomp = models.ForeignKey(acompanantes, blank=True, null=True, on_delete=models.CASCADE)

class antescolares(models.Model):
    FolioConsulta = models.ForeignKey(consultagral, blank=True, null=True, on_delete=models.CASCADE)
    Grado = models.CharField(max_length=50, null=False)
    Promedio = models.DecimalField(max_digits=3, decimal_places=2, null=False)
    RepitioGrado = models.BooleanField(null=False)
    DesercionEsc = models.BooleanField(null=False)
    Causa_DesercionEsc = models.TextField()
    ConflictProf = models.BooleanField(null=False)
    Causa_ConflictProf = models.TextField()
    RelacionComp = models.CharField(max_length=250, null=False)
    TrabajoAnt = models.BooleanField(null=False)
    Obs_TrabajoAnt = models.TextField()
    TrabajoActual = models.BooleanField(null=False)

class antfamiliares(models.Model):
    FolioConsulta = models.ForeignKey(consultagral, blank=True, null=True, on_delete=models.CASCADE)
    Grado = models.CharField(max_length=50, null=False)
    EdadPadre = models.IntegerField(null=False, default=0)
    EdadMadre = models.IntegerField(null=False, default=0)
    EscPadre = models.CharField(max_length=50, null=False)
    EscMadre = models.CharField(max_length=50, null=False)
    Id_EdoCivil = models.ForeignKey(edocivil, blank=True, null=True, on_delete=models.CASCADE)
    NumHermanos = models.IntegerField(null=False, default=0)
    Lugar_NumHermanos = models.IntegerField(null=False, default=0)
    EstatusPadres = models.CharField(max_length=50, null=False, default='')
    ViveCon = models.CharField(max_length=50, null=False, default='')
    PrefPaterna = models.CharField(max_length=50, null=False, default='')
    Obs_PrefPaterna = models.TextField()
    PrefHermano = models.CharField(max_length=50, null=False, default='')
    Obs_PrefHermano = models.TextField()

class antpatheredofam(models.Model):
    FolioConsulta = models.ForeignKey(consultagral, blank=True, null=True, on_delete=models.CASCADE)
    Diabeticos  = models.BooleanField(null=False)
    Hipertensivos  = models.BooleanField(null=False)
    Oncologicos = models.BooleanField(null=False)
    Neurologicos = models.BooleanField(null=False)
    Alergicos = models.BooleanField(null=False)
    Transfuncionales = models.BooleanField(null=False)
    Obesidad = models.BooleanField(null=False)
    ITS = models.BooleanField(null=False)
    SIDA = models.BooleanField(null=False)
    Reumaticos = models.BooleanField(null=False)
    Quirurgicos = models.BooleanField(null=False)
    Tabaquismo = models.BooleanField(null=False)
    Alcoholismo = models.BooleanField(null=False)
    Drogadiccion = models.BooleanField(null=False)
    Obs_Antpatheredofam = models.TextField()

class antrecreathab(models.Model):
    FolioConsulta = models.ForeignKey(consultagral, blank=True, null=True, on_delete=models.CASCADE)
    PractDeporte = models.BooleanField(null=False)
    Comp_Prac = models.CharField(max_length=50, null=False)
    Frecuencia = models.CharField(max_length=50, null=False)
    GrupoConviv = models.BooleanField(null=False)
    Hrs_TVDia = models.IntegerField(null=False, default=0)
    Hrs_PCDia = models.IntegerField(null=False, default=0)
    Hrs_CelDia = models.IntegerField(null=False, default=0)
    Hrs_SuenoDia = models.IntegerField(null=False, default=0)
    Insomnio = models.BooleanField(null=False)
    Enuresis = models.BooleanField(null=False)
    Pesadillas = models.BooleanField(null=False)
    Obs_ConflicSueno = models.TextField()
    ComidasDia = models.IntegerField(null=False, default=0)
    ComidasDia_Fam = models.IntegerField(null=False, default=0)
    TipoAlim = models.CharField(max_length=50, null=False)
    Alcoholismo = models.BooleanField(null=False)
    Tabaquismo = models.BooleanField(null=False)
    Drogadiccion = models.BooleanField(null=False)

class antsex(models.Model):
    FolioConsulta = models.ForeignKey(consultagral, blank=True, null=True, on_delete=models.CASCADE)
    Menarca = models.BooleanField(null=False)
    Ritmo = models.BooleanField(null=False)
    FUM = models.BooleanField(null=False)
    Gesta = models.BooleanField(null=False)
    Para = models.BooleanField(null=False)
    Cesarea = models.BooleanField(null=False)
    Aborto = models.BooleanField(null=False)
    Dismenorrea = models.BooleanField(null=False)
    Espermarca = models.BooleanField(null=False)
    Inicio_ActSex = models.CharField(max_length=50, null=False)
    UsoAnticonc = models.BooleanField(null=False)
    Id_Metodo = models.ForeignKey(metanticonceptivos, blank=True, null=True, on_delete=models.CASCADE)

class exploracionfisica(models.Model):
    FolioConsulta = models.ForeignKey(consultagral, blank=True, null=True, on_delete=models.CASCADE)
    Pulso = models.IntegerField(null=False, default=0)
    FrecCard = models.IntegerField(null=False, default=0)
    FrecResp = models.IntegerField(null=False, default=0)
    Temp = models.IntegerField(null=False, default=0)
    IndMC = models.IntegerField(null=False, default=0)
    TensArt = models.IntegerField(null=False, default=0)
    Obs_Cabeza = models.TextField()
    Obs_Cuello = models.TextField()
    Obs_Torax = models.TextField()
    Obs_Abdomen = models.TextField()
    ObsGenitales = models.TextField()
    Id_ValTanner = models.ForeignKey(valoraciontanner, blank=True, null=True, on_delete=models.CASCADE)

class personalidad(models.Model):
    FolioConsulta = models.ForeignKey(consultagral, blank=True, null=True, on_delete=models.CASCADE)
    PeriodoTristeza = models.BooleanField(null=False)
    Frecuencia_PT = models.CharField(max_length=50, null=False)
    Duracion_PT = models.IntegerField(null=False, default=0)
    ConsidFelicidad = models.BooleanField(null=False)
    Obs_ConsidFelicidad = models.TextField()
    AceptacionFisica = models.BooleanField(null=False)
    Obs_AceptacionFisica = models.TextField()
    OpinionPersonal = models.TextField()
    CompReligPadres = models.BooleanField(null=False)
    Religion = models.CharField(max_length=250, null=False)
    Conflictivo = models.BooleanField(null=False)
    Frecuencia_Conflic = models.CharField(max_length=250, null=False)
    ConflicFamEsc = models.BooleanField(null=False)
    ReaccionAgresion = models.CharField(max_length=50, null=False)

class repevaluacionpsic(models.Model):
    FolioConsulta = models.ForeignKey(consultagral, blank=True, null=True, on_delete=models.CASCADE)
    FichaIndent = models.IntegerField(null=False, default=0)
    CURP = models.ForeignKey(pacientes, blank=True, null=True, on_delete=models.CASCADE)
    Escolaridad = models.CharField(max_length=50, null=False)
    Lateridad = models.CharField(max_length=50, null=False)
    MotConsulta = models.TextField()
    PadecimientoAct = models.TextField()
    AspectoComportGral = models.TextField()
    PruebasAplic = models.CharField(max_length=350, null=False)
    ResultadoPrelim = models.TextField()
    DiagTratam = models.TextField()

class repevaluacionmed(models.Model):
    FolioConsulta = models.ForeignKey(consultagral, blank=True, null=True, on_delete=models.CASCADE)
    CURP = models.ForeignKey(pacientes, blank=True, null=True, on_delete=models.CASCADE)
    Obs_RepMed = models.TextField()

class repevolucionpsic(models.Model):
    FolioConsulta = models.ForeignKey(consultagral, blank=True, null=True, on_delete=models.CASCADE)
    CURP = models.ForeignKey(pacientes, blank=True, null=True, on_delete=models.CASCADE)
    ResumenClin = models.TextField()
    PlanTerap = models.TextField()
    Tratamiento = models.TextField()