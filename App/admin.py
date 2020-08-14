from django.contrib import admin
from django.utils.html import format_html
from .models import pacientes,areastrabajo,domicilios,acompanantes,metanticonceptivos,edocivil,tipoconsultas,valoraciontanner,expedientes,consultagral,antescolares,antfamiliares,antpatheredofam,antrecreathab,antsex,exploracionfisica,personalidad,repevaluacionpsic,repevaluacionmed,repevolucionpsic#,usuarios

#Creacion de clases para visualizar los datos de la DB, en lugar de que se visualicen como objetos de Modelo
class areastrabajoAdmin(admin.ModelAdmin):
    list_display = ("Id_Area","NombreArea")

class usuariosAdmin(admin.ModelAdmin):
    list_display = ("Nombre","Apellidos","Id_Area","Mail","Telefono")
    search_fields = ("Nombre","Apellidos")
    list_filter = ("Id_Area",)

class expedientesAdmin(admin.ModelAdmin):
    list_display = ("Id_Exped","CURP")
    search_fields = ("CURP",)
    raw_id_fields = ("CURP",)

class pacientesAdmin(admin.ModelAdmin):
    list_display = ("Nombre_Pac","Apellidos_Pac","FechaNac", "Peso", "Talla","CURP","Telefono","Sexo","Id_EdoCivil")
    search_fields = ("Nombre_Pac","Apellidos_Pac","CURP")
    list_filter = ("Sexo",)
    raw_id_fields = ("Id_EdoCivil",)

class domiciliosAdmin(admin.ModelAdmin):
    list_display = ("Id_Domicilio","CURP","Calle","NumInt","NumExt","Colonia","CP","Municipio","Estado")
    search_fields = ("CURP",)
    raw_id_fields = ("CURP",)

class edocivilAdmin(admin.ModelAdmin):
    list_display = ("Id_EdoCivil","Nombre_EdoCivil")

class consultagralAdmin(admin.ModelAdmin):
    list_display = ("FolioConsulta","FechaConsulta","CURP_id","Id_Acomp_id","Id_Exped_id","Id_TipoConsulta_id","UserID")
    raw_id_fields = ("CURP_id","Id_Acomp_id","Id_Exped_id","Id_TipoConsulta_id")

class antescolaresAdmin(admin.ModelAdmin):
    list_display = ("id","FolioConsulta_id","Grado","Promedio","RepitioGrado","DesercionEsc","Causa_DesercionEsc","ConflictProf","Causa_ConflictProf","RelacionComp","TrabajoAnt","Obs_TrabajoAnt","TrabajoActual")
    raw_id_fields = ("FolioConsulta_id",)

class antfamiliaresAdmin(admin.ModelAdmin):
    list_display = ("id","FolioConsulta_id","Grado","EdadPadre","EdadMadre","EscPadre","EscMadre","EstatusPadres","Id_EdoCivil_id","NumHermanos","Lugar_NumHermanos","PrefPaterna","Obs_PrefPaterna","PrefHermano","Obs_PrefHermano")
    raw_id_fields = ("FolioConsulta_id",)

class antpatheredofamAdmin(admin.ModelAdmin):
    list_display = ("id","FolioConsulta_id","Diabeticos","Hipertensivos","Oncologicos","Neurologicos","Alergicos","Transfuncionales","Obesidad","ITS","SIDA","Reumaticos","Quirurgicos","Tabaquismo","Alcoholismo","Drogadiccion","Obs_Antpatheredofam")
    raw_id_fields = ("FolioConsulta_id",)

class antrecreathabAdmin(admin.ModelAdmin):
    list_display = ("id","FolioConsulta_id","PractDeporte","Comp_Prac","Frecuencia","GrupoConviv","Hrs_TVDia","Hrs_PCDia","Hrs_CelDia","Hrs_SuenoDia","Insomnio","Enuresis","Pesadillas","Obs_ConflicSueno","ComidasDia","ComidasDia_Fam","TipoAlim","Alcoholismo","Tabaquismo","Drogadiccion")
    raw_id_fields = ("FolioConsulta_id",)

class antsexAdmin(admin.ModelAdmin):
    list_display = ("id","FolioConsulta_id","Menarca","Ritmo","FUM","Gesta","Para","Cesarea","Aborto","Dismenorrea","Espermarca","Inicio_ActSex","UsoAnticonc","Id_Metodo_id")
    raw_id_fields = ("FolioConsulta_id",)

