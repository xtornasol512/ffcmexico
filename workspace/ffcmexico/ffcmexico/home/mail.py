# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
 
def mailing(request, diccionario):
    enviar     = False
    mensaje    = ''
    respuesta  = ''
    asunto     = ''
    asunto_res = ''
    plantilla = True
    if   'envComentario'   in request.POST:

        email  = request.POST.get('email','')
        name   = request.POST.get('name','')
        msg    = request.POST.get('msg','')
 
        enviar   = True
        asunto = 'Dudas y Contacto'
        if plantilla:
            htmly = get_template('emailing/suscripcion_enviado.html')
            d = Context({'asunto':asunto, 'email':email, 'name': name, 'msg':msg})
            mensaje = htmly.render(d)
        else:
            mensaje = 'Hola Brian. Buen dia.<br>%s tiene la siguiente duda o comentario:<br>'%(name)
            mensaje = '%s%s<br><br>Contacto de Correo:<br>%s<br><br><br>Phyro Team'%(mensaje, msg, email)
 
        asunto_res = "Tu duda fue resibida por FFCMexico"
        if plantilla:
            htmly = get_template('emailing/suscripcion_enviado.html')
            #agregar todas las variables al template
            d = Context({'name': name})
            respuesta = htmly.render(d)
        else:
            respuesta =  "Gracias %s por tus comentarios.<br>"%(name)
            respuesta = "%sPronto resibiras una respuesta a ellos<br><br><br>"%(respuesta)
            respuesta = "%s<a href=\"http://ffcmexico.com/\"><span></span>FFCMexico</a>"%(respuesta)
     
    elif 'envSemana'       in request.POST:
        nombre   = request.POST.get('nombre','')
        edad     = request.POST.get('edad','')
        telefono = request.POST.get('telefono','')
        genero   = request.POST.get('genero','')
        email    = request.POST.get('email','')
        comentarios = request.POST.get('comentarios','')
        enviar   = True
        asunto = 'Solicitud de Semana Gratis'
        if plantilla:
            htmly = get_template('email/plantilla1.html')
            d = Context({'email':email, 'name': nombre, 'msg':comentarios, 'edad':edad,
                        'telefono':telefono, 'genero': genero})
            mensaje = htmly.render(d)
        else:
            mensaje = 'Hola Brian. Buen dia.<br>%s esta interesada en tomar su semana gratis,'(nombre)
            mensaje = '%s estos son sus datos:<br>'%(mensaje)
            mensaje = '%sNombre   : %s<br>'%(mensaje, nombre)
            mensaje = '%sEdad     : %s<br>'%(mensaje, edad)
            mensaje = '%sTelefono : %s<br>'%(mensaje, telefono)
            mensaje = '%sGenero   : %s<br>'%(mensaje, genero)
            mensaje = '%sEmail    : %s<br>'%(mensaje, email)
            mensaje = '%sComentarios :<br>%s<br>'%(mensaje, comentarios)
            mensaje = '%s%s<br><br><br>Phyro Team'%(mensaje , email)
 
        asunto_res = "Semana gratis FFCMexico"
        if plantilla:
            htmly = get_template('email/plantilla1.html')
            d = Context({'email':email, 'name': nombre, 'msg':comentarios, 'edad':edad,
                        'telefono':telefono, 'genero': genero})
            respuesta = htmly.render(d)
        else:
            respuesta =  ("Hola %s :D<br>¡Gracias por contactar a nuestra academia!<br>"%(nombre) +
                "Para tomar tu semana de entrenamiento gratis, estos son puntos que debes considerar:<br>"+
                "Encontrar abierto, puedes consultar <a href=\"http://ffcmexico.com/horario\">"+
                "aqui</a> nuestros horarios<br>"+
                "Venir con la ropa adecuada, te recomendamos traer:<br>"+
                "Short o pants deportivo<br>Playera<br>Tenis<br><br>"+
                "Si tienes una duda o comentario, puedes responder a este email o en nuestras redes sociales"+
                "<br><br><br><a href=\"http://ffcmexico.com/\"><span></span>FFCMexico</a>")
 
    elif 'envSubscripcion' in request.POST:
        email    = request.POST.get('email','')
        enviar   = True
        asunto = 'Suscriptor nueo al Newsletter'
        if plantilla:
            htmly = get_template('email/plantilla1.html')
            d = Context({'email':email})
            mensaje = htmly.render(d)
        else:
            mensaje = 'Hola Brian. Buen dia.<br>La siguiente persona se a inscrito al Newsletter:<br>'
            mensaje = '%s%s<br><br><br>Phyro Team'%(mensaje, email)
 
        asunto_res = "Gracias por suscribirte al Newsletter de FFCMexico"
        if plantilla:
            htmly = get_template('email/plantilla1.html')
            d = Context({'email':email})
            respuesta = htmly.render(d)
        else:
            respuesta =  "Hola %s<br>Bienvenido a nuestro Newsletter,<br>te mantendremos informado sobre:<br>"%(email)
            respuesta = "%sEventos<br>Promciones<br>Y todo lo relacionado con la academia<br><br><br>"%(respuesta)
            respuesta = "%s<a href=\"http://ffcmexico.com/\"><span></span>FFCMexico</a>"%(respuesta)
 
    if enviar:
        para   = ['email@email.com'
                    ]
        try:
            for name in para:
                #BRIAN
                #para === to=[name]
                env_email = EmailMessage(asunto, mensaje, to=[name])
                env_email.content_subtype = "html"
                env_email.send()
            diccionario.update({'enviado':True})
            try:
                #CLiente
                res_email = EmailMessage(asunto_res, respuesta, to=[email])
                res_email.content_subtype = "html"
                res_email.send()
            except:
                pass
        except:
            diccionario.update({'noenviado':True})
    return diccionario