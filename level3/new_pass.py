username = "ExecuTroll_404"
password = "cl1mbthel4dder"

reset_code = 927840
code_entered = 927840

if reset_code != code_entered:
    print("Código de restablecimiento incorrecto")
else:
    print("Ingrese la nueva contraseña")

    new_pwd = "ExecSweet16!"
    confirm_pwd = "ExecSweet16?"

    if new_pwd == confirm_pwd:
        password = new_pwd
        print("Contraseña restablecida exitosamente")
    else:
        print("Las contraseñas no coinciden")

  
    