class exploracionfisicaAdmin(admin.ModelAdmin):
    list_display = ("id","FolioConsulta_id","Pulso","FrecCard","FrecResp","Temp","IndMC","TensArt","Obs_Cabeza","Obs_Cuello","Obs_Torax","Obs_Abdomen","ObsGenitales","Id_ValTanner_id")
    raw_id_fields = ("FolioConsulta_id",)

class personalidadAdmin(admin.ModelAdmin):
    list_display = ("id","FolioConsulta_id","PeriodoTristeza","Frecuencia_PT","Duracion_PT","ConsidFelicidad","Obs_ConsidFelicidad","AceptacionFisica","Obs_AceptacionFisica","OpinionPersonal","CompReligPadres","Religion","Conflictivo","Frecuencia_Conflic","ConflicFamEsc","ReaccionAgresion")
    raw_id_fields = ("FolioConsulta_id",)

class repevaluacionmedAdmin(admin.ModelAdmin):
    list_display = ("id","FolioConsulta_id","CURP_id","Obs_RepMed")
    raw_id_fields = ("FolioConsulta_id","CURP_id")

class repevaluacionpsicAdmin(admin.ModelAdmin):
    list_display = ("id","FichaIndent","FolioConsulta_id","CURP_id","Escolaridad","Lateridad","MotConsulta","PadecimientoAct","AspectoComportGral","PruebasAplic","ResultadoPrelim","DiagTratam")
    raw_id_fields = ("FolioConsulta_id","CURP_id")

class repevolucionpsicAdmin(admin.ModelAdmin):
    list_display = ("id","FolioConsulta_id","CURP_id","ResumenClin","PlanTerap","Tratamiento")
    raw_id_fields = ("FolioConsulta_id","CURP_id")

class acompanantesAdmin(admin.ModelAdmin):
    list_display = ("Id_Acomp","Nombre_Acomp")

class metanticonceptivosAdmin(admin.ModelAdmin):
    list_display = ("Id_Metodo","NombreMetodo")

class tipoconsultasAdmin(admin.ModelAdmin):
    list_display = ("Id_TipoConsulta","Nombre_TipoConsulta")

class valoraciontannerAdmin(admin.ModelAdmin):
    search_fields = ("NombreValTanner",)
    def image_tag(self, obj):
        if obj.Img_ValTanner != None:
            return format_html('<img width="135" height="85" src="/media/{}" />'.format(obj.Img_ValTanner))
        else:
            return format_html('<img width="135" height="85" src="/static/images/logo_HPcaaps.png" />')
    image_tag.short_description = "Imagen"
    readonly_fields = ['image_tag']
    list_display = ("Id_ValTanner","image_tag","NombreValTanner", "DescripcionValTanner")


# Register your models here.
#Registro de los modelos migrados para crear las Vistas en el Administrador del Sitio
admin.site.register(areastrabajo,areastrabajoAdmin)
#admin.site.register(usuarios,usuariosAdmin)

admin.site.register(consultagral,consultagralAdmin)
admin.site.register(acompanantes,acompanantesAdmin)
admin.site.register(antescolares,antescolaresAdmin)
admin.site.register(antfamiliares,antfamiliaresAdmin)
admin.site.register(antpatheredofam,antpatheredofamAdmin)
admin.site.register(antrecreathab,antrecreathabAdmin)
admin.site.register(antsex,antsexAdmin)
admin.site.register(exploracionfisica,exploracionfisicaAdmin)
admin.site.register(personalidad,personalidadAdmin)
admin.site.register(repevaluacionpsic,repevaluacionpsicAdmin)
admin.site.register(repevaluacionmed,repevaluacionmedAdmin)
admin.site.register(repevolucionpsic,repevolucionpsicAdmin)

admin.site.register(metanticonceptivos,metanticonceptivosAdmin)
admin.site.register(tipoconsultas,tipoconsultasAdmin)
admin.site.register(valoraciontanner,valoraciontannerAdmin)

admin.site.register(expedientes,expedientesAdmin)
admin.site.register(pacientes,pacientesAdmin)
admin.site.register(domicilios,domiciliosAdmin)
admin.site.register(edocivil,edocivilAdmin)