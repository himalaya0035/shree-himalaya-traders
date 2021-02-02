var windowpathone = $(location).attr('pathname');
if (windowpathone == '/reset_password/'){
    var email_field = document.getElementById('id_email');
    email_field.placeholder = "Email..";

    if (user!='AnonymousUser'){
        email_field.value=user_email;
    }
}
