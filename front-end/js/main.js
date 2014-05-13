

    function newsletterConfirm() {

        if (Notification) {

            if (Notification.permission !== "granted") {

                Notification.requestPermission()

            }
            var title = "FFC México"
            var extra = {

                icon: "/img/logos/svg/logo_fenix_01_portrait_32bits.png",

                body: "Tu email ha sido enviado, espera noticias nuestras en tu mail"

            }
            var noti = new Notification( title, extra)
            noti.onclick = {

                // Al hacer click

            }
            noti.onclose = {

                // Al cerrar

            }
            setTimeout( function() { noti.close() }, 10000)

        }

    }

